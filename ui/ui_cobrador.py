# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_cobrador.ui'
#
# Created: Tue May 14 03:29:22 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Cobrador(object):
    def setupUi(self, Cobrador):
        Cobrador.setObjectName(_fromUtf8("Cobrador"))
        Cobrador.resize(668, 334)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/coin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cobrador.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(Cobrador)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Cobrador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(14, 84, 175);color:#fff;"))
        self.label.setMargin(4)
        self.label.setIndent(13)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tabla = QtGui.QTableView(Cobrador)
        self.tabla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.verticalLayout_2.addWidget(self.tabla)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame = QtGui.QFrame(Cobrador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(228, 228, 228, 255));}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.fLine_2 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine_2.sizePolicy().hasHeightForWidth())
        self.fLine_2.setSizePolicy(sizePolicy)
        self.fLine_2.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QLineEdit{background:transparent; border:0px; padding:3px}"))
        self.fLine_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fLine_2.setFrameShadow(QtGui.QFrame.Raised)
        self.fLine_2.setObjectName(_fromUtf8("fLine_2"))
        self.horizontalLayout_52 = QtGui.QHBoxLayout(self.fLine_2)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setMargin(0)
        self.horizontalLayout_52.setObjectName(_fromUtf8("horizontalLayout_52"))
        self.leRecibo = QtGui.QLineEdit(self.fLine_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leRecibo.sizePolicy().hasHeightForWidth())
        self.leRecibo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.leRecibo.setFont(font)
        self.leRecibo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leRecibo.setObjectName(_fromUtf8("leRecibo"))
        self.horizontalLayout_52.addWidget(self.leRecibo)
        self.gridLayout.addWidget(self.fLine_2, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dsbTotal = QtGui.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.dsbTotal.setFont(font)
        self.dsbTotal.setStyleSheet(_fromUtf8("background:transparent;"))
        self.dsbTotal.setFrame(False)
        self.dsbTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbTotal.setReadOnly(True)
        self.dsbTotal.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbTotal.setAccelerated(True)
        self.dsbTotal.setMaximum(99999.99)
        self.dsbTotal.setObjectName(_fromUtf8("dsbTotal"))
        self.gridLayout.addWidget(self.dsbTotal, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.wCambio = QtGui.QWidget(self.frame)
        self.wCambio.setStyleSheet(_fromUtf8("background-color: rgb(255, 195, 55);color:#222;"))
        self.wCambio.setObjectName(_fromUtf8("wCambio"))
        self.formLayout_2 = QtGui.QFormLayout(self.wCambio)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.wCambio)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dsbCambio = QtGui.QDoubleSpinBox(self.wCambio)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.dsbCambio.setFont(font)
        self.dsbCambio.setStyleSheet(_fromUtf8("background:transparent;"))
        self.dsbCambio.setFrame(False)
        self.dsbCambio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbCambio.setReadOnly(True)
        self.dsbCambio.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbCambio.setAccelerated(True)
        self.dsbCambio.setMaximum(99999.99)
        self.dsbCambio.setObjectName(_fromUtf8("dsbCambio"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.dsbCambio)
        self.verticalLayout.addWidget(self.wCambio)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.botonUnion = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonUnion.sizePolicy().hasHeightForWidth())
        self.botonUnion.setSizePolicy(sizePolicy)
        self.botonUnion.setStyleSheet(_fromUtf8("*{border-radius:8px;\n"
"border: 1.2px solid #999;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));}\n"
"QToolButton::hover,QPushButton::hover{\n"
"    background-color:rgba(133, 217, 255, 100);\n"
"}\n"
"QToolButton::pressed,QPushButton::pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(239, 239, 239, 27), stop:1 rgba(68, 68, 68, 205));\n"
"}\n"
"QPushButton,QToolButton{padding:4px; background:transparent; border-radius:0;}\n"
" \n"
""))
        self.botonUnion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.botonUnion.setFrameShadow(QtGui.QFrame.Raised)
        self.botonUnion.setObjectName(_fromUtf8("botonUnion"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.botonUnion)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbCerrar = QtGui.QPushButton(self.botonUnion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbCerrar.sizePolicy().hasHeightForWidth())
        self.pbCerrar.setSizePolicy(sizePolicy)
        self.pbCerrar.setStyleSheet(_fromUtf8(" border:0px;border-radius:0;\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCerrar.setIcon(icon1)
        self.pbCerrar.setIconSize(QtCore.QSize(18, 18))
        self.pbCerrar.setAutoDefault(False)
        self.pbCerrar.setFlat(True)
        self.pbCerrar.setObjectName(_fromUtf8("pbCerrar"))
        self.horizontalLayout_4.addWidget(self.pbCerrar)
        self.tbCobrar = QtGui.QPushButton(self.botonUnion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbCobrar.sizePolicy().hasHeightForWidth())
        self.tbCobrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbCobrar.setFont(font)
        self.tbCobrar.setStyleSheet(_fromUtf8(" border:0px;border-left:1px solid #999;  \n"
"\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/bill.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbCobrar.setIcon(icon2)
        self.tbCobrar.setIconSize(QtCore.QSize(18, 18))
        self.tbCobrar.setCheckable(False)
        self.tbCobrar.setChecked(False)
        self.tbCobrar.setDefault(True)
        self.tbCobrar.setObjectName(_fromUtf8("tbCobrar"))
        self.horizontalLayout_4.addWidget(self.tbCobrar)
        self.verticalLayout.addWidget(self.botonUnion)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Cobrador)
        QtCore.QObject.connect(self.pbCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), Cobrador.accept)
        QtCore.QMetaObject.connectSlotsByName(Cobrador)
        Cobrador.setTabOrder(self.leRecibo, self.tbCobrar)
        Cobrador.setTabOrder(self.tbCobrar, self.pbCerrar)
        Cobrador.setTabOrder(self.pbCerrar, self.tabla)
        Cobrador.setTabOrder(self.tabla, self.dsbCambio)
        Cobrador.setTabOrder(self.dsbCambio, self.dsbTotal)

    def retranslateUi(self, Cobrador):
        Cobrador.setWindowTitle(QtGui.QApplication.translate("Cobrador", "Cobrar ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Cobrador", "Ventas a cobrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Cobrador", "Recibido:", None, QtGui.QApplication.UnicodeUTF8))
        self.leRecibo.setText(QtGui.QApplication.translate("Cobrador", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Cobrador", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbTotal.setPrefix(QtGui.QApplication.translate("Cobrador", " $ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Cobrador", "Cambio:", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbCambio.setPrefix(QtGui.QApplication.translate("Cobrador", " $ ", None, QtGui.QApplication.UnicodeUTF8))
        self.pbCerrar.setText(QtGui.QApplication.translate("Cobrador", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCobrar.setToolTip(QtGui.QApplication.translate("Cobrador", "Cobrar ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCobrar.setText(QtGui.QApplication.translate("Cobrador", "Cobrar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
