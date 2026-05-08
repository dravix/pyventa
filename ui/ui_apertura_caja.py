# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_apertura_caja.ui'
#
# Created: Sat Oct 15 14:22:11 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(288, 155)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/32/llave.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(180, 180, 180, 255), stop:0.02 rgba(158, 158, 158, 255), stop:1 rgba(124, 124, 124, 255));color:#fff;border:0;}\n"
"QLabel{ border:0px; background:none}\n"
"QAbstractButton{ color:#fff;padding:5px; border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 255), stop:0.43 rgba(163, 163, 163, 255), stop:1 rgba(124, 124, 124, 255));\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setStyleSheet("QWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.05 #FDFDEE, stop:1 #FDFDEE);border-radius:5px; border:0;}\n"
"QLineEdit, QDoubleSpinBox,QLabel{background:#FDFDEE;color:#555;}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dsbInicial = QtWidgets.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.dsbInicial.setFont(font)
        self.dsbInicial.setFrame(False)
        self.dsbInicial.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbInicial.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbInicial.setMaximum(99999.99)
        self.dsbInicial.setObjectName("dsbInicial")
        self.horizontalLayout.addWidget(self.dsbInicial)
        self.verticalLayout.addWidget(self.frame_2)
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
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Apertura de caja"))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "Apertura de Caja"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", "Efectivo inicial: "))
        self.dsbInicial.setPrefix(QtCore.QCoreApplication.translate("Dialog", "$"))

