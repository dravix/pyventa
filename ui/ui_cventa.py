# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_cventa.ui'
#
# Created: Wed Mar 23 23:52:39 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 243)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.trNoprint = QtGui.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trNoprint.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/32/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trNoprint.setIcon(icon)
        self.trNoprint.setChecked(True)
        self.trNoprint.setObjectName("trNoprint")
        self.verticalLayout.addWidget(self.trNoprint)
        self.cobro = QtGui.QWidget(Form)
        self.cobro.setEnabled(True)
        self.cobro.setObjectName("cobro")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.cobro)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ltotal = QtGui.QLabel(self.cobro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ltotal.setFont(font)
        self.ltotal.setObjectName("ltotal")
        self.horizontalLayout_4.addWidget(self.ltotal)
        self.total = QtGui.QLabel(self.cobro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total.sizePolicy().hasHeightForWidth())
        self.total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.total.setFont(font)
        self.total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total.setObjectName("total")
        self.horizontalLayout_4.addWidget(self.total)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.cobro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.trecibo = QtGui.QDoubleSpinBox(self.cobro)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.trecibo.setFont(font)
        self.trecibo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.trecibo.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.trecibo.setAccelerated(True)
        self.trecibo.setMaximum(99999.99)
        self.trecibo.setObjectName("trecibo")
        self.horizontalLayout_3.addWidget(self.trecibo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bPagoCredito = QtGui.QPushButton(self.cobro)
        self.bPagoCredito.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPagoCredito.sizePolicy().hasHeightForWidth())
        self.bPagoCredito.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/32/vcards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bPagoCredito.setIcon(icon1)
        self.bPagoCredito.setChecked(False)
        self.bPagoCredito.setObjectName("bPagoCredito")
        self.horizontalLayout.addWidget(self.bPagoCredito)
        self.bPagoPendiente = QtGui.QPushButton(self.cobro)
        self.bPagoPendiente.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bPagoPendiente.sizePolicy().hasHeightForWidth())
        self.bPagoPendiente.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/32/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bPagoPendiente.setIcon(icon2)
        self.bPagoPendiente.setChecked(False)
        self.bPagoPendiente.setObjectName("bPagoPendiente")
        self.horizontalLayout.addWidget(self.bPagoPendiente)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.cobro)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Cerrar nota", None, QtGui.QApplication.UnicodeUTF8))
        self.trNoprint.setText(QtGui.QApplication.translate("Form", "Imprimir comprobante.", None, QtGui.QApplication.UnicodeUTF8))
        self.ltotal.setText(QtGui.QApplication.translate("Form", "Total:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.total.setText(QtGui.QApplication.translate("Form", "$000.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Recibo:", None, QtGui.QApplication.UnicodeUTF8))
        self.bPagoCredito.setText(QtGui.QApplication.translate("Form", "Pago  con credito", None, QtGui.QApplication.UnicodeUTF8))
        self.bPagoPendiente.setText(QtGui.QApplication.translate("Form", "Pago  pendiente", None, QtGui.QApplication.UnicodeUTF8))

