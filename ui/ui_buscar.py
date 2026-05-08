# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_buscar.ui'
#
# Created: Fri Mar 22 02:10:41 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(683, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(Form)
        self.top.setLineWidth(0)
        self.top.setObjectName("top")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.top)
        self.verticalLayout_2.setContentsMargins(5, 0, -1, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.cbDepartamentos = QtWidgets.QComboBox(self.top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDepartamentos.sizePolicy().hasHeightForWidth())
        self.cbDepartamentos.setSizePolicy(sizePolicy)
        self.cbDepartamentos.setObjectName("cbDepartamentos")
        self.gridLayout.addWidget(self.cbDepartamentos, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.top)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.titulo = QtWidgets.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.top)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.418182 rgba(255, 255, 255, 255));")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.tbusk = QtWidgets.QTableView(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tbusk.setFont(font)
        self.tbusk.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tbusk.setLineWidth(2)
        self.tbusk.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbusk.setAlternatingRowColors(True)
        self.tbusk.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tbusk.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbusk.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tbusk.setSortingEnabled(True)
        self.tbusk.setObjectName("tbusk")
        self.tbusk.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tbusk)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tbusk, self.cbDepartamentos)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Form"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Form", "Departamento:"))
        self.titulo.setText(QtCore.QCoreApplication.translate("Form", "Buscador de productos."))

