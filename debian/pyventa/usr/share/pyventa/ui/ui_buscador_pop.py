# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_buscador_pop.ui'
#
# Created: Wed Nov  2 05:01:41 2011
#      by: PyQt4 UI code generator 4.8.3
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
        Dialog.resize(649, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/32/search-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_4 = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(_fromUtf8("QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));border:1.3px solid #999;  color:#555; padding:5px}\n"
"QLabel{ background:none;border:0}\n"
"QLineEdit{ \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.822727 rgba(251, 251, 251, 255), stop:1 rgba(139, 147, 149, 255)); color:#333;}\n"
"\n"
""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_45 = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setMaximumSize(QtCore.QSize(32, 32))
        self.label_45.setStyleSheet(_fromUtf8("background:0;"))
        self.label_45.setText(_fromUtf8(""))
        self.label_45.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../usr/share/pyventa/images/png/buscar_in.png")))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_2.addWidget(self.label_45)
        self.label_20 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_2.addWidget(self.label_20)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fBuscador = QtGui.QFrame(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fBuscador.sizePolicy().hasHeightForWidth())
        self.fBuscador.setSizePolicy(sizePolicy)
        self.fBuscador.setStyleSheet(_fromUtf8("#fBuscador{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.822727 rgba(251, 251, 251, 255), stop:1 rgba(139, 147, 149, 255));\n"
"border:#bbb solid 1px;\n"
"border-radius:5px;\n"
"color:#333;\n"
"}\n"
"#fBuscador QLineEdit, #fBuscador QToolButton{background:none;border:0;}#"))
        self.fBuscador.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fBuscador.setFrameShadow(QtGui.QFrame.Raised)
        self.fBuscador.setObjectName(_fromUtf8("fBuscador"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.fBuscador)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.leFiltro = QtGui.QLineEdit(self.fBuscador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leFiltro.sizePolicy().hasHeightForWidth())
        self.leFiltro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.leFiltro.setFont(font)
        self.leFiltro.setStyleSheet(_fromUtf8("background:rgba(0,0,0,0)"))
        self.leFiltro.setObjectName(_fromUtf8("leFiltro"))
        self.horizontalLayout_4.addWidget(self.leFiltro)
        self.pbBuscar = QtGui.QToolButton(self.fBuscador)
        self.pbBuscar.setIcon(icon)
        self.pbBuscar.setIconSize(QtCore.QSize(32, 32))
        self.pbBuscar.setObjectName(_fromUtf8("pbBuscar"))
        self.horizontalLayout_4.addWidget(self.pbBuscar)
        self.horizontalLayout.addWidget(self.fBuscador)
        self.comboBox = QtGui.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tvResulta = QtGui.QTableView(Dialog)
        self.tvResulta.setStyleSheet(_fromUtf8("selection-background-color: rgb(90, 203, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 231, 255);"))
        self.tvResulta.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tvResulta.setAlternatingRowColors(True)
        self.tvResulta.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tvResulta.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tvResulta.setSortingEnabled(True)
        self.tvResulta.setObjectName(_fromUtf8("tvResulta"))
        self.verticalLayout_3.addWidget(self.tvResulta)
        self.frame_5 = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(_fromUtf8("QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(137, 137, 137, 255), stop:0.0545455 rgba(156, 156, 156, 255), stop:1 rgba(191, 191, 191, 255));border:1.3px solid #999;  color:#555; padding:5px}\n"
"QLabel{ background:none;border:0}\n"
"QLineEdit{ \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.822727 rgba(251, 251, 251, 255), stop:1 rgba(139, 147, 149, 255)); color:#333;}\n"
"\n"
""))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Dual_4 = QtGui.QSplitter(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dual_4.sizePolicy().hasHeightForWidth())
        self.Dual_4.setSizePolicy(sizePolicy)
        self.Dual_4.setStyleSheet(_fromUtf8("QSplitter{border-radius:4px;\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QToolButton{padding:2px}\n"
" \n"
""))
        self.Dual_4.setLineWidth(0)
        self.Dual_4.setOrientation(QtCore.Qt.Horizontal)
        self.Dual_4.setHandleWidth(1)
        self.Dual_4.setObjectName(_fromUtf8("Dual_4"))
        self.tbCancelar = QtGui.QToolButton(self.Dual_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbCancelar.setFont(font)
        self.tbCancelar.setStyleSheet(_fromUtf8(" border:0px;border-right:1px solid #999;border-radius:0;\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/16/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbCancelar.setIcon(icon1)
        self.tbCancelar.setIconSize(QtCore.QSize(16, 16))
        self.tbCancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCancelar.setObjectName(_fromUtf8("tbCancelar"))
        self.tbDone = QtGui.QToolButton(self.Dual_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbDone.setFont(font)
        self.tbDone.setStyleSheet(_fromUtf8(" border:0px;\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/32/sub_black_accept.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbDone.setIcon(icon2)
        self.tbDone.setIconSize(QtCore.QSize(16, 20))
        self.tbDone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbDone.setObjectName(_fromUtf8("tbDone"))
        self.horizontalLayout_3.addWidget(self.Dual_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.frame_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Buscador rapido.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setStyleSheet(QtGui.QApplication.translate("Dialog", "background:none", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "Buscador", None, QtGui.QApplication.UnicodeUTF8))
        self.leFiltro.setToolTip(QtGui.QApplication.translate("Dialog", "Escriba la descripcion de lo que busca y presione <b>ENTER</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbBuscar.setText(QtGui.QApplication.translate("Dialog", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setToolTip(QtGui.QApplication.translate("Dialog", "Buscar en", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Familias", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Departamentos", None, QtGui.QApplication.UnicodeUTF8))
        self.tvResulta.setToolTip(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selecciona el producto que buscas dando <span style=\" font-weight:600;\">doble click</span> sobre la fila.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbDone.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

