# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_buscador_pop import Ui_Dialog
from lib import libutil
from lib.modelos.qmodelotablasql import QModeloTablaSql

class buscadorPop(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self,parent,texto='',en=1,campos=['Ref','Descripcion','Precio'],tabla='',multi=False):
      #texto= texto inicial de busqueda, en=campo a buscar, campos=campos q se desplegaran, tabla=nombre de la tabla de la DB, multi=modo de seleccion de retorno
        QtWidgets.QDialog.__init__(self,parent)
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
        #for k,i in campos.items():
          #self.head.append(k)
          #self.campos.append(i)
        
        self.producto={}
        self.seleccionados=[]
        self.multi=multi #Indica si require seleccionar multiples productos
        if self.multi:
          self.tvResulta.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.leFiltro.returnPressed.connect(self.listar)
        self.pbBuscar.clicked.connect(self.listar)
        
        self.tvResulta.activated.connect(self.accept)
        #self.tbDone.clicked.connect(self.retornar)
        self.tbCancelar.clicked.connect(self.reject)
        #self.accepted.connect(self.retornar)
        
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
      return [item for key,item in dic.items()]
        
        
    def getFilas(self):
      return libutil.seleccionarFilas(self.tvResulta, self.modelo)
      
    def retornar(self):
        self.done(1)




