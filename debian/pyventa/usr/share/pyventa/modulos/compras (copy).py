# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.dlg_buscador import buscador

class Compras:
    def __init__(self,parent):
		self.ui=parent
		self.curser=parent.curser
		self.ui.twCompras.setContextMenuPolicy(Qt.CustomContextMenu)
		self.ui.twNCompra.setContextMenuPolicy(Qt.CustomContextMenu)
        	self.ui.connect(self.ui.tCompras, SIGNAL("clicked()"), self.iniciar)		
        	self.ui.connect(self.ui.verCompras, SIGNAL("triggered()"), self.iniciar)		
        	#self.ui.connect(self.ui.tNCompras, SIGNAL("clicked()"), self.agregar)		
        	self.ui.connect(self.ui.ordenarCompra, SIGNAL("triggered()"), self.nuevaOrden)		
        	self.ui.connect(self.ui.pbAddCom, SIGNAL("clicked()"), self.agregar)
        	self.ui.connect(self.ui.pbncAgregar, SIGNAL("clicked()"), self.ingresarProducto)
        	self.ui.connect(self.ui.pbncCerrar, SIGNAL("clicked()"), self.guardarCompra)
        	self.ui.connect(self.ui.tbncLimpiar, SIGNAL("clicked()"), self.limpiar)
		self.ui.connect(self.ui.twCompras,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
		self.ui.connect(self.ui.twNCompra,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocmNC)
		self.ui.connect(self.ui.twCompras,SIGNAL('cellDoubleClicked (int, int)'),self.editar)
		self.ui.connect(self.ui.tbncCalimporte, SIGNAL("clicked ()"), self.calculoImporte)
		self.ui.connect(self.ui.tbncCalunidad, SIGNAL("clicked ()"), self.calculoUnitario)
		self.ui.connect(self.ui.lencCodigo, SIGNAL("editingFinished ()"), self.desplegar)
		self.ui.connect(self.ui.twOrdenCompra,SIGNAL("itemActivated ( QTableWidgetItem* )"),self.pedirProducto)
		self.ui.connect(self.ui.twOrdenCompra,SIGNAL("itemChanged( QTableWidgetItem* )"),self.desplegarProducto)
		self.ui.toolCompras.addAction(self.ui.ordenarCompra)
		self.ui.toolCompras.addAction(self.ui.verCompras)
		self.nuevaCompra=[]
		self.header=['ref','descripcion','costo','cantidad','importe']
		self.iniciarActions()
		self.flag={'edicion':None}


    def iniciar(self):
	self.ui.stack.setCurrentIndex(9)
	self.ui.ocultarTools()
	self.ui.toolCompras.show()
	self.listar()

    def iniciarActions(self):
	self.popMenu = QMenu(self.ui)
	action=self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/plus_16.png"),"Registrar compra")
	action.setIconVisibleInMenu(True)
	self.ui.connect(action, SIGNAL("triggered()"), self.agregar)
	self.ui.menuCompras.addAction(action)
	self.ui.toolCompras.addAction(action)

	#action= self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/pencil_16.png"),"Editar ")
	#self.ui.connect(action, SIGNAL("triggered()"), lambda: self.editar(self.ui.twUnidades.currentRow(),self.ui.twUnidades.currentColumn()))
	#self.ui.menuCompras.addAction(action)
	#self.ui.toolCompras.addAction(action)

	#action=self.popMenu.addAction(QIcon("/usr/share/pyventa/images/16/delete_16.png"),"Eliminar")
	#self.ui.connect(action, SIGNAL("triggered()"), self.eliminar)
	#self.ui.menuCompras.addAction(action)
	#self.ui.toolCompras.addAction(action)
	
	self.popMenuNC = QMenu(self.ui)
	action=self.popMenuNC.addAction(QIcon("/usr/share/pyventa/images/16/delete_16.png"),"Quitar")
	self.ui.connect(action, SIGNAL("triggered()"), lambda:self.eliminarElemento(self.nuevaCompra,self.ui.twNCompra))
	#action.setShortcut("F3")
	
	#action.setShortcutContext(0)
    def limpiar(self):
	self.ui.twNCompra.clear()
	self.ui.twNCompra.setColumnCount(0)
	self.nuevaCompra=[]
	self.ui.lencCodigo.setFocus()
    def listar(self):
	sql=str("SELECT * FROM compras order by `id`; ")
	self.ui.tabular(self.ui.twCompras,sql,['Id','Fecha','Proveedor','Total'])

    def agregar(self):
	self.ui.stack.setCurrentIndex(10)
	self.limpiar()
	
	self.flag['edicion']=None


    def eliminar(self):
	self.iniciar()


    def editar(self,y,x):
	key=self.ui.twCompras.item(y,0).text()
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
	    if len(cb)>7:
	      codicion="codigo="+str(cb)
	    else:
	      codicion="ref="+str(cb)
	    try:
	      self.ui.cursor.execute("select `ref`, `descripcion`, `costo`,`ganancia` from productos where "+codicion+" limit 1")
	      qry=self.ui.cursor.fetchone()
	      self.tmp={'ref':str(qry[0]),'descripcion':str(qry[1]),'costo':float(qry[2]),'cantidad':0, 'margen':float(qry[3]),'importe':0}
	      self.ui.lbProducto.setText(self.tmp['descripcion'])
	    except:
		self.ui.lbProducto.setText("<b>Producto no encontrado!!</b>")
		self.tmp=None
	    else:
		self.ui.lencCant.setFocus()
		self.ui.lencCant.selectAll ()
	  else:
	      self.buscar(cb,self.ui.lencCodigo)
	      self.desplegar()



    def ingresarProducto(self):
	self.calculoUnitario()
	self.tmp['importe']=float(self.ui.lencImporte.value())
	co=self.ui.lencCosto.value()
	self.tmp['cantidad']=float(self.ui.lencCant.value())
	if self.tmp!=None:
	  if self.tmp['costo']!=float(co):
		np=float(co)+(self.tmp['margen']*float(co))
	     	msgBox=QMessageBox(QMessageBox.Question,"Cambio de costo?","El costo por unidad de este producto, en esta compra es diferente al que se tiene almacenado. Desea editar el producto con el precio nuevo precio antes de continuar?",
		QMessageBox.Yes|QMessageBox.No,self.ui)
		ret=msgBox.exec_()
		if ret==QMessageBox.Yes:
		    #self.ui.cursor.execute("UPDATE productos set `costo`="+str(co)+", `precio`="+str(np)+" where `ref`="+self.tmp['ref'])
		    self.ui.banderas['retorno']=self.ui.stack.currentIndex()
		    self.ui.siguiente=[]
		    self.ui.anterior=[]
		    self.ui.editarProducto(self.tmp['ref'])
		    self.ui.tpcosto.setValue(float(co))
	  self.tmp['costo']=float(co)
	  tupla=[self.tmp['ref'],self.tmp['descripcion'],float(self.tmp['costo']),float(self.tmp['cantidad']),
	  float(self.tmp['importe'])]
	  if self.buscar_elemento(tupla,self.nuevaCompra,self.ui.twNCompra)!=True:
	    self.nuevaCompra.append(tupla)
	  self.ui.entablar(self.ui.twNCompra,self.nuevaCompra, self.header)
	  self.ui.lencImporte.setValue(0)
	  self.ui.lencCosto.setValue(0)
	  self.ui.lencCant.setValue(0)
	  self.ui.lencCodigo.clear()
	  self.ui.lencCodigo.setFocus()
	  self.tmp=None
	  

    def guardarCompra(self):
	if (self.flag['edicion']!=None):
	     try:
	      self.ui.cursor.execute("""DELETE FROM comprados where compra=%s """,self.flag['edicion'])
	      self.ui.cursor.execute("""DELETE FROM compras where id=%s """,self.flag['edicion'])
	     except:
		pass
	     else:
		self.flag['edicion']=None
		self.guardarCompra()
	else:
	    total=0.0
	    for item in self.nuevaCompra:
		total+=float(item[4])
	    try:
	      self.ui.cursor.execute("insert into compras values(NULL,NOW(),"+str(self.ui.usuario)+","+str(total)+")")
	    except:
	      print "Problema para crear una compra en la base de datos"
	    else:
	      self.ui.cursor.execute("select LAST_INSERT_ID();")
	      last=int(self.ui.cursor.fetchone()[0])
	      for item in self.nuevaCompra:
		  self.ui.cursor.execute("""insert into comprados values(%s,%s,%s,%s,%s)""",(last,item[0],item[3],item[2],total))
		  self.ui.cursor.execute("""UPDATE productos SET stock=stock+%s where ref=%s""",(item[3],item[0]))
	self.limpiar()
	self.iniciar()

    def editarCompra(self,ide):
	self.curser.execute("""SELECT C.*,P.`descripcion` FROM productos as P,  comprados as C WHERE P.ref=C.producto AND  C.compra=%s""",ide)
	prods=self.curser.fetchall()
	self.nuevaCompra=[]
	for item in prods:
	  self.nuevaCompra.append([item['producto'],item['descripcion'],float(item['costo']),float(item['cantidad']),float(item['total'])])
	self.ui.entablar(self.ui.twNCompra,self.nuevaCompra, self.header)
	self.ui.stack.setCurrentIndex(10)
	self.flag['edicion']=str(ide)


	    	
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.ui.twCompras.mapToGlobal(point) )
    
    def ocmNC(self, point):
         self.popMenuNC.exec_(self.ui.twNCompra.mapToGlobal(point) )
         	
    def buscarProducto(self):
	dlg=buscador(self.ui,self.ui.lencCodigo.text())
	self.ui.lencCodigo.setText(str(dlg.exec_()))

    def nuevaOrden(self):
	self.ui.stack.setCurrentIndex(11)

    def buscar(self,texto,item):
	dlg=buscador(self.ui,str(texto))
	item.setText(str(dlg.exec_()))

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
	  
    def buscar_elemento(self,tupla,lista,tabla):
#Busca un elemento dentro de una tabla de compra y regresa verdadero si existe y falso en caso contrario
	ret=False
	if (len(lista)>0):
	  for i,prod in enumerate(lista):
	    if (prod[0]==tupla[0]):
		prod[3]+=float(tupla[3])
		prod[4]=float(prod[2])*float(prod[3])
		for j,data in enumerate(prod):
		  tabla.item(i,j).setText(str(data))
		ret=True
	return ret
	
    def eliminarElemento(self,lista,tabla):
#Elimina el elemento seleccionado de la tabla
	y=int(tabla.currentRow())
	ref=int(tabla.item(y,0).text())
	for prod in lista:
	    if (int(prod[0])==int(ref)):
		lista.remove(prod)
	tabla.removeRow(y)
