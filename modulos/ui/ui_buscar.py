# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_buscar.ui'
#
# Created: Fri Mar 22 02:10:41 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(683, 331)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top = QtGui.QFrame(Form)
        self.top.setLineWidth(0)
        self.top.setObjectName(_fromUtf8("top"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.top)
        self.verticalLayout_2.setContentsMargins(5, 0, -1, 5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbDepartamentos = QtGui.QComboBox(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDepartamentos.sizePolicy().hasHeightForWidth())
        self.cbDepartamentos.setSizePolicy(sizePolicy)
        self.cbDepartamentos.setObjectName(_fromUtf8("cbDepartamentos"))
        self.gridLayout.addWidget(self.cbDepartamentos, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.top)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.titulo = QtGui.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.top)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.418182 rgba(255, 255, 255, 255));"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout.addWidget(self.widget_2)
        self.tbusk = QtGui.QTableView(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tbusk.setFont(font)
        self.tbusk.setFrameShadow(QtGui.QFrame.Plain)
        self.tbusk.setLineWidth(2)
        self.tbusk.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbusk.setAlternatingRowColors(True)
        self.tbusk.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tbusk.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbusk.setGridStyle(QtCore.Qt.SolidLine)
        self.tbusk.setSortingEnabled(True)
        self.tbusk.setObjectName(_fromUtf8("tbusk"))
        self.tbusk.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tbusk)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tbusk, self.cbDepartamentos)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Departamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setText(QtGui.QApplication.translate("Form", "Buscador de productos.", None, QtGui.QApplication.UnicodeUTF8))

