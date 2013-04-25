# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_editor_familia.ui'
#
# Created: Wed Jun 23 16:43:04 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 215)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/address_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_35 = QtGui.QLabel(Dialog)
        self.label_35.setObjectName("label_35")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_35)
        self.leNombre = QtGui.QLineEdit(Dialog)
        self.leNombre.setObjectName("leNombre")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.leNombre)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.cbDepartamentos = QtGui.QComboBox(Dialog)
        self.cbDepartamentos.setObjectName("cbDepartamentos")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbDepartamentos)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dsbDescuento = QtGui.QDoubleSpinBox(Dialog)
        self.dsbDescuento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbDescuento.setAccelerated(True)
        self.dsbDescuento.setObjectName("dsbDescuento")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.dsbDescuento)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.sbMinimo = QtGui.QSpinBox(Dialog)
        self.sbMinimo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbMinimo.setAccelerated(True)
        self.sbMinimo.setMaximum(9999)
        self.sbMinimo.setObjectName("sbMinimo")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.sbMinimo)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edicion de familia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Departamento", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDepartamentos.setToolTip(QtGui.QApplication.translate("Dialog", "El departamento al que pertenece esta familia.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Descuento\n"
"de mayoreo %", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbDescuento.setToolTip(QtGui.QApplication.translate("Dialog", "Este descuento se aplica al precio publico de cada producto que pertenezca a esta familia.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Piezas minimas", None, QtGui.QApplication.UnicodeUTF8))
        self.sbMinimo.setToolTip(QtGui.QApplication.translate("Dialog", "Cantidad minima de articulos conprados para aplicar mayoreo", None, QtGui.QApplication.UnicodeUTF8))

