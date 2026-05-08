# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_selector.ui'
#
# Created: Sun Mar 17 04:01:43 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Seleccion(object):
    def setupUi(self, Seleccion):
        Seleccion.setObjectName("Seleccion")
        Seleccion.resize(508, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/images/actions/color_18/binoculars.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Seleccion.setWindowIcon(icon)
        Seleccion.setStyleSheet("QHeaderView::section:horizontal,QHeaderView::section:horizontal{background-color: #1162A7;\n"
"border:0;color:#fff;padding:8 3 8 3;\n"
"}\n"
"QTableView{ \n"
"    selection-background-color:qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));alternate-background-color: #EDF1F2;border:0px solid #555;selection-color:#fff;} ")
        self.verticalLayout = QtWidgets.QVBoxLayout(Seleccion)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QWidget(Seleccion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));")
        self.top.setObjectName("top")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_14.setContentsMargins(2, 5, 2, 5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.fLine = QtWidgets.QFrame(self.top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QToolButton, QLineEdit{background:transparent; border:0px; padding:3px}")
        self.fLine.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fLine.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fLine.setObjectName("fLine")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.leEntidad = QtWidgets.QLabel(self.fLine)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.leEntidad.setFont(font)
        self.leEntidad.setObjectName("leEntidad")
        self.horizontalLayout_51.addWidget(self.leEntidad)
        self.texto = QtWidgets.QLineEdit(self.fLine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        self.texto.setObjectName("texto")
        self.horizontalLayout_51.addWidget(self.texto)
        self.tbBuscar = QtWidgets.QToolButton(self.fLine)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tbBuscar.setFont(font)
        self.tbBuscar.setIcon(icon)
        self.tbBuscar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbBuscar.setObjectName("tbBuscar")
        self.horizontalLayout_51.addWidget(self.tbBuscar)
        self.horizontalLayout_14.addWidget(self.fLine)
        self.verticalLayout.addWidget(self.top)
        self.tabla = QtWidgets.QTableView(Seleccion)
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla.setSortingEnabled(True)
        self.tabla.setObjectName("tabla")
        self.verticalLayout.addWidget(self.tabla)

        self.retranslateUi(Seleccion)
        QtCore.QMetaObject.connectSlotsByName(Seleccion)

    def retranslateUi(self, Seleccion):
        Seleccion.setWindowTitle(QtCore.QCoreApplication.translate("Seleccion", "Seleccione el cliente"))
        Seleccion.setWindowFilePath(QtCore.QCoreApplication.translate("Seleccion", "Qt::Popup"))
        self.leEntidad.setStyleSheet(QtCore.QCoreApplication.translate("Seleccion", "background:none"))
        self.leEntidad.setText(QtCore.QCoreApplication.translate("Seleccion", "Entidad:"))
        self.tbBuscar.setText(QtCore.QCoreApplication.translate("Seleccion", "Buscar"))
# 
import icons_rc
  # TODO: regenerate with pyrcc6