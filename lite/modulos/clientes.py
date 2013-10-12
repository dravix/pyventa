#['Id','Nombre','rfc','direccion','poblacion','estado','tel','correo','credito']
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QLineEdit,QSpinBox
from PyQt4 import QtCore
from modulos.control1 import Admin1

class Clientes(Admin1):
    def __init__(self,parent,attached=False):
      cp=QLineEdit(parent)
      tel=QLineEdit(parent)
      tipo=QSpinBox(parent)
      tipo.setMaximum(2)
      tipo.setMinimum(0)
      tipo.setButtonSymbols(2)
      #cp.setInputMask("#####")
      tel.setInputMask("(###)-###-##-##")
      cp.setAlignment(QtCore.Qt.AlignCenter)
      tipo.setAlignment(QtCore.Qt.AlignCenter)
      tel.setAlignment(QtCore.Qt.AlignCenter)
      Admin1.__init__(self,parent,'clientes',
      [['id','Id:','str',None,False],
      ['nombre','Nombre:','str',None,True],
      ['rfc','RFC:','str',None,True],
      ['direccion','Direccion:','str',None,True],
      ['poblacion','Poblacion:','str',None,True],
      ['estado','Estado:','str',None,True],
      ['tel','Telefono:','str',tel,True],
      ['correo','E-mail:','str',cp,True],
      ['tipo','Tipo:','hide',0,True],
      ['credito','Credito:','hide',0,False]],
      info="",logo=":/modulos/images/png/elegant/clientes.png",ide=-1,ancla=True,cond=" WHERE tipo=0 order by nombre"
      )
      self.ui=parent
      self.ui.connect(self.ui.tClientes, QtCore.SIGNAL("clicked()"), self.iniciar)
      self.ui.connect(self.ui.verClientes, QtCore.SIGNAL("triggered()"), self.iniciar)

      self.anclar(attached)
	