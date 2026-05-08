# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_agregar_deposito.ui'
#
# Created: Wed May  8 12:56:36 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(220, 119)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/32/llave.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("#Dialog{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));\n"
"\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fLine = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QLabel, QDoubleSpinBox{background:transparent; border:0px; padding:3px}")
        self.fLine.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fLine.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fLine.setObjectName("fLine")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.dsbInicial = QtWidgets.QDoubleSpinBox(self.fLine)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dsbInicial.setFont(font)
        self.dsbInicial.setFrame(False)
        self.dsbInicial.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbInicial.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbInicial.setMaximum(99999.99)
        self.dsbInicial.setObjectName("dsbInicial")
        self.horizontalLayout_51.addWidget(self.dsbInicial)
        self.verticalLayout.addWidget(self.fLine)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Spanish, QtCore.QLocale.Country.Mexico))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Deposito inicial"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", "Deposito de efectivo inicial: "))
        self.dsbInicial.setPrefix(QtCore.QCoreApplication.translate("Dialog", "$ "))

