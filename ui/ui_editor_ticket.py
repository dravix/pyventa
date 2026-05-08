# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/ui_editor_ticket.ui'
#
# Created: Fri Dec  9 05:06:39 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../usr/share/pyventa/images/32/blog_compose.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(180, 180, 180, 255), stop:0.02 rgba(158, 158, 158, 255), stop:1 rgba(124, 124, 124, 255));color:#fff;}\n"
"  QScrollBar:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #ccc;\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"  QScrollBar::handle:vertical {\n"
"      background: #555;\n"
"      min-height: 20px;\n"
"  }\n"
"  QScrollBar::add-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #ccc;\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"  QScrollBar::sub-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #ccc;\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"      border: 2px solid grey;\n"
"      width: 3px;\n"
"      height: 3px;\n"
"      background: white;\n"
"  }\n"
"\n"
"  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"")
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.teTicket = QtWidgets.QPlainTextEdit(Dialog)
        self.teTicket.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(232, 232, 232, 255), stop:0.0818182 rgba(247, 247, 247, 255), stop:0.713636 rgba(255, 255, 255, 255));")
        self.teTicket.setObjectName("teTicket")
        self.verticalLayout.addWidget(self.teTicket)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("QPushButton{border-radius:4px;border: 1.2px solid #999;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:0.5 rgba(226, 226, 226, 255), stop:0.509091 rgba(219, 219, 219, 255), stop:0.986364 rgba(179, 179, 179, 255), stop:1 rgba(207, 228, 255, 255));padding:5;}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(216, 216, 216, 255), stop:0.495455 rgba(229, 229, 229, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Editor Simple de tickets"))
        self.titulo.setText(QtCore.QCoreApplication.translate("Dialog", "Editor simple de texto plano"))

