# -*- coding: utf-8 -*-
from PyQt4.QtGui import QComboBox
from PyQt4.QtCore import SIGNAL
from modulos.control1 import Admin1

class Conexiones(Admin1):
    def __init__(self,parent,attached=False):
      info="Para poder hacer conexiones remotas a otros servidores es necesario antes registrar los datos de esas conexiones."
      logo=":/actions/images/actions/color_18/connect.png"
      Admin1.__init__(self,parent,'conexiones',[
      ['id','Id','str',None,False],
      ['nombre','Nombre distintivo*','str',None,True] ,
      ['servidor','Nombre del servidor*','str',None,True],
      ['esquema','Nombre de Base de datos*','str',None,True],
      ['version','Version','double',None,True],
      ['usuario','Usuario*','str',None,True],
      ['clave','Clave','hide',None,False],
      ['principal','Favorita','int',None,True],
      ['ultima_conexion','Ultima conexion','date',None,True],
      ],info,logo,cond=" ORDER BY nombre ")
      self.ui=parent
      self.ui.connect(self.ui.actionConexiones, SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tConexiones, SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verFamilias)
      self.anclar(not attached)