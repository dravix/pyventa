# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_selector.ui'
#
# Created: Sun Mar 17 04:01:43 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Seleccion(object):
    def setupUi(self, Seleccion):
        Seleccion.setObjectName(_fromUtf8("Seleccion"))
        Seleccion.resize(508, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/binoculars.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Seleccion.setWindowIcon(icon)
        Seleccion.setStyleSheet(_fromUtf8("QHeaderView::section:horizontal,QHeaderView::section:horizontal{background-color: #1162A7;\n"
"border:0;color:#fff;padding:8 3 8 3;\n"
"}\n"
"QTableView{ \n"
"    selection-background-color:qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));alternate-background-color: #EDF1F2;border:0px solid #555;selection-color:#fff;} "))
        self.verticalLayout = QtGui.QVBoxLayout(Seleccion)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top = QtGui.QWidget(Seleccion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));"))
        self.top.setObjectName(_fromUtf8("top"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.top)
        self.horizontalLayout_14.setContentsMargins(2, 5, 2, 5)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.fLine = QtGui.QFrame(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QToolButton, QLineEdit{background:transparent; border:0px; padding:3px}"))
        self.fLine.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fLine.setFrameShadow(QtGui.QFrame.Raised)
        self.fLine.setObjectName(_fromUtf8("fLine"))
        self.horizontalLayout_51 = QtGui.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName(_fromUtf8("horizontalLayout_51"))
        self.leEntidad = QtGui.QLabel(self.fLine)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leEntidad.setFont(font)
        self.leEntidad.setObjectName(_fromUtf8("leEntidad"))
        self.horizontalLayout_51.addWidget(self.leEntidad)
        self.texto = QtGui.QLineEdit(self.fLine)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        self.texto.setObjectName(_fromUtf8("texto"))
        self.horizontalLayout_51.addWidget(self.texto)
        self.tbBuscar = QtGui.QToolButton(self.fLine)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tbBuscar.setFont(font)
        self.tbBuscar.setIcon(icon)
        self.tbBuscar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbBuscar.setObjectName(_fromUtf8("tbBuscar"))
        self.horizontalLayout_51.addWidget(self.tbBuscar)
        self.horizontalLayout_14.addWidget(self.fLine)
        self.verticalLayout.addWidget(self.top)
        self.tabla = QtGui.QTableView(Seleccion)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setSortingEnabled(True)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout.addWidget(self.tabla)

        self.retranslateUi(Seleccion)
        QtCore.QMetaObject.connectSlotsByName(Seleccion)

    def retranslateUi(self, Seleccion):
        Seleccion.setWindowTitle(QtGui.QApplication.translate("Seleccion", "Seleccione el cliente", None, QtGui.QApplication.UnicodeUTF8))
        Seleccion.setWindowFilePath(QtGui.QApplication.translate("Seleccion", "Qt::Popup", None, QtGui.QApplication.UnicodeUTF8))
        self.leEntidad.setStyleSheet(QtGui.QApplication.translate("Seleccion", "background:none", None, QtGui.QApplication.UnicodeUTF8))
        self.leEntidad.setText(QtGui.QApplication.translate("Seleccion", "Entidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbBuscar.setText(QtGui.QApplication.translate("Seleccion", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
