# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dave/Dropbox/Pyventa/pyventa-2.3/qt/ui_corte2.ui'
#
# Created: Sat Mar 30 13:26:33 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 537)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.topReportes = QtWidgets.QWidget(Form)
        self.topReportes.setObjectName("topReportes")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.topReportes)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.topReportes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frDia = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frDia.sizePolicy().hasHeightForWidth())
        self.frDia.setSizePolicy(sizePolicy)
        self.frDia.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frDia.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frDia.setObjectName("frDia")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frDia)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.deCorte = QtWidgets.QDateEdit(self.frDia)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deCorte.setFont(font)
        self.deCorte.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.deCorte.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.deCorte.setAccelerated(True)
        self.deCorte.setCalendarPopup(True)
        self.deCorte.setObjectName("deCorte")
        self.horizontalLayout_8.addWidget(self.deCorte)
        self.label_3 = QtWidgets.QLabel(self.frDia)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frDia)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tbFHome = QtWidgets.QToolButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbFHome.sizePolicy().hasHeightForWidth())
        self.tbFHome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbFHome.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/report.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbFHome.setIcon(icon)
        self.tbFHome.setIconSize(QtCore.QSize(18, 18))
        self.tbFHome.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbFHome.setAutoRaise(True)
        self.tbFHome.setObjectName("tbFHome")
        self.horizontalLayout_9.addWidget(self.tbFHome)
        self.tbTitulo = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbTitulo.sizePolicy().hasHeightForWidth())
        self.tbTitulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbTitulo.setFont(font)
        self.tbTitulo.setObjectName("tbTitulo")
        self.horizontalLayout_9.addWidget(self.tbTitulo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.splitter = QtWidgets.QSplitter(self.topReportes)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_17 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.deFrom = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deFrom.setFont(font)
        self.deFrom.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.deFrom.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.deFrom.setAccelerated(True)
        self.deFrom.setCalendarPopup(True)
        self.deFrom.setObjectName("deFrom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deFrom)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.deTo = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deTo.setFont(font)
        self.deTo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.deTo.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.deTo.setAccelerated(True)
        self.deTo.setCalendarPopup(True)
        self.deTo.setObjectName("deTo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.deTo)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cbListas = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cbListas.setFont(font)
        self.cbListas.setObjectName("cbListas")
        self.cbListas.addItem("")
        self.cbListas.addItem("")
        self.cbListas.addItem("")
        self.cbListas.addItem("")
        self.cbListas.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbListas)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cbCaja = QtWidgets.QComboBox(self.widget)
        self.cbCaja.setObjectName("cbCaja")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbCaja)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.widget)
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(".QFrame{\n"
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
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tbListar = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbListar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/images/actions/black_18/list.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbListar.setIcon(icon1)
        self.tbListar.setIconSize(QtCore.QSize(18, 18))
        self.tbListar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbListar.setAutoRaise(True)
        self.tbListar.setObjectName("tbListar")
        self.horizontalLayout_3.addWidget(self.tbListar)
        self.tbGraficas = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbGraficas.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/images/actions/black_18/stats_bars.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbGraficas.setIcon(icon2)
        self.tbGraficas.setIconSize(QtCore.QSize(18, 18))
        self.tbGraficas.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbGraficas.setAutoRaise(True)
        self.tbGraficas.setObjectName("tbGraficas")
        self.horizontalLayout_3.addWidget(self.tbGraficas)
        self.bCorteT = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bCorteT.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/images/actions/black_18/scissors.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bCorteT.setIcon(icon3)
        self.bCorteT.setIconSize(QtCore.QSize(18, 18))
        self.bCorteT.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.bCorteT.setObjectName("bCorteT")
        self.horizontalLayout_3.addWidget(self.bCorteT)
        self.tbImprimir = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tbImprimir.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/images/actions/black_18/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbImprimir.setIcon(icon4)
        self.tbImprimir.setIconSize(QtCore.QSize(18, 18))
        self.tbImprimir.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.tbImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tbImprimir.setAutoRaise(True)
        self.tbImprimir.setObjectName("tbImprimir")
        self.horizontalLayout_3.addWidget(self.tbImprimir)
        self.pbListaVentas = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pbListaVentas.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/images/actions/black_18/reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pbListaVentas.setIcon(icon5)
        self.pbListaVentas.setIconSize(QtCore.QSize(18, 18))
        self.pbListaVentas.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbListaVentas.setAutoRaise(True)
        self.pbListaVentas.setObjectName("pbListaVentas")
        self.horizontalLayout_3.addWidget(self.pbListaVentas)
        self.verticalLayout_3.addWidget(self.frame)
        self.teDetalles = QtWidgets.QTextEdit(self.layoutWidget)
        self.teDetalles.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setPointSize(10)
        self.teDetalles.setFont(font)
        self.teDetalles.setObjectName("teDetalles")
        self.verticalLayout_3.addWidget(self.teDetalles)
        self.stackReportes = QtWidgets.QStackedWidget(self.splitter)
        self.stackReportes.setObjectName("stackReportes")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tVentas = QtWidgets.QTableView(self.page_5)
        self.tVentas.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tVentas.setAlternatingRowColors(True)
        self.tVentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tVentas.setSortingEnabled(True)
        self.tVentas.setObjectName("tVentas")
        self.tVentas.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tVentas)
        self.stackReportes.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grafica = QtWidgets.QGraphicsView(self.page_6)
        self.grafica.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.grafica.setObjectName("grafica")
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
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Form"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Form", "Dia"))
        self.tbFHome.setText(QtCore.QCoreApplication.translate("Form", "Tienda"))
        self.tbFHome.setShortcut(QtCore.QCoreApplication.translate("Form", "Home"))
        self.tbTitulo.setText(QtCore.QCoreApplication.translate("Form", "Reportes de ventas:"))
        self.label_17.setText(QtCore.QCoreApplication.translate("Form", "Desde:"))
        self.deFrom.setDisplayFormat(QtCore.QCoreApplication.translate("Form", "dd MMM yy   "))
        self.label_4.setText(QtCore.QCoreApplication.translate("Form", "Hasta:"))
        self.deTo.setDisplayFormat(QtCore.QCoreApplication.translate("Form", "dd MMM yy   "))
        self.label_8.setText(QtCore.QCoreApplication.translate("Form", "Filtrar formato:"))
        self.cbListas.setItemText(0, QtCore.QCoreApplication.translate("Form", "Ventas"))
        self.cbListas.setItemText(1, QtCore.QCoreApplication.translate("Form", "Compras"))
        self.cbListas.setItemText(2, QtCore.QCoreApplication.translate("Form", "Gastos"))
        self.cbListas.setItemText(3, QtCore.QCoreApplication.translate("Form", "Retiros"))
        self.cbListas.setItemText(4, QtCore.QCoreApplication.translate("Form", "Depositos"))
        self.label.setText(QtCore.QCoreApplication.translate("Form", "Filtrar caja:"))
        self.tbListar.setText(QtCore.QCoreApplication.translate("Form", "Listado"))
        self.tbGraficas.setText(QtCore.QCoreApplication.translate("Form", "Graficar"))
        self.bCorteT.setToolTip(QtCore.QCoreApplication.translate("Form", "Realizar corte de ventas."))
        self.bCorteT.setText(QtCore.QCoreApplication.translate("Form", "Corte"))
        self.tbImprimir.setText(QtCore.QCoreApplication.translate("Form", "Imprimir"))
        self.pbListaVentas.setText(QtCore.QCoreApplication.translate("Form", "Actualizar"))
        self.teDetalles.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:11pt;\">$</span></p></td></tr></table></body></html>", None, QtWidgets.QApplication.UnicodeUTF8))
# 
import icons_rc
  # TODO: regenerate with pyrcc6