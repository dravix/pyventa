#!/usr/bin/env python3
# lib/librerias/configurador.py
# Global configuration manager for Pyventa.
# Replaces Python 2 ConfigParser + PyQt4 with Python 3 configparser + platformdirs.

import os
import sys
import shutil
import logging
import configparser

from platformdirs import user_config_dir, user_data_dir

logger = logging.getLogger(__name__)


def get_homedir() -> str:
    """Return the per-user pyventa data directory, platform-aware."""
    if sys.platform == "linux":
        return os.path.join(os.path.expanduser("~"), ".pyventa")
    return os.path.join(os.path.expanduser("~"), "pyventa")


class Configurador:
    """
    Interface to the pyventa configuration file (config.cfg).

    Backward-compatible replacement for the Python 2 version:
    - Uses stdlib configparser (was ConfigParser in Python 2)
    - Uses platformdirs for home-dir resolution
    - No longer imports PyQt4; Qt dialogs are handled by callers
    """

    def __init__(self, parent=None, configFile: str = None):
        self.parent = parent
        home = get_homedir()

        if configFile:
            self.ruta = configFile
        else:
            self.ruta = os.path.join(home, "config.cfg")

        cfg = configparser.ConfigParser()
        if os.path.exists(self.ruta) and cfg.read([self.ruta]):
            self.cfg = cfg
            self.stat = True
        else:
            self.stat = self._setup_init_config()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _setup_init_config(self) -> bool:
        """
        Copy the bundled default profile when no config file is found.

        Returns True when a config was successfully copied and loaded,
        False when the config file is still missing.
        """
        if os.path.exists(self.ruta):
            # File exists but is empty / unreadable — reload
            return self._reload_from_disk()

        home_dir = get_homedir()
        # Locate bundled default profile relative to this file
        module_dir = os.path.dirname(os.path.abspath(__file__))
        perfil_src = os.path.join(module_dir, "..", "..", "perfil")
        perfil_src = os.path.normpath(perfil_src)

        try:
            if os.path.isdir(perfil_src):
                shutil.copytree(perfil_src, home_dir, dirs_exist_ok=True)
                logger.info("Default profile copied to %s", home_dir)
            else:
                logger.warning("Default profile directory not found at %s", perfil_src)
                return False
        except Exception as exc:
            logger.error("Could not copy default profile: %s", exc)
            return False

        return self._reload_from_disk()

    def _reload_from_disk(self) -> bool:
        cfg = configparser.ConfigParser()
        if os.path.exists(self.ruta) and cfg.read([self.ruta]):
            self.cfg = cfg
            return True
        return False

    # ------------------------------------------------------------------
    # Public API  (backward-compatible)
    # ------------------------------------------------------------------

    def recargar(self):
        """Reload configuration from disk."""
        self.__init__(self.parent, self.ruta)

    def get_homedir(self) -> str:
        return get_homedir()

    def has_option(self, modulo: str, propiedad: str) -> bool:
        return self.cfg.has_option(modulo, propiedad)

    def get(self, modulo: str, propiedad: str, fallback=None) -> str:
        """
        Return the value for (modulo, propiedad).
        Creates the key with value 0 when missing (legacy behavior).
        """
        if self.cfg.has_option(modulo, propiedad):
            return self.cfg.get(modulo, propiedad)
        # Legacy: auto-create missing keys
        self.setCambio(modulo, propiedad, 0)
        return fallback if fallback is not None else "False"

    def getDato(self, modulo: str, propiedad: str):
        """
        Return the value for (modulo, propiedad), or False when absent.
        Legacy alias for get(); new code should use get() directly.
        """
        if self.cfg.has_option(modulo, propiedad):
            return self.cfg.get(modulo, propiedad)
        self.setCambio(modulo, propiedad, 0)
        return False

    def set(self, modulo: str, propiedad: str, valor) -> None:
        """Update a value in memory (does not write to disk automatically)."""
        try:
            self.cfg.set(str(modulo), str(propiedad), str(valor))
        except configparser.Error as exc:
            raise exc

    def setCambio(self, modulo: str, propiedad: str, valor) -> None:
        """Update a value and immediately persist it to disk."""
        try:
            # Add section if it doesn't exist yet
            if not self.cfg.has_section(modulo):
                self.cfg.add_section(modulo)
            self.cfg.set(str(modulo), str(propiedad), str(valor))
        except configparser.Error as exc:
            logger.error("Could not save config key %s/%s: %s", modulo, propiedad, exc)
        else:
            self.guardar()

    def add_section(self, section: str) -> None:
        if not self.cfg.has_section(section):
            self.cfg.add_section(section)

    def config(self) -> configparser.ConfigParser:
        return self.cfg

    def guardar(self) -> None:
        """Write the full configuration to disk."""
        os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as fh:
            self.cfg.write(fh)
        logger.debug("Configuration saved to %s", self.ruta)
