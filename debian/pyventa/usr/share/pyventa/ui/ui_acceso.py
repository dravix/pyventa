# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_simpleaccess.ui'
#
# Created: Thu Mar 21 23:00:21 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Acceso(object):
    def setupUi(self, Acceso):
        Acceso.setObjectName(_fromUtf8("Acceso"))
        Acceso.resize(365, 144)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/id.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Acceso.setWindowIcon(icon)
        Acceso.setStyleSheet(_fromUtf8(".QWidget{background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(228, 228, 228, 255));}\n"
"QLineEdit{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}"))
        self.verticalLayout = QtGui.QVBoxLayout(Acceso)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbInfo = QtGui.QLabel(Acceso)
        self.lbInfo.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.lbInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo.setWordWrap(True)
        self.lbInfo.setObjectName(_fromUtf8("lbInfo"))
        self.verticalLayout.addWidget(self.lbInfo)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.logo = QtGui.QLabel(Acceso)
        self.logo.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/pyventa.simple.logo.png")))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.horizontalLayout_2.addWidget(self.logo)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_19 = QtGui.QLabel(Acceso)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)
        self.leUsuario = QtGui.QLineEdit(Acceso)
        self.leUsuario.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.leUsuario.setFont(font)
        self.leUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.leUsuario.setObjectName(_fromUtf8("leUsuario"))
        self.gridLayout.addWidget(self.leUsuario, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(Acceso)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        self.leClave = QtGui.QLineEdit(Acceso)
        self.leClave.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.leClave.setFont(font)
        self.leClave.setEchoMode(QtGui.QLineEdit.Password)
        self.leClave.setAlignment(QtCore.Qt.AlignCenter)
        self.leClave.setObjectName(_fromUtf8("leClave"))
        self.gridLayout.addWidget(self.leClave, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbCerrar = QtGui.QPushButton(Acceso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(10)
        self.pbCerrar.setFont(font)
        self.pbCerrar.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QAbstractButton::hover{\n"
"color:#fff;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"\n"
"}"))
        self.pbCerrar.setObjectName(_fromUtf8("pbCerrar"))
        self.horizontalLayout.addWidget(self.pbCerrar)
        self.pbAceptar = QtGui.QPushButton(Acceso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pbAceptar.setFont(font)
        self.pbAceptar.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(10, 125, 159, 255), stop:1 rgba(0, 188, 255, 255));color:#fff;\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;\n"
"}\n"
"QAbstractButton::hover{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/actions/sticker/key.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon1)
        self.pbAceptar.setDefault(True)
        self.pbAceptar.setObjectName(_fromUtf8("pbAceptar"))
        self.horizontalLayout.addWidget(self.pbAceptar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Acceso)
        QtCore.QMetaObject.connectSlotsByName(Acceso)

    def retranslateUi(self, Acceso):
        Acceso.setWindowTitle(QtGui.QApplication.translate("Acceso", "Inicio de sesion", None, QtGui.QApplication.UnicodeUTF8))
        self.lbInfo.setText(QtGui.QApplication.translate("Acceso", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Punto de venta.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Acceso", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Acceso", "Clave:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCerrar.setText(QtGui.QApplication.translate("Acceso", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAceptar.setText(QtGui.QApplication.translate("Acceso", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
