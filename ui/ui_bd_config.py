# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/bd_config.ui'
#
# Created: Wed Jun  2 04:14:28 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 366)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tserver = QtWidgets.QLineEdit(Dialog)
        self.tserver.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tserver.setObjectName("tserver")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tserver)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tuser = QtWidgets.QLineEdit(Dialog)
        self.tuser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tuser.setObjectName("tuser")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tuser)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tpass = QtWidgets.QLineEdit(Dialog)
        self.tpass.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tpass.setObjectName("tpass")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tpass)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.tdb = QtWidgets.QLineEdit(Dialog)
        self.tdb.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tdb.setObjectName("tdb")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tdb)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.display = QtWidgets.QTextBrowser(Dialog)
        self.display.setEnabled(False)
        self.display.setLineWidth(2)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.bset = QtWidgets.QPushButton(self.splitter)
        self.bset.setEnabled(False)
        self.bset.setObjectName("bset")
        self.bprobar = QtWidgets.QPushButton(self.splitter)
        self.bprobar.setObjectName("bprobar")
        self.bclose = QtWidgets.QPushButton(self.splitter)
        self.bclose.setObjectName("bclose")
        self.bcreate = QtWidgets.QPushButton(self.splitter)
        self.bcreate.setObjectName("bcreate")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Configuracion de base de datos"))
        self.label.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "background-color: rgba(127, 191, 221,100);\n"
"border: 2px solid rgb(42, 110, 139);\n"
"border-radius:5px;", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Configuraciones de la base de datos"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Dialog", "Servidor"))
        self.tserver.setToolTip(QtCore.QCoreApplication.translate("Dialog", "Este puede ser en IP o en nombre DNS"))
        self.tserver.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", "Usuario"))
        self.tuser.setToolTip(QtWidgets.QApplication.translate("Dialog", "Escriba un usuario con los permisos\n"
"necesarios para las operaciones de seleccion.", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tuser.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_5.setText(QtCore.QCoreApplication.translate("Dialog", "Clave"))
        self.tpass.setToolTip(QtCore.QCoreApplication.translate("Dialog", "La clave se guardara bajo cifrado"))
        self.tpass.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_4.setText(QtCore.QCoreApplication.translate("Dialog", "BD"))
        self.tdb.setToolTip(QtCore.QCoreApplication.translate("Dialog", "El nombre de la base de datos."))
        self.tdb.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtWidgets.QApplication.UnicodeUTF8))
        self.display.setStyleSheet(QtCore.QCoreApplication.translate("Dialog", "color: rgb(44, 94, 132);"))
        self.bset.setText(QtCore.QCoreApplication.translate("Dialog", "Establecer"))
        self.bprobar.setText(QtCore.QCoreApplication.translate("Dialog", "Probar"))
        self.bclose.setText(QtCore.QCoreApplication.translate("Dialog", "Cerrar"))
        self.bcreate.setText(QtCore.QCoreApplication.translate("Dialog", "Crear base de datos"))

