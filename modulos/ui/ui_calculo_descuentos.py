# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_calculo_descuentos.ui'
#
# Created: Tue Apr 30 03:02:35 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Calculo(object):
    def setupUi(self, Calculo):
        Calculo.setObjectName(_fromUtf8("Calculo"))
        Calculo.resize(302, 198)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../Users/usr/share/pyventa/images/32/calculator-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculo.setWindowIcon(icon)
        Calculo.setStyleSheet(_fromUtf8("QWidget{border:0;\n"
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
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Calculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Calculo)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtGui.QFrame(Calculo)
        self.frame_2.setStyleSheet(_fromUtf8("QWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QLineEdit, QDoubleSpinBox{background:#fff;color:#555;}\n"
"QLabel{background:transparent;color:#555;border:0px}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dsbPrecioDesc = QtGui.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbPrecioDesc.setFont(font)
        self.dsbPrecioDesc.setFrame(False)
        self.dsbPrecioDesc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbPrecioDesc.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbPrecioDesc.setMaximum(100000.0)
        self.dsbPrecioDesc.setSingleStep(0.5)
        self.dsbPrecioDesc.setObjectName(_fromUtf8("dsbPrecioDesc"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dsbPrecioDesc)
        self.label_5 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dsbDescuento = QtGui.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbDescuento.setFont(font)
        self.dsbDescuento.setFrame(False)
        self.dsbDescuento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbDescuento.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbDescuento.setMaximum(100000.0)
        self.dsbDescuento.setObjectName(_fromUtf8("dsbDescuento"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dsbDescuento)
        self.dsbPrecio = QtGui.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbPrecio.setFont(font)
        self.dsbPrecio.setFrame(False)
        self.dsbPrecio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbPrecio.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbPrecio.setMaximum(99999.99)
        self.dsbPrecio.setObjectName(_fromUtf8("dsbPrecio"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dsbPrecio)
        self.label_3 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtGui.QDialogButtonBox(Calculo)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.fLine = QtGui.QFrame(Calculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QToolButton, QLineEdit{background:transparent; border:0px; padding:3px}"))
        self.fLine.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fLine.setFrameShadow(QtGui.QFrame.Raised)
        self.fLine.setObjectName(_fromUtf8("fLine"))
        self.horizontalLayout_51 = QtGui.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName(_fromUtf8("horizontalLayout_51"))
        self.verticalLayout.addWidget(self.fLine)

        self.retranslateUi(Calculo)
        QtCore.QMetaObject.connectSlotsByName(Calculo)

    def retranslateUi(self, Calculo):
        Calculo.setWindowTitle(QtGui.QApplication.translate("Calculo", "Calculadora de descuentos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Calculo", "Calculo de descuentos.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Calculo", "Precio con descuento", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbPrecioDesc.setPrefix(QtGui.QApplication.translate("Calculo", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Calculo", "Descuento aplicado", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbDescuento.setSuffix(QtGui.QApplication.translate("Calculo", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbPrecio.setPrefix(QtGui.QApplication.translate("Calculo", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Calculo", "Precio publico", None, QtGui.QApplication.UnicodeUTF8))

