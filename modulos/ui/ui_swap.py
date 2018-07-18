# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_swap.ui'
#
# Created: Sun Jun 17 19:27:01 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Swap(object):
    def setupUi(self, Swap):
        Swap.setObjectName(_fromUtf8("Swap"))
        Swap.resize(532, 298)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../usr/share/pyventa/images/16/page-swap-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Swap.setWindowIcon(icon)
        Swap.setStyleSheet(_fromUtf8("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.000909091 rgba(71, 71, 71, 255), stop:0.00636364 rgba(158, 158, 158, 255), stop:0.468182 rgba(163, 163, 163, 255), stop:1 rgba(124, 124, 124, 255));\n"
"\n"
"color:#fff;border:0;}\n"
"QLabel{ border:0px; background:none; color:#fff}\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Swap)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stack = QtGui.QStackedWidget(Swap)
        self.stack.setStyleSheet(_fromUtf8(""))
        self.stack.setObjectName(_fromUtf8("stack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbProducto = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbProducto.sizePolicy().hasHeightForWidth())
        self.lbProducto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lbProducto.setFont(font)
        self.lbProducto.setStyleSheet(_fromUtf8("color: #ddd;"))
        self.lbProducto.setWordWrap(True)
        self.lbProducto.setMargin(1)
        self.lbProducto.setObjectName(_fromUtf8("lbProducto"))
        self.verticalLayout_2.addWidget(self.lbProducto)
        self.frame = QtGui.QFrame(self.page)
        self.frame.setStyleSheet(_fromUtf8("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.118182 rgba(255, 255, 255, 255), stop:0.281818 rgba(255, 255, 255, 255), stop:0.686364 rgba(250, 249, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px solid #888; border-radius:0px; padding:4px;border-radius:5px}\n"
"*{border:0;}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.leBusca = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.leBusca.setFont(font)
        self.leBusca.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.leBusca.setText(_fromUtf8(""))
        self.leBusca.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.leBusca.setObjectName(_fromUtf8("leBusca"))
        self.horizontalLayout_4.addWidget(self.leBusca)
        self.tbLimpiar = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbLimpiar.sizePolicy().hasHeightForWidth())
        self.tbLimpiar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbLimpiar.setFont(font)
        self.tbLimpiar.setStyleSheet(_fromUtf8(" border:0px;border-right:1px solid #999;border-radius:0;\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/trash_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbLimpiar.setIcon(icon1)
        self.tbLimpiar.setIconSize(QtCore.QSize(12, 16))
        self.tbLimpiar.setObjectName(_fromUtf8("tbLimpiar"))
        self.horizontalLayout_4.addWidget(self.tbLimpiar)
        self.verticalLayout_2.addWidget(self.frame)
        self.contain = QtGui.QFrame(self.page)
        self.contain.setToolTip(_fromUtf8(""))
        self.contain.setStyleSheet(_fromUtf8("#contain{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(158, 158, 158, 255), stop:0.43 rgba(163, 163, 163, 255), stop:1 rgba(124, 124, 124, 255));\n"
"border:1px solid #777; \n"
"}\n"
"QWidget{\n"
"\n"
"border-radius:5px; border:0;}\n"
"QLineEdit, QDoubleSpinBox,QComboBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.118182 rgba(255, 255, 255, 255), stop:0.281818 rgba(255, 255, 255, 255), stop:0.686364 rgba(250, 249, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px solid #888; border-radius:0px; padding:4px;border-radius:5px}\n"
"QLabel{color:#FFF;}\n"
"QComboBox{border:1px solid #888;}\n"
"QComboBox *{background:rgb(190, 212, 221)}\n"
" QComboBox:editable {\n"
"padding:5;\n"
" }\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"color:#444; }\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
" }\n"
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
        self.contain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.contain.setFrameShadow(QtGui.QFrame.Raised)
        self.contain.setObjectName(_fromUtf8("contain"))
        self.gridLayout = QtGui.QGridLayout(self.contain)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leProp = QtGui.QLabel(self.contain)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.leProp.setFont(font)
        self.leProp.setObjectName(_fromUtf8("leProp"))
        self.gridLayout.addWidget(self.leProp, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cbProd = QtGui.QComboBox(self.contain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbProd.sizePolicy().hasHeightForWidth())
        self.cbProd.setSizePolicy(sizePolicy)
        self.cbProd.setObjectName(_fromUtf8("cbProd"))
        self.gridLayout.addWidget(self.cbProd, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.leProd = QtGui.QLineEdit(self.contain)
        self.leProd.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);background:rgba(200,200,200,0)"))
        self.leProd.setReadOnly(True)
        self.leProd.setObjectName(_fromUtf8("leProd"))
        self.gridLayout.addWidget(self.leProd, 0, 2, 1, 1)
        self.frame1 = QtGui.QFrame(self.contain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dsbCant = QtGui.QDoubleSpinBox(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.dsbCant.setFont(font)
        self.dsbCant.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbCant.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbCant.setMaximum(99999.99)
        self.dsbCant.setProperty(_fromUtf8("value"), 1.0)
        self.dsbCant.setObjectName(_fromUtf8("dsbCant"))
        self.horizontalLayout_2.addWidget(self.dsbCant)
        self.label_8 = QtGui.QLabel(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dsbStock = QtGui.QDoubleSpinBox(self.frame1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbStock.sizePolicy().hasHeightForWidth())
        self.dsbStock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.dsbStock.setFont(font)
        self.dsbStock.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);background:rgba(200,200,200,0)"))
        self.dsbStock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbStock.setReadOnly(True)
        self.dsbStock.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbStock.setMinimum(-9999.0)
        self.dsbStock.setMaximum(9999.99)
        self.dsbStock.setObjectName(_fromUtf8("dsbStock"))
        self.horizontalLayout_2.addWidget(self.dsbStock)
        self.gridLayout.addWidget(self.frame1, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.contain)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Dual_3 = QtGui.QSplitter(self.page)
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
        font.setWeight(50)
        font.setBold(False)
        self.tbCerrar.setFont(font)
        self.tbCerrar.setStyleSheet(_fromUtf8(" border:0px;border-right:1px solid #999;border-radius:0;\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbCerrar.setIcon(icon2)
        self.tbCerrar.setIconSize(QtCore.QSize(12, 16))
        self.tbCerrar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCerrar.setObjectName(_fromUtf8("tbCerrar"))
        self.tbAplicar = QtGui.QToolButton(self.Dual_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbAplicar.sizePolicy().hasHeightForWidth())
        self.tbAplicar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbAplicar.setFont(font)
        self.tbAplicar.setStyleSheet(_fromUtf8(" border:0px;\n"
""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/tick_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbAplicar.setIcon(icon3)
        self.tbAplicar.setIconSize(QtCore.QSize(16, 16))
        self.tbAplicar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbAplicar.setObjectName(_fromUtf8("tbAplicar"))
        self.horizontalLayout.addWidget(self.Dual_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.page_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 494, 214))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lbResulta = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbResulta.sizePolicy().hasHeightForWidth())
        self.lbResulta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbResulta.setFont(font)
        self.lbResulta.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border:1px solid #999;color:#333;"))
        self.lbResulta.setTextFormat(QtCore.Qt.RichText)
        self.lbResulta.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbResulta.setWordWrap(True)
        self.lbResulta.setMargin(5)
        self.lbResulta.setObjectName(_fromUtf8("lbResulta"))
        self.verticalLayout_4.addWidget(self.lbResulta)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Dual_5 = QtGui.QSplitter(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dual_5.sizePolicy().hasHeightForWidth())
        self.Dual_5.setSizePolicy(sizePolicy)
        self.Dual_5.setStyleSheet(_fromUtf8("QSplitter{border-radius:4px;\n"
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
        self.Dual_5.setLineWidth(0)
        self.Dual_5.setMidLineWidth(1)
        self.Dual_5.setOrientation(QtCore.Qt.Horizontal)
        self.Dual_5.setHandleWidth(1)
        self.Dual_5.setObjectName(_fromUtf8("Dual_5"))
        self.tbRegresar = QtGui.QToolButton(self.Dual_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbRegresar.sizePolicy().hasHeightForWidth())
        self.tbRegresar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.tbRegresar.setFont(font)
        self.tbRegresar.setStyleSheet(_fromUtf8(" border:0px;border-right:1px solid #999;border-radius:0;\n"
""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pyventa/images/16/left_16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbRegresar.setIcon(icon4)
        self.tbRegresar.setIconSize(QtCore.QSize(12, 16))
        self.tbRegresar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbRegresar.setObjectName(_fromUtf8("tbRegresar"))
        self.tbConfirmar = QtGui.QToolButton(self.Dual_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbConfirmar.sizePolicy().hasHeightForWidth())
        self.tbConfirmar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbConfirmar.setFont(font)
        self.tbConfirmar.setStyleSheet(_fromUtf8(" border:0px;\n"
""))
        self.tbConfirmar.setIcon(icon3)
        self.tbConfirmar.setIconSize(QtCore.QSize(16, 16))
        self.tbConfirmar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbConfirmar.setObjectName(_fromUtf8("tbConfirmar"))
        self.horizontalLayout_3.addWidget(self.Dual_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stack.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stack)

        self.retranslateUi(Swap)
        self.stack.setCurrentIndex(0)
        QtCore.QObject.connect(self.tbLimpiar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.leBusca.clear)
        QtCore.QObject.connect(self.tbCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), Swap.reject)
        QtCore.QMetaObject.connectSlotsByName(Swap)
        Swap.setTabOrder(self.leBusca, self.dsbCant)
        Swap.setTabOrder(self.dsbCant, self.tbAplicar)
        Swap.setTabOrder(self.tbAplicar, self.tbCerrar)
        Swap.setTabOrder(self.tbCerrar, self.tbLimpiar)
        Swap.setTabOrder(self.tbLimpiar, self.dsbStock)

    def retranslateUi(self, Swap):
        Swap.setWindowTitle(QtGui.QApplication.translate("Swap", "Intercambio de presentaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lbProducto.setText(QtGui.QApplication.translate("Swap", "Convierte X unidades de un producto en Y unidades de otro, siempre y cuando estos guarden  una relacion de proporcionalidad.", None, QtGui.QApplication.UnicodeUTF8))
        self.leBusca.setToolTip(QtGui.QApplication.translate("Swap", "Buscar producto por iniciales.", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLimpiar.setText(QtGui.QApplication.translate("Swap", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.leProp.setToolTip(QtGui.QApplication.translate("Swap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Es la relacion de proporcionalidad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Por ejemplo: <span style=\" font-weight:600;\">1:12</span> significa que se tomara 1 producto del inventario</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">y se repondra como 12 del segundo producto</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.leProp.setText(QtGui.QApplication.translate("Swap", "1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Swap", "Proporcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Swap", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Swap", "Convertir en:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Swap", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Swap", "Existencia actual:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCerrar.setText(QtGui.QApplication.translate("Swap", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAplicar.setText(QtGui.QApplication.translate("Swap", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResulta.setText(QtGui.QApplication.translate("Swap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Se tomaran <span style=\" font-weight:600;\">%s</span> unidades de %s y se agregaran como %s unidades de<span style=\" font-weight:600;\"> %s , </span>quedando de la siguiente manera:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tbRegresar.setText(QtGui.QApplication.translate("Swap", "Regresar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbConfirmar.setText(QtGui.QApplication.translate("Swap", "Confirmar", None, QtGui.QApplication.UnicodeUTF8))

