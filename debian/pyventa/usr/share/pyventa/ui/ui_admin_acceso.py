# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_admin_acceso.ui'
#
# Created: Thu Jun  7 01:45:40 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(284, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/padmin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("#Form{color: rgb(67, 67, 67);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(186, 186, 186, 255), stop:0.495455 rgba(190, 190, 190, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"QLineEdit{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(60, 60, 60, 255), stop:0.0730337 rgba(246, 246, 246, 255));border:1 solid rgb(158, 158, 158);border-radius:5;  color:#555; padding:3px;}\n"
"QPushButton{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));color:#333;border:1px solid #777;border-radius:5px;}"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/admin-alone.png")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lbInfo = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbInfo.sizePolicy().hasHeightForWidth())
        self.lbInfo.setSizePolicy(sizePolicy)
        self.lbInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo.setWordWrap(True)
        self.lbInfo.setObjectName(_fromUtf8("lbInfo"))
        self.verticalLayout.addWidget(self.lbInfo)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.leUsuario = QtGui.QLineEdit(Form)
        self.leUsuario.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.leUsuario.setFont(font)
        self.leUsuario.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.118182 rgba(255, 255, 255, 255), stop:0.281818 rgba(255, 255, 255, 255), stop:0.686364 rgba(250, 249, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:1px solid #888; border-radius:5px; padding:4px;"))
        self.leUsuario.setObjectName(_fromUtf8("leUsuario"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leUsuario)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.leClave = QtGui.QLineEdit(Form)
        self.leClave.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.leClave.setFont(font)
        self.leClave.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.118182 rgba(255, 255, 255, 255), stop:0.281818 rgba(255, 255, 255, 255), stop:0.686364 rgba(250, 249, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:1px solid #888; border-radius:5px; padding:4px;"))
        self.leClave.setEchoMode(QtGui.QLineEdit.Password)
        self.leClave.setObjectName(_fromUtf8("leClave"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.leClave)
        self.verticalLayout.addLayout(self.formLayout)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setMinimumSize(QtCore.QSize(0, 30))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pbCerrar = QtGui.QPushButton(self.splitter)
        self.pbCerrar.setMaximumSize(QtCore.QSize(120, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/16/delete_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCerrar.setIcon(icon1)
        self.pbCerrar.setIconSize(QtCore.QSize(16, 16))
        self.pbCerrar.setObjectName(_fromUtf8("pbCerrar"))
        self.pbAceptar = QtGui.QPushButton(self.splitter)
        self.pbAceptar.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pbAceptar.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/16/tick_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptar.setIcon(icon2)
        self.pbAceptar.setIconSize(QtCore.QSize(16, 16))
        self.pbAceptar.setObjectName(_fromUtf8("pbAceptar"))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Acceso a Padmin", None, QtGui.QApplication.UnicodeUTF8))
        self.lbInfo.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Bienvenido al administrador de Pyventa.<br /></span>Necesita identificarse como administrador de la empresa. </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Clave :", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCerrar.setText(QtGui.QApplication.translate("Form", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAceptar.setText(QtGui.QApplication.translate("Form", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))

