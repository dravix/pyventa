from PyQt4 import  Qt
from PyQt4.QtCore import Qt,SIGNAL,QModelIndex,QDate
from PyQt4.QtGui import QMessageBox, QIcon, QDialog,QMenu
from lib.selector import Selector
from ui.ui_editor_oferta import Ui_Editor
from lib.dialogos.calcula_descuentos import CalculaDescuentos
from lib.librerias.conexion import dicursor
class EditorOferta(QDialog, Ui_Editor):
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
		self.CP=CalculaDescuentos(self)

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
	self.curser.execute("""SELECT * FROM promociones where id=%s """%self.ide)
	row=self.curser.fetchone()
	if row!=None:
	  row=dicursor(self.curser,row)
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
	  conjuntos=['PRODUCTO','FAMILIA','DEPARTAMENTO']
      	  sql=""" select conjunto,CASE  WHEN tipo=0 THEN (SELECT descripcion from productos where ref=conjunto) WHEN tipo =2 THEN (SELECT nombre from familias where id=conjunto)  WHEN tipo =3 THEN (SELECT nombre from departamentos where id=conjunto) END AS nombre,tipo, tipo from ofertas where promocion=%s group by conjunto"""%self.ide
      	  self.cursor.execute(sql)
	  rows=self.cursor.fetchall()
	  self.lista=[]
	  if rows!=None:
	    for li in rows:
	      li=list(li)	      
	      li[2]=conjuntos[li[2]]
	      self.lista.append(li)
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
	    sql=self.parent.conexion.lastId()
	    self.cursor.execute(sql)
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
	      self.cursor.execute(""" INSERT INTO ofertas VALUES(%s,%s,%s)"""%(self.ide,item[0],item[3]))
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
	app=Selector(self,"Departamentos",'departamentos','id,nombre','Id,Nombre',filtros=" nombre like '%{0}%' order by nombre ")
	done=app.exec_()
	if done==1:
	  items=app.retorno
	  [i.extend(['DEPARTAMENTO','2']) for i in items]
	  self.lista.extend(items)
	  self.listar()

    def listarFams(self):    
	app=Selector(self,"Familias",'familias','id,nombre','Id,Nombre',filtros=" nombre like '%{0}%' order by nombre ")
	done=app.exec_()
	if done==1:
	  items=app.retorno
	  [i.extend(['FAMILIA','1']) for i in items]
	  self.lista.extend(items)
	  self.listar()
    
    def listarProds(self):    
	app=Selector(self,"Productos",'productos','ref,descripcion','Ref,Descripcion del producto',filtros=" descripcion like '%{0}%' order by descripcion ")
	done=app.exec_()
	if done==1:
	  prods=app.retorno
	  [i.extend(['PRODUCTO','0']) for i in prods]
	  self.lista.extend(prods)
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
