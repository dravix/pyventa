# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_calculo_descuentos.ui'
#
# Created: Tue Apr 30 03:02:35 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Calculo(object):
    def setupUi(self, Calculo):
        Calculo.setObjectName("Calculo")
        Calculo.resize(302, 198)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../Users/usr/share/pyventa/images/32/calculator-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Calculo.setWindowIcon(icon)
        Calculo.setStyleSheet("QWidget{border:0;\n"
"background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));}\n"
"QLabel{ border:0px; background:none}\n"
"QAbstractButton{ color:#fff;padding:5px; border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 255), stop:0.43 rgba(163, 163, 163, 255), stop:1 rgba(124, 124, 124, 255));\n"
"}\n"
"QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QAbstractButton::pressed{\n"
"color:#fff;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Calculo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Calculo)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(Calculo)
        self.frame_2.setStyleSheet("QWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QLineEdit, QDoubleSpinBox{background:#fff;color:#555;}\n"
"QLabel{background:transparent;color:#555;border:0px}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dsbPrecioDesc = QtWidgets.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbPrecioDesc.setFont(font)
        self.dsbPrecioDesc.setFrame(False)
        self.dsbPrecioDesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbPrecioDesc.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbPrecioDesc.setMaximum(100000.0)
        self.dsbPrecioDesc.setSingleStep(0.5)
        self.dsbPrecioDesc.setObjectName("dsbPrecioDesc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dsbPrecioDesc)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dsbDescuento = QtWidgets.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbDescuento.setFont(font)
        self.dsbDescuento.setFrame(False)
        self.dsbDescuento.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbDescuento.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbDescuento.setMaximum(100000.0)
        self.dsbDescuento.setObjectName("dsbDescuento")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dsbDescuento)
        self.dsbPrecio = QtWidgets.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbPrecio.setFont(font)
        self.dsbPrecio.setFrame(False)
        self.dsbPrecio.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbPrecio.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbPrecio.setMaximum(99999.99)
        self.dsbPrecio.setObjectName("dsbPrecio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dsbPrecio)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Calculo)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.fLine = QtWidgets.QFrame(Calculo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QToolButton, QLineEdit{background:transparent; border:0px; padding:3px}")
        self.fLine.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fLine.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fLine.setObjectName("fLine")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.verticalLayout.addWidget(self.fLine)

        self.retranslateUi(Calculo)
        QtCore.QMetaObject.connectSlotsByName(Calculo)

    def retranslateUi(self, Calculo):
        Calculo.setWindowTitle(QtCore.QCoreApplication.translate("Calculo", "Calculadora de descuentos"))
        self.label.setText(QtCore.QCoreApplication.translate("Calculo", "Calculo de descuentos."))
        self.label_4.setText(QtCore.QCoreApplication.translate("Calculo", "Precio con descuento"))
        self.dsbPrecioDesc.setPrefix(QtCore.QCoreApplication.translate("Calculo", "$"))
        self.label_5.setText(QtCore.QCoreApplication.translate("Calculo", "Descuento aplicado"))
        self.dsbDescuento.setSuffix(QtCore.QCoreApplication.translate("Calculo", "%"))
        self.dsbPrecio.setPrefix(QtCore.QCoreApplication.translate("Calculo", "$"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Calculo", "Precio publico"))

