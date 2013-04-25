# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.ui_buscador_pop import Ui_Dialog
from lib import libutil
from lib.modelos.qmodelotablasql import QModeloTablaSql

class buscadorPop(QtGui.QDialog, Ui_Dialog):
    def __init__(self,parent,texto='',en=1,campos=['Ref','Descripcion','Precio'],tabla='',multi=False):
      #texto= texto inicial de busqueda, en=campo a buscar, campos=campos q se desplegaran, tabla=nombre de la tabla de la DB, multi=modo de seleccion de retorno
	QtGui.QDialog.__init__(self,parent)
	self.setupUi(self)
	self.cursor=parent.cursor
	self.parent=parent
	self.en=en
	self.campos=campos
	self.tabla=tabla
	self.modelo=QModeloTablaSql(self.parent.cursor,self)
	self.tvResulta.setModel(self.modelo)
	self.leFiltro.setText(str(texto))
	self.leFiltro.setFocus()
	#for k,i in campos.iteritems():
	  #self.head.append(k)
	  #self.campos.append(i)
	
	self.producto={}
	self.seleccionados=[]
	self.multi=multi #Indica si require seleccionar multiples productos
	if self.multi:
	  self.tvResulta.setSelectionMode(QAbstractItemView.ExtendedSelection)
	self.connect(self.leFiltro, QtCore.SIGNAL("returnPressed()"), self.listar)
	self.connect(self.pbBuscar, QtCore.SIGNAL("clicked()"), self.listar)
	
	self.connect(self.tvResulta,QtCore.SIGNAL('activated(const QModelIndex&)'),self.accept)
	#self.connect(self.tbDone,QtCore.SIGNAL('clicked()'),self.retornar)
	self.connect(self.tbCancelar,QtCore.SIGNAL('clicked()'),self.reject)
	#self.connect(self,QtCore.SIGNAL('accepted()'),self.retornar)
	
	self.listar(texto)
	
	
	
    def listar(self,texto=False):
      if not texto:
	texto=str(self.leFiltro.text())	
      where=''
      if len(texto)>0:
	where=" WHERE  `%s` like '%%%s%%' "%(self.campos[self.en],texto)
      sql="SELECT %s from %s %s "%(','.join(self.campos), self.tabla, where)
      #print sql
      self.modelo.query(sql,self.campos)    
      self.tvResulta.resizeColumnsToContents()  
    
    def selected(self,cols=()):
      #cols es un conjunto de numeros de columnas que se retornara
      indices=self.tvResulta.selectedIndexes()
      dic={}
      for index in indices:
	if index.column()==0:
	  dic[index.row()]=[str(index.data().toString())]
	elif index.column() in cols:
	  dic[index.row()].append(str(index.data().toString()))
      return [item for key,item in dic.iteritems()]
	
	
    def getFilas(self):
      return libutil.seleccionarFilas(self.tvResulta, self.modelo)
      
    def retornar(self):
	self.done(1)




