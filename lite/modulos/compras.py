# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb as my
import lib.libutil
from lib.selector import Selector
import sqlite3
class Compras:
    def __init__(self,parent):
		self.ui=parent
		self.curser=parent.curser
		self.cursor=parent.cursor
		self.ui.tvCompras.setContextMenuPolicy(Qt.CustomContextMenu)
		self.ui.twNCompra.setContextMenuPolicy(Qt.CustomContextMenu)
		self.index=6
        	self.ui.connect(self.ui.tCompras, SIGNAL("clicked()"), self.ver)		
        	self.ui.connect(self.ui.tbCompras, SIGNAL("clicked()"), self.ver)	
        	self.ui.connect(self.ui.tbcEditor, SIGNAL("clicked()"), lambda:self.ui.stkCompras.setCurrentIndex(1))	
        	self.ui.connect(self.ui.tbcoLimpiar, SIGNAL("clicked()"), self.limpiar)		
        	self.ui.connect(self.ui.verCompras, SIGNAL("triggered()"), self.ver)		
        	#self.ui.connect(self.ui.tNCompras, SIGNAL("clicked()"), self.agregar)		
        	#self.ui.connect(self.ui.tbcoNuevo, SIGNAL("clicked()"), self.agregar)
        	self.ui.connect(self.ui.pbncAgregar, SIGNAL("clicked()"), self.ingresarProducto)
        	self.ui.connect(self.ui.tbcoGuardar, SIGNAL("clicked()"), self.guardarCompra)
		self.ui.connect(self.ui.tvCompras,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
		self.ui.connect(self.ui.twNCompra,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocmNC)
		self.ui.connect(self.ui.tvCompras,SIGNAL('activated(const QModelIndex&)'),self.editar)
		self.ui.connect(self.ui.tbncCalimporte, SIGNAL("clicked ()"), self.calculoImporte)
		self.ui.connect(self.ui.tbncCalunidad, SIGNAL("clicked ()"), self.calculoUnitario)
		self.ui.connect(self.ui.lencCodigo, SIGNAL("returnPressed ()"), self.desplegar)
		#self.ui.connect(self.ui.lencCant, SIGNAL("returnPressed ()"), self.ingresarProducto)
		#self.ui.connect(self.ui.twOrdenCompra,SIGNAL("itemActivated ( QTableWidgetItem* )"),self.pedirProducto)
		#self.ui.connect(self.ui.twOrdenCompra,SIGNAL("itemChanged( QTableWidgetItem* )"),self.desplegarProducto)
		self.ui.connect(self.ui.decfecha, SIGNAL("dateChanged ( const QDate)"), self.listar)
		self.ui.connect(self.ui.decHasta, SIGNAL("dateChanged ( const QDate)"), self.listar)
	      
		#self.ui.toolCompras.addAction(self.ui.ordenarCompra)
		#self.ui.toolCompras.addAction(self.ui.verCompras)
		self.nuevaCompra=[]
		self.modelo=None
		self.nuevoModelo=None
		self.header=['ref','descripcion','costo','cantidad','importe']
		self.iniciarActions()
		self.flag={'edicion':None}
		self.ui.decfecha.setDate(QDate.currentDate())
		self.ui.decHasta.setDate(QDate.currentDate())
		self.ui.cbcProveedor.setModel(self.ui.proveedores.modelo)
		self.ui.cbcProveedor.setModelColumn(1)
		self.ui.lbcoComprador.setText(str(self.ui.usuario['nombre']))
		self.iniciar()




    def iniciar(self):
   
	self.ui.stkCompras.setCurrentIndex(0)
	#self.ui.toolCompras.show()
	self.listar()
    
    def ver(self):
      	self.ui.stack.setCurrentIndex(self.index)
      	self.ui.stkCompras.setCurrentIndex(0)
      
    def iniciarActions(self):
	self.popMenu = QMenu(self.ui)
	action=self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/plus_16.png"),"Nueva compra",self.agregar)
	action.setIconVisibleInMenu(True)

	action= self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/pencil_16.png"),"Editar ",self.editar)
	action.setIconVisibleInMenu(True)
	#self.ui.connect(action, SIGNAL("triggered()"), lambda: self.editar(self.ui.twUnidades.currentRow(),self.ui.twUnidades.currentColumn()))
	#self.ui.menuCompras.addAction(action)
	#self.ui.toolCompras.addAction(action)

	action=self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/delete_16.png"),"Eliminar")
	self.ui.connect(action, SIGNAL("triggered()"), self.eliminar)
	
	self.popMenuNC = QMenu(self.ui)
	action=self.popMenuNC.addAction(QIcon("/usr/share/pyventa/images/16/delete_16.png"),"Quitar")
	self.ui.connect(action, SIGNAL("triggered()"), self.eliminarElemento)
	#action.setShortcut("F3")
	
	#action.setShortcutContext(0)
    def limpiar(self):
	#self.ui.twNCompra.clear()
	#self.ui.twNCompra.setColumnCount(0)
	self.nuevaCompra=[]
	self.ui.lencCodigo.setFocus()
	self.flag['edicion']=None
	
    def listar(self):
	sql=str("SELECT compras.id,fecha,c.nombre, u.nombre,total FROM compras,clientes as c, usuarios as u where date(fecha)  between '%s' and '%s' and c.id=proveedor and id_usuario=comprador order by fecha ; "%(self.ui.decfecha.date().toString('yyyy-MM-dd'),self.ui.decHasta.date().toString('yyyy-MM-dd')))
	head=('Id','Fecha','Proveedor','Comprador', 'Total')
	self.modelo=self.ui.entabla(self.ui.tvCompras,head,sql,self.modelo)    
	self.ui.tvCompras.resizeColumnsToContents() 
	#self.datar() 

    #def datar(self):
      	#sql=str("SELECT ZEROsum(total) as totales, count(compras.id) as num FROM compras where date(fecha)  between '%s' and '%s'  order by fecha ; "%(self.ui.decfecha.date().toString('yyyy-MM-dd'),self.ui.decHasta.date().toString('yyyy-MM-dd')))
	#self.cursor.execute(sql)
	#datos=self.cursor.fetchone()
	#if datos!=None:
	  #print datos
	  ##self.ui.dsbNum.setValue(float(datos[1]))
	  ##self.ui.dsbEfectivo.setValue(float(datos[0]))
      
    def agregar(self):
	#Prepara todo para que se cree una nueva compra
	self.ui.stack.setCurrentIndex(self.index)
	self.ui.stkCompras.setCurrentIndex(1)
	self.ui.lencCodigo.setFocus()
	if self.flag['edicion']!=None:
	  self.limpiar()


    def eliminar(self):
	keys=libutil.seleccionar(self.ui.tvCompras,self.modelo)
	msgBox=QMessageBox(QMessageBox.Question,"Confirmacion","Esta a punto de eliminar una compra, esto quitara del inventario los articulos que esten registrados en esta compra.<br><b>Desea continuar con la eliminacion?</b>",QMessageBox.Yes|QMessageBox.No,self.ui)
	ret=msgBox.exec_()
	if ret==QMessageBox.Yes:
	  for key in keys:
	    try:
	      self.ui.cursor.execute("UPDATE existencia as e, comprados as cc SET stock_logico=stock_logico-cantidad WHERE e.producto=cc.producto and compra=%s;"%key)	      
	      self.ui.cursor.execute("""DELETE FROM comprados where compra=%s """%key)
	      self.ui.cursor.execute("""DELETE FROM compras where id=%s """%key)
	    except my.Error, e:
	      print "Error al eliminar compra",e
	      msgBox=QMessageBox(QMessageBox.Information,"No se puede eliminar","No se puede eliminar este elemento, verifique el log.",QMessageBox.Ok,self.ui)
	      msgBox.exec_()
	    else:
	      self.ui.conexion.commit()
	      self.ui.lblStatus.setText("Eliminacion completa. La operacion termino correctamente.")
	      self.listar()
	


    def editar(self):
	key=libutil.seleccionar(self.ui.tvCompras,self.modelo)
	self.editarCompra(key)
    
    
    def calculoUnitario(self):
	im=self.ui.lencImporte.value()
	co=self.ui.lencCosto.value()
	ca=self.ui.lencCant.value()
	if im>0  and ca>0:
	    self.ui.lencCosto.setValue(float(im)/float(ca))
	#if co>0  and ca>0:
	    #self.ui.lencImporte.setValue( float(co)*float(ca))

    def calculoImporte(self):
	im=self.ui.lencImporte.value()
	co=self.ui.lencCosto.value()
	ca=self.ui.lencCant.value()
	self.ui.lencImporte.setValue(float(co)*float(ca))      

    def desplegar(self):
	cb=str(self.ui.lencCodigo.text())
	if len(cb)>0:
	  if cb[0].isdigit():
	    print "Buscando codigo",cb
	    self.adomatic(cb)
	  elif cb[0]!='@':
	      print "Buscando descripcion",cb
	      self.buscar(cb,self.ui.lencCodigo)
	      self.desplegar()

    def adomatic(self,ide):
	if len(ide)>7:
	  codicion="codigo="+str(ide)
	else:
	  codicion="ref="+str(ide)
	#try:
	  sql="select `ref`, `descripcion`, `costo`,`ganancia`, precio from productos where "+codicion+" limit 1"
	  #print sql
	  self.ui.cursor.execute(sql)
	  qry=self.ui.cursor.fetchone()
	  if qry!=None:
	    self.tmp={'ref':str(qry[0]),'descripcion':str(qry[1]),'costo':float(qry[2]),'cantidad':0, 'margen':float(qry[3]),'importe':0}
	    self.ui.lencCodigo.setText(self.tmp['descripcion'])
	    self.ui.dsbcCosto.setValue(float(qry[2]))
	    self.ui.dsbcPrecio.setValue(float(qry[4]))
	    self.ui.dsbcCant.setFocus()
	    self.ui.dsbcCant.selectAll()
	  else:
	    self.ui.lencCodigo.setText("@ Producto no encontrado!")
	    self.ui.lencCodigo.selectAll()
	    self.tmp=None
	#except sqlite3.Error,e:
	    #self.ui.lencCodigo.setText("@ Producto no encontrado!")
	    #self.ui.lencCodigo.selectAll()
	    #self.tmp=None
	    #raise(e)
	#except:
	    #self.ui.lencCodigo.setText("@ Producto no encontrado!")
	    #self.ui.lencCodigo.selectAll()
	    #self.tmp=None
	#else:
	    #self.ui.lencCant.setFocus()
	    #self.ui.lencCant.selectAll ()

    def ingresarProducto(self):
	self.calculoUnitario()
	self.tmp['importe']=float(self.ui.lencCant.value())*float(self.ui.lencCosto.value())
	co=self.ui.lencCosto.value()
	self.tmp['cantidad']=float(self.ui.lencCant.value())
	if self.tmp!=None:
	  #print self.tmp['costo'],float(co)
	  if self.tmp['costo']!=float(co):
		np=float(co)+(self.tmp['margen']*float(co))
	     	msgBox=QMessageBox(QMessageBox.Question,"Cambio de costo?","El costo por unidad de este producto, en esta compra es diferente al que se tiene almacenado. Desea editar el producto con el precio nuevo precio antes de continuar?",
		QMessageBox.Yes|QMessageBox.No,self.ui)
		ret=msgBox.exec_()
		if ret==QMessageBox.Yes:
		    #self.ui.cursor.execute("UPDATE productos set `costo`="+str(co)+", `precio`="+str(np)+" where `ref`="+self.tmp['ref'])
		    self.ui.banderas['retorno']=self.ui.stack.currentIndex()
		    self.ui.banderas['editor']='e'
		    self.ui.siguiente=[]
		    self.ui.anterior=[]
		    self.ui.editarProducto(self.tmp['ref'])
		    self.ui.tpcosto.setValue(float(co))
	  self.tmp['costo']=float(co)
	  tupla=[self.tmp['ref'],self.tmp['descripcion'],float(self.tmp['costo']),float(self.tmp['cantidad']),
	  float(self.tmp['importe'])]
	  if self.buscar_elemento(tupla,self.nuevaCompra)!=True:
	    self.nuevaCompra.append(tupla)
	    #print self.nuevaCompra
	  self.enlistar()
	  self.ui.lencImporte.setValue(0)
	  self.ui.lencCosto.setValue(0)
	  self.ui.lencCant.setValue(0)
	  self.ui.lencCodigo.clear()
	  self.ui.lencCodigo.setFocus()
	  self.tmp=None
	  

    def guardarCompra(self):
	
	if (self.flag['edicion']!=None):
	     try:
	      self.ui.cursor.execute( "UPDATE existencia as e, comprados as cc SET stock_logico=stock_logico-cantidad WHERE e.producto=cc.producto and compra=%s;"%self.flag['edicion'])
	      self.ui.cursor.execute("""DELETE FROM comprados where compra=%s """%self.flag['edicion'])
	      self.ui.cursor.execute("""DELETE FROM compras where id=%s """%self.flag['edicion'])
	     except:
		pass
	     else:
		self.ui.conexion.commit()
		self.flag['edicion']=None
		self.guardarCompra()
	else:
	    total=0.0
	    for item in self.nuevaCompra:
		total+=float(item[4])
	    try:
	      self.ui.cursor.execute("insert into compras values(NULL,NOW(),%s,%s,%s)"%( self.ui.cbProveedor.model().celda(self.ui.cbProveedor.currentIndex(),0),self.ui.usuario,total) )
	    except:
	      print "Problema para crear una compra en la base de datos"
	    else:
	      self.ui.conexion.commit()
	      sql=self.ui.conexion.lastId()
	      self.ui.cursor.execute(sql)
	      last=int(self.ui.cursor.fetchone()[0])
	      for item in self.nuevaCompra:
		  self.ui.cursor.execute("""insert into comprados values(%s,%s,%s,%s,%s)"""%(last,item[0],item[3],item[2],item[4]))
		  sql="UPDATE existencia SET stock_logico=stock_logico+%s where producto=%s"%(item[3],item[0])
		  self.ui.cursor.execute(sql)
		  self.ui.cursor.execute("DELETE FROM faltantes WHERE producto=%s "%item[0])
	      self.ui.conexion.commit()  
	self.limpiar()
	self.iniciar()

    def editarCompra(self,ide):
	try:
	  sql="SELECT proveedor,nombre from compras,usuarios where compras.id=%s and id_usuario=comprador limit 1"%ide[0]
	  self.cursor.execute(sql)
	  compra=self.cursor.fetchone()
	except:
	  print "Error al localizar al proveedor o al usuario."
	else:
	  if compra!=None:
	    self.ui.cbProveedor.setCurrentIndex( self.ui.cbProveedor.model().buscarKey(compra[0],0) )
	    self.ui.lbcoComprador.setText(compra[1])
	self.curser.execute("""SELECT C.*,P.`descripcion` FROM productos as P,  comprados as C WHERE P.ref=C.producto AND  C.compra=%s"""%ide[0])

	prods=self.curser.fetchall()
	if prods!=None:
	  prods=dicursor(self.curser,prods)
	self.nuevaCompra=[]
	for item in prods:
	  self.nuevaCompra.append([item['producto'],item['descripcion'],float(item['costo']),float(item['cantidad']),float(item['total'])])
	self.enlistar()
	self.agregar()
	self.flag['edicion']=str(ide[0])
    	
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.ui.tvCompras.mapToGlobal(point) )
    
    def ocmNC(self, point):
         self.popMenuNC.exec_(self.ui.twNCompra.mapToGlobal(point) )
         	

    def nuevaOrden(self):

	self.ui.stack.setCurrentIndex(11)

    def buscar(self,texto,item):
      	app=Selector(self,"Productos",'productos','ref,descripcion,precio','Ref,Descripcion, Precio publico',filtros=" descripcion like '%{0}%' order by descripcion ",inicial=str(texto))
	done=app.exec_()
	if done==1:
	  item.setText(str(app.retorno[0][0]))
	#dlg=buscador(self.ui,str(texto))
	#item.setText(str(dlg.exec_()))

    def pedirProducto(self,item):
	col=self.ui.twOrdenCompra.column(item)
	row=self.ui.twOrdenCompra.row(item)
	if (col==0):
	  self.buscar('',item)
	elif col==3:
	    cantidad=str(self.ui.twOrdenCompra.item(row,3).text())
	    costo=str(self.ui.twOrdenCompra.item(row,2).text())
	    self.ui.twOrdenCompra.setItem(row,4,QTableWidgetItem(str(float(cantidad)*float(costo)),1))
	    
	elif col==4:
	    self.ui.twOrdenCompra.insertRow(self.ui.twOrdenCompra.rowCount())
	else:
	  print self.ui.twOrdenCompra.column(item)

    def desplegarProducto(self,item):
	row=self.ui.twOrdenCompra.row(item)
	col=self.ui.twOrdenCompra.column(item)
	if col<1:
	  ref=self.ui.twOrdenCompra.item(row,0).text()
	  self.ui.cursor.execute("select `descripcion`, costo from productos where ref="+str(ref))
	  prod=self.ui.cursor.fetchone()
	#print prod[0]
	#.setText(str(prod[0]))
	  self.ui.twOrdenCompra.setItem(row,2,QTableWidgetItem(str(prod[1]),1))
	  self.ui.twOrdenCompra.setItem(row,1,QTableWidgetItem(str(prod[0]),1))
	  self.ui.twOrdenCompra.resizeColumnsToContents()
	elif col<2:
	    #self.buscar(self.ui.twOrdenCompra.item(row,1).text(),self.ui.twOrdenCompra.item(0,row))
	    pass
    #def insertar(self,tupla):
      #self.buscarKey(tupla[0])
      
    def enlistar(self):
	self.nuevoModelo=self.ui.listaTabla(self.ui.twNCompra,self.header,self.nuevaCompra, self.nuevoModelo)
	self.ui.twNCompra.resizeColumnsToContents()  
      
    def buscar_elemento(self,tupla,lista):
#Busca un elemento dentro de una tabla de compra y regresa verdadero si existe y falso en caso contrario
	ret=False
	if (len(lista)>0):
	  for i,prod in enumerate(lista):
	    if (prod[0]==tupla[0]):
		prod[3]+=float(tupla[3])
		prod[4]=float(prod[2])*float(prod[3])
		#for j,data in enumerate(prod):
		  #tabla.item(i,j).setText(str(data))
		#
		ret=True
	return ret
	
    def eliminarElemento(self):
#Elimina el elemento seleccionado de la tabla
	refs=libutil.seleccionar(self.ui.twNCompra,self.nuevoModelo)
	for ref in refs:	  
	  for prod in self.nuevaCompra:
	      if (int(prod[0])==int(ref)):
		  self.nuevaCompra.remove(prod)
		  self.enlistar()
		  break
	
