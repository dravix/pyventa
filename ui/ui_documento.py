# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_documento.ui'
#
# Created: Thu Jul  8 07:15:34 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/Print-Preview-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tbImprimir = QtWidgets.QToolButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/32/Document-Print-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbImprimir.setIcon(icon1)
        self.tbImprimir.setIconSize(QtCore.QSize(24, 24))
        self.tbImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbImprimir.setAutoRaise(True)
        self.tbImprimir.setObjectName("tbImprimir")
        self.horizontalLayout_3.addWidget(self.tbImprimir)
        self.tbGuardar = QtWidgets.QToolButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/32/Save-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbGuardar.setIcon(icon2)
        self.tbGuardar.setIconSize(QtCore.QSize(24, 24))
        self.tbGuardar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbGuardar.setAutoRaise(True)
        self.tbGuardar.setObjectName("tbGuardar")
        self.horizontalLayout_3.addWidget(self.tbGuardar)
        self.titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.horizontalLayout_3.addWidget(self.titulo)
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 738, 468))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(342, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gvDocumento = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvDocumento.sizePolicy().hasHeightForWidth())
        self.gvDocumento.setSizePolicy(sizePolicy)
        self.gvDocumento.setObjectName("gvDocumento")
        self.horizontalLayout.addWidget(self.gvDocumento)
        spacerItem1 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Visor de documentos."))
        Form.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));"))
        self.widget.setStyleSheet(QtWidgets.QApplication.translate("Form", "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(42, 129, 159, 255), stop:0.495455 rgba(25, 99, 114, 255), stop:0.507692 rgba(42, 118, 149, 255), stop:1 rgba(58, 159, 202, 255));\n"
"color: rgb(255, 255, 255);", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tbImprimir.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background-color:none;"))
        self.tbImprimir.setText(QtCore.QCoreApplication.translate("Form", "Imprimir"))
        self.tbImprimir.setShortcut(QtCore.QCoreApplication.translate("Form", "Ctrl+P"))
        self.tbGuardar.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background-color:none;"))
        self.tbGuardar.setText(QtCore.QCoreApplication.translate("Form", "Guardar como PDF"))
        self.tbGuardar.setShortcut(QtCore.QCoreApplication.translate("Form", "Ctrl+G"))
        self.titulo.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background-color:none;"))
        self.titulo.setText(QtCore.QCoreApplication.translate("Form", "Titulo del documento"))
        self.gvDocumento.setStyleSheet(QtCore.QCoreApplication.translate("Form", "background-color: rgb(255, 255, 255);"))

