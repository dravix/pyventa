#!/usr/bin/env python3
# lib/librerias/conexion.py
# Database connection manager for Pyventa.
#
# Replaces the Python 2 / MySQLdb / PyQt4 version with:
#   - PyMySQL (drop-in MySQLdb replacement, pure Python)
#   - SQLAlchemy 2.x engine with connection pooling and auto-reconnect
#   - sqlite3 kept for the embedded/offline mode
#   - Backward-compatible Conexion interface so callers need no immediate changes

from __future__ import annotations

import base64
import logging
import os
import shutil
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Generator, Optional

import pymysql
import pymysql.cursors
from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import QueuePool

from lib.librerias.comun import home
from lib.librerias.configurador import Configurador

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# SQLite compatibility functions (replicate MySQL built-ins used in queries)
# ---------------------------------------------------------------------------


def _sqlite_now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _sqlite_today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _sqlite_elt(n: int, *args: str) -> str:
    idx = n - 1
    return args[idx] if 0 <= idx < len(args) else ""


def _sqlite_dateformat(fecha: str, fmt: str) -> str:
    try:
        return datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").strftime(fmt)
    except ValueError:
        return fecha


# ---------------------------------------------------------------------------
# dicursor helpers  (legacy shim — convert sqlite3 tuple rows to dicts)
# ---------------------------------------------------------------------------


def dicursor(cursor, row):
    """
    Convert a row (or list of rows) to dict format when using sqlite3.
    For MySQL dict-cursor rows (already dicts) this is a no-op.
    """
    if isinstance(cursor, sqlite3.Cursor):
        if isinstance(row, list):
            return [_row_to_dict(cursor, r) for r in row]
        if isinstance(row, tuple):
            return _row_to_dict(cursor, row)
    return row


def _row_to_dict(cursor: sqlite3.Cursor, row: tuple) -> dict:
    if cursor.description is None:
        return {}
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


# ---------------------------------------------------------------------------
# Engine factory
# ---------------------------------------------------------------------------


def build_engine(cfg: Configurador) -> Engine:
    """Create a SQLAlchemy engine from the pyventa configuration."""
    motor = cfg.getDato("pyventa", "motor") or "mysql"

    if motor == "sqlite3":
        db_path = os.path.join(home, "pyventa.sqlite")
        if not os.path.exists(db_path):
            _copy_default_sqlite(db_path)

        engine = create_engine(
            f"sqlite:///{db_path}",
            connect_args={"check_same_thread": False},
        )

        @event.listens_for(engine, "connect")
        def _register_sqlite_functions(dbapi_conn, _):
            dbapi_conn.create_function("NOW", 0, _sqlite_now)
            dbapi_conn.create_function("CURDATE", 0, _sqlite_today)
            dbapi_conn.create_function("DATE_FORMAT", 2, _sqlite_dateformat)
            dbapi_conn.create_function("ELT", -1, _sqlite_elt)

    else:
        host = cfg.getDato("mysql", "host") or "localhost"
        user = cfg.getDato("mysql", "user") or "root"
        raw_pass = cfg.getDato("mysql", "pass") or ""
        # Legacy: password stored as base64 in config
        try:
            password = base64.b64decode(raw_pass).decode("utf-8")
        except Exception:
            password = raw_pass
        schema = cfg.getDato("mysql", "db") or "tpv"

        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{schema}",
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,   # auto-reconnect on stale connections
            pool_recycle=3600,    # recycle connections every hour
            echo=False,
        )

    return engine


def _copy_default_sqlite(dest: str) -> None:
    """Copy the bundled default SQLite database to the user's data directory."""
    module_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.normpath(os.path.join(module_dir, "..", "..", "perfil", "pyventa.sqlite"))
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(src, dest)
        logger.info("Default SQLite database copied to %s", dest)
    else:
        raise FileNotFoundError(
            f"Default SQLite database not found at {src} and no existing DB at {dest}"
        )


# ---------------------------------------------------------------------------
# Conexion — backward-compatible connection wrapper
# ---------------------------------------------------------------------------


class Conexion:
    """
    Database connection wrapper for Pyventa.

    Provides the same interface as the legacy MySQLdb-based class so existing
    callers (pyventa.py, padmin.py, all modulos/) require no immediate changes.

    Internals:
      - SQLAlchemy engine with QueuePool for MySQL (auto-reconnect via pool_pre_ping)
      - sqlite3 for embedded mode
      - PyMySQL as the MySQL driver (pure Python, no C compile required)

    Attributes exposed for callers:
      stat    -- True when connection is up, False otherwise
      cursor  -- tuple-mode cursor (legacy)
      curser  -- dict-mode cursor  (legacy)
      db      -- underlying raw connection (legacy; use engine for new code)
      engine  -- SQLAlchemy Engine (new code should prefer this)
    """

    def __init__(self, parent=None, config: Optional[Configurador] = None, datos: Optional[dict] = None):
        self.parent = parent
        self.stat = False
        self.db = None
        self.cursor = None
        self.curser = None
        self.engine: Optional[Engine] = None
        self._cfg: Optional[Configurador] = None

        if datos and isinstance(datos, dict) and len(datos) > 0:
            self._host = datos["host"]
            self._user = datos["user"]
            self._pass = datos["pass"]
            self._schema = datos["schema"]
            self._conectar_mysql_directo()
        else:
            self._cfg = config if config else Configurador(parent)
            if self._cfg.stat:
                self._conectar()
            else:
                logger.warning("No valid configuration found — connection deferred.")

    # ------------------------------------------------------------------
    # Connection setup
    # ------------------------------------------------------------------

    def _conectar(self) -> None:
        """Connect using configuration from the Configurador."""
        motor = self._cfg.getDato("pyventa", "motor") or "mysql"
        if motor == "sqlite3":
            self._conectar_sqlite()
        else:
            self._conectar_mysql()

    def _conectar_sqlite(self) -> None:
        db_path = os.path.join(home, "pyventa.sqlite")
        if not os.path.exists(db_path):
            _copy_default_sqlite(db_path)
        try:
            self.db = sqlite3.connect(db_path)
            self.db.create_function("NOW", 0, _sqlite_now)
            self.db.create_function("CURDATE", 0, _sqlite_today)
            self.db.create_function("DATE_FORMAT", 2, _sqlite_dateformat)
            self.db.create_function("ELT", -1, _sqlite_elt)
            self.cursor = self.db.cursor()
            self.curser = self.db.cursor()
            self.stat = True
            logger.info("Connected to SQLite at %s", db_path)
        except Exception as exc:
            logger.error("SQLite connection failed: %s", exc)
            self.stat = False

    def _conectar_mysql(self) -> None:
        host = self._cfg.getDato("mysql", "host") or "localhost"
        user = self._cfg.getDato("mysql", "user") or "root"
        raw_pass = self._cfg.getDato("mysql", "pass") or ""
        try:
            password = base64.b64decode(raw_pass).decode("utf-8")
        except Exception:
            password = raw_pass
        schema = self._cfg.getDato("mysql", "db") or "tpv"

        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=schema,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.Cursor,
                autocommit=False,
            )
            self.cursor = self.db.cursor()
            self.curser = self.db.cursor(pymysql.cursors.DictCursor)
            # Build the SQLAlchemy engine alongside for new-style code
            self.engine = build_engine(self._cfg)
            self.stat = True
            logger.info("Connected to MySQL at %s/%s", host, schema)
        except pymysql.Error as exc:
            err_code = exc.args[0]
            if err_code == 2006:
                logger.warning("MySQL server gone away — will retry on next query.")
            else:
                logger.error("MySQL connection error %s: %s", err_code, exc)
                if self.parent is not None:
                    self.asistente()
            self.stat = False

    def _conectar_mysql_directo(self) -> None:
        """Connect with credentials supplied directly (not from config file)."""
        try:
            self.db = pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._pass,
                database=self._schema,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.Cursor,
                autocommit=False,
            )
            self.cursor = self.db.cursor()
            self.curser = self.db.cursor(pymysql.cursors.DictCursor)
            self.stat = True
        except pymysql.Error as exc:
            logger.error("Direct MySQL connection error: %s", exc)
            self.stat = False

    def _reconnect(self) -> None:
        """Attempt to re-establish a lost connection."""
        try:
            self.db.ping(reconnect=True)
            self.cursor = self.db.cursor()
            self.curser = self.db.cursor(pymysql.cursors.DictCursor)
            logger.info("Reconnected to database.")
        except Exception:
            self._conectar()

    # ------------------------------------------------------------------
    # Legacy API
    # ------------------------------------------------------------------

    def asistente(self) -> None:
        """Open the DB configuration dialog (caller must provide a Qt parent)."""
        from lib.db_conf import configurador as BDConfig
        logger.info("Opening DB configuration assistant.")
        ui = BDConfig(self._cfg)
        dialog = ui.exec()
        if dialog == 1:
            self.__init__(self.parent)
        else:
            self.stat = False

    def lastId(self) -> str:
        """Return the SQL fragment to retrieve the last inserted row ID."""
        motor = self._cfg.getDato("pyventa", "motor") if self._cfg else "mysql"
        if motor == "sqlite3":
            return "SELECT last_insert_rowid();"
        return "SELECT LAST_INSERT_ID();"

    def conectar(self) -> None:
        """Public reconnect entry-point (used by legacy callers)."""
        self._conectar()

    def commit(self) -> None:
        if self.db:
            self.db.commit()

    def rollback(self) -> None:
        if self.db:
            self.db.rollback()

    def ultimo(self) -> Any:
        """Return the last inserted row ID."""
        if self._cfg and self._cfg.getDato("pyventa", "motor") == "sqlite3":
            return self.cursor.lastrowid if self.cursor else None
        if self.db:
            return self.db.insert_id()
        return None

    def close(self) -> None:
        if self.db:
            self.db.close()
        if self.engine:
            self.engine.dispose()

    def ejecutar(self, sql: str, params=None, dic: bool = False) -> None:
        """
        Execute a SQL statement without returning results.

        Parameters
        ----------
        sql    : SQL string (use %s placeholders for parameters)
        params : tuple/list/dict of bind values (prevents SQL injection)
        dic    : use the dict cursor when True
        """
        cursor = self.curser if dic else self.cursor
        try:
            cursor.execute(sql, params or ())
        except (pymysql.Error, sqlite3.Error) as exc:
            code = exc.args[0] if exc.args else 0
            if code in (2006, 2013):
                logger.warning("Lost connection during execute — reconnecting.")
                self._reconnect()
                cursor.execute(sql, params or ())
            else:
                raise

    def query(self, sql: str, params=None, single: bool = False, tipo: int = 0):
        """
        Execute a SELECT and return results.

        Parameters
        ----------
        sql    : SQL string (use %s placeholders for parameters)
        params : bind values
        single : return only the first row when True
        tipo   : 0 = tuple rows, 1 = dict rows

        Returns a row, list of rows, or None on error.
        """
        cursor = self.curser if tipo == 1 else self.cursor
        try:
            cursor.execute(sql, params or ())
        except pymysql.Error as exc:
            code = exc.args[0] if exc.args else 0
            if code == 2006:
                self._reconnect()
                cursor.execute(sql, params or ())
            elif code == 1054:
                logger.error(
                    "Incorrect database version — please reconfigure. %s", exc
                )
                self.asistente()
                return None
            else:
                logger.error("Query error: %s", exc)
                return None
        except sqlite3.Error as exc:
            logger.error("SQLite query error: %s", exc)
            return None

        if single:
            return cursor.fetchone()
        return cursor.fetchall()

    # ------------------------------------------------------------------
    # New-style context-manager API (for Phase 2+ callers)
    # ------------------------------------------------------------------

    @contextmanager
    def session(self) -> Generator:
        """
        Provide a SQLAlchemy connection context for new-style code.

        Usage::
            with conexion.session() as conn:
                result = conn.execute(text("SELECT 1"))
        """
        if self.engine is None:
            raise RuntimeError("SQLAlchemy engine not initialised (sqlite3 mode?)")
        with self.engine.connect() as conn:
            try:
                yield conn
                conn.commit()
            except Exception:
                conn.rollback()
                raise
