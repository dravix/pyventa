# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_cambia_precios.ui'
#
# Created: Thu Apr 11 03:55:34 2013
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
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(522, 454)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.topModule = QtGui.QWidget(Form)
        self.topModule.setStyleSheet(_fromUtf8("QToolButton, QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;color:#333;\n"
"}\n"
"QPushButton::pressed{\n"
"color:#fff;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"\n"
"}"))
        self.topModule.setObjectName(_fromUtf8("topModule"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.topModule)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chbGanancia = QtGui.QCheckBox(self.topModule)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbGanancia.setFont(font)
        self.chbGanancia.setObjectName(_fromUtf8("chbGanancia"))
        self.gridLayout.addWidget(self.chbGanancia, 3, 0, 1, 1)
        self.dsbIncremento = QtGui.QDoubleSpinBox(self.topModule)
        self.dsbIncremento.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dsbIncremento.setFont(font)
        self.dsbIncremento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbIncremento.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbIncremento.setPrefix(_fromUtf8(""))
        self.dsbIncremento.setDecimals(3)
        self.dsbIncremento.setMinimum(-999.99)
        self.dsbIncremento.setMaximum(999.99)
        self.dsbIncremento.setObjectName(_fromUtf8("dsbIncremento"))
        self.gridLayout.addWidget(self.dsbIncremento, 5, 1, 1, 1)
        self.dsbCosto = QtGui.QDoubleSpinBox(self.topModule)
        self.dsbCosto.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dsbCosto.setFont(font)
        self.dsbCosto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbCosto.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbCosto.setMaximum(99999.99)
        self.dsbCosto.setObjectName(_fromUtf8("dsbCosto"))
        self.gridLayout.addWidget(self.dsbCosto, 2, 1, 1, 1)
        self.dsbGanancia = QtGui.QDoubleSpinBox(self.topModule)
        self.dsbGanancia.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dsbGanancia.setFont(font)
        self.dsbGanancia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbGanancia.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbGanancia.setPrefix(_fromUtf8(""))
        self.dsbGanancia.setMaximum(99999.99)
        self.dsbGanancia.setObjectName(_fromUtf8("dsbGanancia"))
        self.gridLayout.addWidget(self.dsbGanancia, 3, 1, 1, 1)
        self.dsbPreciop = QtGui.QDoubleSpinBox(self.topModule)
        self.dsbPreciop.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dsbPreciop.setFont(font)
        self.dsbPreciop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbPreciop.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dsbPreciop.setMaximum(99999.99)
        self.dsbPreciop.setObjectName(_fromUtf8("dsbPreciop"))
        self.gridLayout.addWidget(self.dsbPreciop, 4, 1, 1, 1)
        self.chbPrecio = QtGui.QCheckBox(self.topModule)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbPrecio.setFont(font)
        self.chbPrecio.setObjectName(_fromUtf8("chbPrecio"))
        self.gridLayout.addWidget(self.chbPrecio, 4, 0, 1, 1)
        self.chbCosto = QtGui.QCheckBox(self.topModule)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chbCosto.setFont(font)
        self.chbCosto.setObjectName(_fromUtf8("chbCosto"))
        self.gridLayout.addWidget(self.chbCosto, 2, 0, 1, 1)
        self.chbIncremento = QtGui.QCheckBox(self.topModule)
        self.chbIncremento.setObjectName(_fromUtf8("chbIncremento"))
        self.gridLayout.addWidget(self.chbIncremento, 5, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pbProbar = QtGui.QPushButton(self.topModule)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbProbar.sizePolicy().hasHeightForWidth())
        self.pbProbar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(10)
        self.pbProbar.setFont(font)
        self.pbProbar.setStyleSheet(_fromUtf8(""))
        self.pbProbar.setObjectName(_fromUtf8("pbProbar"))
        self.gridLayout_2.addWidget(self.pbProbar, 0, 1, 1, 1)
        self.pbRestaurar = QtGui.QPushButton(self.topModule)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbRestaurar.sizePolicy().hasHeightForWidth())
        self.pbRestaurar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(10)
        self.pbRestaurar.setFont(font)
        self.pbRestaurar.setObjectName(_fromUtf8("pbRestaurar"))
        self.gridLayout_2.addWidget(self.pbRestaurar, 1, 1, 1, 1)
        self.pbGuardar = QtGui.QPushButton(self.topModule)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGuardar.sizePolicy().hasHeightForWidth())
        self.pbGuardar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pbGuardar.setFont(font)
        self.pbGuardar.setStyleSheet(_fromUtf8("QToolButton, QAbstractButton{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(10, 125, 159, 255), stop:1 rgba(0, 188, 255, 255));color:#fff;\n"
"border-radius:4px;border:1px solid #777; padding:2 9 2 9;\n"
"}\n"
"QAbstractButton::pressed{\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 66, 255, 255), stop:1 rgba(0, 107, 227, 255));\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/actions/sticker/key.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbGuardar.setIcon(icon)
        self.pbGuardar.setDefault(True)
        self.pbGuardar.setObjectName(_fromUtf8("pbGuardar"))
        self.gridLayout_2.addWidget(self.pbGuardar, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.topModule)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tvProductos = QtGui.QTableView(Form)
        self.tvProductos.setAlternatingRowColors(True)
        self.tvProductos.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tvProductos.setObjectName(_fromUtf8("tvProductos"))
        self.tvProductos.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tvProductos)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.chbCosto, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dsbCosto.setEnabled)
        QtCore.QObject.connect(self.chbGanancia, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dsbGanancia.setEnabled)
        QtCore.QObject.connect(self.chbPrecio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dsbPreciop.setEnabled)
        QtCore.QObject.connect(self.chbIncremento, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dsbIncremento.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Cambio de precios por lote", None, QtGui.QApplication.UnicodeUTF8))
        self.chbGanancia.setText(QtGui.QApplication.translate("Form", "Ganancia", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbIncremento.setToolTip(QtGui.QApplication.translate("Form", "Un incremento sube o baja el costo en una tasa porcentual", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbIncremento.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbCosto.setPrefix(QtGui.QApplication.translate("Form", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbGanancia.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.dsbPreciop.setPrefix(QtGui.QApplication.translate("Form", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.chbPrecio.setText(QtGui.QApplication.translate("Form", "Precio publico", None, QtGui.QApplication.UnicodeUTF8))
        self.chbCosto.setText(QtGui.QApplication.translate("Form", "Costo", None, QtGui.QApplication.UnicodeUTF8))
        self.chbIncremento.setText(QtGui.QApplication.translate("Form", "Incremento", None, QtGui.QApplication.UnicodeUTF8))
        self.pbProbar.setToolTip(QtGui.QApplication.translate("Form", "Hace una simulacion del cambio y lo muestra en la tabla, no aplica los cambios en la base de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.pbProbar.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRestaurar.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Descarta todos los cambios y regresa los productos al estado inicial.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRestaurar.setText(QtGui.QApplication.translate("Form", "Restaurar", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGuardar.setToolTip(QtGui.QApplication.translate("Form", "Aplica los cambios en la base de  datos.", None, QtGui.QApplication.UnicodeUTF8))
        self.pbGuardar.setText(QtGui.QApplication.translate("Form", "Guardar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
