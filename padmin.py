#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, datetime, urllib2, tarfile, base64, sqlite3
from time import time
aqui=os.getcwd()
#aqui="/usr/share/pyventa/"

#sys.path.append(os.path.join("/usr/share/pyventa/admin"))
home=os.path.join(os.path.expanduser('~'),"pyventa")
if sys.platform == 'linux2':
    home=os.path.join(os.path.expanduser('~'),".pyventa")
    # Set process name.  Only works on Linux >= 2.1.57.
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, 'padmin\0')
    except:
        pass
else:
	sys.stdout = open(os.path.join(os.path.expanduser('~'),"pad_salida.log"),"w")
	sys.stderr = open(os.path.join(os.path.expanduser('~'),"pad_error.log"),"w")
	
#sys.path.append(os.path.join(aqui,'plugins'))
#sys.path.append(os.path.join(aqui,'import'))
#sys.path.append(os.path.join(aqui,"admin"))

import datetime, tempfile
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4.QtCore import *
from ui.ui_admin import Ui_admin
import MySQLdb, ConfigParser  
#from db_conf import configurador
from PyQt4.QtGui import QMessageBox, QDialog, QMainWindow, QInputDialog, QApplication,QTableWidgetItem
from PyQt4.QtCore import SIGNAL, Qt,QTimer, QLocale
from modulos.productos import Productos
from modulos.impuestos import Impuestos
from modulos.departamentos import Departamentos
from modulos.familias import Familias
from modulos.unidades import Unidades
from modulos.control1 import Admin1
from modulos.compras import Compras
from modulos.cajas import Cajas
from modulos.clientes import Clientes
from modulos.proveedores import Proveedores
from modulos.usuarios import Usuarios
from modulos.inventario import  Inventario
from modulos.faltantes import  Faltantes
from modulos.ofertas import Oferta
from modulos.conexiones import Conexiones
from ui.dlg_buscador import buscador
from lib.utileria import MyListModel, MyTableModel
from lib import libutil
from lib.librerias.configurador import Configurador
from lib.librerias.conexion import Conexion
from lib.librerias.seguridad import Seguridad
class Administrador(QMainWindow, Ui_admin):  
    def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.curser=None
		self.cursor=None
		self.home=home
		self.cfg=Configurador(self)
		if self.cfg.stat:
		  self.conexion=Conexion(self,self.cfg)
		  if self.conexion.stat:
		    self.cursor=self.conexion.cursor
		    self.curser=self.conexion.curser
		    self.conexion.db.text_factory = str
		    self.iniciarEstilo()
		    self.iniciarSesion()
		else:
		  print "Error al iniciar configuraciones"
		  sys.exit()
		#Inicio de funciones
		self.showMaximized()
		self.stack.setCurrentIndex(1)
		self.impuesto=Impuestos(self)
		self.departamento=Departamentos(self)
		self.familia=Familias(self)		
		self.unidad=Unidades(self)
		self.productos=Productos(self)
		self.clientes=Clientes(self,True)
		self.proveedores=Proveedores(self,True)
		self.usuarios=Usuarios(self)
		self.ofertas=Oferta(self)
		self.cajas=Cajas(self,True)
		self.inv=Inventario(self)
		self.faltantes=Faltantes(self)
		self.compras=Compras(self)
		try:
		  self.conexiones=Conexiones(self)
		except:
		  self.tConexiones.setVisible()
		#Inicio de combos
		self.iniciarCombos()
		#self.familias=self.familia.getLista()
		self.menuHerramientas.addAction("Recargar estilo",self.iniciarEstilo)
		self.iniciarEstilo()
    
    def conexion():
      self.conexion=Conexion(self,self.cfg)
      if self.conexion.stat:
	self.cursor=self.conexion.cursor
	self.curser=self.conexion.curser
	self.iniciarEstilo()
	self.iniciarSesion()

    def iniciarEstilo(self):
	 try:
	  kcss = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"perfil","estilos",self.cfg.get("pyventa","estilo")),"r")
	  estilo=kcss.read()
	  self.setStyleSheet(estilo)
	  kcss.close()	
	 except:
	    try:
		kcss = open(os.path.join(self.home,"estilos",self.cfg.get("pyventa","estilo")),"r")
		estilo=kcss.read()
		self.setStyleSheet(estilo)
		kcss.close()	
	    except:
		print "No se cargo el estilo "+self.cfg.get("pyventa","estilo")
    	
    def iniciarSesion(self):
	dlg=Seguridad(self,nivel=5,logo=":/actions/images/padmin.simple.logo.png", nombre="Administrador de Pyventa")
	acceso=dlg.exec_()
	if acceso>-1:
	  self.usuario=dlg.usuario
	  self.cursor=dlg.cursor
	  self.curser=dlg.curser
	else:
	  sys.exit()
	  
    def iniciarCombos(self):
	#self.cbpDepartamentos.clear()
	#self.cbpFamilias.clear()
	self.cbeFamilias.clear()
	self.cbeImpuestos.clear()
	self.cbeUnidades.clear()
	
	#combo=self.departamento.getModelo()
	#self.cbpDepartamentos.setModel(combo)
	#self.cbpDepartamentos.setModelColumn(1)
	
	#self.cbpFamilias.setModel(self.familia.getModelo())
	self.cbeFamilias.setModel(self.familia.getModelo())
	#self.cbpFamilias.setModelColumn(1)
	self.cbeFamilias.setModelColumn(1)
	
	self.cbeImpuestos.setModel(self.impuesto.getModelo())
	self.cbeImpuestos.setModelColumn(1)
	
	self.cbeUnidades.setModel(self.unidad.getModelo())
	self.cbeUnidades.setModelColumn(1)
	
    def goHome(self):
	self.stack.setCurrentIndex(0)
	#self.tbrProductos.hide()


	    
    def tabular(self,tabla,sql,head):
#Recibe una consulta de sql la ejecuta y tabula el resultado
	    lista=[]
	    try:
	      self.cursor.execute(sql)
	      result = self.cursor.fetchall()
	    except MySQLdb.Error, e:
	      print e
	    else:
	      tabla.setColumnCount(len(head))
	      tabla.setRowCount(len(result))
	      for i,data in enumerate(head):
		  item = QTableWidgetItem(1)
		  item.setText(str(data))
		  tabla.setHorizontalHeaderItem(i,item)
	      for i,elem in enumerate(result):
		  if len(elem)==len(head):	 
		    lista.append(list(elem))
		    for j,data in enumerate(elem):
		      item = QTableWidgetItem(1)
		      item.setText(str(data))
		      tabla.setItem(i,j,item)
	      result=None
	      tabla.resizeColumnsToContents()
	      return lista 
    def entablar(self,tabla,lista,head):
	    #Cumple la misma funcion que tabular, con la diferencia que esta recibe una lista de tuplas 
	      tabla.clear()
	      tabla.setColumnCount(len(head))
	      tabla.setRowCount(len(lista))	 	 
	      for i,data in enumerate(head):
		  item = QTableWidgetItem(1)
		  item.setText(str(data))
		  tabla.setHorizontalHeaderItem(i,item)
	      for i,elem in enumerate(lista):
		  for j,data in enumerate(elem):
		    item = QTableWidgetItem(1)
		    item.setText(str(data))
		    tabla.setItem(i,j,item)
	      tabla.resizeColumnsToContents()
	      
    def tablar(self,tabla,lista,head):
	    #Cumple la misma funcion que entablar, con la diferencia que esta recibe una lista de diccionarios 
	      tabla.clear()
	      tabla.setColumnCount(len(head))
	      tabla.setRowCount(len(lista))	 	 
	      for i,data in enumerate(head):
		  item = QTableWidgetItem(1)
		  item.setText(str(data))
		  tabla.setHorizontalHeaderItem(i,item)
	      for i,elem in enumerate(lista):
		  for j,data in enumerate(elem):
		    item = QTableWidgetItem(1)
		    item.setText(str(elem[data]))
		    tabla.setItem(i,j,item)
	      tabla.resizeColumnsToContents() 
	      
    def copy(self,a):
	b=[]
	for i,fila in enumerate(a):
	  tmp=[]
	  for j,col in enumerate(fila):
	    tmp.append(col)
	  b.append(tmp)
	return b
	  
    def setStatus(self,stat,msg='Estado de operaciones'):
      timer=QTimer()
      if stat==0: #Normal
	#self.pbStat.setStyleSheet("border:1.3px solid rgb(42, 129, 159); border-radius:12px; color:#fff;\nbackground-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 102, 128, 255), stop:0.563636 rgba(0, 34, 43, 255), stop:0.568182 rgba(0, 65, 82, 255), stop:1 rgba(0, 67, 85, 255));")
	self.pbStat.setText("Sin operaciones")
	self.lblStatus.setText(msg)
      elif stat==1:
	#self.pbStat.setStyleSheet("border:1.3px solid rgb(84, 126, 28);border-radius:12px; color:#fff;background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(111, 159, 42, 255), stop:0.495455 rgba(25, 114, 28, 255), stop:0.507692 rgba(87, 149, 42, 255), stop:1 rgba(110, 202, 58, 255));")
	self.pbStat.setText("Hecho")
	self.lblStatus.setText(msg)
	timer.start(3000)
	self.connect(timer, SIGNAL("timeout()"), lambda:self.setStatus(0))
      elif stat==2: #ERROR
	self.pbStat.setStyleSheet("border:1.3px solid #700;border-radius:12px; color:#fff;\nbackground-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.995, y2:0.011, stop:0 rgba(86, 19, 19, 255), stop:1 rgba(176, 50, 50, 255));")
	self.pbStat.setText("Error!")	
	self.lblStatus.setText(msg)
	timer.start(4000)
	self.connect(timer, SIGNAL("timeout()"), lambda:self.setStatus(0))
	
    #def listarInventario(self):
      #sql="SELECT * FROM "
      #self.entabla(self.tblInventario,)
      
    def entabla(self,tabla,header,query,modelo=None):
      #tabla, header, query, modelo
	sql=str(query)
	try:
	  self.cursor.execute(sql)
	  lista=self.cursor.fetchall()
	except sqlite3.Error, e:
	  print "Error al entablar"
	  raise(e)
	except:
	  print "Problema al ejecutar el query"
	else:
	  if lista!=None:
	    #print lista
	    if modelo==None:
	      modelo = MyTableModel(lista, header, self) 
	      tabla.setModel(modelo)
	    else:
	      modelo.setVector(lista) 
	return modelo
	
    def listaTabla(self,tabla,header,lista,modelo=None):
      #tabla, header, lista, modelo
	  if lista!=None:
	    #print lista
	    if modelo==None:
	      modelo = MyTableModel(lista, header, self) 
	      tabla.setModel(modelo)
	    else:
	      modelo.setVector(lista) 
	    return modelo	
	
    def enlista(self,lista,query,modelo=None):
      #lista, header, query, modelo
	sql=str(query)
	try:
	  self.cursor.execute(sql)
	  res=self.cursor.fetchall()
	except:
	  print "Problema al ejecutar el query"
	else:
	  if res!=None:
	    res=list(res[0][1])
	    print res
	    if modelo==None:
	      modelo = MyListModel(res, self) 
	      lista.setModel(modelo)
	    else:
	      modelo.setVector(res) 
	return modelo
	
    def aut(self,nivel):
    #recibe una clave (key) y un valor requerido (req) para ver si tiene el nivel necesario
      #if (self.stack.currentIndex()==modulo):
	Acceso =QInputDialog.getText(self, self.tr("Filtro de Acceso"),self.tr("Ingrese su clave de autorizacion."),QLineEdit.Password)                         
	key=str(Acceso[0])
	self.cursor.execute('select id_usuario,nivel from usuarios where clave=MD5(\''+key+'\');')
	val=self.cursor.fetchone()
	if val!=None:
	  if int(val[1])>=int(nivel):
	    return val[0]
	  else :
	    return False
  
    def setUsuario(self,usuario):
      self.usuario=usuario
   
    def notify(self,tipo,event,detail='',time=5):
	    dia=QMessageBox(self)
	    
	    timer=QTimer.singleShot(time*1000,dia.accept)
	    # dia=QtGui.QDialog(self)
	    dia.setText(event)
	    dia.setInformativeText(detail)
	    # dia.setDetailedText(detail)
	    dia.setWindowModality(0)
	    dia.setWindowOpacity(.8)
	    dia.setStandardButtons(QMessageBox.NoButton)
	    if tipo=='error':
		    dia.setStyleSheet(".QMessageBox{background:rgba(250,30,10,255);color:#fff}QLabel{background:transparent;color:#fff}")
		    dia.setIcon(QMessageBox.Critical)
	    elif tipo=='info':
		    dia.setStyleSheet(".QMessageBox{background:rgba(30,30,10,255);color:#fff}QLabel{background:transparent;color:#fff}")	
		    dia.setIcon(QMessageBox.Information)
	    elif tipo=='advertencia':
		    dia.setStyleSheet(".QMessageBox{background:rgba(255,200,0,255);color:#fff}QLabel{background:transparent;color:#fff}")	
		    dia.setIcon(QMessageBox.Warning)
	    elif tipo=='exito':	
		    dia.setStyleSheet(".QMessageBox{background:rgba(0,128,0,255);color:#fff}QLabel{background:transparent;color:#fff}")	
		    dia.setIcon(QMessageBox.Information)
		    
	    dia.move(self.width()-dia.width(),104)
	    # dia.addWidget(QLabel(event))
	    dia.setWindowFlags(dia.windowFlags()|Qt.FramelessWindowHint)
	    dia.show()
    
    def closeEvent(self, event): 
	self.conexion.commit()
	event.accept()
	print "Cerrando el administrador" 
	#self.destory()      
        
	      
from lib.dlg_ingreso import acceso
	
if __name__=="__main__":

    app = QApplication(sys.argv)
    app.processEvents()
    QLocale.setDefault(QLocale(111,139)) 
    #dlg=acceso()
    #key=-1
    #key=dlg.exec_()
    #if key>0:
    aw = Administrador()
    #aw.setUsuario()
    aw.show()
    app.exec_()
    
