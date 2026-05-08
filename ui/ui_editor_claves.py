# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_editor_claves.ui'
#
# Created: Fri Jul  2 07:13:57 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Claves(object):
    def setupUi(self, Claves):
        Claves.setObjectName("Claves")
        Claves.resize(329, 209)
        self.verticalLayout = QtWidgets.QVBoxLayout(Claves)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbUsuario = QtWidgets.QLabel(Claves)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.lbUsuario.setFont(font)
        self.lbUsuario.setObjectName("lbUsuario")
        self.verticalLayout.addWidget(self.lbUsuario)
        self.lbAlerta = QtWidgets.QLabel(Claves)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbAlerta.setFont(font)
        self.lbAlerta.setObjectName("lbAlerta")
        self.verticalLayout.addWidget(self.lbAlerta)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Claves)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leActual = QtWidgets.QLineEdit(Claves)
        self.leActual.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leActual.setObjectName("leActual")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leActual)
        self.label_2 = QtWidgets.QLabel(Claves)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.leNueva = QtWidgets.QLineEdit(Claves)
        self.leNueva.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leNueva.setObjectName("leNueva")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leNueva)
        self.label_3 = QtWidgets.QLabel(Claves)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leRepeticion = QtWidgets.QLineEdit(Claves)
        self.leRepeticion.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leRepeticion.setObjectName("leRepeticion")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leRepeticion)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Claves)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Claves)
        self.buttonBox.accepted.connect(Claves.accept)
        self.buttonBox.rejected.connect(Claves.reject)
        QtCore.QMetaObject.connectSlotsByName(Claves)

    def retranslateUi(self, Claves):
        Claves.setWindowTitle(QtCore.QCoreApplication.translate("Claves", "Cambio de clave"))
        self.lbUsuario.setText(QtCore.QCoreApplication.translate("Claves", "Usuario: "))
        self.lbAlerta.setStyleSheet(QtCore.QCoreApplication.translate("Claves", "color: rgb(159, 18, 18);"))
        self.label.setText(QtCore.QCoreApplication.translate("Claves", "Clave actual"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Claves", "Nueva clave"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Claves", "Repita la clave"))

