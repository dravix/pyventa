#!/usr/bin/env python3
# lib/dialogos/notificaciones.py
# Non-blocking toast-style notification dialog.
# Migrated from PyQt4 → PyQt6.

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMessageBox


def notify(parent, tipo: str, event: str, info: str = "", detail: str = "",
           time: int = 5, coords=None) -> None:
    """
    Display a self-dismissing notification dialog.

    Parameters
    ----------
    parent  : Qt parent widget
    tipo    : 'error' | 'info' | 'advertencia' | 'exito'
    event   : Short title text
    info    : Informative body text
    detail  : Detailed text (shown in expandable area)
    time    : Seconds before auto-close (default 5)
    coords  : (x, y) tuple to position the dialog
    """
    dia = QMessageBox(parent)
    QTimer.singleShot(time * 1000, dia.accept)

    dia.setText(event)
    dia.setInformativeText(info)
    if detail:
        dia.setDetailedText(detail)
    dia.setWindowModality(Qt.WindowModality.NonModal)
    dia.setStandardButtons(QMessageBox.StandardButton.NoButton)

    if tipo == "error":
        dia.setStyleSheet(
            ".QMessageBox{background:rgba(250,30,10,255);color:#fff}"
            "QLabel{background:transparent;color:#fff}"
        )
        dia.setIcon(QMessageBox.Icon.Critical)
    elif tipo == "info":
        dia.setStyleSheet(
            ".QMessageBox{background:rgba(255,255,255,255);color:#333}"
            "QLabel{background:transparent;color:#333;border:0;}"
        )
        dia.setIcon(QMessageBox.Icon.Information)
    elif tipo == "advertencia":
        dia.setStyleSheet(
            ".QMessageBox{background:rgba(255,200,0,255);color:#fff}"
            "QLabel{background:transparent;color:#fff}"
        )
        dia.setIcon(QMessageBox.Icon.Warning)
    elif tipo == "exito":
        dia.setStyleSheet(
            ".QMessageBox{background:rgba(0,128,0,255);color:#fff}"
            "QLabel{background:transparent;color:#fff}"
        )
        dia.setIcon(QMessageBox.Icon.Information)

    if coords:
        dia.move(coords[0], coords[1])

    dia.setWindowFlags(dia.windowFlags() | Qt.WindowType.FramelessWindowHint)
    dia.show()
