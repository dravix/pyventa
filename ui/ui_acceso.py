# -*- coding: utf-8 -*-
# Form implementation migrated from PyQt4 → PyQt6
# Original: qt/dialogos/ui_acceso.ui (PyQt4 UI code generator 4.9.3)
# Migrated: PyQt6 6.x

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Acceso(object):
    def setupUi(self, Acceso):
        Acceso.setObjectName("Acceso")
        Acceso.setStyleSheet(
            ".QWidget{background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0,"
            " stop:0 rgba(201,201,201,255), stop:1 rgba(228,228,228,255));}\n"
            "QLineEdit{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,"
            " stop:0 rgba(150,150,150,255), stop:0.084833 rgba(255,255,255,255),"
            " stop:1 rgba(250,250,250,255));padding:0px;border-radius:4px;border:1px solid #999}"
        )

        self.verticalLayout = QtWidgets.QVBoxLayout(Acceso)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")

        # Info label (welcome / module name)
        self.lbInfo = QtWidgets.QLabel(Acceso)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.lbInfo.setSizePolicy(sizePolicy)
        self.lbInfo.setStyleSheet("background:none;border:0;")
        self.lbInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbInfo.setWordWrap(True)
        self.lbInfo.setObjectName("lbInfo")
        self.verticalLayout.addWidget(self.lbInfo)

        # Alert label
        self.lblAlerta = QtWidgets.QLabel(Acceso)
        self.lblAlerta.setStyleSheet(
            "background-color: rgb(255,178,158);\n"
            "border:2px solid rgb(186,75,75);\n"
            "color:rgb(175,56,56);\n"
            "padding:5px;"
        )
        self.lblAlerta.setText("")
        self.lblAlerta.setObjectName("lblAlerta")
        self.verticalLayout.addWidget(self.lblAlerta)

        # Logo + form row
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.logo = QtWidgets.QLabel(Acceso)
        sizePolicy2 = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setStyleSheet("background:none;border:0;")
        self.logo.setText("")
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)

        # Form grid
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 3)
        self.gridLayout.setObjectName("gridLayout")

        bold10 = QtGui.QFont()
        bold10.setPointSize(10)
        bold10.setBold(True)
        bold10.setWeight(75)

        regular10 = QtGui.QFont()
        regular10.setPointSize(10)
        regular10.setBold(False)
        regular10.setWeight(50)

        bold14 = QtGui.QFont()
        bold14.setPointSize(14)
        bold14.setBold(True)
        bold14.setWeight(75)

        align_right = (
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )

        # "Usuario:" label
        self.label_19 = QtWidgets.QLabel(Acceso)
        self.label_19.setFont(bold10)
        self.label_19.setStyleSheet("background:none;border:0;")
        self.label_19.setAlignment(align_right)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        # "Clave:" label
        self.label_20 = QtWidgets.QLabel(Acceso)
        self.label_20.setFont(bold10)
        self.label_20.setStyleSheet("background:none;border:0;")
        self.label_20.setAlignment(align_right)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)

        # Username field
        self.leUsuario = QtWidgets.QLineEdit(Acceso)
        self.leUsuario.setMaximumSize(QtCore.QSize(170, 16777215))
        self.leUsuario.setFont(bold14)
        self.leUsuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.leUsuario.setObjectName("leUsuario")
        self.gridLayout.addWidget(self.leUsuario, 0, 1, 1, 1)

        # Password field
        self.leClave = QtWidgets.QLineEdit(Acceso)
        self.leClave.setMaximumSize(QtCore.QSize(170, 16777215))
        self.leClave.setFont(bold14)
        self.leClave.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.leClave.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.leClave.setObjectName("leClave")
        self.gridLayout.addWidget(self.leClave, 1, 1, 1, 1)

        # "Servidor:" label
        self.lblServidor = QtWidgets.QLabel(Acceso)
        self.lblServidor.setFont(regular10)
        self.lblServidor.setAlignment(align_right)
        self.lblServidor.setObjectName("lblServidor")
        self.gridLayout.addWidget(self.lblServidor, 2, 0, 1, 1)

        # Remote server combo
        self.cbServidores = QtWidgets.QComboBox(Acceso)
        sp_exp = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.cbServidores.setSizePolicy(sp_exp)
        self.cbServidores.setObjectName("cbServidores")
        self.gridLayout.addWidget(self.cbServidores, 2, 1, 1, 1)

        # "Clave servidor" label
        self.lblClaveServidor = QtWidgets.QLabel(Acceso)
        self.lblClaveServidor.setFont(regular10)
        self.lblClaveServidor.setAlignment(align_right)
        self.lblClaveServidor.setObjectName("lblClaveServidor")
        self.gridLayout.addWidget(self.lblClaveServidor, 3, 0, 1, 1)

        # Server password field
        self.leClaveServidor = QtWidgets.QLineEdit(Acceso)
        self.leClaveServidor.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.leClaveServidor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.leClaveServidor.setObjectName("leClaveServidor")
        self.gridLayout.addWidget(self.leClaveServidor, 3, 1, 1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Button row
        btn_style = (
            "QToolButton, QAbstractButton{"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,"
            " stop:0 rgba(239,239,239,255), stop:0.5 rgba(226,226,226,255),"
            " stop:0.509091 rgba(219,219,219,255), stop:0.986364 rgba(179,179,179,255),"
            " stop:1 rgba(207,228,255,255));"
            "border-radius:4px;border:1px solid #777;padding:2px 9px 2px 9px;color:#333;}"
            "QAbstractButton::pressed{color:#fff;"
            "background-color:qlineargradient(spread:reflect,x1:1,y1:1,x2:1,y2:0,"
            "stop:0 rgba(0,66,255,255),stop:1 rgba(0,107,227,255));}"
        )
        remote_style = btn_style + (
            "QAbstractButton::checked{background-color:qlineargradient(spread:reflect,"
            "x1:1,y1:1,x2:1,y2:0,stop:0.0382775 rgba(159,11,0,255),stop:1 rgba(213,52,0,255));"
            "color:#efefef;}"
        )
        accept_style = (
            "QToolButton, QAbstractButton{background-color:qlineargradient(spread:reflect,"
            "x1:1,y1:1,x2:1,y2:0,stop:0 rgba(10,125,159,255),stop:1 rgba(0,188,255,255));"
            "color:#fff;border-radius:4px;border:1px solid #777;padding:2px 9px 2px 9px;}"
            "QAbstractButton::pressed{background-color:qlineargradient(spread:reflect,"
            "x1:1,y1:1,x2:1,y2:0,stop:0 rgba(0,66,255,255),stop:1 rgba(0,107,227,255));}"
        )

        font_btn = QtGui.QFont()
        font_btn.setFamily("Droid Sans")
        font_btn.setPointSize(10)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pbRemoto = QtWidgets.QPushButton(Acceso)
        self.pbRemoto.setFont(font_btn)
        self.pbRemoto.setStyleSheet(remote_style)
        self.pbRemoto.setCheckable(True)
        self.pbRemoto.setObjectName("pbRemoto")
        self.horizontalLayout.addWidget(self.pbRemoto)

        spacer = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacer)

        self.pbCerrar = QtWidgets.QPushButton(Acceso)
        self.pbCerrar.setFont(font_btn)
        self.pbCerrar.setStyleSheet(btn_style)
        self.pbCerrar.setObjectName("pbCerrar")
        self.horizontalLayout.addWidget(self.pbCerrar)

        self.pbAceptar = QtWidgets.QPushButton(Acceso)
        self.pbAceptar.setFont(font_btn)
        self.pbAceptar.setStyleSheet(accept_style)
        self.pbAceptar.setDefault(True)
        self.pbAceptar.setObjectName("pbAceptar")
        self.horizontalLayout.addWidget(self.pbAceptar)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Acceso)
        QtCore.QMetaObject.connectSlotsByName(Acceso)

        Acceso.setTabOrder(self.leUsuario, self.leClave)
        Acceso.setTabOrder(self.leClave, self.cbServidores)
        Acceso.setTabOrder(self.cbServidores, self.leClaveServidor)
        Acceso.setTabOrder(self.leClaveServidor, self.pbAceptar)
        Acceso.setTabOrder(self.pbAceptar, self.pbRemoto)
        Acceso.setTabOrder(self.pbRemoto, self.pbCerrar)

    def retranslateUi(self, Acceso):
        _t = QtCore.QCoreApplication.translate
        Acceso.setWindowTitle(_t("Acceso", "Inicio de sesión"))
        self.lbInfo.setText(_t("Acceso", "<b>Punto de venta.</b>"))
        self.label_19.setText(_t("Acceso", "Usuario:"))
        self.label_20.setText(_t("Acceso", "Clave:"))
        self.lblClaveServidor.setText(_t("Acceso", "Clave servidor"))
        self.lblServidor.setText(_t("Acceso", "Servidor:"))
        self.pbRemoto.setText(_t("Acceso", "Conexión remota"))
        self.pbCerrar.setText(_t("Acceso", "Cancelar"))
        self.pbAceptar.setText(_t("Acceso", "Ingresar"))
