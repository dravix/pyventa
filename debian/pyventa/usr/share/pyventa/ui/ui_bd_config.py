# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/bd_config.ui'
#
# Created: Wed Jun  2 04:14:28 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 366)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.tserver = QtGui.QLineEdit(Dialog)
        self.tserver.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tserver.setObjectName("tserver")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.tserver)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.tuser = QtGui.QLineEdit(Dialog)
        self.tuser.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tuser.setObjectName("tuser")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.tuser)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.tpass = QtGui.QLineEdit(Dialog)
        self.tpass.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tpass.setEchoMode(QtGui.QLineEdit.Password)
        self.tpass.setObjectName("tpass")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.tpass)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.tdb = QtGui.QLineEdit(Dialog)
        self.tdb.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tdb.setObjectName("tdb")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.tdb)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.display = QtGui.QTextBrowser(Dialog)
        self.display.setEnabled(False)
        self.display.setLineWidth(2)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.bset = QtGui.QPushButton(self.splitter)
        self.bset.setEnabled(False)
        self.bset.setObjectName("bset")
        self.bprobar = QtGui.QPushButton(self.splitter)
        self.bprobar.setObjectName("bprobar")
        self.bclose = QtGui.QPushButton(self.splitter)
        self.bclose.setObjectName("bclose")
        self.bcreate = QtGui.QPushButton(self.splitter)
        self.bcreate.setObjectName("bcreate")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configuracion de base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgba(127, 191, 221,100);\n"
"border: 2px solid rgb(42, 110, 139);\n"
"border-radius:5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Configuraciones de la base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Servidor", None, QtGui.QApplication.UnicodeUTF8))
        self.tserver.setToolTip(QtGui.QApplication.translate("Dialog", "Este puede ser en IP o en nombre DNS", None, QtGui.QApplication.UnicodeUTF8))
        self.tserver.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.tuser.setToolTip(QtGui.QApplication.translate("Dialog", "Escriba un usuario con los permisos\n"
"necesarios para las operaciones de seleccion.", None, QtGui.QApplication.UnicodeUTF8))
        self.tuser.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Clave", None, QtGui.QApplication.UnicodeUTF8))
        self.tpass.setToolTip(QtGui.QApplication.translate("Dialog", "La clave se guardara bajo cifrado", None, QtGui.QApplication.UnicodeUTF8))
        self.tpass.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "DB", None, QtGui.QApplication.UnicodeUTF8))
        self.tdb.setToolTip(QtGui.QApplication.translate("Dialog", "El nombre de la base de datos.", None, QtGui.QApplication.UnicodeUTF8))
        self.tdb.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: rgba(220, 220, 220,100);\n"
"border: 2px solid  rgb(147, 147, 147);\n"
"border-radius:6px;", None, QtGui.QApplication.UnicodeUTF8))
        self.display.setStyleSheet(QtGui.QApplication.translate("Dialog", "color: rgb(44, 94, 132);", None, QtGui.QApplication.UnicodeUTF8))
        self.bset.setText(QtGui.QApplication.translate("Dialog", "Establecer", None, QtGui.QApplication.UnicodeUTF8))
        self.bprobar.setText(QtGui.QApplication.translate("Dialog", "Probar", None, QtGui.QApplication.UnicodeUTF8))
        self.bclose.setText(QtGui.QApplication.translate("Dialog", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.bcreate.setText(QtGui.QApplication.translate("Dialog", "Crear database", None, QtGui.QApplication.UnicodeUTF8))

