# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_visor_venta.ui'
#
# Created: Mon May 13 17:59:44 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(521, 519)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/window.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QHeaderView::section:horizontal,QHeaderView::section:horizontal{background-color: #1162A7;\n"
"border:0;color:#fff;padding:8 3 8 3;\n"
"}\n"
"QTableView{ \n"
"    selection-background-color:qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));alternate-background-color: #EDF1F2;border:0px solid #555;selection-color:#fff;} "))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbResumen = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbResumen.setFont(font)
        self.lbResumen.setStyleSheet(_fromUtf8(".QLabel{    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));color:#333;}"))
        self.lbResumen.setText(_fromUtf8(""))
        self.lbResumen.setMargin(5)
        self.lbResumen.setObjectName(_fromUtf8("lbResumen"))
        self.verticalLayout_2.addWidget(self.lbResumen)
        self.tvProductos = QtGui.QTableView(Dialog)
        self.tvProductos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tvProductos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tvProductos.setShowGrid(False)
        self.tvProductos.setObjectName(_fromUtf8("tvProductos"))
        self.tvProductos.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tvProductos)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Resumen de venta", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
