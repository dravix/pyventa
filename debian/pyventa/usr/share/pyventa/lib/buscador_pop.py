# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.ui_buscador_pop import Ui_Dialog
from lib import libutil

class buscadorPop(QtGui.QDialog, Ui_Dialog):
    def __init__(self,parent,texto='',en=1,campos=['Ref','Descripcion','Precio'],tabla='',multi=False):
	QtGui.QDialog.__init__(self)
	self.setupUi(self)
	self.cursor=parent.cursor
	self.parent=parent
	self.en=en
	self.campos=campos
	self.tabla=tabla
	self.modelo=None
	self.leFiltro.setText(str(texto))
	self.leFiltro.setFocus()
	#for k,i in campos.iteritems():
	  #self.head.append(k)
	  #self.campos.append(i)

      
	self.listar()
	self.producto={}
	self.seleccionados=[]
	self.multi=multi #Indica si require seleccionar multiples productos
	if self.multi:
	  self.tvResulta.setSelectionMode(QAbstractItemView.ExtendedSelection)
	self.connect(self.leFiltro, QtCore.SIGNAL("returnPressed()"), self.listar)
	self.connect(self.pbBuscar, QtCore.SIGNAL("clicked()"), self.listar)
	
	self.connect(self.tvResulta,QtCore.SIGNAL('activated(const QModelIndex&)'),self.retornar)
	#self.connect(self.tbDone,QtCore.SIGNAL('clicked()'),self.retornar)
	self.connect(self.tbCancelar,QtCore.SIGNAL('clicked()'),self.reject)
	self.connect(self,QtCore.SIGNAL('accepted()'),self.retornar)
	self.listar(texto)
	
	
	
    def listar(self,texto=False):
      if not texto:
	texto=str(self.leFiltro.text())	
      where=''
      if len(texto)>0:
	where=" WHERE  `%s` like '%%%s%%' "%(self.campos[self.en],texto)
      sql="SELECT %s from %s %s "%(','.join(self.campos), self.tabla, where)
      #print sql
      self.modelo=self.parent.entabla(self.tvResulta,self.campos,sql)    
      self.tvResulta.resizeColumnsToContents()  
    

    def getFilas(self):
      return libutil.seleccionarFilas(self.tvResulta, self.modelo)
      
    def retornar(self):
	#try:
	  #ret=int(libutil.seleccionar(self.tvResulta, self.modelo)[0])
	#except:
	  #ret=-1
	#else:
	  self.done(int(libutil.seleccionar(self.tvResulta, self.modelo)[0])) 




