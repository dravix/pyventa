#!/usr/bin/env python3
# lib/librerias/seguridad.py
# Login / authentication dialog for Pyventa.
#
# Migrated from Python 2 / PyQt4 / MySQLdb / md5 to:
#   - Python 3
#   - PyQt6 (new-style signals)
#   - PyMySQL (via the Conexion layer)
#   - hashlib for legacy MD5 verification + bcrypt for new passwords
#   - Parameterised SQL queries (no more string-format injection)

from __future__ import annotations

import hashlib
import logging

import bcrypt
import pymysql
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QCursor, QPixmap
from PyQt6.QtWidgets import QDialog

from lib.librerias.comun import home
from lib.librerias.conexion import dicursor
from ui.ui_acceso import Ui_Acceso

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Password utilities
# ---------------------------------------------------------------------------

def _hash_legacy(password: str) -> str:
    """MD5 hex-digest — matches the hash stored by the original app."""
    return hashlib.md5(password.encode("utf-8")).hexdigest()  # noqa: S324


def _hash_new(password: str) -> str:
    """bcrypt hash for new/upgraded passwords."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, stored: str) -> bool:
    """
    Verify *password* against *stored*.

    Supports both legacy MD5 hashes (32-char hex) and modern bcrypt hashes
    (start with ``$2b$``).  During the migration period both formats coexist;
    once a user logs in with a valid legacy hash the caller should upgrade it
    with :func:`upgrade_hash`.
    """
    if stored.startswith("$2b$") or stored.startswith("$2a$"):
        return bcrypt.checkpw(password.encode("utf-8"), stored.encode("utf-8"))
    # Legacy MD5 fallback
    return _hash_legacy(password) == stored


def upgrade_hash(cursor, user_id: int, new_hash: str) -> None:
    """
    Replace the stored password hash for *user_id* with the bcrypt *new_hash*.
    Safe to call after a successful legacy-MD5 login.
    """
    try:
        cursor.execute(
            "UPDATE usuarios SET clave = %s WHERE id_usuario = %s",
            (new_hash, user_id),
        )
    except Exception as exc:
        logger.warning("Could not upgrade password hash for user %s: %s", user_id, exc)


# ---------------------------------------------------------------------------
# Seguridad dialog
# ---------------------------------------------------------------------------


class Seguridad(QDialog, Ui_Acceso):
    """
    Login dialog.

    Emits ``done(user_id)`` on success (positive int) or ``done(-1)`` on
    cancel / too many failed attempts.
    """

    def __init__(self, parent=None, nivel: int = 1, logo: str = None,
                 nombre: str = "Pyventa"):
        super().__init__(parent)
        self.setupUi(self)

        self.nivel = nivel
        self.parent = parent
        self.cursor = parent.cursor
        self.curser = parent.curser
        self.home = home
        self.count = 0
        self.usuario: dict = {
            "nivel": 0,
            "nombre": "Pyventa",
            "usuario": "Pyventa",
            "id_usuario": 1,
        }

        self.lbInfo.setText(f"<h4>{nombre.capitalize()}</h4>")
        if logo:
            self.logo.setPixmap(QPixmap(logo))

        # Default visibility
        self.pbAceptar.setDefault(True)
        self.pbCerrar.setVisible(True)
        self.lblServidor.setVisible(False)
        self.cbServidores.setVisible(False)
        self.leClaveServidor.setVisible(False)
        self.lblClaveServidor.setVisible(False)
        self.lblAlerta.setVisible(False)
        self.updateGeometry()

        # Populate remote-server combo
        try:
            self.cursor.execute("SELECT * FROM conexiones")
            self.conexiones = self.cursor.fetchall()
            self.cbServidores.addItem("Local", 0)
            for c in self.conexiones:
                self.cbServidores.addItem(c[1], c[0])
        except Exception:
            self.pbRemoto.setVisible(False)
        else:
            self.pbRemoto.setVisible(True)

        # New-style PyQt6 signal connections
        self.leClave.returnPressed.connect(self.autentificar)
        self.pbAceptar.clicked.connect(self.autentificar)
        self.rejected.connect(self.getUser)
        self.pbCerrar.clicked.connect(lambda: self.done(-1))
        self.pbRemoto.toggled.connect(self.activateRemote)

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def getUser(self) -> dict:
        return self.usuario

    # ------------------------------------------------------------------
    # Remote-server panel
    # ------------------------------------------------------------------

    def activateRemote(self, visible: bool) -> None:
        self.lblServidor.setVisible(visible)
        self.cbServidores.setVisible(visible)
        self.leClaveServidor.setVisible(visible)
        self.lblClaveServidor.setVisible(visible)
        self.adjustSize()

    def changeConection(self, index: int) -> bool:
        """Switch the active cursors to a remote connection when index > 0."""
        self.setCursor(QCursor(Qt.CursorShape.WaitCursor))

        if index == 0:
            # Restore local cursors
            self.cursor = self.parent.cursor
            self.curser = self.parent.curser
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            return True

        conexion = self.conexiones[index - 1]
        conn_data = {
            "host": conexion[2],
            "schema": conexion[3],
            "user": conexion[5],
            "pass": str(self.leClaveServidor.text()),
        }
        try:
            db = pymysql.connect(
                host=conn_data["host"],
                user=conn_data["user"],
                password=conn_data["pass"],
                database=conn_data["schema"],
                charset="utf8mb4",
            )
        except pymysql.Error as exc:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            code = exc.args[0]
            if code == 1045:
                self._notify("Acceso denegado.\nPor favor verifique su clave de servidor.")
            elif code in range(2001, 2006):
                self._notify("Acceso denegado.\nEl servidor no se encuentra disponible.")
            elif code == 1049:
                self._notify("Acceso denegado.\nLa base de datos no fue localizada.")
            else:
                logger.error("Remote connection error %s: %s", code, exc)
            return False
        else:
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            self.cursor = db.cursor()
            self.curser = db.cursor(pymysql.cursors.DictCursor)
            return True

    # ------------------------------------------------------------------
    # Notification
    # ------------------------------------------------------------------

    def _notify(self, info: str) -> None:
        QTimer.singleShot(50_000, self._hide_alert)
        self.lblAlerta.setVisible(True)
        self.lblAlerta.setText(info)

    # Keep the old name as an alias for legacy callers
    notify = _notify  # type: ignore[assignment]

    def _hide_alert(self) -> None:
        self.lblAlerta.setVisible(False)

    ocultarAlerta = _hide_alert  # legacy alias

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    def autentificar(self) -> None:
        """Validate credentials and close the dialog with the user ID."""
        if not self.changeConection(self.cbServidores.currentIndex()):
            return

        usuario = self.leUsuario.text().strip()
        clave = self.leClave.text()

        if not usuario:
            return

        # Fetch the user record using a parameterised query (no SQL injection)
        try:
            self.curser.execute(
                "SELECT * FROM usuarios WHERE usuario = %s",
                (usuario,),
            )
            row = self.curser.fetchone()
        except Exception as exc:
            logger.error("Authentication query failed: %s", exc)
            self._notify("Error al consultar la base de datos.")
            return

        if row is None:
            self._fail_attempt()
            return

        user = dicursor(self.curser, row)
        if user is None:
            self._fail_attempt()
            return

        stored_hash = user.get("clave", "")
        if not verify_password(clave, stored_hash):
            self._fail_attempt()
            return

        if user.get("nivel", 0) < self.nivel:
            self._notify(
                "Su nivel de acceso es menor al necesario,\n"
                "consulte con su superior."
            )
            return

        # Success — optionally upgrade legacy MD5 hash to bcrypt
        if not (stored_hash.startswith("$2b$") or stored_hash.startswith("$2a$")):
            upgrade_hash(self.curser, user["id_usuario"], _hash_new(clave))

        self.lbInfo.setText(f"<h2>Bienvenido {user['nombre']}</h2>")
        logger.info("User '%s' authenticated (level %s).", user["usuario"], user["nivel"])
        self.usuario = user
        self.done(int(user["id_usuario"]))

    def _fail_attempt(self) -> None:
        if self.count < 2:
            self._notify(
                f"El usuario/clave son incorrectos.\n"
                f"Inténtelo nuevamente (Intento {self.count + 1} de 3)."
            )
            self.count += 1
        else:
            self.done(-1)
