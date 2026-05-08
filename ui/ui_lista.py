# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_lista.ui'
#
# Created: Tue Apr  2 15:03:45 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Listado(object):
    def setupUi(self, Listado):
        Listado.setObjectName("Listado")
        Listado.resize(381, 438)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/address_book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Listado.setWindowIcon(icon)
        Listado.setStyleSheet("#Editor{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QLabel{background:none;}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Listado)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Listado)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QtWidgets.QWidget(Listado)
        self.widget.setStyleSheet("background:none")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lvLista = QtWidgets.QTableView(self.widget)
        self.lvLista.setStyleSheet("background-color: rgb(240, 240, 255);\n"
"border:1.5px solid rgb(170, 181, 186)")
        self.lvLista.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.lvLista.setAlternatingRowColors(True)
        self.lvLista.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.lvLista.setSortingEnabled(True)
        self.lvLista.setObjectName("lvLista")
        self.lvLista.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.lvLista)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.masomenos = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.masomenos.sizePolicy().hasHeightForWidth())
        self.masomenos.setSizePolicy(sizePolicy)
        self.masomenos.setMaximumSize(QtCore.QSize(16777215, 22))
        self.masomenos.setStyleSheet("#masomenos{border-radius:0px;padding:2;\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
" \n"
"")
        self.masomenos.setObjectName("masomenos")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.masomenos)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tbMenos = QtWidgets.QToolButton(self.masomenos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMenos.sizePolicy().hasHeightForWidth())
        self.tbMenos.setSizePolicy(sizePolicy)
        self.tbMenos.setStyleSheet(" border:0px; padding:5 5 5 7;border-right:1px solid #999;border-radius:0;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/images/actions/color_18/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbMenos.setIcon(icon1)
        self.tbMenos.setIconSize(QtCore.QSize(12, 16))
        self.tbMenos.setObjectName("tbMenos")
        self.horizontalLayout_13.addWidget(self.tbMenos)
        self.tbMas = QtWidgets.QToolButton(self.masomenos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMas.sizePolicy().hasHeightForWidth())
        self.tbMas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbMas.setFont(font)
        self.tbMas.setStyleSheet(" border:0px;\n"
"padding:5 5 5 7;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/images/actions/color_18/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbMas.setIcon(icon2)
        self.tbMas.setIconSize(QtCore.QSize(16, 16))
        self.tbMas.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbMas.setObjectName("tbMas")
        self.horizontalLayout_13.addWidget(self.tbMas)
        self.horizontalLayout.addWidget(self.masomenos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Listado)
        QtCore.QMetaObject.connectSlotsByName(Listado)

    def retranslateUi(self, Listado):
        Listado.setWindowTitle(QtCore.QCoreApplication.translate("Listado", "Listado"))
        self.label.setText(QtCore.QCoreApplication.translate("Listado", "Lista"))
        self.tbMenos.setText(QtCore.QCoreApplication.translate("Listado", "Quitar"))
        self.tbMenos.setShortcut(QtCore.QCoreApplication.translate("Listado", "-"))
        self.tbMas.setText(QtCore.QCoreApplication.translate("Listado", "Agregar"))
        self.tbMas.setShortcut(QtCore.QCoreApplication.translate("Listado", "+"))
# 
import icons_rc
  # TODO: regenerate with pyrcc6