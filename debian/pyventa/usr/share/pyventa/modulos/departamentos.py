# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from modulos.control1 import Admin1
class Departamentos(Admin1):
    def __init__(self,parent,attached=False):
      info="Las familias se agrupan de manera semantica en departamentos que son basicamente areas dentro de la misma tienda."
      logo=":/actions/images/actions/color_18/pyramid.png"      
      Admin1.__init__(self,parent,'departamentos',[['id','Id','str',None,False],['nombre','Nombre','str',None,True]],info,logo,cond=" ORDER BY nombre ")
      self.ui=parent
      self.ui.connect(self.ui.verDepartamentos, SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tDepartamentos, SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verDepartamentos)
      self.anclar(attached)