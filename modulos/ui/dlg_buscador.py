# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui,  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_buscador import Ui_Dialog
import  datetime
import MySQLdb
class buscador(QtGui.QDialog, Ui_Dialog):
    def __init__(self,parent,texto='',campos=['Ref','Descripcion','Precio'],multi=False):
	QtGui.QDialog.__init__(self)
	self.setupUi(self)
	self.cursor=parent.cursor
	self.parent=parent
	self.head=campos
	self.leFiltro.setText(str(texto))
	self.leFiltro.setFocus(True)
	self.leFiltro.selectAll()
	self.buscar()
	self.producto={}
	self.seleccionados=[]
	self.multi=multi #Indica si require seleccionar multiples productos
	if self.multi:
	  self.twResulta.setSelectionMode(QAbstractItemView.ExtendedSelection)
	self.connect(self.leFiltro, SIGNAL("returnPressed()"), self.buscar)
	self.connect(self.cbDep,SIGNAL("activated(int)"),self.filtrarFamilias)
	self.connect(self.cbFam,SIGNAL("activated(int)"),self.buscar)
	self.connect(self.twResulta,SIGNAL('cellActivated (int, int)'),self.retornar)
	self.connect(self.tbDone,SIGNAL('clicked()'),self.retornar)
	self.connect(self.tbCancelar,SIGNAL('clicked()'),self.reject)
	
	self.iniciarCombos()
	  
    def iniciarCombos(self):
	self.cbDep.addItem("Todos",-1)
	self.cbFam.addItem("Todas",-1)
	self.cursor.execute("SELECT * FROM departamentos;")
	deps=self.cursor.fetchall()
	for dep in deps:
	    self.cbDep.addItem(dep[1],dep[0])
	self.cursor.execute("SELECT * FROM familias;")
	fams=self.cursor.fetchall()
	for fam in fams:
	    self.cbFam.addItem(fam[1],fam[0])

    def filtrarFamilias(self):
	  dep=self.cbDep.itemData(self.cbDep.currentIndex()).toString()
	  self.cbFam.clear()
	  self.cursor.execute("SELECT id,nombre from familias where departamento="+str(dep))
	  fams=self.cursor.fetchall()
	  for item in fams:
	      self.cbFam.addItem(item[1],item[0])
	  self.buscar()

    def buscar(self):
      txt=str(self.leFiltro.text())
      if len(txt)>0:
	if len(txt)>2 or txt[0].isdigit():
	  departamentos=""
	  familias=""
	  tipo=''
    	  fam=self.cbFam.itemData(self.cbFam.currentIndex()).toString()
	  dep=self.cbDep.itemData(self.cbDep.currentIndex()).toString()
	  if fam!='-1': 
	    familias=" AND `familia` = '"+fam+"'"
	  #if dep!='-1':
	    #familias=""
	  if (txt[0].isdigit()==False):
	    tipo=" `descripcion` like '%"+txt+"%' "
	  else:
	    tipo= "codigo="+txt+" or ref="+txt+""
	  col='`'
	  col+='`,`'.join(self.head)
	  col+='`'
	  sql=str("SELECT "+col+" FROM productos where "+tipo+"  "+familias+" order by `vendidas`; ")
	  self.matriz=self.parent.tabular(self.twResulta,sql,self.head)

    def retornar(self):
	self.retorno=int(self.twResulta.item(self.twResulta.currentRow(),0).text())
	if self.multi:
	  tmp=[]
	  lastrow=-1
	  lista=self.twResulta.selectedItems()
	  for i in lista:
	    try:
	     tmp.index(i.row())
	    except: 
	      tmp.append(i.row())
	      self.seleccionados.append(self.matriz[i.row()])
	      
    	  #for i,li in enumerate(lista):
	    #self.productos[tmp.index(li.row())][self.head[li.column()]]=li.text()
	  self.done(1)
	else:  
	  for i,item in enumerate(self.head):
	    self.producto[item]=str(self.twResulta.item(self.twResulta.currentRow(),i).text())
	  self.done(self.retorno)
	  
class BuscadorF(buscador):
    def __init__(self,parent,texto='',campos=['Id','Nombre','Departamento'],multi=False):
	buscador.__init__(self,parent,texto,campos,multi)
	self.cbDep.setVisible(False)
	self.cbFam.setVisible(False)
	self.lblDep.setVisible(False)
	self.lblFam.setVisible(False)
	
    def iniciarCombos(self):
	pass

    def filtrarFamilias(self):
      pass
    
    def buscar(self):
      txt=str(self.leFiltro.text())
      if len(txt)>0:
	  tipo=''
	  if (txt[0].isdigit()==False):
	    tipo=" nombre like '%"+txt+"%' "
	  else:
	    tipo= "id="+txt
	  col='`'
	  col+='`,`'.join(self.head)
	  col+='`'
	  sql=str("SELECT "+col+" FROM familias where "+tipo+"  order by `nombre`; ")
	  self.matriz=self.parent.tabular(self.twResulta,sql,self.head)	

class BuscadorF(buscador):
    def __init__(self,parent,texto='',campos=['Id','Nombre'],multi=False):
	buscador.__init__(self,parent,texto,campos,multi)
	self.cbDep.setVisible(False)
	self.cbFam.setVisible(False)
	self.lblDep.setVisible(False)
	self.lblFam.setVisible(False)
	self.titulo.setText("Buscador de Familias")
	self.lblInfo.setText("Escriba el nombre o el ID")
	
    def iniciarCombos(self):
	pass

    def filtrarFamilias(self):
      pass
    
    def buscar(self):
      txt=str(self.leFiltro.text())
      tipo=" nombre like '%"+txt+"%' "
      if len(txt)>0:
	tipo=''
	if txt[0].isdigit():
	  tipo= "id="+txt
      col='`'
      col+='`,`'.join(self.head)
      col+='`'
      sql=str("SELECT "+col+" FROM familias where "+tipo+"  order by `nombre`; ")
      self.matriz=self.parent.tabular(self.twResulta,sql,self.head)

class BuscadorD(buscador):
    def __init__(self,parent,texto='',campos=['Id','Nombre'],multi=False):
	buscador.__init__(self,parent,texto,campos,multi)
	self.cbDep.setVisible(False)
	self.cbFam.setVisible(False)
	self.lblDep.setVisible(False)
	self.lblFam.setVisible(False)
	self.titulo.setText("Buscador de Departamentos")
	self.lblInfo.setText("Escriba el nombre o el ID")
	
    def iniciarCombos(self):
	pass

    def filtrarFamilias(self):
      pass
    
    def buscar(self):
      txt=str(self.leFiltro.text())
      tipo=" nombre like '%"+txt+"%' "
      if len(txt)>0:
	tipo=''
	if (txt[0].isdigit()==False):
	  tipo=" nombre like '%"+txt+"%' "
	else:
	  tipo= "id="+txt
      col='`'
      col+='`,`'.join(self.head)
      col+='`'
      sql=str("SELECT "+col+" FROM departamentos where "+tipo+"  order by `nombre`; ")
      self.matriz=self.parent.tabular(self.twResulta,sql,self.head)
