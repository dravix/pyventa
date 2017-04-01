# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QComboBox
from PyQt4 import QtCore
from modulos.control1 import Admin1

class Familias(Admin1):
    def __init__(self,parent,attached=False):
      info="Los productos con caracteristicas similares se agrupan familias y estas a su vez pertenecen a un departamento."
      logo=":/actions/images/actions/color_18/card_spades.png"
      deps=QComboBox(parent)
      deps.setModel(parent.departamento.getModelo())
      deps.setModelColumn(1)
      Admin1.__init__(self,parent,'familias',[['id','Id','str',None,False],['nombre','Nombre','str',None,True] ,['departamento','Departamento','combo',deps,True]],info,logo,cond=" ORDER BY nombre ")
      self.ui=parent
      self.ui.connect(self.ui.verFamilias, QtCore.SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tFamilias, QtCore.SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verFamilias)
      self.anclar(not attached)