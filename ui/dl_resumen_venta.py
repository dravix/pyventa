# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dl_resumen_venta.ui'
#
# Created: Fri Dec 17 03:51:00 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 519)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/receipt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(42, 133, 163, 255), stop:1 rgba(116, 176, 202, 255));\n"
"color:#fff;")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbResumen = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbResumen.setFont(font)
        self.lbResumen.setStyleSheet("background:none;")
        self.lbResumen.setText("")
        self.lbResumen.setObjectName("lbResumen")
        self.verticalLayout.addWidget(self.lbResumen)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.twProductos = QtWidgets.QTableWidget(Dialog)
        self.twProductos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.twProductos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.twProductos.setShowGrid(False)
        self.twProductos.setObjectName("twProductos")
        self.twProductos.setColumnCount(0)
        self.twProductos.setRowCount(0)
        self.twProductos.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.twProductos)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Resumen de venta"))
        self.groupBox.setTitle(QtCore.QCoreApplication.translate("Dialog", "Resumen de venta"))

