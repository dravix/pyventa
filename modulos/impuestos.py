# -*- coding: utf-8 -*-
from PyQt4.QtGui import QComboBox
from PyQt4 import QtCore
from modulos.control1 import Admin1

class Impuestos(Admin1):
    def __init__(self,parent,attached=False):
      icono=":/actions/images/actions/color_18/money_bag.png"
      Admin1.__init__(self,parent,'impuestos',[['id','Id','str',None,False],['nombre','Nombre','str',None,True],['porcentaje','Porcentaje','double',None,True]],"Estos impuestos son solo indicativos, debe existir por lo menos un impuesto por cada producto",icono)
      self.ui=parent
      self.ui.connect(self.ui.verImpuestos, QtCore.SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tImpuestos, QtCore.SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verImpuestos)
      self.anclar(attached)