# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_reportero.ui'
#
# Created: Sat Jul  7 05:30:28 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Reporte(object):
    def setupUi(self, Reporte):
        Reporte.setObjectName("Reporte")
        Reporte.resize(795, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(Reporte)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topReportes = QtWidgets.QFrame(Reporte)
        self.topReportes.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));")
        self.topReportes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topReportes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topReportes.setObjectName("topReportes")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.topReportes)
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tbTitulo = QtWidgets.QToolButton(self.topReportes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbTitulo.sizePolicy().hasHeightForWidth())
        self.tbTitulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.tbTitulo.setFont(font)
        self.tbTitulo.setStyleSheet("border:0;background:none;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/png/graficas_out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbTitulo.setIcon(icon)
        self.tbTitulo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbTitulo.setAutoRaise(True)
        self.tbTitulo.setArrowType(QtCore.Qt.NoArrow)
        self.tbTitulo.setObjectName("tbTitulo")
        self.horizontalLayout_4.addWidget(self.tbTitulo)
        self.frame = QtWidgets.QFrame(self.topReportes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame{border-radius:4px;\n"
"border: 1.2px solid #999;\n"
"}\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tbVer = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbVer.sizePolicy().hasHeightForWidth())
        self.tbVer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.tbVer.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../../usr/share/pyventa/images/32/cventa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbVer.setIcon(icon1)
        self.tbVer.setIconSize(QtCore.QSize(32, 32))
        self.tbVer.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbVer.setAutoRaise(True)
        self.tbVer.setObjectName("tbVer")
        self.horizontalLayout_3.addWidget(self.tbVer)
        self.tbPrint = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.tbPrint.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../../usr/share/pyventa/images/32/print-down.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbPrint.setIcon(icon2)
        self.tbPrint.setIconSize(QtCore.QSize(32, 32))
        self.tbPrint.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.tbPrint.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbPrint.setAutoRaise(True)
        self.tbPrint.setObjectName("tbPrint")
        self.horizontalLayout_3.addWidget(self.tbPrint)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.topReportes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background:rgba(0,0,0,0);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frDesde = QtWidgets.QFrame(self.widget)
        self.frDesde.setStyleSheet("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.00909091 rgba(71, 71, 71, 255), stop:0.0636364 rgba(106, 143, 146, 255), stop:0.468182 rgba(73, 122, 127, 255), stop:1 rgba(52, 98, 104, 255));\n"
"border-radius:5px; border:0;}\n"
"QDateEdit, QLabel{background:rgba(0,0,0,0);color:#eee;}\n"
"#frDia,frDesde,frHasta QLabel{color:#fff;font-weight:600;font-size:16;}\n"
"QDateEdit::drop-down{border:0;}\n"
"QDateEdit::down-arrow{image:url(/usr/share/pyventa/images/16/calendar_16.png)}\n"
"\n"
"QDateEdit QWidget{\n"
"background:rgba(73, 122, 127, 255);\n"
"color:#eee}")
        self.frDesde.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frDesde.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frDesde.setObjectName("frDesde")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frDesde)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frDesde)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.deDesde = QtWidgets.QDateEdit(self.frDesde)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.deDesde.setFont(font)
        self.deDesde.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.deDesde.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.deDesde.setAccelerated(True)
        self.deDesde.setCalendarPopup(True)
        self.deDesde.setObjectName("deDesde")
        self.verticalLayout_8.addWidget(self.deDesde)
        self.horizontalLayout_2.addWidget(self.frDesde)
        self.frHasta = QtWidgets.QFrame(self.widget)
        self.frHasta.setStyleSheet("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.00909091 rgba(71, 71, 71, 255), stop:0.0636364 rgba(106, 143, 146, 255), stop:0.468182 rgba(73, 122, 127, 255), stop:1 rgba(52, 98, 104, 255));\n"
"border-radius:5px; border:0;}\n"
"QDateEdit, QLabel{background:rgba(0,0,0,0);color:#eee;}\n"
"#frDia,frDesde,frHasta QLabel{color:#fff;font-weight:600;font-size:16;}\n"
"QDateEdit::drop-down{border:0;}\n"
"QDateEdit::down-arrow{image:url(/usr/share/pyventa/images/16/calendar_16.png)}\n"
"\n"
"QDateEdit QWidget{\n"
"background:rgba(73, 122, 127, 255);\n"
"color:#eee}")
        self.frHasta.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frHasta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frHasta.setObjectName("frHasta")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frHasta)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frHasta)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.deHasta = QtWidgets.QDateEdit(self.frHasta)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.deHasta.setFont(font)
        self.deHasta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.deHasta.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.deHasta.setAccelerated(True)
        self.deHasta.setCalendarPopup(True)
        self.deHasta.setObjectName("deHasta")
        self.verticalLayout_7.addWidget(self.deHasta)
        self.horizontalLayout_2.addWidget(self.frHasta)
        self.verticalLayout_4.addWidget(self.widget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.topReportes)
        self.pteQuery = QtWidgets.QPlainTextEdit(Reporte)
        self.pteQuery.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pteQuery.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.00507614 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pteQuery.setObjectName("pteQuery")
        self.verticalLayout.addWidget(self.pteQuery)
        self.tvTabla = QtWidgets.QTableView(Reporte)
        self.tvTabla.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tvTabla.setAlternatingRowColors(True)
        self.tvTabla.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tvTabla.setSortingEnabled(True)
        self.tvTabla.setObjectName("tvTabla")
        self.verticalLayout.addWidget(self.tvTabla)

        self.retranslateUi(Reporte)
        QtCore.QMetaObject.connectSlotsByName(Reporte)

    def retranslateUi(self, Reporte):
        Reporte.setWindowTitle(QtCore.QCoreApplication.translate("Reporte", "Form"))
        self.tbTitulo.setText(QtCore.QCoreApplication.translate("Reporte", "Reporte."))
        self.tbVer.setText(QtCore.QCoreApplication.translate("Reporte", "Ejecutar"))
        self.tbPrint.setText(QtCore.QCoreApplication.translate("Reporte", "Imprimir"))
        self.label_5.setText(QtCore.QCoreApplication.translate("Reporte", "Desde"))
        self.deDesde.setDisplayFormat(QtCore.QCoreApplication.translate("Reporte", "dd|MMM|yyyy"))
        self.label_4.setText(QtCore.QCoreApplication.translate("Reporte", "Hasta"))
        self.deHasta.setDisplayFormat(QtCore.QCoreApplication.translate("Reporte", "dd|MMM|yyyy"))
        self.pteQuery.setPlainText(QtCore.QCoreApplication.translate("Reporte", "Select ref,descripcion,precio  from productos where ultima_modificacion> \'2010-10-10\' limit 20;"))

