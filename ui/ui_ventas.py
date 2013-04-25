# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/modulos/ui_ventas.ui'
#
# Created: Sun Mar 31 13:31:58 2013
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
        Form.resize(772, 630)
        Form.setStyleSheet(_fromUtf8("color:rgb(0, 32, 47);"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.top = QtGui.QWidget(Form)
        self.top.setMinimumSize(QtCore.QSize(0, 40))
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setObjectName(_fromUtf8("top"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.top)
        self.horizontalLayout_12.setContentsMargins(10, 5, -1, 5)
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
        self.botonUnion_2.setStyleSheet(_fromUtf8(".QFrame{border-radius:8px;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboDetalles.setIcon(icon)
        self.tboDetalles.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tboDetalles.setObjectName(_fromUtf8("tboDetalles"))
        self.horizontalLayout_6.addWidget(self.tboDetalles)
        self.tboImprimir = QtGui.QToolButton(self.botonUnion_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tboImprimir.sizePolicy().hasHeightForWidth())
        self.tboImprimir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tboImprimir.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboImprimir.setIcon(icon1)
        self.tboImprimir.setIconSize(QtCore.QSize(16, 16))
        self.tboImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
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
        self.stack = QtGui.QStackedWidget(Form)
        self.stack.setStyleSheet(_fromUtf8(" QScrollBar:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     height: 15px;\n"
"     margin: 0px 20px 0 20px;\n"
" }\n"
" QScrollBar::handle:horizontal {\n"
"     background: white;\n"
"     min-width: 20px;\n"
" }\n"
" QScrollBar::add-line:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     width: 20px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     width: 20px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }"))
        self.stack.setObjectName(_fromUtf8("stack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_6 = QtGui.QGroupBox(self.page)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tboActualizar.setIcon(icon2)
        self.tboActualizar.setIconSize(QtCore.QSize(24, 24))
        self.tboActualizar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tboActualizar.setObjectName(_fromUtf8("tboActualizar"))
        self.horizontalLayout_4.addWidget(self.tboActualizar)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tboInicial = QtGui.QToolButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
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
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pbVerEnDetallada.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../Users/usr/share/pyventa/images/32/edit-select-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVerEnDetallada.setIcon(icon3)
        self.pbVerEnDetallada.setObjectName(_fromUtf8("pbVerEnDetallada"))
        self.verticalLayout.addWidget(self.pbVerEnDetallada)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.page)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tbAgregar = QtGui.QToolButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbAgregar.sizePolicy().hasHeightForWidth())
        self.tbAgregar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbAgregar.setFont(font)
        self.tbAgregar.setIconSize(QtCore.QSize(16, 24))
        self.tbAgregar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbAgregar.setObjectName(_fromUtf8("tbAgregar"))
        self.verticalLayout_4.addWidget(self.tbAgregar)
        self.pbVerDetallada = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerDetallada.sizePolicy().hasHeightForWidth())
        self.pbVerDetallada.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pbVerDetallada.setFont(font)
        self.pbVerDetallada.setObjectName(_fromUtf8("pbVerDetallada"))
        self.verticalLayout_4.addWidget(self.pbVerDetallada)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 557, 586))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.teDetalles = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        self.teDetalles.setFont(font)
        self.teDetalles.setReadOnly(True)
        self.teDetalles.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.teDetalles.setObjectName(_fromUtf8("teDetalles"))
        self.gridLayout_2.addWidget(self.teDetalles, 0, 0, 1, 1)
        self.teDetalles_2 = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        self.teDetalles_2.setFont(font)
        self.teDetalles_2.setReadOnly(True)
        self.teDetalles_2.setObjectName(_fromUtf8("teDetalles_2"))
        self.gridLayout_2.addWidget(self.teDetalles_2, 2, 0, 1, 1)
        self.teDetalles_3 = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        self.teDetalles_3.setFont(font)
        self.teDetalles_3.setReadOnly(True)
        self.teDetalles_3.setObjectName(_fromUtf8("teDetalles_3"))
        self.gridLayout_2.addWidget(self.teDetalles_3, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pbVerResumen = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerResumen.sizePolicy().hasHeightForWidth())
        self.pbVerResumen.setSizePolicy(sizePolicy)
        self.pbVerResumen.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QAbstractButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(175, 236, 224, 255), stop:0.536364 rgba(94, 192, 226, 255), stop:0.554545 rgba(72, 170, 199, 255), stop:0.977273 rgba(65, 163, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/arrow_left2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbVerResumen.setIcon(icon4)
        self.pbVerResumen.setObjectName(_fromUtf8("pbVerResumen"))
        self.verticalLayout_9.addWidget(self.pbVerResumen)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.twGastos = QtGui.QTableWidget(self.groupBox_4)
        self.twGastos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twGastos.setAlternatingRowColors(True)
        self.twGastos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twGastos.setShowGrid(False)
        self.twGastos.setGridStyle(QtCore.Qt.NoPen)
        self.twGastos.setObjectName(_fromUtf8("twGastos"))
        self.twGastos.setColumnCount(0)
        self.twGastos.setRowCount(0)
        self.twGastos.horizontalHeader().setVisible(False)
        self.twGastos.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.twGastos)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.twCompras = QtGui.QTableWidget(self.groupBox_5)
        self.twCompras.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twCompras.setAlternatingRowColors(True)
        self.twCompras.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twCompras.setShowGrid(False)
        self.twCompras.setGridStyle(QtCore.Qt.NoPen)
        self.twCompras.setObjectName(_fromUtf8("twCompras"))
        self.twCompras.setColumnCount(0)
        self.twCompras.setRowCount(0)
        self.twCompras.horizontalHeader().setVisible(False)
        self.twCompras.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.twCompras)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.stack.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.pbVerResumen_2 = QtGui.QPushButton(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbVerResumen_2.sizePolicy().hasHeightForWidth())
        self.pbVerResumen_2.setSizePolicy(sizePolicy)
        self.pbVerResumen_2.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QAbstractButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(175, 236, 224, 255), stop:0.536364 rgba(94, 192, 226, 255), stop:0.554545 rgba(72, 170, 199, 255), stop:0.977273 rgba(65, 163, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}"))
        self.pbVerResumen_2.setIcon(icon4)
        self.pbVerResumen_2.setObjectName(_fromUtf8("pbVerResumen_2"))
        self.verticalLayout_13.addWidget(self.pbVerResumen_2)
        self.groupBox_7 = QtGui.QGroupBox(self.page_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.teEntradasDetalle = QtGui.QTextEdit(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        self.teEntradasDetalle.setFont(font)
        self.teEntradasDetalle.setReadOnly(True)
        self.teEntradasDetalle.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.teEntradasDetalle.setObjectName(_fromUtf8("teEntradasDetalle"))
        self.verticalLayout_12.addWidget(self.teEntradasDetalle)
        self.verticalLayout_13.addWidget(self.groupBox_7)
        self.stack.addWidget(self.page_3)
        self.verticalLayout_3.addWidget(self.stack)

        self.retranslateUi(Form)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.titulo.setText(QtGui.QApplication.translate("Form", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.tboDetalles.setText(QtGui.QApplication.translate("Form", "Detalles", None, QtGui.QApplication.UnicodeUTF8))
        self.tboImprimir.setText(QtGui.QApplication.translate("Form", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.deHasta.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMMM yy", None, QtGui.QApplication.UnicodeUTF8))
        self.deDesde.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMMM yy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Hasta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
        self.tboActualizar.setText(QtGui.QApplication.translate("Form", "Aplicar periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Entradas", None, QtGui.QApplication.UnicodeUTF8))
        self.tboInicial.setText(QtGui.QApplication.translate("Form", "Efectivo inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerEnDetallada.setText(QtGui.QApplication.translate("Form", "Ver detalles de entradas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Salidas", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAgregar.setText(QtGui.QApplication.translate("Form", "Registrar gasto", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerDetallada.setText(QtGui.QApplication.translate("Form", "Ver detalles de gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.teDetalles.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Tabla de ventas</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Concepto</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Valor</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Ventas realizadas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Ventas cobradas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Facturas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Notas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">En efectivo</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">En credito</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.teDetalles_2.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Tabla de Salidas de recursos.</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Concepto</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Valor</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Compras </span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td></td>\n"
"<td></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Pagos por gastos</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td></td>\n"
"<td></td>\n"
"<td></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.teDetalles_3.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Tabla general de efectivo.</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Concepto</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Valor</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Total por ventas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Total de pagos/gastos</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Efectivo inicial</p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">$</span></p></td></tr></table>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Efectivo actual</p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">$</span></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbVerResumen.setText(QtGui.QApplication.translate("Form", "Regresar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Tabla detallada de gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.twGastos.setSortingEnabled(True)
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Tabla compras", None, QtGui.QApplication.UnicodeUTF8))
        self.twCompras.setSortingEnabled(True)
        self.pbVerResumen_2.setText(QtGui.QApplication.translate("Form", "Regresar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Form", "Tabla detallada de entradas", None, QtGui.QApplication.UnicodeUTF8))
        self.teEntradasDetalle.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Tabla de ventas</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Concepto</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Cantidad</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Valor</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Ventas realizadas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Ventas cobradas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Facturas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Notas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">En efectivo</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">En credito</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">$</span></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
