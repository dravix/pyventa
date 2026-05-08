# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_resumen.ui'
#
# Created: Thu Aug  2 03:43:15 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 325)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowOpacity(0.95)
        Form.setStyleSheet("background-color: rgb(14, 25, 26);color:#fff")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.info = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.info.setFont(font)
        self.info.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.info.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:none;")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cambio = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setWeight(75)
        font.setBold(True)
        self.cambio.setFont(font)
        self.cambio.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 0);")
        self.cambio.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.cambio.setObjectName("cambio")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cambio)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aceptar = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.aceptar.setFont(font)
        self.aceptar.setStyleSheet("*{padding:9px; border:2px solid  rgb(93, 207, 255); border-radius:12px; \n"
"color: #fff;\n"
"background-color:rgb(0, 170, 255);}\n"
"*:hover{background-color: rgb(0, 104, 156)}\n"
"*:pressed{background-color: rgb(0, 118, 177)}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/fx/button-check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.aceptar.setIcon(icon)
        self.aceptar.setIconSize(QtCore.QSize(32, 32))
        self.aceptar.setAutoDefault(True)
        self.aceptar.setDefault(True)
        self.aceptar.setObjectName("aceptar")
        self.horizontalLayout.addWidget(self.aceptar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Resumen de transaccion."))
        self.titulo.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background:none;"))
        self.titulo.setText(QtCore.QCoreApplication.translate("Form", "Resumen de transaccion "))
        self.info.setText(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"5\" cellpadding=\"0\">\n"
"<tr>\n"
"<td width=\"70%\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Total</span></p></td>\n"
"<td width=\"30%\">\n"
"<p align=\"right\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">$000.00</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Monto recibido: </span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">$000.00</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Num. de articulos: </span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">#000</span></p></td></tr></table></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_8.setText(QtCore.QCoreApplication.translate("Form", "Cambio:"))
        self.cambio.setText(QtCore.QCoreApplication.translate("Form", "$000.00"))
        self.aceptar.setText(QtCore.QCoreApplication.translate("Form", "Ok, cerrar"))
        self.aceptar.setShortcut(QtCore.QCoreApplication.translate("Form", "Return"))

