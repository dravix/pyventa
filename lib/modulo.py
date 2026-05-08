# -*- coding: utf-8 -*-
import sys
import os
import random
from PyQt6 import QtCore, QtGui, QtWidgets
from qt import Qt
import datetime
# from chart import chart


class Modulo():
    def __init__(self, parent, nombre):
        self.curser = parent.curser
        self.cursor = parent.cursor
        self.datos = {
            'nombre': "Reportes",
            'descripcion': "Muestra el todo lo relacionado con ventas.",
            'version': "0.05",
            'id': id,
            'nivel': 2}
        self.id = id
        self.parent = parent
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName(self.datos['nombre'] + str(id))
        # self.action.setShortcut("F4")
        # self.action.setShortcut(QtCore.QCoreApplication.translate("Principal", "F4"))
        icon28 = QtGui.QIcon()
        icon28.addPixmap(
            QtGui.QPixmap("/usr/share/pyventa/images/32/silver/ptch.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off)
        self.action.setIcon(icon28)
        self.action.setText(self.datos['nombre'])
        # self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.stackMove(self.id))
        self.connect(
            self.action,
            QtCore.SIGNAL("triggered()"),
            lambda: parent.move(
                self.datos['nombre']))

        self.verGrafica.clicked.connect(self.graficar)
        # self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),lambda: parent.aut(self.id,2) )
        # self.bvShowinfo.clicked.connect(self.weekPlot)
        self.tVentas.itemActivated.connect(self.mostrarResumen)
        self.pbListaVentas.clicked.connect(self.tablarVentas)
        self.bCorteT.clicked.connect(self.corte)
        self.bCorteP.clicked.connect(self.parcial)
        self.rbHoy.clicked.connect(self.dayPlot)
        self.rbSemana.clicked.connect(self.weekPlot)
        self.rbMes.clicked.connect(self.monthPlot)
        self.rbAnio.clicked.connect(self.yearPlot)
        self.tbPrint.clicked.connect(self.imprimirGrafica)
        self.tbImprimir.clicked.connect(self.imprimir)
        self.tVentas.setContextMenuPolicy(3)
        self.tVentas.customContextMenuRequested.connect(self.ocm)
        self.connect(
            self.deCorte,
            QtCore.SIGNAL("dateChanged ( const QDate)"),
            self.cambiarFecha)
        self.popMenu = QtWidgets.QMenu(self)
        action = self.popMenu.addAction(
            QtGui.QIcon("/usr/share/pyventa/images/16/block_16.png"), " Ignorar ")
        action.setIconVisibleInMenu(True)
        action2 = self.popMenu.addAction(
            QtGui.QIcon("/usr/share/pyventa/images/32/receipt.png"),
            " Reimprimir copia ")
        action2.setIconVisibleInMenu(True)
        action.triggered.connect(self.ignorarVentas)
        action2.triggered.connect(self.imprimirTicket)
        self.fecha = 'CURDATE()'
        self.deDesde.setDate(QtCore.QDate.currentDate())
        self.deHasta.setDate(QtCore.QDate.currentDate())
        self.deCorte.setDate(QtCore.QDate.currentDate())
        self.cbEscala.addItem("Hora", '%H')
        self.cbEscala.addItem("Dia", '%j')
        self.cbEscala.addItem("Dia de la semana", '%w')
        self.cbEscala.addItem("Semana", '%u')
        self.cbEscala.addItem("Mes", '%m')
        self.cbEscala.addItem("Anualidad", '%Y')
        # self.graf=QWidget(self)
        # self.vlVentas1.addWidget(self.graf)

    def setId(self, ide):
        self.id = ide
        self.datos['id'] = ide

    def setNivel(self, nivel):
        self.datos['nivel'] = nivel

    def datos(self):
        return self.datos
