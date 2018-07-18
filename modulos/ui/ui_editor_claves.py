# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_editor_claves.ui'
#
# Created: Fri Jul  2 07:13:57 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Claves(object):
    def setupUi(self, Claves):
        Claves.setObjectName("Claves")
        Claves.resize(329, 209)
        self.verticalLayout = QtGui.QVBoxLayout(Claves)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbUsuario = QtGui.QLabel(Claves)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lbUsuario.setFont(font)
        self.lbUsuario.setObjectName("lbUsuario")
        self.verticalLayout.addWidget(self.lbUsuario)
        self.lbAlerta = QtGui.QLabel(Claves)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbAlerta.setFont(font)
        self.lbAlerta.setObjectName("lbAlerta")
        self.verticalLayout.addWidget(self.lbAlerta)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Claves)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.leActual = QtGui.QLineEdit(Claves)
        self.leActual.setEchoMode(QtGui.QLineEdit.Password)
        self.leActual.setObjectName("leActual")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leActual)
        self.label_2 = QtGui.QLabel(Claves)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.leNueva = QtGui.QLineEdit(Claves)
        self.leNueva.setEchoMode(QtGui.QLineEdit.Password)
        self.leNueva.setObjectName("leNueva")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.leNueva)
        self.label_3 = QtGui.QLabel(Claves)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.leRepeticion = QtGui.QLineEdit(Claves)
        self.leRepeticion.setEchoMode(QtGui.QLineEdit.Password)
        self.leRepeticion.setObjectName("leRepeticion")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.leRepeticion)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Claves)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Claves)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Claves.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Claves.reject)
        QtCore.QMetaObject.connectSlotsByName(Claves)

    def retranslateUi(self, Claves):
        Claves.setWindowTitle(QtGui.QApplication.translate("Claves", "Cambio de clave", None, QtGui.QApplication.UnicodeUTF8))
        self.lbUsuario.setText(QtGui.QApplication.translate("Claves", "Usuario: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lbAlerta.setStyleSheet(QtGui.QApplication.translate("Claves", "color: rgb(159, 18, 18);", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Claves", "Clave actual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Claves", "Nueva clave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Claves", "Repita la clave", None, QtGui.QApplication.UnicodeUTF8))

