# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_corte2.ui'
#
# Created: Sat Mar 30 13:26:33 2013
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
        Form.resize(793, 537)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.topReportes = QtGui.QWidget(Form)
        self.topReportes.setObjectName(_fromUtf8("topReportes"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.topReportes)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.stackedWidget = QtGui.QStackedWidget(self.topReportes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frDia = QtGui.QFrame(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frDia.sizePolicy().hasHeightForWidth())
        self.frDia.setSizePolicy(sizePolicy)
        self.frDia.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frDia.setFrameShadow(QtGui.QFrame.Raised)
        self.frDia.setObjectName(_fromUtf8("frDia"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frDia)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.deCorte = QtGui.QDateEdit(self.frDia)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deCorte.setFont(font)
        self.deCorte.setAlignment(QtCore.Qt.AlignCenter)
        self.deCorte.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.deCorte.setAccelerated(True)
        self.deCorte.setCalendarPopup(True)
        self.deCorte.setObjectName(_fromUtf8("deCorte"))
        self.horizontalLayout_8.addWidget(self.deCorte)
        self.label_3 = QtGui.QLabel(self.frDia)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frDia)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tbFHome = QtGui.QToolButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbFHome.sizePolicy().hasHeightForWidth())
        self.tbFHome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbFHome.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/modulos/images/png/elegant/report.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbFHome.setIcon(icon)
        self.tbFHome.setIconSize(QtCore.QSize(18, 18))
        self.tbFHome.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbFHome.setAutoRaise(True)
        self.tbFHome.setObjectName(_fromUtf8("tbFHome"))
        self.horizontalLayout_9.addWidget(self.tbFHome)
        self.tbTitulo = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbTitulo.sizePolicy().hasHeightForWidth())
        self.tbTitulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbTitulo.setFont(font)
        self.tbTitulo.setObjectName(_fromUtf8("tbTitulo"))
        self.horizontalLayout_9.addWidget(self.tbTitulo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.splitter = QtGui.QSplitter(self.topReportes)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget = QtGui.QWidget(self.layoutWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_17 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_17)
        self.deFrom = QtGui.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deFrom.setFont(font)
        self.deFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.deFrom.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.deFrom.setAccelerated(True)
        self.deFrom.setCalendarPopup(True)
        self.deFrom.setObjectName(_fromUtf8("deFrom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deFrom)
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.deTo = QtGui.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deTo.setFont(font)
        self.deTo.setAlignment(QtCore.Qt.AlignCenter)
        self.deTo.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.deTo.setAccelerated(True)
        self.deTo.setCalendarPopup(True)
        self.deTo.setObjectName(_fromUtf8("deTo"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.deTo)
        self.label_8 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.cbListas = QtGui.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cbListas.setFont(font)
        self.cbListas.setObjectName(_fromUtf8("cbListas"))
        self.cbListas.addItem(_fromUtf8(""))
        self.cbListas.addItem(_fromUtf8(""))
        self.cbListas.addItem(_fromUtf8(""))
        self.cbListas.addItem(_fromUtf8(""))
        self.cbListas.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbListas)
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.cbCaja = QtGui.QComboBox(self.widget)
        self.cbCaja.setObjectName(_fromUtf8("cbCaja"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbCaja)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.widget)
        self.frame = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(_fromUtf8(".QFrame{\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QToolButton, QLabel{padding:2 4 2 4; color:#555;border:0;}\n"
" \n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tbListar = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbListar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbListar.setIcon(icon1)
        self.tbListar.setIconSize(QtCore.QSize(18, 18))
        self.tbListar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbListar.setAutoRaise(True)
        self.tbListar.setObjectName(_fromUtf8("tbListar"))
        self.horizontalLayout_3.addWidget(self.tbListar)
        self.tbGraficas = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbGraficas.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/stats_bars.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbGraficas.setIcon(icon2)
        self.tbGraficas.setIconSize(QtCore.QSize(18, 18))
        self.tbGraficas.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbGraficas.setAutoRaise(True)
        self.tbGraficas.setObjectName(_fromUtf8("tbGraficas"))
        self.horizontalLayout_3.addWidget(self.tbGraficas)
        self.bCorteT = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bCorteT.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/scissors.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCorteT.setIcon(icon3)
        self.bCorteT.setIconSize(QtCore.QSize(18, 18))
        self.bCorteT.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.bCorteT.setObjectName(_fromUtf8("bCorteT"))
        self.horizontalLayout_3.addWidget(self.bCorteT)
        self.tbImprimir = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbImprimir.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbImprimir.setIcon(icon4)
        self.tbImprimir.setIconSize(QtCore.QSize(18, 18))
        self.tbImprimir.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.tbImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbImprimir.setAutoRaise(True)
        self.tbImprimir.setObjectName(_fromUtf8("tbImprimir"))
        self.horizontalLayout_3.addWidget(self.tbImprimir)
        self.pbListaVentas = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pbListaVentas.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/black_18/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbListaVentas.setIcon(icon5)
        self.pbListaVentas.setIconSize(QtCore.QSize(18, 18))
        self.pbListaVentas.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbListaVentas.setAutoRaise(True)
        self.pbListaVentas.setObjectName(_fromUtf8("pbListaVentas"))
        self.horizontalLayout_3.addWidget(self.pbListaVentas)
        self.verticalLayout_3.addWidget(self.frame)
        self.teDetalles = QtGui.QTextEdit(self.layoutWidget)
        self.teDetalles.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(10)
        self.teDetalles.setFont(font)
        self.teDetalles.setObjectName(_fromUtf8("teDetalles"))
        self.verticalLayout_3.addWidget(self.teDetalles)
        self.stackReportes = QtGui.QStackedWidget(self.splitter)
        self.stackReportes.setObjectName(_fromUtf8("stackReportes"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tVentas = QtGui.QTableView(self.page_5)
        self.tVentas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tVentas.setAlternatingRowColors(True)
        self.tVentas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tVentas.setSortingEnabled(True)
        self.tVentas.setObjectName(_fromUtf8("tVentas"))
        self.tVentas.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tVentas)
        self.stackReportes.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.grafica = QtGui.QGraphicsView(self.page_6)
        self.grafica.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.grafica.setObjectName(_fromUtf8("grafica"))
        self.verticalLayout_2.addWidget(self.grafica)
        self.stackReportes.addWidget(self.page_6)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.topReportes)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.stackReportes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Dia", None, QtGui.QApplication.UnicodeUTF8))
        self.tbFHome.setText(QtGui.QApplication.translate("Form", "Tienda", None, QtGui.QApplication.UnicodeUTF8))
        self.tbFHome.setShortcut(QtGui.QApplication.translate("Form", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.tbTitulo.setText(QtGui.QApplication.translate("Form", "Reportes de ventas:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Form", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
        self.deFrom.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMM yy   ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Hasta:", None, QtGui.QApplication.UnicodeUTF8))
        self.deTo.setDisplayFormat(QtGui.QApplication.translate("Form", "dd MMM yy   ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Filtrar formato:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListas.setItemText(0, QtGui.QApplication.translate("Form", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListas.setItemText(1, QtGui.QApplication.translate("Form", "Compras", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListas.setItemText(2, QtGui.QApplication.translate("Form", "Gastos", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListas.setItemText(3, QtGui.QApplication.translate("Form", "Retiros", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListas.setItemText(4, QtGui.QApplication.translate("Form", "Depositos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Filtrar caja:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbListar.setText(QtGui.QApplication.translate("Form", "Listado", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGraficas.setText(QtGui.QApplication.translate("Form", "Graficar", None, QtGui.QApplication.UnicodeUTF8))
        self.bCorteT.setToolTip(QtGui.QApplication.translate("Form", "Realizar corte de ventas.", None, QtGui.QApplication.UnicodeUTF8))
        self.bCorteT.setText(QtGui.QApplication.translate("Form", "Corte", None, QtGui.QApplication.UnicodeUTF8))
        self.tbImprimir.setText(QtGui.QApplication.translate("Form", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.pbListaVentas.setText(QtGui.QApplication.translate("Form", "Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.teDetalles.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">Tabla general de ventas</span></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"100%\" cellspacing=\"4\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">Concepto</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-weight:600;\">Monto</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">Ventas realizadas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">Ventas cobradas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">Facturas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">Notas</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">En efectivo</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">En credito</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">#</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
