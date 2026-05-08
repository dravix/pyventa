# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_editor_familia.ui'
#
# Created: Wed Jun 23 16:43:04 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 215)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/address_blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setObjectName("label_35")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.leNombre = QtWidgets.QLineEdit(Dialog)
        self.leNombre.setObjectName("leNombre")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leNombre)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cbDepartamentos = QtWidgets.QComboBox(Dialog)
        self.cbDepartamentos.setObjectName("cbDepartamentos")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbDepartamentos)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dsbDescuento = QtWidgets.QDoubleSpinBox(Dialog)
        self.dsbDescuento.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbDescuento.setAccelerated(True)
        self.dsbDescuento.setObjectName("dsbDescuento")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dsbDescuento)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sbMinimo = QtWidgets.QSpinBox(Dialog)
        self.sbMinimo.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sbMinimo.setAccelerated(True)
        self.sbMinimo.setMaximum(9999)
        self.sbMinimo.setObjectName("sbMinimo")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbMinimo)
        self.verticalLayout.addLayout(self.formLayout_3)
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
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Edicion de familia"))
        self.label_35.setText(QtCore.QCoreApplication.translate("Dialog", "Nombre"))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Departamento"))
        self.cbDepartamentos.setToolTip(QtCore.QCoreApplication.translate("Dialog", "El departamento al que pertenece esta familia."))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Descuento\n"
"de mayoreo %", None, QtWidgets.QApplication.UnicodeUTF8))
        self.dsbDescuento.setToolTip(QtCore.QCoreApplication.translate("Dialog", "Este descuento se aplica al precio publico de cada producto que pertenezca a esta familia."))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", "Piezas minimas"))
        self.sbMinimo.setToolTip(QtCore.QCoreApplication.translate("Dialog", "Cantidad minima de articulos conprados para aplicar mayoreo"))

