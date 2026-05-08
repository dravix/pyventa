# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_swap.ui'
#
# Created: Sun Jun 17 19:27:01 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Swap(object):
    def setupUi(self, Swap):
        Swap.setObjectName("Swap")
        Swap.resize(532, 298)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/16/page-swap-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Swap.setWindowIcon(icon)
        Swap.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.000909091 rgba(71, 71, 71, 255), stop:0.00636364 rgba(158, 158, 158, 255), stop:0.468182 rgba(163, 163, 163, 255), stop:1 rgba(124, 124, 124, 255));\n"
"\n"
"color:#fff;border:0;}\n"
"QLabel{ border:0px; background:none; color:#fff}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Swap)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stack = QtWidgets.QStackedWidget(Swap)
        self.stack.setStyleSheet("")
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbProducto = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
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
        self.lbProducto.setStyleSheet("color: #ddd;")
        self.lbProducto.setWordWrap(True)
        self.lbProducto.setMargin(1)
        self.lbProducto.setObjectName("lbProducto")
        self.verticalLayout_2.addWidget(self.lbProducto)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:0.118182 rgba(255, 255, 255, 255), stop:0.281818 rgba(255, 255, 255, 255), stop:0.686364 rgba(250, 249, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:0px solid #888; border-radius:0px; padding:4px;border-radius:5px}\n"
"*{border:0;}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leBusca = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.leBusca.setFont(font)
        self.leBusca.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.leBusca.setText("")
        self.leBusca.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.leBusca.setObjectName("leBusca")
        self.horizontalLayout_4.addWidget(self.leBusca)
        self.tbLimpiar = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbLimpiar.sizePolicy().hasHeightForWidth())
        self.tbLimpiar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbLimpiar.setFont(font)
        self.tbLimpiar.setStyleSheet(" border:0px;border-right:1px solid #999;border-radius:0;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/16/trash_16.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbLimpiar.setIcon(icon1)
        self.tbLimpiar.setIconSize(QtCore.QSize(12, 16))
        self.tbLimpiar.setObjectName("tbLimpiar")
        self.horizontalLayout_4.addWidget(self.tbLimpiar)
        self.verticalLayout_2.addWidget(self.frame)
        self.contain = QtWidgets.QFrame(self.page)
        self.contain.setToolTip("")
        self.contain.setStyleSheet("#contain{\n"
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
"")
        self.contain.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.contain.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.contain.setObjectName("contain")
        self.gridLayout = QtWidgets.QGridLayout(self.contain)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.leProp = QtWidgets.QLabel(self.contain)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.leProp.setFont(font)
        self.leProp.setObjectName("leProp")
        self.gridLayout.addWidget(self.leProp, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cbProd = QtWidgets.QComboBox(self.contain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbProd.sizePolicy().hasHeightForWidth())
        self.cbProd.setSizePolicy(sizePolicy)
        self.cbProd.setObjectName("cbProd")
        self.gridLayout.addWidget(self.cbProd, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.contain)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.leProd = QtWidgets.QLineEdit(self.contain)
        self.leProd.setStyleSheet("color: rgb(255, 255, 255);background:rgba(200,200,200,0)")
        self.leProd.setReadOnly(True)
        self.leProd.setObjectName("leProd")
        self.gridLayout.addWidget(self.leProd, 0, 2, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.contain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dsbCant = QtWidgets.QDoubleSpinBox(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.dsbCant.setFont(font)
        self.dsbCant.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbCant.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbCant.setMaximum(99999.99)
        self.dsbCant.setProperty("value", 1.0)
        self.dsbCant.setObjectName("dsbCant")
        self.horizontalLayout_2.addWidget(self.dsbCant)
        self.label_8 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dsbStock = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbStock.sizePolicy().hasHeightForWidth())
        self.dsbStock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.dsbStock.setFont(font)
        self.dsbStock.setStyleSheet("color: rgb(255, 255, 255);background:rgba(200,200,200,0)")
        self.dsbStock.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbStock.setReadOnly(True)
        self.dsbStock.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbStock.setMinimum(-9999.0)
        self.dsbStock.setMaximum(9999.99)
        self.dsbStock.setObjectName("dsbStock")
        self.horizontalLayout_2.addWidget(self.dsbStock)
        self.gridLayout.addWidget(self.frame1, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.contain)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Dual_3 = QtWidgets.QSplitter(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dual_3.sizePolicy().hasHeightForWidth())
        self.Dual_3.setSizePolicy(sizePolicy)
        self.Dual_3.setStyleSheet("QSplitter{border-radius:4px;\n"
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
"")
        self.Dual_3.setLineWidth(0)
        self.Dual_3.setMidLineWidth(1)
        self.Dual_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Dual_3.setHandleWidth(1)
        self.Dual_3.setObjectName("Dual_3")
        self.tbCerrar = QtWidgets.QToolButton(self.Dual_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbCerrar.sizePolicy().hasHeightForWidth())
        self.tbCerrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.tbCerrar.setFont(font)
        self.tbCerrar.setStyleSheet(" border:0px;border-right:1px solid #999;border-radius:0;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/16/edit-delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbCerrar.setIcon(icon2)
        self.tbCerrar.setIconSize(QtCore.QSize(12, 16))
        self.tbCerrar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCerrar.setObjectName("tbCerrar")
        self.tbAplicar = QtWidgets.QToolButton(self.Dual_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbAplicar.sizePolicy().hasHeightForWidth())
        self.tbAplicar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbAplicar.setFont(font)
        self.tbAplicar.setStyleSheet(" border:0px;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/16/tick_16.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbAplicar.setIcon(icon3)
        self.tbAplicar.setIconSize(QtCore.QSize(16, 16))
        self.tbAplicar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbAplicar.setObjectName("tbAplicar")
        self.horizontalLayout.addWidget(self.Dual_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 494, 214))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbResulta = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbResulta.sizePolicy().hasHeightForWidth())
        self.lbResulta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbResulta.setFont(font)
        self.lbResulta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"border:1px solid #999;color:#333;")
        self.lbResulta.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lbResulta.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lbResulta.setWordWrap(True)
        self.lbResulta.setMargin(5)
        self.lbResulta.setObjectName("lbResulta")
        self.verticalLayout_4.addWidget(self.lbResulta)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Dual_5 = QtWidgets.QSplitter(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dual_5.sizePolicy().hasHeightForWidth())
        self.Dual_5.setSizePolicy(sizePolicy)
        self.Dual_5.setStyleSheet("QSplitter{border-radius:4px;\n"
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
"")
        self.Dual_5.setLineWidth(0)
        self.Dual_5.setMidLineWidth(1)
        self.Dual_5.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Dual_5.setHandleWidth(1)
        self.Dual_5.setObjectName("Dual_5")
        self.tbRegresar = QtWidgets.QToolButton(self.Dual_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbRegresar.sizePolicy().hasHeightForWidth())
        self.tbRegresar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.tbRegresar.setFont(font)
        self.tbRegresar.setStyleSheet(" border:0px;border-right:1px solid #999;border-radius:0;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/16/left_16.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbRegresar.setIcon(icon4)
        self.tbRegresar.setIconSize(QtCore.QSize(12, 16))
        self.tbRegresar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbRegresar.setObjectName("tbRegresar")
        self.tbConfirmar = QtWidgets.QToolButton(self.Dual_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbConfirmar.sizePolicy().hasHeightForWidth())
        self.tbConfirmar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tbConfirmar.setFont(font)
        self.tbConfirmar.setStyleSheet(" border:0px;\n"
"")
        self.tbConfirmar.setIcon(icon3)
        self.tbConfirmar.setIconSize(QtCore.QSize(16, 16))
        self.tbConfirmar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbConfirmar.setObjectName("tbConfirmar")
        self.horizontalLayout_3.addWidget(self.Dual_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stack.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stack)

        self.retranslateUi(Swap)
        self.stack.setCurrentIndex(0)
        self.tbLimpiar.clicked.connect(self.leBusca.clear)
        self.tbCerrar.clicked.connect(Swap.reject)
        QtCore.QMetaObject.connectSlotsByName(Swap)
        Swap.setTabOrder(self.leBusca, self.dsbCant)
        Swap.setTabOrder(self.dsbCant, self.tbAplicar)
        Swap.setTabOrder(self.tbAplicar, self.tbCerrar)
        Swap.setTabOrder(self.tbCerrar, self.tbLimpiar)
        Swap.setTabOrder(self.tbLimpiar, self.dsbStock)

    def retranslateUi(self, Swap):
        Swap.setWindowTitle(QtCore.QCoreApplication.translate("Swap", "Intercambio de presentaciones"))
        self.lbProducto.setText(QtCore.QCoreApplication.translate("Swap", "Convierte X unidades de un producto en Y unidades de otro, siempre y cuando estos guarden  una relacion de proporcionalidad."))
        self.leBusca.setToolTip(QtCore.QCoreApplication.translate("Swap", "Buscar producto por iniciales."))
        self.tbLimpiar.setText(QtCore.QCoreApplication.translate("Swap", "Limpiar"))
        self.leProp.setToolTip(QtWidgets.QApplication.translate("Swap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Es la relacion de proporcionalidad</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Por ejemplo: <span style=\" font-weight:600;\">1:12</span> significa que se tomara 1 producto del inventario</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">y se repondra como 12 del segundo producto</p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.leProp.setText(QtCore.QCoreApplication.translate("Swap", "1:1"))
        self.label.setText(QtCore.QCoreApplication.translate("Swap", "Proporcion:"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Swap", "Producto"))
        self.label_6.setText(QtCore.QCoreApplication.translate("Swap", "Convertir en:"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Swap", "Cantidad:"))
        self.label_8.setText(QtCore.QCoreApplication.translate("Swap", "Existencia actual:"))
        self.tbCerrar.setText(QtCore.QCoreApplication.translate("Swap", "Cerrar"))
        self.tbAplicar.setText(QtCore.QCoreApplication.translate("Swap", "Aplicar"))
        self.lbResulta.setText(QtWidgets.QApplication.translate("Swap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Se tomaran <span style=\" font-weight:600;\">%s</span> unidades de %s y se agregaran como %s unidades de<span style=\" font-weight:600;\"> %s , </span>quedando de la siguiente manera:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
        self.tbRegresar.setText(QtCore.QCoreApplication.translate("Swap", "Regresar"))
        self.tbConfirmar.setText(QtCore.QCoreApplication.translate("Swap", "Confirmar"))

