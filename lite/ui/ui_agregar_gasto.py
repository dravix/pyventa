# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_agregar_gasto.ui'
#
# Created: Tue May  7 14:51:58 2013
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
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(498, 170)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../../usr/share/pyventa/images/32/pyventa-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("#Form{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));\n"
"\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbinfo = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbinfo.sizePolicy().hasHeightForWidth())
        self.lbinfo.setSizePolicy(sizePolicy)
        self.lbinfo.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lbinfo.setText(_fromUtf8(""))
        self.lbinfo.setTextFormat(QtCore.Qt.RichText)
        self.lbinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbinfo.setWordWrap(True)
        self.lbinfo.setObjectName(_fromUtf8("lbinfo"))
        self.verticalLayout.addWidget(self.lbinfo)
        self.frame_4 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgba(0,0,0,0);border-radius:5px;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame_4)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_20 = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_20)
        self.label_19 = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("background:none;border:0;"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_19)
        self.fLine = QtGui.QFrame(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine.sizePolicy().hasHeightForWidth())
        self.fLine.setSizePolicy(sizePolicy)
        self.fLine.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
"QToolButton, QLineEdit{background:transparent; border:0px; padding:3px}"))
        self.fLine.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fLine.setFrameShadow(QtGui.QFrame.Raised)
        self.fLine.setObjectName(_fromUtf8("fLine"))
        self.horizontalLayout_51 = QtGui.QHBoxLayout(self.fLine)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_51.setObjectName(_fromUtf8("horizontalLayout_51"))
        self.leConcepto = QtGui.QLineEdit(self.fLine)
        self.leConcepto.setObjectName(_fromUtf8("leConcepto"))
        self.horizontalLayout_51.addWidget(self.leConcepto)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.fLine)
        self.fLine_2 = QtGui.QFrame(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fLine_2.sizePolicy().hasHeightForWidth())
        self.fLine_2.setSizePolicy(sizePolicy)
        self.fLine_2.setStyleSheet(_fromUtf8(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}\n"
" QDoubleSpinBox{background:transparent; border:0px; padding:3px}"))
        self.fLine_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fLine_2.setFrameShadow(QtGui.QFrame.Raised)
        self.fLine_2.setObjectName(_fromUtf8("fLine_2"))
        self.horizontalLayout_52 = QtGui.QHBoxLayout(self.fLine_2)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_52.setObjectName(_fromUtf8("horizontalLayout_52"))
        self.dsbCantidad = QtGui.QDoubleSpinBox(self.fLine_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbCantidad.sizePolicy().hasHeightForWidth())
        self.dsbCantidad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.dsbCantidad.setFont(font)
        self.dsbCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbCantidad.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbCantidad.setMaximum(99999.99)
        self.dsbCantidad.setObjectName(_fromUtf8("dsbCantidad"))
        self.horizontalLayout_52.addWidget(self.dsbCantidad)
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.fLine_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tbCancelar = QtGui.QToolButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbCancelar.sizePolicy().hasHeightForWidth())
        self.tbCancelar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbCancelar.setFont(font)
        self.tbCancelar.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QAbstractButton::pressed{\n"
"color:#fff;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/color_18/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbCancelar.setIcon(icon1)
        self.tbCancelar.setIconSize(QtCore.QSize(12, 16))
        self.tbCancelar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCancelar.setObjectName(_fromUtf8("tbCancelar"))
        self.horizontalLayout.addWidget(self.tbCancelar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tbDone = QtGui.QToolButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbDone.sizePolicy().hasHeightForWidth())
        self.tbDone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbDone.setFont(font)
        self.tbDone.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(10, 125, 159, 255), stop:1 rgba(0, 188, 255, 255));color:#fff;\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;\n"
"}\n"
"QAbstractButton::pressed{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/actions/white_18/checkmark2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbDone.setIcon(icon2)
        self.tbDone.setIconSize(QtCore.QSize(16, 16))
        self.tbDone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbDone.setObjectName(_fromUtf8("tbDone"))
        self.horizontalLayout.addWidget(self.tbDone)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Registro de gasto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "Concepto:", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbCantidad.setPrefix(QtGui.QApplication.translate("Form", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.tbCancelar.setText(QtGui.QApplication.translate("Form", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.tbDone.setText(QtGui.QApplication.translate("Form", "Registrar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
