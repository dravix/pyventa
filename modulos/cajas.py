#['Id','Nombre','rfc','direccion','poblacion','estado','tel','correo','credito']
# -*- coding: utf-8 -*-
from PyQt6.QtWidgets import QLineEdit, QSpinBox
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
from modulos.control1 import Admin1

class Cajas(Admin1):
    def __init__(self,parent,attached=False):
      #ip=QLineEdit(parent)
      tipo=QSpinBox(parent)
      tipo.setMaximum(2)
      tipo.setMinimum(0)
      tipo.setButtonSymbols(2)
      #ip.setInputMask("000.000.000.000")
      tipo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      #ip.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
      info="Las ventas son distribuidas en cajas, asi que debe existir una caja por menos."
      icono=":/actions/images/actions/color_18/monitor.png"
      Admin1.__init__(self,parent,'cajas',
      [['num_caja','Id:','str',None,False],
      ['nombre','Nombre:','str',None,True],
      ['maquina','Direccion IP (Opcional):','str',None,True],
      ['saldo_inicial','Saldo inicial:','double',None,True],
      ['estado','Ultima apertura :','date',None,True],
      ['efectivo','Efectivo:','double',None,True]
      ],info, icono,-1,True)
      self.ui=parent
      action= self.ui.menuObjetos.addAction(QIcon(icono),"Cajas")
      action.setIconVisibleInMenu(True)
      #self.ui.menuObjetos.addAction()
      self.ui.connect(action, QtCore.SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(parent.tCajas, QtCore.SIGNAL("clicked()"), self.iniciar)
      #self.iniciar()
      #self.ui.stack.addWidget(self)
      #self.num=self.ui.stack.count()-1
      self.anclar(attached)