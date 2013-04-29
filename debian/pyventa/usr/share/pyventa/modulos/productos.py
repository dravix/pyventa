from PyQt4.QtCore import Qt, SIGNAL 
from PyQt4.QtGui import QMenu, QMessageBox, QIcon
import MySQLdb
from lib.utileria import MyTableModel, Faltante, setComboModelKey
from lib.listacodigos import ListadorCodigos
from lib import libutil
class Productos:
    def __init__(self,parent):
	self.parent=parent
	self.cursor=parent.cursor
	self.curser=parent.curser
	self.setupSignals()
	self.setTools()
	self.siguiente=[]      
	self.anterior=[]      
	self.alternos=[]
	self.banderas={'retorno':1,'anterior':[],'siguiente':[],'editor':'e'} #Editor:n nuevo, e edicion, m edicion masiva
	self.tmpRef=0
	self.modelo=None
      
    def setupSignals(self):
	self.parent.tblProductos.setContextMenuPolicy(Qt.CustomContextMenu)
	self.parent.connect(self.parent.verProductos, SIGNAL("triggered()"), self.goProductos)
	self.parent.connect(self.parent.tProductos, SIGNAL("clicked()"), self.goProductos)
	self.parent.connect(self.parent.tbProductos, SIGNAL("clicked()"), self.goProductos)
	self.parent.connect(self.parent.tbpEditor, SIGNAL("clicked()"), lambda: self.parent.stkProductos.setCurrentIndex(0))
	self.parent.connect(self.parent.tblProductos,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocmProductos)
	self.parent.connect(self.parent.tbpBuscar, SIGNAL("clicked()"), self.buscar)
	self.parent.connect(self.parent.tbpSiguiente, SIGNAL("clicked()"), self.editarSiguiente)
	self.parent.connect(self.parent.tbpAnterior, SIGNAL("clicked()"), self.editarAnterior)
	self.parent.connect(self.parent.tbpNuevo, SIGNAL("clicked()"), self.nuevoProducto)
	self.parent.connect(self.parent.tbpEliminar, SIGNAL("clicked()"), self.eliminarProducto)
	self.parent.connect(self.parent.tbpAgregarFamilia, SIGNAL("clicked()"), self.parent.familia.iniciar)
	self.parent.connect(self.parent.tbpAgregarImpuesto, SIGNAL("clicked()"), self.parent.impuesto.iniciar)
	self.parent.connect(self.parent.tbpAgregarUnidad, SIGNAL("clicked()"), self.parent.unidad.iniciar)
	self.parent.connect(self.parent.tbpAgregarStock, SIGNAL("clicked()"), self.agregarStock)
	self.parent.connect(self.parent.lepFiltro, SIGNAL("returnPressed()"), self.buscar)
	self.parent.connect(self.parent.tpcodigo, SIGNAL("returnPressed()"), self.checkCodigo)
	self.parent.connect(self.parent.leProd, SIGNAL("returnPressed()"), lambda:self.buscarProducto(self.parent.leProd))
	#self.connect(self.parent.tstock, SIGNAL("valueChanged ( double d )"), addStock)
	#self.connect(self.parent.cbpDepartamentos,SIGNAL("activated(int )"), lambda:self.filtrarFamilias(self.parent.cbpDepartamentos.itemData(self.parent.cbpDepartamentos.currentIndex()).toString(),self.parent.cbpFamilias))
	#self.parent.connect(self.parent.cbpFamilias,SIGNAL("currentIndexChanged(int )"),self.buscar)
	self.parent.connect(self.parent.tblProductos,SIGNAL("activated(const QModelIndex&)"),self.editarProductos)
	self.parent.connect(self.parent.tbpRestaurar,SIGNAL("clicked()"), lambda: self.editarProducto(self.tmpRef))
	self.parent.connect(self.parent.tbpGuardar,SIGNAL("clicked()"),self.editarProducto_guardar)
	self.parent.connect(self.parent.tpgana, SIGNAL("editingFinished()"), self.calcprecio)
	self.parent.connect(self.parent.tbListarCodigos,SIGNAL("clicked()"), self.listarCodigos)
		
    def setTools(self):
	#actionInicio= self.menuInicio.addAction(QIcon("/usr/share/pyventa/images/32/Log-out-32.png"),"Regresar al inicio")
	#actionInicio.setShortcut(QKeySequence("Esc"))
	#self.connect(actionInicio, SIGNAL("triggered()"),self.goHome )
	#self.menuInicio.addSeparator()
	#actionInicio= self.menuInicio.addAction(QIcon("/usr/share/pyventa/images/32/Remove-32.png"),"Cerrar programa")
	#self.connect(actionInicio, SIGNAL("triggered()"),self.close )
	self.popMenu = QMenu(self.parent)
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/battery_empty.png"),"Marcar como faltante",self.marcarFalta)
	action.setIconVisibleInMenu(True)
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar producto",self.eliminarProducto)
	#self.connect(action, SIGNAL("triggered()"),self.productos.eliminarProducto)

		
    def goProductos(self):
	self.parent.stack.setCurrentIndex(1)
	self.parent.stkProductos.setCurrentIndex(1)
	#self.parent.tbrProductos.show()
	self.parent.lepFiltro.setFocus(True)
	self.parent.lepFiltro.selectAll ()
	  
    def editarProducto(self):
	self.banderas['retorno']=self.parent.stack.currentIndex ()
	self.parent.stkProductos.setCurrentIndex(0)	
	self.parent.stack.setCurrentIndex(1)
	#self.pbeNuevo.setEnabled(True)
	self.parent.tbpGuardar.setEnabled(True)
	self.parent.tbpRestaurar.setEnabled(False)	  
      
    def buscar(self):
	txt=str(self.parent.lepFiltro.text())
	if len(txt)>0:
	  departamentos=""
	  familias=""
	  tipo=''
	  #dep=self.parent.cbpDepartamentos.itemData(self.parent.cbpDepartamentos.currentIndex()).toString()
	  #dep=self.parent.cbpDepartamentos.model().celda(self.parent.cbpDepartamentos.currentIndex(),0)
	  #fam=self.parent.cbpFamilias.model().celda(self.parent.cbpFamilias.currentIndex(),0)
	  ##fam=self.parent.cbpFamilias.itemData(self.parent.cbpFamilias.currentIndex()).toString()
	  #if int(dep)>1: 
	    #familias=" AND `familia` = '"+fam+"'"
	  if (txt[0].isalpha()):
	    li=txt.split(' ')
	    fil=[]
	    for l in li:
		  fil.append(" descripcion like '%{0}%' ".format(l))
	    tipo="and".join(fil)
	  elif txt[0].isdigit() :
	    tipo= "((P.codigo={0} OR ref={0})or ref=(select producto from codigos as c where c.codigo={0}))".format(txt)
	  elif txt[0]=='*':
	    tipo='true'
	  else:
	    return True
	  head=['Ref','Codigos','Descripcion','Famlia','Cost','Gan','Prcio','Exist','Unidad','Impto','Ventas','U.Modifica']
	  campos="ref, codigo, descripcion, familias.nombre, costo, ganancia, precio, stock_logico, unidades.nombre, impuestos.nombre,vendidas, ultima_modificacion"
	  sql="SELECT {0} FROM productos as P, familias ,existencia , unidades, impuestos where existencia.producto=ref and unidades.id=unidad and familias.id=familia and impuestos.id=impuesto and {1}  group by ref order by `descripcion`; ".format(campos,tipo)
	  try:
	    self.cursor.execute(sql)
	    lista=self.cursor.fetchall()
	  except:
	    print "No se encontraron productos con tales criterios de busqueda",sql
	  else:
	    if lista!=None:
	      if self.modelo==None:
		self.modelo = MyTableModel(lista, head, self.parent) 
		self.parent.tblProductos.setModel(self.modelo)
	      else:
		self.modelo.setVector(lista)
	    self.parent.tblProductos.resizeColumnsToContents()
	    self.parent.stkProductos.setCurrentIndex(1)
	    self.parent.setStatus(0,"Mostrando %s resultados en la tabla."%self.modelo.getRowCount())
	      
    def edicionMasiva(self):
	  lista=self.parent.tblProductos.selectedItems()
	  for li in lista:
	      if (li.row()!=lastrow) :
		lastrow=li.row()
		refs.append(int(self.parent.tblProductos.item(li.row(),0).text()))
	  return refs
	
    def editarProductos(self,index=None):
	#self.pbeNuevo.setEnabled(False)
	self.parent.tbpGuardar.setEnabled(True)
	self.parent.tbpRestaurar.setEnabled(True)
	if index!=None:
	  refs=[]
 #edicion Masiva
	  lista=self.parent.tblProductos.selectedIndexes()
	  for li in lista:
	    refs.append(self.modelo.getCell(li,0))
	  self.parent.tbpSiguiente.setEnabled(True)
	  self.banderas['edicion']='m'
	  self.siguiente=refs
	  #print "siguiente %s "%len(self.siguiente)
	  self.anterior=[]
	else: #edicion simple
	  refs.append(self.modelo.getCell(index,0))
	  self.banderas['retorno']=self.parent.stack.currentIndex ()
	  self.banderas['edicion']='e'
	  self.siguiente=[]
	  self.anterior=[]
	#try:
	self.editarProducto(refs[0])
	#except:
	  #print "No se selecciono producto para editar"
	  
    def seleccionarProds(self):
      refs=[]
 #edicion Masiva
      lista=self.parent.tblProductos.selectedIndexes()
      for indice in lista:
	refs.append(self.modelo.getCell(indice,0))
      self.parent.tbpSiguiente.setEnabled(True)
      self.banderas['edicion']='m'
      return refs
	  
    def eliminarProducto(self):
	#self.parent.stack.setCurrentIndex(2)
	if self.tmpRef>0:
	  ref=self.tmpRef
	else:
	  ref=str(self.seleccionarProds()[0])
	if len(ref)>0:
	  self.cursor.execute("select count(producto) from vendidos where producto=%s"%ref)
	  vendidos=self.cursor.fetchone()
	  if int(vendidos[0])>0:
	    msgBox=QMessageBox(QMessageBox.Critical,"Advertencia!","El producto no puede ser eliminado porque ya existen ventas ligadas a el.",QMessageBox.Close,self.parent)
	    msgBox.exec_()
	  else:
	    try:
		self.cursor.execute("DELETE FROM productos where ref="+str(ref))
		self.cursor.execute("DELETE FROM existencia where producto=%s"%ref)
	    except:
		print "No se pudo eliminar el producto"
	    else:
		mb=QMessageBox.information(self.parent, "Producto eliminado", "El producto fue eliminado de la base de datos ")
	self.buscar()
      
    def calcprecio(self):
	x=(float(self.parent.tpcosto.value())*float(self.parent.tpgana.value()))/100
	self.parent.tpprecio.setValue(float(self.parent.tpcosto.value())+x)      

    def limpiarEditor(self):
	self.banderas['editor']='n'
	self.parent.leeRef.clear()
	self.parent.tpcodigo.clear()
	self.parent.tpdesc.clear()
	self.parent.cbeFamilias.setCurrentIndex(0)
	self.parent.tpcosto.setValue(0)
	self.parent.tpgana.setValue(0)
	self.parent.tpprecio.setValue(0)
	self.parent.tstock.setValue(0)
	self.parent.dsbStock.setValue(0)
	self.parent.dsbStock.setValue(0)
	#self.parent.cbeImpuestos.setCurrentIndex(0)
	#self.parent.cbeUnidades.setCurrentIndex(0)
	self.tmpRef=0
	self.parent.leNum.clear()
	self.parent.leProd.clear()
	self.parent.tbpGuardar.setEnabled(True)
	self.parent.tbpRestaurar.setEnabled(False)
	#self.parent.tbrpInfo.setText('')
	#self.siguiente=[]
	#self.anterior=[]
	self.parent.tpcodigo.setFocus(True)
    
    def extraInfo(self,ref):
	html='<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#002d42;">%s</span></p><table width="100%%" style=" font-weight:600; color:#002d42;"><tr><td>Apartir de</td>  <td>Desc.</td></tr><tr style="color:#f00;text-align:right"><td>%s</td> <td >%s%%</td></tr><tr><td>Precio</td>  <td>Subtotal</td></tr><tr><td>$ %s</td> <td>$ %s</td></tr></table><br/>'
	
	sql="SELECT P.nombre,minimo,descuento,precio-(precio*descuento*0.01), (precio-(precio*descuento*0.01))*minimo FROM ofertas as O,promociones as P, productos, familias as F WHERE ((conjunto=ref AND tipo=0) OR (conjunto=familia AND tipo=1) OR (conjunto=departamento AND tipo=2) ) AND O.promocion=P.id AND curdate() BETWEEN P.inicio AND P.fin AND familia=F.id and ref=%s   order by P.descuento desc"%ref
	#self.cursor.execute()
	self.parent.entabla(self.parent.tvpPrecios,['Promocion','Apartir de','%','P.Unitario','P.Total'],sql)
	#ofertas=self.cursor.fetchall()
	#if ofertas!=None:
	  #for oferta in ofertas:	    
	    #self.parent.tbrpInfo.setText(str(self.parent.tbrpInfo.toHtml())+html%oferta)
      
    def editarProducto(self, ref):
	i=0
	#ed=self.banderas['editor']
	self.limpiarEditor()
	self.banderas['editor']='e'
	self.extraInfo(ref)
	#self.pbeNuevo.setEnabled(False)
	self.parent.tbpGuardar.setEnabled(True)
	self.parent.tbpRestaurar.setEnabled(True)
	self.parent.stack.setCurrentIndex(1)
	self.parent.stkProductos.setCurrentIndex(0)	
	self.parent.leeRef.setText(str(ref))
	sql="select P.*,D.nombre as dep,F.nombre as fam, stock_logico  from productos as P,departamentos as D, familias as F, existencia where producto=ref and P.familia=F.id and P.ref={0} ;".format(ref)
	self.curser.execute(sql)
	producto=self.curser.fetchone()
	if producto!=None:
	  self.parent.tpcodigo.setText(str(producto['codigo']))
	  self.parent.tpdesc.setText(str(producto['descripcion']))
	  setComboModelKey(self.parent.cbeFamilias,producto['familia'])#Pone el combo en el valor del Id
	  self.parent.tpcosto.setValue(float(producto['costo']))
	  self.parent.tpgana.setValue(float(producto['ganancia']))
	  self.parent.tpprecio.setValue(float(producto['precio']))
	  self.parent.dsbStock.setValue(float(producto['stock_logico']))
	  setComboModelKey(self.parent.cbeImpuestos,producto['impuesto'])#Pone el combo en el valor del Id
	  setComboModelKey(self.parent.cbeUnidades,producto['unidad'])#Pone el combo en el valor del Id	  
	  #self.parent.cbeImpuestos.setCurrentIndex(self.parent.cbeImpuestos.findData(producto['impuesto']))
	  #self.parent.cbeUnidades.setCurrentIndex(self.parent.cbeUnidades.findData(producto['unidad']))
	  self.tmpRef=str(ref)
	  try:
	    self.curser.execute("SELECT *,count(subproducto)as num FROM subproductos where subproducto="+str(ref))
	    sub=self.curser.fetchone()
	    if sub['num']>0:
	      self.parent.leNum.setValue(float(sub['cantidad']))
	      self.parent.leProd.setText(str(sub['producto']))
	      self.parent.gbRelacion.setChecked(True)
	    else:
	      self.parent.leNum.clear()
	      self.parent.leProd.clear()
	      self.parent.gbRelacion.setChecked(False)
	  except:
	      self.parent.gbRelacion.setChecked(False)

    def nuevoProducto(self):
	self.parent.stack.setCurrentIndex(1)
	self.parent.stkProductos.setCurrentIndex(0)	
	#self.pbeNuevo.setEnabled(True)
	self.parent.tbpGuardar.setEnabled(True)
	self.parent.tbpRestaurar.setEnabled(False)
	self.parent.leeRef.setEnabled(False)
	self.limpiarEditor()
	self.banderas['editor']='n'

    def nuevoProducto_guardar(self, articulo=None):
	if articulo!=None:
	  producto=articulo
	else:
	  producto={
	  'codigo':str(self.parent.tpcodigo.text()),
	  'descripcion':str(self.parent.tpdesc.text()),
	  'familia':str(self.parent.cbeFamilias.model().celda(self.parent.cbeFamilias.currentIndex(),0)),
	  'costo':str(self.parent.tpcosto.value()),
	  'ganancia':str(self.parent.tpgana.value()),
	  'precio':str(self.parent.tpprecio.value()),
	  'stock':str(self.parent.tstock.value()+self.parent.dsbStock.value()),
	  'unidad':str(self.parent.cbeUnidades.model().celda(self.parent.cbeUnidades.currentIndex(),0)),
	  'vendidas':'0',
	  'impuesto':str(self.parent.cbeImpuestos.model().celda(self.parent.cbeImpuestos.currentIndex(),0))}
	if producto['codigo']=='':
		msgBox=QMessageBox(QMessageBox.Question,"Falta el codigo de barras","No ha escrito ningun codigo de barras, es necesario un codigo unico.<br>Desea que se genere automaticamente?",QMessageBox.Yes|QMessageBox.No,self.parent)
		ret=msgBox.exec_()
		if ret==QMessageBox.Yes:
		    suma=0
		    for e in producto['descripcion']:
		      suma+=ord(e)
		    producto['codigo']="%s"%(int(time()))
		    self.nuevoProducto_guardar(producto)
		else:
		   self.parent.tpcodigo.setFocus(True)
	else:
	  try:
		prev=self.buscarProd(producto['codigo'])
		if prev!=None:
		    QMessageBox.critical (self.parent, "Codigo duplicado", "Este codigo ya fue asignado a\n%s."%prev[0]) 
		    return False
		else:
		    self.cursor.execute("INSERT INTO productos VALUES(%s,NULL,%s,%s,%s,%s,%s,%s,%s,0,%s,NOW())",(producto['codigo'],producto['descripcion'],producto['familia'],producto['costo'],producto['ganancia'],producto['precio'],producto['stock'],producto['unidad'],producto['impuesto']))
	  except MySQLdb.Error, e:
                mb=QMessageBox.critical(self.parent, "Error!", "No se ha podido ingresar. Verifique los datos")
                self.parent.setStatus(2,"No se ha podido ingresar. Verifique los datos")
                print e
                self.pbStat.setToolTip("%s"%e)
	  else:
		self.cursor.execute("COMMIT")
		self.cursor.execute("SELECT LAST_INSERT_ID()")
		pd=self.cursor.fetchone()
		for code in self.alternos:
		  try:
		    sql="INSERT INTO codigos values (%s,%s)"%(pd[0],code[0])
		    self.cursor.execute(sql)
		  except:
		    pass
		self.alternos=[]
		self.cursor.execute("INSERT INTO existencia VALUES(%s,0,0,0,0)"%pd[0])
                mb=QMessageBox.information(self.parent, "El producto ha sido dado de alta", ".Su referencia es: %s "%pd[0])
                self.parent.setStatus(1,"El producto ha sido dado de alta. Su referencia es: {0}".format(pd[0]))
                if self.parent.gbRelacion.isChecked()==True:
		    sub={'cantidad':str(self.parent.leNum.value()),'producto':str(self.parent.leProd.text())}
		    self.cursor.execute("""INSERT INTO subproductos VALUES( %s,%s,%s)""",(pd[0],sub['cantidad'],sub['producto']))
		    self.cursor.execute("COMMIT")
		self.limpiarEditor()
		#self.goProductos()

    def checkCodigo(self):
	texto=str(self.parent.tpcodigo.text())
	if len(texto)>0:
	  try:
	    prod=self.buscarProd(texto,'ref')
	    #self.curser.execute("SELECT ref,count(ref)as num from productos where codigo="+texto)
	    #prod=self.curser.fetchone()
	    if prod!=None:
	      self.editarProducto(str(prod[0]))
	      self.banderas['editor']='e'
	      self.parent.tpcodigo.setFocus(True)
	      self.parent.tpcodigo.selectAll()
	    else:
	      self.parent.tpdesc.setFocus(True)
	    
	  except:
	    self.parent.tpdesc.setFocus(True)

    def editarProducto_guardar(self):
      if self.banderas['editor']=='n':
	self.nuevoProducto_guardar()
      else:
	producto={'codigo':'','descripcion':'','familia':'','costo':'','ganancia':'','precio':'',
	'stock':'','unidad':'','impuesto':''}
	producto['descripcion']="'%s'"%(self.parent.tpdesc.text())
	producto['familia']="'%s'"%self.parent.cbeFamilias.model().celda(self.parent.cbeFamilias.currentIndex(),0)
	#utileria.getComboModelKey(self.parent.cbeFamilias,0)
	#print producto['familia'],utileria.getComboModelKey(self.parent.cbeFamilias,0)
	producto['costo']="'%s'"%(self.parent.tpcosto.value())
	producto['ganancia']="'%s'"%(self.parent.tpgana.value())
	producto['precio']="'%s'"%(self.parent.tpprecio.value())
	producto['stock']="'%s'"%(self.parent.tstock.value()+self.parent.dsbStock.value())
	producto['impuesto']="'%s'"%self.parent.cbeImpuestos.model().celda(self.parent.cbeImpuestos.currentIndex(),0)
	producto['unidad']="'%s'"%self.parent.cbeUnidades.model().celda(self.parent.cbeUnidades.currentIndex(),0)
	producto['ultima_modificacion']='now()'
	if self.parent.tpcodigo.text()!='':
	    producto['codigo']=str(self.parent.tpcodigo.text())
	    out='set ref='+str(self.parent.leeRef.text())+" "
	    for key,val in producto.iteritems():
	      out+=" , `%s`=%s "%(key,val)
	    try:
	      sql="UPDATE productos %s where ref=%s"%(out,self.tmpRef)
	      self.cursor.execute(str(sql))
	    except MySQLdb.Error, e:
                self.parent.setStatus(2,"El producto no pudo ser actualizado correctamente, verifique los datos")
                print e
                self.pbStat.setToolTip("%s"%e)                
		msgBox=QMessageBox(QMessageBox.Critical,"Error","El producto no pudo ser actualizado correctamente, verifique los datos.",QMessageBox.Close,self.parent)
		msgBox.exec_()
	    else:
		self.parent.setStatus(1,"El articulo ha sido editado correctamente")
		self.cursor.execute("COMMIT")
		self.parent.stack.setCurrentIndex(2)
		#self.buscar()
	else:
		msgBox=QMessageBox(QMessageBox.Question,"Falta el codigo de barras","No ha escrito ningun codigo de barras, es necesario un codigo unico.<br>Desea que se genere automaticamente?",QMessageBox.Yes|QMessageBox.No,self.parent)
		ret=msgBox.exec_()
		if ret==QMessageBox.Yes:
		    suma=0
		    for e in producto['descripcion']:
		      suma+=ord(e)
		    self.parent.tpcodigo.setText("2500%s0%s0%s"%(producto['familia'],suma,producto['precio']))
		else:
		    self.parent.tpcodigo.setFocus(True)
	
	if self.parent.gbRelacion.isChecked()==True:
	  	sub={'cantidad':str(self.parent.leNum.value()),'producto':str(self.parent.leProd.text())}
	  	self.cursor.execute("select count(subproducto) from subproductos where subproducto="+str(self.tmpRef))
	  	num=self.cursor.fetchone()[0]
	  	if num>0:
		    self.cursor.execute("""UPDATE subproductos set cantidad=%s, producto=%s where subproducto=%s""",(sub['cantidad'],sub['producto'],self.tmpRef))
		    self.cursor.execute("COMMIT")
		else:
		    self.cursor.execute("""INSERT INTO subproductos VALUES( %s,%s,%s)""",(self.tmpRef,sub['cantidad'],sub['producto']))
		    self.cursor.execute("COMMIT")
	
	if len(self.siguiente)>0:
	  self.editarSiguiente()
	else:
	  self.parent.stack.setCurrentIndex(self.banderas['retorno'])

	#self.limpiarEditor()
	

    def editarSiguiente(self):
	#print len(self.siguiente)
	if len(self.siguiente)>0:
	  ref=self.siguiente.pop()
	  self.parent.tbpAnterior.setEnabled(True)
	  self.anterior.append(ref)
	  self.editarProducto(ref)
	else:
	  self.parent.tbpSiguiente.setEnabled(False)
	  self.parent.stack.setCurrentIndex(self.banderas['retorno'])
	  #self.parent.stkProductos.setCurrentIndex(0)
	  
    def editarAnterior(self):
	if len(self.anterior)>0:
	  ref=self.anterior.pop()
	  self.parent.tbpSiguiente.setEnabled(True)
	  self.siguiente.append(ref)
	  self.editarProducto(ref)
	else:
	  self.parent.tbpAnterior.setEnabled(False)


    def ocmProductos(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.parent.tblProductos.mapToGlobal(point) )

    def buscarProducto(self,item):
	dlg=buscador(self,str(item.text()))
	item.setText(str(dlg.exec_()))	
	
    def agregarStock(self):
      dsc=QInputDialog.getDouble(self, self.tr("Ajustar stock."),self.tr("Unidades adicionales:"))
      dsc=dsc[0]
      if dsc!=0 and self.tmpRef>0:
	print "Agregando %s piezas "%(dsc)
	try:
	  self.cursor.execute('UPDATE existencia set stock_logico=stock_logico+%s WHERE producto=%s'%(dsc,self.tmpRef))
	except:
	  print "Error al agregar unidades."
	else:
	  self.parent.dsbStock.setValue(float(self.parent.dsbStock.value())+dsc)
	  
    def listarCodigos(self):
      #print self.tmpRef
      if self.tmpRef==0:
	lis=ListadorCodigos(self.parent,-1,self.alternos)
	lis.exec_()
	self.alternos=lis.codes
      else:
	lis=ListadorCodigos(self.parent,self.tmpRef)	
	lis.exec_()
      
	
	
    def buscarProd(self,codigo,campos='descripcion'):
	sql=" select %s from productos as p where p.codigo=%s OR ref=%s or (ref=(select producto from codigos as c where c.codigo=%s));"%(campos,codigo,codigo,codigo)
	#print sql
	self.cursor.execute(sql)
	prev=self.cursor.fetchone()
	return prev    	
      
    def marcarFalta(self, ide=False):
      refs=libutil.seleccionar(self.parent.tblProductos,self.modelo,1)
      lis=Faltante(self.parent,refs,self.parent.usuario)	
      lis.exec_()      