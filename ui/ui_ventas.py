# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/modulos/ui_ventas.ui'
#
# Created: Thu May  9 19:02:26 2013
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
        Form.resize(741, 464)
        Form.setStyleSheet(_fromUtf8("QToolButton, QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QPushButton::pressed,QToolButton::pressed{\n"
"color:#fff;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"\n"
"}"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.top = QtGui.QWidget(Form)
        self.top.setMinimumSize(QtCore.QSize(0, 40))
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setObjectName(_fromUtf8("top"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.top)
        self.horizontalLayout_12.setContentsMargins(10, 5, 2, 5)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.titulo = QtGui.QLabel(self.top)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.horizontalLayout_12.addWidget(self.titulo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.botonUnion_2 = QtGui.QFrame(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonUnion_2.sizePolicy().hasHeightForWidth())
        self.botonUnion_2.setSizePolicy(sizePolicy)
        self.botonUnion_2.setStyleSheet(_fromUtf8(".QFrame{border-radius:3px;\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QToolButton{background:transparent; border-radius:0;border:0px; padding:4px}\n"
" \n"
""))
        self.botonUnion_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.botonUnion_2.setFrameShadow(QtGui.QFrame.Raised)
        self.botonUnion_2.setObjectName(_fromUtf8("botonUnion_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.botonUnion_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pbVerResumen = QtGui.QToolButton(self.botonUnion_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerResumen.sizePolicy().hasHeightForWidth())
        self.pbVerResumen.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/abacus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVerResumen.setIcon(icon)
        self.pbVerResumen.setIconSize(QtCore.QSize(18, 18))
        self.pbVerResumen.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.pbVerResumen.setObjectName(_fromUtf8("pbVerResumen"))
        self.horizontalLayout_6.addWidget(self.pbVerResumen)
        self.tboDetalles = QtGui.QToolButton(self.botonUnion_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tboDetalles.sizePolicy().hasHeightForWidth())
        self.tboDetalles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tboDetalles.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboDetalles.setIcon(icon1)
        self.tboDetalles.setIconSize(QtCore.QSize(18, 18))
        self.tboDetalles.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tboDetalles.setObjectName(_fromUtf8("tboDetalles"))
        self.horizontalLayout_6.addWidget(self.tboDetalles)
        self.tbGraficar = QtGui.QToolButton(self.botonUnion_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/stats_bars.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbGraficar.setIcon(icon2)
        self.tbGraficar.setIconSize(QtCore.QSize(18, 18))
        self.tbGraficar.setObjectName(_fromUtf8("tbGraficar"))
        self.horizontalLayout_6.addWidget(self.tbGraficar)
        self.tboImprimir = QtGui.QToolButton(self.botonUnion_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tboImprimir.sizePolicy().hasHeightForWidth())
        self.tboImprimir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tboImprimir.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboImprimir.setIcon(icon3)
        self.tboImprimir.setIconSize(QtCore.QSize(18, 18))
        self.tboImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tboImprimir.setObjectName(_fromUtf8("tboImprimir"))
        self.horizontalLayout_6.addWidget(self.tboImprimir)
        self.horizontalLayout_12.addWidget(self.botonUnion_2)
        self.botonUnion = QtGui.QFrame(self.top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonUnion.sizePolicy().hasHeightForWidth())
        self.botonUnion.setSizePolicy(sizePolicy)
        self.botonUnion.setStyleSheet(_fromUtf8("*{border-radius:8px;    \n"
"}\n"
"\n"
"QToolButton::hover{border-radius:8 0 8 0;\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QToolButton{ background:transparent; border-radius:0;}\n"
" \n"
""))
        self.botonUnion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.botonUnion.setFrameShadow(QtGui.QFrame.Raised)
        self.botonUnion.setObjectName(_fromUtf8("botonUnion"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.botonUnion)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_12.addWidget(self.botonUnion)
        self.verticalLayout_3.addWidget(self.top)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_6 = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.deHasta = QtGui.QDateEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deHasta.sizePolicy().hasHeightForWidth())
        self.deHasta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deHasta.setFont(font)
        self.deHasta.setAlignment(QtCore.Qt.AlignCenter)
        self.deHasta.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.deHasta.setAccelerated(True)
        self.deHasta.setCalendarPopup(True)
        self.deHasta.setObjectName(_fromUtf8("deHasta"))
        self.gridLayout.addWidget(self.deHasta, 1, 1, 1, 1)
        self.deDesde = QtGui.QDateEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deDesde.sizePolicy().hasHeightForWidth())
        self.deDesde.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deDesde.setFont(font)
        self.deDesde.setAlignment(QtCore.Qt.AlignCenter)
        self.deDesde.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.deDesde.setAccelerated(True)
        self.deDesde.setCalendarPopup(True)
        self.deDesde.setObjectName(_fromUtf8("deDesde"))
        self.gridLayout.addWidget(self.deDesde, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tboActualizar = QtGui.QToolButton(self.groupBox_6)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboActualizar.setIcon(icon4)
        self.tboActualizar.setIconSize(QtCore.QSize(24, 24))
        self.tboActualizar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tboActualizar.setObjectName(_fromUtf8("tboActualizar"))
        self.horizontalLayout_4.addWidget(self.tboActualizar)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pbDepositar = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbDepositar.setFont(font)
        self.pbDepositar.setObjectName(_fromUtf8("pbDepositar"))
        self.verticalLayout.addWidget(self.pbDepositar)
        self.tboInicial = QtGui.QToolButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tboInicial.sizePolicy().hasHeightForWidth())
        self.tboInicial.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tboInicial.setFont(font)
        self.tboInicial.setIconSize(QtCore.QSize(16, 24))
        self.tboInicial.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tboInicial.setObjectName(_fromUtf8("tboInicial"))
        self.verticalLayout.addWidget(self.tboInicial)
        self.pbVerEnDetallada = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerEnDetallada.sizePolicy().hasHeightForWidth())
        self.pbVerEnDetallada.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pbVerEnDetallada.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../Users/usr/share/pyventa/images/32/edit-select-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVerEnDetallada.setIcon(icon5)
        self.pbVerEnDetallada.setObjectName(_fromUtf8("pbVerEnDetallada"))
        self.verticalLayout.addWidget(self.pbVerEnDetallada)
        self.pbDetallarProds = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbDetallarProds.setFont(font)
        self.pbDetallarProds.setObjectName(_fromUtf8("pbDetallarProds"))
        self.verticalLayout.addWidget(self.pbDetallarProds)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tbRetirar = QtGui.QToolButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbRetirar.sizePolicy().hasHeightForWidth())
        self.tbRetirar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tbRetirar.setFont(font)
        self.tbRetirar.setIconSize(QtCore.QSize(16, 24))
        self.tbRetirar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbRetirar.setObjectName(_fromUtf8("tbRetirar"))
        self.verticalLayout_4.addWidget(self.tbRetirar)
        self.pbAgregarGasto = QtGui.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbAgregarGasto.setFont(font)
        self.pbAgregarGasto.setObjectName(_fromUtf8("pbAgregarGasto"))
        self.verticalLayout_4.addWidget(self.pbAgregarGasto)
        self.pbVerDetallada = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerDetallada.sizePolicy().hasHeightForWidth())
        self.pbVerDetallada.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pbVerDetallada.setFont(font)
        self.pbVerDetallada.setObjectName(_fromUtf8("pbVerDetallada"))
        self.verticalLayout_4.addWidget(self.pbVerDetallada)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.stack = QtGui.QStackedWidget(Form)
        self.stack.setStyleSheet(_fromUtf8("#stack{background:transparent}"))
        self.stack.setObjectName(_fromUtf8("stack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widget_2 = QtGui.QWidget(self.page)
        self.widget_2.setStyleSheet(_fromUtf8(".QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.976077 rgba(71, 71, 71, 255), stop:1 rgba(55, 55, 55, 255));\n"
"\n"
"}\n"
"QTextEdit{border:1.5px solid #ccc;border-top:1px;border-bottom:1px;}"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.scrollArea = QtGui.QScrollArea(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(700, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 425, 420))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.teResumen = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.teResumen.setMaximumSize(QtCore.QSize(700, 16777215))
        self.teResumen.setReadOnly(True)
        self.teResumen.setObjectName(_fromUtf8("teResumen"))
        self.verticalLayout_6.addWidget(self.teResumen)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.addWidget(self.scrollArea)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.stack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(self.page_2)
        self.widget.setStyleSheet(_fromUtf8(".QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.976077 rgba(71, 71, 71, 255), stop:1 rgba(55, 55, 55, 255));\n"
"\n"
"}\n"
"QTextEdit{border:1.5px solid #ccc;border-top:1px;border-bottom:1px;}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.scrollArea_2 = QtGui.QScrollArea(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(700, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.teEntradasDetalle = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teEntradasDetalle.sizePolicy().hasHeightForWidth())
        self.teEntradasDetalle.setSizePolicy(sizePolicy)
        self.teEntradasDetalle.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        self.teEntradasDetalle.setFont(font)
        self.teEntradasDetalle.setReadOnly(True)
        self.teEntradasDetalle.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.teEntradasDetalle.setObjectName(_fromUtf8("teEntradasDetalle"))
        self.verticalLayout_7.addWidget(self.teEntradasDetalle)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.widget)
        self.stack.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.lblGrafica = QtGui.QLabel(self.page_3)
        self.lblGrafica.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGrafica.setObjectName(_fromUtf8("lblGrafica"))
        self.verticalLayout_8.addWidget(self.lblGrafica)
        self.stack.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stack)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setText(QtGui.QApplication.translate("Form", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerResumen.setText(QtGui.QApplication.translate("Form", "Simple", None, QtGui.QApplication.UnicodeUTF8))
        self.tboDetalles.setText(QtGui.QApplication.translate("Form", "Detallado", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGraficar.setToolTip(QtGui.QApplication.translate("Form", "Mostrar grafica", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGraficar.setText(QtGui.QApplication.translate("Form", "Grafica", None, QtGui.QApplication.UnicodeUTF8))
        self.tboImprimir.setText(QtGui.QApplication.translate("Form", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.deHasta.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMMM yy", None, QtGui.QApplication.UnicodeUTF8))
        self.deDesde.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMMM yy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Hasta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
        self.tboActualizar.setText(QtGui.QApplication.translate("Form", "Aplicar periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Entradas", None, QtGui.QApplication.UnicodeUTF8))
        self.pbDepositar.setText(QtGui.QApplication.translate("Form", "Registrar deposito", None, QtGui.QApplication.UnicodeUTF8))
        self.tboInicial.setText(QtGui.QApplication.translate("Form", "Registrar efectivo inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerEnDetallada.setText(QtGui.QApplication.translate("Form", "Detallar entradas", None, QtGui.QApplication.UnicodeUTF8))
        self.pbDetallarProds.setText(QtGui.QApplication.translate("Form", "Detallar ventas por\n"
"productos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Salidas", None, QtGui.QApplication.UnicodeUTF8))
        self.tbRetirar.setText(QtGui.QApplication.translate("Form", "Registrar retiro", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAgregarGasto.setText(QtGui.QApplication.translate("Form", "Registrar gasto", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerDetallada.setText(QtGui.QApplication.translate("Form", "Detallar salidas", None, QtGui.QApplication.UnicodeUTF8))
        self.teEntradasDetalle.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGrafica.setText(QtGui.QApplication.translate("Form", "Grafica", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
