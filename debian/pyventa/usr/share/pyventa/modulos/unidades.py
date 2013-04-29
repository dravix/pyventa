# -*- coding: utf-8 -*-
from PyQt4.QtGui import QComboBox
from PyQt4 import QtCore
from modulos.control1 import Admin1

class Unidades(Admin1):
    def __init__(self,parent,attached=False):
      info="Las unidades sirven como indicativos para la presentacion del producto."
      logo=":/actions/images/actions/color_18/ruler_square.png"
      Admin1.__init__(self,parent,'unidades',[['id','Id','str',None,False],['nombre','Nombre','str',None,True]],info,logo)
      self.ui=parent
      self.ui.connect(self.ui.verUnidades, QtCore.SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tUnidades, QtCore.SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verUnidades)
      self.anclar(attached)