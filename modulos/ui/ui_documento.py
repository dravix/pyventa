# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_documento.ui'
#
# Created: Thu Jul  8 07:15:34 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/Print-Preview-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tbImprimir = QtGui.QToolButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/32/Document-Print-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbImprimir.setIcon(icon1)
        self.tbImprimir.setIconSize(QtCore.QSize(24, 24))
        self.tbImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbImprimir.setAutoRaise(True)
        self.tbImprimir.setObjectName("tbImprimir")
        self.horizontalLayout_3.addWidget(self.tbImprimir)
        self.tbGuardar = QtGui.QToolButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/32/Save-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbGuardar.setIcon(icon2)
        self.tbGuardar.setIconSize(QtCore.QSize(24, 24))
        self.tbGuardar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbGuardar.setAutoRaise(True)
        self.tbGuardar.setObjectName("tbGuardar")
        self.horizontalLayout_3.addWidget(self.tbGuardar)
        self.titulo = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.horizontalLayout_3.addWidget(self.titulo)
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 738, 468))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(342, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gvDocumento = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvDocumento.sizePolicy().hasHeightForWidth())
        self.gvDocumento.setSizePolicy(sizePolicy)
        self.gvDocumento.setObjectName("gvDocumento")
        self.horizontalLayout.addWidget(self.gvDocumento)
        spacerItem1 = QtGui.QSpacerItem(224, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Visor de documentos.", None, QtGui.QApplication.UnicodeUTF8))
        Form.setStyleSheet(QtGui.QApplication.translate("Form", "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("Form", "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(42, 129, 159, 255), stop:0.495455 rgba(25, 99, 114, 255), stop:0.507692 rgba(42, 118, 149, 255), stop:1 rgba(58, 159, 202, 255));\n"
"color: rgb(255, 255, 255);", None, QtGui.QApplication.UnicodeUTF8))
        self.tbImprimir.setStyleSheet(QtGui.QApplication.translate("Form", "background-color:none;", None, QtGui.QApplication.UnicodeUTF8))
        self.tbImprimir.setText(QtGui.QApplication.translate("Form", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.tbImprimir.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGuardar.setStyleSheet(QtGui.QApplication.translate("Form", "background-color:none;", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGuardar.setText(QtGui.QApplication.translate("Form", "Guardar como PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGuardar.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setStyleSheet(QtGui.QApplication.translate("Form", "background-color:none;", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setText(QtGui.QApplication.translate("Form", "Titulo del documento", None, QtGui.QApplication.UnicodeUTF8))
        self.gvDocumento.setStyleSheet(QtGui.QApplication.translate("Form", "background-color: rgb(255, 255, 255);", None, QtGui.QApplication.UnicodeUTF8))

