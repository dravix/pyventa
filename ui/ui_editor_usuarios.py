# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_editor_usuario.ui'
#
# Created: Fri Jul  2 08:18:57 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 186)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/User-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leNombre = QtWidgets.QLineEdit(Dialog)
        self.leNombre.setObjectName("leNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leNombre)
        self.leUsuario = QtWidgets.QLineEdit(Dialog)
        self.leUsuario.setMaximumSize(QtCore.QSize(150, 16777215))
        self.leUsuario.setObjectName("leUsuario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leUsuario)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leClave = QtWidgets.QLineEdit(Dialog)
        self.leClave.setMaximumSize(QtCore.QSize(150, 16777215))
        self.leClave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leClave.setObjectName("leClave")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leClave)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cbNivel = QtWidgets.QComboBox(Dialog)
        self.cbNivel.setObjectName("cbNivel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbNivel)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Editor de usuarios"))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Nombre completo:"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Dialog", "Usuario"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", "Clave"))
        self.label_4.setText(QtCore.QCoreApplication.translate("Dialog", "Nivel"))

