# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_marcar_faltante.ui'
#
# Created: Fri Dec  9 06:30:08 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Faltante(object):
    def setupUi(self, Faltante):
        Faltante.setObjectName(_fromUtf8("Faltante"))
        Faltante.resize(316, 200)
        Faltante.setStyleSheet(_fromUtf8("QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(180, 180, 180, 255), stop:0.02 rgba(158, 158, 158, 255), stop:1 rgba(124, 124, 124, 255));color:#fff;border:0;}\n"
"QLabel{ border:0px; background:none; color:#fff}\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Faltante)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbProducto = QtGui.QLabel(Faltante)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbProducto.sizePolicy().hasHeightForWidth())
        self.lbProducto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.lbProducto.setFont(font)
        self.lbProducto.setWordWrap(True)
        self.lbProducto.setMargin(1)
        self.lbProducto.setObjectName(_fromUtf8("lbProducto"))
        self.verticalLayout.addWidget(self.lbProducto)
        self.frame_2 = QtGui.QFrame(Faltante)
        self.frame_2.setStyleSheet(_fromUtf8("QWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.05 #FDFDEE, stop:1 #FDFDEE);border-radius:5px; border:0;}\n"
"QLineEdit, QDoubleSpinBox,QLabel{background:#FDFDEE;color:#555;}\n"
"QComboBox{\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"QComboBox *{background:rgb(190, 212, 221)}\n"
" QComboBox:editable {\n"
"padding:5;\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"        \n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 17px;\n"
"     border-left-width: 3px;\n"
"     border-left-color:none;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"     image: url(/usr/share/pyventa/images/16/zoom-in.png);\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.dsbCantidad = QtGui.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.dsbCantidad.setFont(font)
        self.dsbCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbCantidad.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbCantidad.setMaximum(99999.99)
        self.dsbCantidad.setProperty(_fromUtf8("value"), 1.0)
        self.dsbCantidad.setObjectName(_fromUtf8("dsbCantidad"))
        self.gridLayout.addWidget(self.dsbCantidad, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cbPrioridad = QtGui.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.cbPrioridad.setFont(font)
        self.cbPrioridad.setObjectName(_fromUtf8("cbPrioridad"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/warning_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbPrioridad.addItem(icon, _fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/view-sort-descending.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbPrioridad.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/tick_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbPrioridad.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/view-sort-ascending.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbPrioridad.addItem(icon3, _fromUtf8(""))
        self.gridLayout.addWidget(self.cbPrioridad, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Dual_3 = QtGui.QSplitter(Faltante)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dual_3.sizePolicy().hasHeightForWidth())
        self.Dual_3.setSizePolicy(sizePolicy)
        self.Dual_3.setStyleSheet(_fromUtf8("QSplitter{border-radius:4px;\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QToolButton{padding:4px}\n"
" \n"
""))
        self.Dual_3.setLineWidth(0)
        self.Dual_3.setMidLineWidth(1)
        self.Dual_3.setOrientation(QtCore.Qt.Horizontal)
        self.Dual_3.setHandleWidth(1)
        self.Dual_3.setObjectName(_fromUtf8("Dual_3"))
        self.tbCerrar = QtGui.QToolButton(self.Dual_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbCerrar.sizePolicy().hasHeightForWidth())
        self.tbCerrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbCerrar.setFont(font)
        self.tbCerrar.setStyleSheet(_fromUtf8(" border:0px;border-right:1px solid #999;border-radius:0;\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/16/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbCerrar.setIcon(icon4)
        self.tbCerrar.setIconSize(QtCore.QSize(12, 16))
        self.tbCerrar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCerrar.setObjectName(_fromUtf8("tbCerrar"))
        self.tbMarcar = QtGui.QToolButton(self.Dual_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMarcar.sizePolicy().hasHeightForWidth())
        self.tbMarcar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbMarcar.setFont(font)
        self.tbMarcar.setStyleSheet(_fromUtf8(" border:0px;\n"
""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pyventa/images/32/sub_black_accept.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbMarcar.setIcon(icon5)
        self.tbMarcar.setIconSize(QtCore.QSize(16, 16))
        self.tbMarcar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbMarcar.setObjectName(_fromUtf8("tbMarcar"))
        self.horizontalLayout.addWidget(self.Dual_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Faltante)
        self.cbPrioridad.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Faltante)

    def retranslateUi(self, Faltante):
        Faltante.setWindowTitle(QtGui.QApplication.translate("Faltante", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lbProducto.setText(QtGui.QApplication.translate("Faltante", "Nombre del producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Faltante", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Faltante", "Prioridad", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPrioridad.setItemText(0, QtGui.QApplication.translate("Faltante", "Urgente", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPrioridad.setItemText(1, QtGui.QApplication.translate("Faltante", "Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPrioridad.setItemText(2, QtGui.QApplication.translate("Faltante", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPrioridad.setItemText(3, QtGui.QApplication.translate("Faltante", "Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCerrar.setText(QtGui.QApplication.translate("Faltante", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMarcar.setText(QtGui.QApplication.translate("Faltante", "Marcar", None, QtGui.QApplication.UnicodeUTF8))

