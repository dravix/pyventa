# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/dialogos/ui_marcar_faltante.ui'
#
# Created: Sun May  5 08:42:23 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Faltante(object):
    def setupUi(self, Faltante):
        Faltante.setObjectName("Faltante")
        Faltante.resize(310, 172)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/images/actions/color_18/checkmark.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Faltante.setWindowIcon(icon)
        Faltante.setStyleSheet("QDialog{\n"
"    \n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(159, 159, 159, 255), stop:1 rgba(203, 203, 203, 255));\n"
"\n"
"color:#fff;border:0;}\n"
"QLabel{ border:0px; background:none; color:#222}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Faltante)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbProducto = QtWidgets.QLabel(Faltante)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbProducto.sizePolicy().hasHeightForWidth())
        self.lbProducto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbProducto.setFont(font)
        self.lbProducto.setWordWrap(True)
        self.lbProducto.setMargin(1)
        self.lbProducto.setObjectName("lbProducto")
        self.verticalLayout.addWidget(self.lbProducto)
        self.frame_2 = QtWidgets.QFrame(Faltante)
        self.frame_2.setStyleSheet(".QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:0.084833 rgba(255, 255, 255, 255), stop:1 rgba(250, 250, 250, 255));padding:0px; border-radius:4px;border:1px solid #999}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.dsbCantidad = QtWidgets.QDoubleSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dsbCantidad.setFont(font)
        self.dsbCantidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dsbCantidad.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dsbCantidad.setMaximum(99999.99)
        self.dsbCantidad.setProperty("value", 1.0)
        self.dsbCantidad.setObjectName("dsbCantidad")
        self.gridLayout.addWidget(self.dsbCantidad, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cbPrioridad = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbPrioridad.setFont(font)
        self.cbPrioridad.setObjectName("cbPrioridad")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/16/warning_16.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cbPrioridad.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/16/view-sort-descending.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cbPrioridad.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/16/tick_16.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cbPrioridad.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/pyventa/images/16/view-sort-ascending.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cbPrioridad.addItem(icon4, "")
        self.gridLayout.addWidget(self.cbPrioridad, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Dual_3 = QtWidgets.QSplitter(Faltante)
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
        font.setBold(False)
        font.setWeight(50)
        self.tbCerrar.setFont(font)
        self.tbCerrar.setStyleSheet(" border:0px;border-right:1px solid #999;border-radius:0;\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../../../../../Users/usr/share/pyventa/images/16/edit-delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbCerrar.setIcon(icon5)
        self.tbCerrar.setIconSize(QtCore.QSize(12, 16))
        self.tbCerrar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbCerrar.setObjectName("tbCerrar")
        self.tbMarcar = QtWidgets.QToolButton(self.Dual_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbMarcar.sizePolicy().hasHeightForWidth())
        self.tbMarcar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tbMarcar.setFont(font)
        self.tbMarcar.setStyleSheet(" border:0px;\n"
"background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(10, 125, 159, 255), stop:1 rgba(0, 188, 255, 255));color:#fff\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../../../../../Users/usr/share/pyventa/images/32/sub_black_accept.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tbMarcar.setIcon(icon6)
        self.tbMarcar.setIconSize(QtCore.QSize(16, 16))
        self.tbMarcar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tbMarcar.setObjectName("tbMarcar")
        self.horizontalLayout.addWidget(self.Dual_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Faltante)
        self.cbPrioridad.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Faltante)

    def retranslateUi(self, Faltante):
        Faltante.setWindowTitle(QtCore.QCoreApplication.translate("Faltante", "Marcar como faltante"))
        self.lbProducto.setText(QtCore.QCoreApplication.translate("Faltante", "Nombre del producto"))
        self.label_3.setText(QtCore.QCoreApplication.translate("Faltante", "Cantidad"))
        self.label_2.setText(QtCore.QCoreApplication.translate("Faltante", "Prioridad"))
        self.cbPrioridad.setItemText(0, QtCore.QCoreApplication.translate("Faltante", "Urgente"))
        self.cbPrioridad.setItemText(1, QtCore.QCoreApplication.translate("Faltante", "Alta"))
        self.cbPrioridad.setItemText(2, QtCore.QCoreApplication.translate("Faltante", "Normal"))
        self.cbPrioridad.setItemText(3, QtCore.QCoreApplication.translate("Faltante", "Baja"))
        self.tbCerrar.setText(QtCore.QCoreApplication.translate("Faltante", "Cerrar"))
        self.tbMarcar.setText(QtCore.QCoreApplication.translate("Faltante", "Marcar"))
# 
import icons_rc
  # TODO: regenerate with pyrcc6