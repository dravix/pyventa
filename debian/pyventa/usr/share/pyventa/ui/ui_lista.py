# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_lista.ui'
#
# Created: Tue Apr  2 15:03:45 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Listado(object):
    def setupUi(self, Listado):
        Listado.setObjectName(_fromUtf8("Listado"))
        Listado.resize(381, 438)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/32/address_book.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Listado.setWindowIcon(icon)
        Listado.setStyleSheet(_fromUtf8("#Editor{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QLabel{background:none;}\n"
""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Listado)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Listado)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QtGui.QWidget(Listado)
        self.widget.setStyleSheet(_fromUtf8("background:none"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lvLista = QtGui.QTableView(self.widget)
        self.lvLista.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 255);\n"
"border:1.5px solid rgb(170, 181, 186)"))
        self.lvLista.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lvLista.setAlternatingRowColors(True)
        self.lvLista.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lvLista.setSortingEnabled(True)
        self.lvLista.setObjectName(_fromUtf8("lvLista"))
        self.lvLista.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.lvLista)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.masomenos = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.masomenos.sizePolicy().hasHeightForWidth())
        self.masomenos.setSizePolicy(sizePolicy)
        self.masomenos.setMaximumSize(QtCore.QSize(16777215, 22))
        self.masomenos.setStyleSheet(_fromUtf8("#masomenos{border-radius:0px;padding:2;\n"
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
""))
        self.masomenos.setObjectName(_fromUtf8("masomenos"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.masomenos)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.tbMenos = QtGui.QToolButton(self.masomenos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMenos.sizePolicy().hasHeightForWidth())
        self.tbMenos.setSizePolicy(sizePolicy)
        self.tbMenos.setStyleSheet(_fromUtf8(" border:0px; padding:5 5 5 7;border-right:1px solid #999;border-radius:0;\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMenos.setIcon(icon1)
        self.tbMenos.setIconSize(QtCore.QSize(12, 16))
        self.tbMenos.setObjectName(_fromUtf8("tbMenos"))
        self.horizontalLayout_13.addWidget(self.tbMenos)
        self.tbMas = QtGui.QToolButton(self.masomenos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMas.sizePolicy().hasHeightForWidth())
        self.tbMas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbMas.setFont(font)
        self.tbMas.setStyleSheet(_fromUtf8(" border:0px;\n"
"padding:5 5 5 7;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMas.setIcon(icon2)
        self.tbMas.setIconSize(QtCore.QSize(16, 16))
        self.tbMas.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbMas.setObjectName(_fromUtf8("tbMas"))
        self.horizontalLayout_13.addWidget(self.tbMas)
        self.horizontalLayout.addWidget(self.masomenos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Listado)
        QtCore.QMetaObject.connectSlotsByName(Listado)

    def retranslateUi(self, Listado):
        Listado.setWindowTitle(QtGui.QApplication.translate("Listado", "Listado", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Listado", "Lista", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMenos.setText(QtGui.QApplication.translate("Listado", "Quitar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMenos.setShortcut(QtGui.QApplication.translate("Listado", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMas.setText(QtGui.QApplication.translate("Listado", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMas.setShortcut(QtGui.QApplication.translate("Listado", "+", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
