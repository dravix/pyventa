# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import Qt,SIGNAL,QModelIndex,QDate
from PyQt4.QtGui import QMessageBox, QIcon, QDialog,QMenu
from ui.dlg_buscador import buscador, BuscadorF,BuscadorD
from lib.modelos.qmodelotablasql import QModeloTablaSql
from lib.dialogos.editor_ofertas import EditorOferta
from lib.dialogos.calcula_descuentos import CalculaDescuentos
class Oferta:
    def __init__(self,parent):
	self.ui=parent
	self.index=7
	self.ui.tvOfertas.setContextMenuPolicy(Qt.CustomContextMenu)
	self.modelo=QModeloTablaSql(parent.cursor,parent)
	self.ui.tvOfertas.setModel(self.modelo)
        self.ui.connect(self.ui.tOfertas, SIGNAL("clicked()"), self.ver)		
	self.ui.connect(self.ui.tboHome, SIGNAL("clicked()"), self.ver)
	self.ui.connect(self.ui.tbOfertas, SIGNAL("clicked()"), self.ver)
	self.ui.connect(self.ui.verOfertas, SIGNAL("triggered()"), self.ver)
	self.ui.productos.popMenu.addAction(self.ui.verOfertas)
	#self.ui.tbrProductos.addAction(self.ui.verOfertas)
	action=self.ui.menuHerramientas.addAction("Calcular precios")
	self.ui.connect(action, SIGNAL("triggered()"), self.calcularPrecio)
	self.ui.connect(self.ui.leOFIltro, SIGNAL("returnPressed()"), lambda:self.listar(str(self.ui.leOFIltro.text())))
	self.ui.connect(self.ui.tboAgregar, SIGNAL("clicked()"), self.agregar)
	self.ui.connect(self.ui.pboBuscar, SIGNAL("clicked()"), self.buscarProd)
	self.ui.connect(self.ui.tvOfertas,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
	#self.ui.connect(self.ui.deInicio, SIGNAL("dateChanged ( const QDate)"), self.listar)
	self.ui.connect(self.ui.deFecha, SIGNAL("dateChanged ( const QDate)"), self.listar)
	self.ui.connect(self.ui.tvOfertas,SIGNAL('activated(const QModelIndex&)'),self.editar)
	self.ui.deFecha.setDate(QDate.currentDate())
	self.iniciarActions()

    def iniciar(self):
	#self.ui.ocultarTools()
	#self.ui.tbrProductos.show()
	self.ui.lboProducto.setText("")
	self.listar()
	
	
    def ver(self):
      	self.ui.stack.setCurrentIndex(self.index)

      
    def iniciarActions(self):
	self.popMenu = QMenu(self.ui)
	#action=self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/plus_16.png"),"Nuevo impuesto")
	#self.ui.connect(action, SIGNAL("triggered()"), self.agregar)
	#self.ui.menuImpuestos.addAction(action)

	action= self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/pencil.png"),"Editar")
	action.setIconVisibleInMenu(True)
	self.ui.connect(action, SIGNAL("triggered()"), self.editar)
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar")
	action.setIconVisibleInMenu(True)
	self.ui.connect(action, SIGNAL("triggered()"), self.eliminar)
	  
    def listar(self,nombre=''):
	if isinstance(nombre,QDate):
	  nombre=''
	fecha=str(self.ui.deFecha.date().toString('yyyy-MM-dd'))
	head=['Id','Nombre de la promocion', 'Descuento','Inicia','Caduca','U. Minimas','U. Maximas']
	if len(nombre)>0:
	  nombre=" and nombre like '%{0}%' ".format(nombre)
	sql="SELECT id,nombre, descuento,inicio,fin,minimo, maximo FROM promociones WHERE DATE('{0}') between inicio and fin {1}; ".format(fecha,nombre)
	self.modelo.query(sql,head)
	self.ui.tvOfertas.resizeColumnsToContents()
	#self.modelo=self.ui.entabla(self.ui.tvOfertas,head,sql,self.modelo) 
	
    def buscarProd(self):
	dlg=buscador(self.ui,'',['Ref','Descripcion','Familia'])
	if dlg.exec_()>0:
	  producto=dlg.producto
	  #print producto
	  self.ui.lboProducto.setText("Ofertas de "+producto['Descripcion'])
	  try:
	    self.ui.cursor.execute("""SELECT departamento from familias where id=%s"""%producto['Familia'])
	  except:
	    print "Hay un problema en la base de datos los campos del producto %s estan incompletos o corruptos."%producto['Ref']
	  else:
	    row=self.ui.cursor.fetchone()
	    if row!=None:
	      producto['Dep']=row[0]
	      self.checkPromos(producto)
	    else:
	      print "El producto %s no tiene una referencia hacia un departamento, verfique su familia."%producto['Ref']
	      
    def agregar(self):
	self.iniciar()
	editor=EditorOferta(self.ui)
	if editor.exec_()>0:
	  print " Promocion agregada "
	  self.listar()
	  #self.ui.iniciarCombos()
	  
    #def showEditor(self):
      
      
    def eliminar(self,index=None):
	if index==None:
	  index=self.ui.tvOfertas.selectedIndexes()[1]
	if isinstance(index,QModelIndex):
	  key=str(index.sibling(index.row(),0).data().toString())
	  msgBox=QMessageBox(QMessageBox.Question,"Eliminar promocion","Confirma eliminar la promocion %s?"%key,QMessageBox.Yes|QMessageBox.No,self.ui, Qt.WindowStaysOnTopHint)
	  ret=msgBox.exec_()
	  if ret==QMessageBox.Yes:
	    self.ui.cursor.execute("""DELETE FROM ofertas where promocion=%s"""%key)
	    self.ui.cursor.execute("delete from promociones where id="+str(key))
	    self.listar()

    def editar(self,index=None):
	if index==None:
	  index=self.ui.tvOfertas.selectedIndexes()[1]
	if isinstance(index,QModelIndex):
	  key=str(index.sibling(index.row(),0).data().toString())
	  editor=EditorOferta(self.ui,key)
	  if editor.exec_()>0:
	    self.listar()


    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.ui.tvOfertas.mapToGlobal(point) )	
         
    def checkPromos(self,prod):
	  head=['id','nombre', 'descuento','Precio Pub.','Precio c/Desc','inicio','fin','minimo','maximo']
	  sql="SELECT P.id,P.nombre, P.descuento,precio, precio-(P.descuento*precio*.1),P.inicio,P.fin,P.minimo, maximo FROM ofertas as O,promociones as P, productos WHERE ref=conjunto and tipo=0  and (conjunto=%s OR conjunto=%s OR conjunto=%s) AND O.promocion=P.id AND date(current_timestamp) BETWEEN P.inicio AND P.fin"%(prod['Ref'],prod['Familia'],prod['Dep'])
	  self.ui.entabla(self.ui.tvOfertas,head,sql) 
	  
    def calcularPrecio(self):
	CP=CalculaDescuentos(self.ui)
	CP.exec_()

	

      
	
	
