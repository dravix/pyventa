# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogos/ui_buscador.ui'
#
# Created: Thu Sep 30 03:37:46 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/search-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.barra_superior = QtWidgets.QWidget(Dialog)
        self.barra_superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.barra_superior.setObjectName("barra_superior")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.barra_superior)
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tbCancelar = QtWidgets.QToolButton(self.barra_superior)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.tbCancelar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/sub_blue_delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbCancelar.setIcon(icon1)
        self.tbCancelar.setIconSize(QtCore.QSize(16, 24))
        self.tbCancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCancelar.setObjectName("tbCancelar")
        self.horizontalLayout_14.addWidget(self.tbCancelar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.titulo = QtWidgets.QLabel(self.barra_superior)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.horizontalLayout_14.addWidget(self.titulo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.tbDone = QtWidgets.QToolButton(self.barra_superior)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.tbDone.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../usr/share/pyventa/images/32/sub_blue_accept.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbDone.setIcon(icon2)
        self.tbDone.setIconSize(QtCore.QSize(16, 24))
        self.tbDone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbDone.setObjectName("tbDone")
        self.horizontalLayout_14.addWidget(self.tbDone)
        self.verticalLayout_2.addWidget(self.barra_superior)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("""QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));border:1.3px solid #999; border-radius:12px; color:#fff; margin:5px;}
QLabel{ background:none;border:0}
QLineEdit{ 
background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.822727 rgba(251, 251, 251, 255), stop:1 rgba(139, 147, 149, 255)); color:#333;}""")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.leFiltro = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.leFiltro.setFont(font)
        self.leFiltro.setStyleSheet("""background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.822727 rgba(251, 251, 251, 255), stop:1 rgba(139, 147, 149, 255));
border:#bbb solid 1px;
color:#333;""")
        self.leFiltro.setObjectName("leFiltro")
        self.gridLayout.addWidget(self.leFiltro, 1, 0, 1, 1)
        self.cbFam = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbFam.setFont(font)
        self.cbFam.setObjectName("cbFam")
        self.gridLayout.addWidget(self.cbFam, 1, 2, 1, 1)
        self.lblFam = QtWidgets.QLabel(self.frame_4)
        self.lblFam.setObjectName("lblFam")
        self.gridLayout.addWidget(self.lblFam, 0, 2, 1, 1)
        self.cbDep = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbDep.setFont(font)
        self.cbDep.setObjectName("cbDep")
        self.gridLayout.addWidget(self.cbDep, 1, 1, 1, 1)
        self.lblDep = QtWidgets.QLabel(self.frame_4)
        self.lblDep.setObjectName("lblDep")
        self.gridLayout.addWidget(self.lblDep, 0, 1, 1, 1)
        self.lblInfo = QtWidgets.QLabel(self.frame_4)
        self.lblInfo.setObjectName("lblInfo")
        self.gridLayout.addWidget(self.lblInfo, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.twResulta = QtWidgets.QTableWidget(Dialog)
        self.twResulta.setStyleSheet("""selection-background-color: rgb(90, 203, 255);
selection-color: rgb(255, 255, 255);
background-color: rgb(226, 231, 255);""")
        self.twResulta.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.twResulta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.twResulta.setShowGrid(False)
        self.twResulta.setObjectName("twResulta")
        self.twResulta.setColumnCount(0)
        self.twResulta.setRowCount(0)
        self.twResulta.verticalHeader().setVisible(False)
        self.twResulta.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.twResulta)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.leFiltro, self.twResulta)
        Dialog.setTabOrder(self.twResulta, self.cbDep)
        Dialog.setTabOrder(self.cbDep, self.cbFam)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Buscador rapido."))
        self.barra_superior.setStyleSheet(QtWidgets.QApplication.translate("Dialog", " color:#fff;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(42, 129, 159, 255), stop:0.495455 rgba(25, 99, 114, 255), stop:0.507692 rgba(42, 118, 149, 255), stop:1 rgba(58, 159, 202, 255));", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tbCancelar.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "border:1.3px solid rgb(42, 129, 159); border-radius:12px; color:#fff;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 102, 128, 255), stop:0.563636 rgba(0, 34, 43, 255), stop:0.568182 rgba(0, 65, 82, 255), stop:1 rgba(0, 67, 85, 255));", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tbCancelar.setText(QtCore.QCoreApplication.translate("Dialog", "Cancelar"))
        self.titulo.setStyleSheet(QtCore.QCoreApplication.translate("Dialog", "background:none"))
        self.titulo.setText(QtCore.QCoreApplication.translate("Dialog", "Buscador de productos"))
        self.tbDone.setStyleSheet(QtWidgets.QApplication.translate("Dialog", "border:1.3px solid rgb(42, 129, 159); border-radius:12px; color:#fff;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 102, 128, 255), stop:0.563636 rgba(0, 34, 43, 255), stop:0.568182 rgba(0, 65, 82, 255), stop:1 rgba(0, 67, 85, 255));", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tbDone.setText(QtCore.QCoreApplication.translate("Dialog", "Aceptar"))
        self.lblFam.setText(QtCore.QCoreApplication.translate("Dialog", "Familia"))
        self.lblDep.setText(QtCore.QCoreApplication.translate("Dialog", "Departamento"))
        self.lblInfo.setText(QtCore.QCoreApplication.translate("Dialog", "Escriba la descripcion, la referencia o el codigo de barras"))
        self.twResulta.setToolTip(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selecciona el producto que buscas dando <span style=\" font-weight:600;\">doble click</span> sobre la fila.</p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))

