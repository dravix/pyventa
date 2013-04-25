# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import Qt,SIGNAL,QModelIndex,QDate
from PyQt4.QtGui import QMessageBox, QIcon, QDialog,QMenu
from ui.ui_editor_oferta import Ui_Editor
from ui.dlg_buscador import buscador, BuscadorF,BuscadorD
from ui.ui_calculo_precio import Ui_Calculo
from lib.modelos.qmodelotablasql import QModeloTablaSql

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
	    self.ui.cursor.execute("""SELECT departamento from familias where id=%s""",producto['Familia'])
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
	editor=editorOfertas(self.ui)
	if editor.exec_()>0:
	  print " Promocion agregada "
	  self.listar()
	  #self.ui.iniciarCombos()
	  
    def eliminar(self,index=None):
	if index==None:
	  index=self.ui.tvOfertas.selectedIndexes()[1]
	if isinstance(index,QModelIndex):
	  key=str(index.sibling(index.row(),0).data().toString())
	  msgBox=QMessageBox(QMessageBox.Question,"Eliminar promocion","Confirma eliminar la promocion %s?"%key,QMessageBox.Yes|QMessageBox.No,self.ui, Qt.WindowStaysOnTopHint)
	  ret=msgBox.exec_()
	  if ret==QMessageBox.Yes:
	    self.ui.cursor.execute("""DELETE FROM ofertas where promocion=%s""",key)
	    self.ui.cursor.execute("delete from promociones where id="+str(key))
	    self.listar()

    def editar(self,index=None):
	if index==None:
	  index=self.ui.tvOfertas.selectedIndexes()[1]
	if isinstance(index,QModelIndex):
	  key=str(index.sibling(index.row(),0).data().toString())
	  editor=editorOfertas(self.ui,key)
	  if editor.exec_()>0:
	    self.listar()


    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.ui.tvOfertas.mapToGlobal(point) )	
         
    def checkPromos(self,prod):
	  head=['id','nombre', 'descuento','Precio Pub.','Precio c/Desc','inicio','fin','minimo','maximo']
	  sql="SELECT P.id,P.nombre, P.descuento,precio, precio-(P.descuento*precio*.1),P.inicio,P.fin,P.minimo, maximo FROM ofertas as O,promociones as P, productos WHERE ref=conjunto and tipo=0  and (conjunto=%s OR conjunto=%s OR conjunto=%s) AND O.promocion=P.id AND curdate() BETWEEN P.inicio AND P.fin"%(prod['Ref'],prod['Familia'],prod['Dep'])
	  self.ui.entabla(self.ui.tvOfertas,head,sql) 
	  
    def calcularPrecio(self):
	CP=CalculaPrecio(self.ui)
	CP.exec_()

	
class CalculaPrecio(QDialog, Ui_Calculo):
    def __init__(self,parent,ide=-1):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.parent=parent
		self.ide=ide
    		self.connect(self.dsbPrecioDesc, SIGNAL("editingFinished ()"), self.calcularDesc)
    		self.connect(self.dsbDescuento, SIGNAL("editingFinished ()"), self.calcularPrecio)
    		self.show()
    		#print self.isModal ()

    def iniciar(self):
      if ide>0:
	self.cursor.execute("""SELECT precio FROM productos where ref=%s """,self.ide)
	qry=self.cursor.fetchone()
	if qry!=None:
	  self.dsbPrecio.setValue(qry)
	  
    def calcularDesc(self):
      precio=self.dsbPrecio.value()
      if precio>0:
	pcd=self.dsbPrecioDesc.value()
	self.dsbDescuento.setValue((precio-pcd)*100/precio)
      
    def calcularPrecio(self):
      desc=self.dsbDescuento.value()      
      precio=self.dsbPrecio.value()
      self.dsbPrecioDesc.setValue(precio-(precio*desc*0.01))
      
	
	
class editorOfertas(QDialog, Ui_Editor):
    def __init__(self,parent,ide=-1):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.parent=parent
		self.ide=ide
		self.banderas={'edicion':False}
		self.matriz={'productos':[],'familias':[],'departamentos':[]}
		self.lista=[]
		self.menuAdd = QMenu(self)
		#Menu contextual de tipos de impresion
		self.menuAdd.addAction("Productos",self.listarProds)
		self.menuAdd.addAction("Familias",self.listarFams)
		self.menuAdd.addAction("Departamentos",self.listarDeps)
		self.tbMas.setMenu(self.menuAdd)
		self.tbMas.setPopupMode(2)
		self.CP=CalculaPrecio(self)

		#self.connect(self.rbDepa, SIGNAL("clicked ()"), self.listarDeps)
		#self.connect(self.rbFam, SIGNAL("clicked ()"), self.listarFams)
		#self.connect(self.rbProd, SIGNAL("clicked ()"), self.listarProds)

		self.connect(self.tbPublicar, SIGNAL("clicked ( )"), self.terminar)
		self.connect(self.tbCerrar, SIGNAL("clicked ()"), self.close)
		self.connect(self.tbMenos, SIGNAL("clicked ()"), self.quitar)
		self.connect(self.tbCalcDes, SIGNAL("clicked ()"), self.calcularPrecio)
		self.connect(self.sbMinimo,SIGNAL("editingFinished ()"),self.checkMaximo)		
		self.connect(self.CP.dsbDescuento,SIGNAL("valueChanged ( double )"),lambda:self.dsDescuento.setValue(self.CP.dsbDescuento.value()))		
		
        	self.deInicio.setDate(QDate.currentDate())
        	self.deFin.setDate(QDate.currentDate())
        	self.promo={'nombre':'','descuento':'','inicio':'','fin':'','minimo':''}
        	self.iniciar()
        	
    def iniciar(self): #iniciar para edicion
      self.extraTool.addWidget(self.CP)  
      self.tools.setVisible(False)
      if self.ide!=-1:
	self.curser.execute("""SELECT * FROM promociones where id=%s """,self.ide)
	row=self.curser.fetchone()
	if row!=None:
	  self.leNombre.setText(row['nombre'])
	  self.dsDescuento.setValue(row['descuento'])
	  self.sbMinimo.setValue(row['minimo'])
	  self.sbMaximo.setValue(row['maximo'])
	  self.deInicio.setDate(QDate().fromString(str(row['inicio']), "yyyy-MM-dd"))
	  self.deFin.setDate(QDate().fromString(str(row['fin']), "yyyy-MM-dd"))
	  self.cargarLista()
	 	    #print ofertas  
	    #self.parent.listaTabla(self.tabla,ofertas,head)
	    
    def cargarLista(self): #Carga la lista desde la base de datos 
      	  sql=" select conjunto,ELT(tipo+1 , (SELECT descripcion from productos where ref=conjunto), (SELECT nombre from familias where id=conjunto), (SELECT nombre from departamentos where id=conjunto)),ELT(tipo+1,'Producto','Familia','Departamento') ,tipo from ofertas where promocion=%s group by conjunto"%self.ide
	  self.cursor.execute(sql)
	  rows=self.cursor.fetchall()
	  if rows!=None:
	    self.lista=list(rows)
	    self.listar()
	    
    def terminar(self):
	self.promo['nombre']=str(self.leNombre.text())
	self.promo['descuento']=str(self.dsDescuento.value())
	self.promo['minimo']=str(self.sbMinimo.value())
	self.promo['maximo']=str(self.sbMaximo.value())
	self.promo['inicio']=str(self.deInicio.date().toString('yyyy-MM-dd'))
	self.promo['fin']=str(self.deFin.date().toString('yyyy-MM-dd'))	
	if self.ide==-1:#Si NO se esta editando una oferta
	  sql="INSERT INTO promociones values(NULL,'%s',%s,'%s','%s',%s,%s)"%(self.promo['nombre'],self.promo['descuento'],self.promo['inicio'],self.promo['fin'],self.promo['minimo'],self.promo['maximo'])
	  try:
	    self.cursor.execute(sql)
	  except:
	    print "No se pudo ingresar la promocion\n	>",sql
	    return
	  else:
	    self.cursor.execute('SELECT LAST_INSERT_ID()')
	    self.ide=self.cursor.fetchone()[0]

	else:# Se esta editando una oferta
	  print "Actualizando oferta."
	  #print "UPDATE promociones SET nombre='%s', descuento=%s,inicio='%s',fin='%s',minimo=%s, maximo=%s where id=%s"%(self.promo['nombre'],self.promo['descuento'],self.promo['inicio'],self.promo['fin'],self.promo['minimo'],self.promo['maximo'],self.ide)
	  try:
	    self.cursor.execute("UPDATE promociones SET nombre='%s', descuento=%s,inicio='%s',fin='%s',minimo=%s, maximo=%s where id=%s"%(self.promo['nombre'],self.promo['descuento'],self.promo['inicio'],self.promo['fin'],self.promo['minimo'],self.promo['maximo'],self.ide))
	  except:
	    print "No se pudo actualizar la promocion"
	    return
	for item in self.lista:
	    try:
	      self.cursor.execute(""" INSERT INTO ofertas VALUES(%s,%s,%s)""",(self.ide,item[0],item[3]))
	    except:
		pass
		#print "Registro duplicado -Ignorado-"
	#lista=self.parent.copy(self.matriz['productos'])
	#lista.extend(self.matriz['familias'])
	#lista.extend(self.matriz['departamentos'])

	      
	self.done(1)
	
    def listar(self):
      #tmp=self.parent.copy(self.matriz['productos'])
      #tmp.extend(self.matriz['familias'])
      #tmp.extend(self.matriz['departamentos'])
      head=['Id','Nombre','Conjunto','Tipo']
      self.parent.listaTabla(self.tabla,head,self.lista)
      self.tabla.resizeColumnsToContents()
      

    def listarDeps(self):
	#if val:
	  head=['Id','Nombre']
	  dlg=BuscadorD(self.parent,'',head,True)
	  if dlg.exec_()>0:
	    departamentos=dlg.seleccionados
	    for i in departamentos:
	      i.append('DEPARTAMENTO')
	      i.append('2')
	    self.lista.extend(departamentos)
	    self.listar()
	    #self.parent.entablar(self.tabla,dlg.seleccionados,head)
	    #self.tabla.selectAll ()

    def listarFams(self):
	#if val:
	  head=['Id','Nombre']
	  dlg=BuscadorF(self.parent,'',head,True)
	  if dlg.exec_()>0:
	    familias=dlg.seleccionados
	    for i in familias:
	      i.append('FAMILIA')
	      i.append('1')
	    self.lista.extend(familias)
	    self.listar()
	    
	    #self.parent.entablar(self.tabla,dlg.seleccionados,head)
	    #self.tabla.selectAll ()
    
    def listarProds(self):
	  head=['Ref','descripcion']
	  dlg=buscador(self.parent,'',head,True)
	  if dlg.exec_()>0:
	    #print dlg.productos
	    productos=dlg.seleccionados
	    for i in productos:
	      i.append('PRODUCTO')	    
	      i.append('0')
	    self.lista.extend(productos)
	    self.listar()
	    #self.parent.entablar(self.tabla,dlg.seleccionados,head)
	    #self.tabla.selectAll ()
	    
    def setProductos(self,li):
      for i in li:
	i.append('PRODUCTO')	    
	i.append('0')
      self.lista.extend(li)
      self.listar()
	
    def quitar(self):
      sel=self.tabla.selectedIndexes()
      if len(sel)>0:
	if self.ide==-1:
	    del(self.lista[sel[0].row()])
	    self.listar()
	else:
	  try:
	    item=self.lista[sel[0].row()]
	    sql="DELETE FROM ofertas WHERE promocion=%s and conjunto=%s and tipo =%s"%(self.ide,item[0],item[3])
	    print sql
	    self.cursor.execute(sql)
	    self.cargarLista()
	  except:
	    print "No se elimino el conjunto"
	
    def checkMaximo(self):
      maxx=float(self.sbMaximo.value())
      if maxx<float(self.sbMinimo.value()):
	self.sbMaximo.setValue(self.sbMinimo.value())
	
    def calcularPrecio(self):
      self.tools.setVisible(True)
