#!/usr/bin/env python
# Inventario
import sys, os, datetime as dt
#aqui="/usr/share/pyventa/"
aqui=os.getcwd()
#sys.path.append(os.getcwd())
sys.path.append(os.path.join(aqui,'lib'))
sys.path.append(os.path.join(aqui,'ui'))
home=os.path.join(os.path.expanduser('~'),"pyventa")
if sys.platform == 'linux2':
    home=os.path.join(os.path.expanduser('~'),".pyventa")
    #sys.stdout = open(os.path.join(os.path.expanduser('~'),".pinve_salida.log"),"w")
    #sys.stderr = open(os.path.join(os.path.expanduser('~'),".pinve_error.log"),"w")
    # Set process name.  Only works on Linux >= 2.1.57.
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, 'Pinventa\0')
    except:
        pass
else:
	sys.stdout = open(os.path.join(os.path.expanduser('~'),"pinve_salida.log"),"w")
	sys.stderr = open(os.path.join(os.path.expanduser('~'),"pinve_error.log"),"w")
	
import datetime, tempfile
from PyQt4 import QtCore, QtGui
from ui.ui_asistente_inventario import Ui_Asistente 
import lib.utileria as ut
from lib import libutil

class Inventario:
    def __init__(self,parent):
	self.ui=parent
	self.cursor=parent.cursor
	self.curser=parent.curser
	self.modelo=None
	self.index=5
	self.ui.connect(self.ui.actionAsistente, QtCore.SIGNAL("triggered()"), self.nuevo)
	self.ui.connect(self.ui.tInventario, QtCore.SIGNAL("clicked()"), self.ver)
	self.ui.connect(self.ui.tbiNuevo, QtCore.SIGNAL("clicked()"), self.nuevo)
	self.ui.connect(self.ui.pbiActualizar, QtCore.SIGNAL("clicked()"), self.listar)
	self.ui.connect(self.ui.pbiVerInc, QtCore.SIGNAL("clicked()"), self.verInc)
	self.ui.connect(self.ui.tbInventarios, QtCore.SIGNAL("clicked()"), self.iniciar)
	self.ui.connect(self.ui.tbPrintInc, QtCore.SIGNAL("clicked()"), self.printInc)
	self.ui.connect(self.ui.tbExport, QtCore.SIGNAL("clicked()"), self.exportCvs)
	self.ui.connect(self.ui.deiFecha, QtCore.SIGNAL("dateChanged ( const QDate)"), self.listar)
	self.ui.connect(self.ui.tblInventario, QtCore.SIGNAL("activated(const QModelIndex&)"), self.verInc)
	self.ui.tblInventario.setContextMenuPolicy(3)
	self.ui.connect(self.ui.tblInventario,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)	
	self.menuPop = QtGui.QMenu(self.ui)
	#Menu contextual de tipos de impresion
	aNuevoInv=self.menuPop.addAction(QtGui.QIcon(":/actions/images/actions/black_18/add.png")," Iniciar nuevo inventario")
	aNuevoInv.setIconVisibleInMenu(True)
	aEliminar=self.menuPop.addAction(QtGui.QIcon(":/actions/images/actions/black_18/delete.png")," Eliminar inventario ")
	aEliminar.setIconVisibleInMenu(True)	
	aDetalle=self.menuPop.addAction(QtGui.QIcon(":/actions/images/actions/black_18/list.png")," Detalle inventario ")
	aDetalle.setIconVisibleInMenu(True)	
	aInc=self.menuPop.addAction(QtGui.QIcon(":/actions/images/actions/black_18/checkmark.png")," Ver inconsistencias ")
	aInc.setIconVisibleInMenu(True)		
	self.ui.connect(aEliminar, QtCore.SIGNAL("triggered()"), self.eliminarInv)
	self.ui.connect(aNuevoInv, QtCore.SIGNAL("triggered()"), self.nuevo)
	self.ui.connect(aDetalle, QtCore.SIGNAL("triggered()"), self.verDetalle)
	self.ui.connect(aInc, QtCore.SIGNAL("triggered()"), self.verInc)
	self.ui.deiFecha.setDate(QtCore.QDate.currentDate())
	self.iniciar()
	
    def iniciar(self):
	self.ui.stackInventario.setCurrentIndex(0)
	self.listar()
	
    def ver(self):
      	self.ui.stack.setCurrentIndex(self.index)

	
    def listar(self):
	fecha=str(self.ui.deiFecha.date().toString('yyyy-MM-dd'))
	head=('Id','Fecha','Saldo','Dominio','Orden','Estado', 'Auditor', 'Gerente')
	sql="SELECT id_inventario,fecha, saldo, dominio, orden, estado, auditor, gerente FROM inventarios WHERE fecha>date('%s') order by fecha ;"%fecha
	self.modelo=self.ui.entabla(self.ui.tblInventario,head,sql,self.modelo)    
	self.ui.tblInventario.resizeColumnsToContents()  
   
    def eliminarInv(self):
	if self.ui.aut(4)!=False:
	  if self.eliminar(libutil.seleccionar(self.ui.tblInventario, self.modelo)[0]):
	    self.listar()
    
    def eliminar(self,ide):
      if ide>0:
	try:
	  self.cursor.execute("DELETE FROM inventarios where id_inventario=%s;"%ide)
	except:
	  return False
	else:
	  self.ui.conexion.commit()
	  return True
	  
    def nuevo(self):
      self.ui.stackInventario.addWidget(AsistInventario(self.ui))
      self.ui.stackInventario.setCurrentIndex(4)

      #self.aInv.exec_()
      
    def verDetalle(self):
      self.ui.stackInventario.setCurrentIndex(1)
      self.resumir(libutil.seleccionar(self.ui.tblInventario, self.modelo)[0])
      
    def verInc(self):
      self.ui.stackInventario.setCurrentIndex(2)
      self.listarIncon(libutil.seleccionar(self.ui.tblInventario, self.modelo)[0])    
      
    def resumir(self,inventario):
	self.curser.execute("SELECT id_inventario, date(fecha) as fecha, dominio, saldo  FROM inventarios where id_inventario=%s; "%inventario)
	inv=self.curser.fetchone()
	self.cursor.execute("select count(*),round(sum(costo*inconsistencia),3) as balance,round(sum(costo*stock_logico),3) as valor from existencia,productos where producto=ref and inventario=%s;"%inventario)
	data=self.cursor.fetchone()
	self.cursor.execute("select count(*) from existencia,productos where producto=ref and inventario=%s and inconsistencia!=0;"%inventario)
	data2=self.cursor.fetchone()
	filde=" AND ( id=%s )"%' OR id='.join(inv['dominio'].split(','))
	self.cursor.execute("select nombre from departamentos where id>0 %s ;"%filde)
	data3=self.cursor.fetchall()
	depa=''
	for item in data3:
	  depa+=item[0]
	campos={'$fecha':inv['fecha'],'$empresa':'','$deps':'','$nacontados':'','$invalor':'','$naicon':'','$baincon':''}	    
	campos['$deps']=depa
	campos['$empresa']=str(self.ui.cfg.get('empresa','nombre'))
	
	if data!=None:
	  campos['$nacontados']=str(data[0])	      
	  campos['$invalor']=str(data[2])
	  campos['$naicon']=str(data2[0])
	  campos['$baincon']=str(data[1])
	html=str(self.ui.qteResumen.toHtml())
	for key,item in campos.iteritems():
	  html=html.replace(key,str(item))
	self.ui.qteResumen.setHtml(html)
	
    def listarIncon(self,inventario):
	self.ui.stackInventario.setCurrentIndex(2)
	self.ui.lbiInc.setText("Tabla de inconsistencias de acuerdo al inventario %s."%inventario)
	head=('Ref','Descripcion','Falte/Sobrante','Costo','Monto')
	sql="SELECT ref,descripcion,inconsistencia,costo, inconsistencia*costo FROM productos,existencia WHERE producto=ref and inconsistencia!=0 and inventario=%s order by ref ;"%inventario
	modelo=self.ui.entabla(self.ui.tviInc,head,sql)    
	self.ui.tviInc.resizeColumnsToContents()  
	self.incos=modelo.getVector()
	return modelo
	
	
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
	 self.menuPop.exec_(self.ui.tblInventario.mapToGlobal(point) )	
   
    def printInc(self):
      titulo="Inconsistencias del inventario %s"%libutil.seleccionar(self.ui.tblInventario, self.modelo)[0]
      html=libutil.listaHtml(self.incos,titulo, cabezas=['Ref','Descripcion','Falte/Sobrante','Costo','Monto'],anchos=[10,40,15,15,20])
      libutil.printa(html,titulo,self.ui)
      
    def exportCvs(self):
      tabla=[('Ref','Descripcion','Falte/Sobrante','Costo','Monto')]
      tabla.extend(self.incos)
      #print tabla
      libutil.toCsv(tabla,self.ui)
      
      
class AsistInventario(QtGui.QDialog, Ui_Asistente):  
    def __init__(self,parent,usuario=-1):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.deps=[] #Lista con los numeros de los departamentos seleccionados
		self.orden='familia' #define el order by
		self.columnas={'Referencia':'ref','Descripcion':'descripcion','Precio':'precio','Costo':'costo','Stock logico':'stock_logico'}
		self.ordenes={'familia':self.rbFam,'departamento':self.rbDeps,'descripcion':self.rbDesc, 'precio':self.rbPrecio, 'ref':self.rbRef, 'ultima_modificacion':self.rbModif}
		self.query="" #Esta variable guarda la consulta que genera la lista de articulos participantes en el inventario
		self.producto=None
		con=ut.conexion()
		self.ui=parent
		self.incos=[]
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.auditor=parent.usuario
		self.gerente=1
		self.inventario=1
		self.filde=''
		self.modelo=None
		self.cfg =ut.Konfig()
		hoy=dt.date.today()
		self.fecha=str(hoy.strftime("%d-%m-%Y"))
		#self.timer=QtCore.QTimer(self)
		self.limite=['1','1']
		self.stack.setCurrentIndex(0)
		self.modo=0
		#insert=QtGui.QAction(self)
		#insert.setShortcut("Ins")
		self.connect(self.tbAdelante, QtCore.SIGNAL("clicked()"), self.continuar)
		self.connect(self.tbManual, QtCore.SIGNAL("stateChanged ( int  )"), self.manual)
		
		self.connect(self.tbAtras, QtCore.SIGNAL("clicked()"), self.retroceder)
		self.connect(self.tbCancelar, QtCore.SIGNAL("clicked()"), self.cancelar)
		self.connect(self.tbSigProd, QtCore.SIGNAL("clicked()"), self.sigProd)
		self.connect(self.tbAntProd, QtCore.SIGNAL("clicked()"), self.antProd)
		self.connect(self.tbSetStock, QtCore.SIGNAL("clicked()"), self.setStock)
		self.connect(self.tbImprimir, QtCore.SIGNAL("clicked()"), self.imprimir)
		self.connect(self.tbIncon, QtCore.SIGNAL("clicked()"), self.listarIncon)
		self.connect(self.tabla, QtCore.SIGNAL("activated(const QModelIndex&)"), self.seleccionar)
		self.connect(self.tbPrintInc, QtCore.SIGNAL("clicked()"), self.printInc)
		
		#self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.autoGuardar)
		self.connect(self.leExistencias, QtCore.SIGNAL("returnPressed ()"), self.setStock)
		self.connect(self.leFiltro, QtCore.SIGNAL("textChanged(QString)"), self.buscar)
		self.connect(self.leFiltro, QtCore.SIGNAL("returnPressed()"), self.contar)
		self.inicio()
		self.listarDepartamentos()
		
		
    def inicio(self):
	sql="SELECT * FROM inventarios where estado=1 limit 1"
	self.curser.execute(sql)
	res=self.curser.fetchone()
	if res!=None:
	  msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Question,"Inventario en curso","Actualmente hay un inventario en proceso de conteo.<h3>Desea participar en este conteo?</h3>",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,self)
	  #if msgBox.exec_()==QtGui.QMessageBox.Yes:
	    #self.exec_()
	  self.inventario=res['id_inventario']
	  self.auditor=res['auditor']
	  self.gerente=res['gerente']
	  self.deps=res['dominio'].split(',')
	  if res['orden']!=None:
	    self.orden=res['orden']
	  if len(self.deps)>0:
	    self.filde=' AND (departamento!=-1 '
	    for dep in self.deps:
	      if dep.isdigit():
		self.filde+=' OR departamento=%s'%dep
	    self.filde+=') '
	  self.iniConteo()
	  self.stack.setCurrentIndex(3)

	  self.lbStatus.setText("Etapa de conteo...")
	  self.tbCancelar.setEnabled(False)
	  self.tbAtras.setEnabled(False)
	  #else:
	    #self.done(2)
	    
	    
    def continuar(self):
	current=self.stack.currentIndex()
	if (current+1==1): 			#Si es el primer paso selecciona los departamentos
	  self.lbStatus.setText("Preparacion de la tabla de conteo")

	  lista=self.tablaDeps.selectedItems()
	  self.deps=[]
	  for item in lista:	#Agrupa en una lista los id de los departamentos tomando de la listWidget los que fueron seleccionados
	    if self.tablaDeps.column(item)==0:
	      self.deps.append(str(item.text()))
	  self.stack.setCurrentIndex(current+1)
	
	elif (current+1==2):			#Si es el segundo paso ordena las columnas y prepara el query
	  self.lbStatus.setText("Vista previa de los productos")
	  self.cols=""
	  lista=self.lsColumnas.selectedItems()
	  for i in range(int(self.lsColumnas.count())):
	    if self.lsColumnas.item(i).checkState()==2:
	      if len(self.cols)>0:self.cols+="," # Coma inteligente para evitar que sobren o falten
	      self.cols+=self.columnas[str(self.lsColumnas.item(i).text())] #convierte en texto las columnas
	  for val,radio in self.ordenes.iteritems():	#Por cada radiobutton si este esta checado toma su valor para ordenar
	    if radio.isChecked()==True:
		self.orden=val
	  #print "columnas %s\nordenadas por %s"%(self.cols,self.orden)
	  #Lo siguiente es para comprobar que todos los productos tienen una existencia asociada y si no la tiene la crean
	  self.setCursor(QtGui.QCursor(16))
	  sql="INSERT INTO existencia SELECT ref,1,0,0,0 FROM productos WHERE ref NOT IN (SELECT producto from existencia)"
	  self.cursor.execute(sql)
	  qry=self.cursor.fetchall()
	  if qry !=None:
	    #for prod in qry:
	      #self.cursor.execute("INSERT INTO existencia VALUES(%s,1,0,0,0)"%prod[0])
	    self.ui.conexion.commit()
	  #Hasta este punto si todo sale bien registra los cambios en la base de datos
	  self.filde=''
	  if len(self.deps)>0:
	    rcv=str(self.deps.pop())
	    self.filde=' AND (departamento='+rcv
	    for dep in self.deps:
	      self.filde+=' OR departamento=%s'%dep
	    self.deps.append(rcv)
	    self.filde+=') '
	  self.query="SELECT %s from productos, familias as f, existencia as e where familia=f.id and e.producto=ref %s order by %s "%(self.cols,self.filde,self.orden)
	  #print self.query
	  self.cursor.execute(self.query)
	  resul=self.cursor.fetchall()
	  if resul !=None:
	    ut.entablar(self.tablaProductos,resul,self.cols.split(','))
	    #self.tablaProductos.setColumnCount (self.tablaProductos.columnCount()+1) #Pone una columna extra en la tabla
	  self.setCursor(QtGui.QCursor(0))
	  self.stack.setCurrentIndex(self.stack.currentIndex()+1)
#Al pasar a la etapa de conteo	  
	elif current+1==3:
	  self.lbStatus.setText("Etapa de conteo")	  
	  msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Question,"Confirmacion","A continuacion se procedera a contar y no sera posible cancelar o editar las configuraciones del inventario hasta que se de por terminado.<h3>Desea continuar?</h3>",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,self)
	  if msgBox.exec_()==QtGui.QMessageBox.Yes:
	    self.tbCancelar.setEnabled(False)
	    self.tbAtras.setEnabled(False)
	    try:
	      sql="INSERT INTO inventarios VALUES(Null, Now(),0,'%s','%s',1,%s,%s)"%(','.join(self.deps),self.orden,self.auditor,self.gerente)
	      self.cursor.execute(sql)
	    except :
	      print "Error, %s"%(sql) 
	    else:
	      self.ui.conexion.commit()
	      sql=self.ui.conexion.lastId()
	      self.cursor.execute(sql)
	      self.inventario=self.cursor.fetchone()[0]	    
	      sql="UPDATE existencia as e,productos, familias as f set inconsistencia=0, stock_fisico=stock_logico  where   familia=f.id and e.producto=ref %s ;"%(self.filde)
	      self.cursor.execute(sql)
	      self.ui.conexion.commit()
	      self.iniConteo()
	    self.stack.setCurrentIndex(self.stack.currentIndex()+1)
#Al terminar de contar	    
	elif (current+1==4):
	  msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Question,"Confirmacion","En este punto, todos los productos deben estar contabilizados, y se procedera a cerrar el inventario.<h3>Desea seguro que desea terminar el inventario?</h3>",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,self)
	  self.gerente=self.autentificacion(2)
	  if msgBox.exec_()==QtGui.QMessageBox.Yes and self.gerente!=False:	  
	    self.stack.setCurrentIndex(self.stack.currentIndex()+1)
	    self.setCursor(QtGui.QCursor(16))
	    sql="UPDATE existencia set   stock_logico=stock_fisico where inventario=%s"%(self.inventario)
	    self.curser.execute(sql)	
	    self.curser.execute("UPDATE inventarios set estado=0,auditor=%s, gerente=%s, saldo=(select round(sum(costo*inconsistencia),3) from existencia,productos where producto=ref and inventario=id_inventario) where id_inventario=%s"%(self.auditor,self.gerente['id_usuario'],self.inventario))	
	    self.ui.conexion.commit()
	    self.setCursor(QtGui.QCursor(0))
	    self.cursor.execute("select count(*),round(sum(costo*inconsistencia),3) as balance,round(sum(costo*stock_logico),3) as valor from existencia,productos where producto=ref and inventario=%s;"%self.inventario)
	    data=self.cursor.fetchone()
	    self.cursor.execute("select count(*) from existencia,productos where producto=ref and inventario=%s and inconsistencia!=0;"%self.inventario)
	    data2=self.cursor.fetchone()
	    filde=self.filde.replace('departamento','id')
	    self.cursor.execute("select nombre from departamentos where id>0 %s ;"%filde)
	    data3=self.cursor.fetchall()
	    depa=''
	    for item in data3:
	      depa+=" %s "%(item)
	    campos={'$fecha':self.fecha,'$empresa':'','$deps':'','$nacontados':'','$invalor':'','$naicon':'','$baincon':''}	    
	    campos['$deps']=depa
	    campos['$empresa']=str(self.cfg.getDato('empresa','nombre'))
	    
	    if data!=None:
	      campos['$nacontados']=str(data[0])	      
	      campos['$invalor']=str(data[2])
	      campos['$naicon']=str(data2[0])
	      campos['$baincon']=str(data[1])
	    html=str(self.qteResumen.toHtml())
	    for key,item in campos.iteritems():
	      html=html.replace(key,str(item))
	    self.qteResumen.setHtml(html)
	    
	elif (current+1==5):
	    self.listarIncon()
	    self.tbAdelante.setText("Finalizar")
	elif    (current+1==6):
	  self.done(1)
	    
    def retroceder(self):
	self.stack.setCurrentIndex(self.stack.currentIndex()-1)	
    
    def iniConteo(self,producto='',forza=False):
	if int(self.limite[0])>=0 and int(self.limite[1])>=0:
	  inventario=""
	  if forza==True:
	    inventario=" and inventario!=%s"%self.inventario
	  if len(str(producto))>0:
	    producto=" and (ref=%s or codigo like '%s%%')"%(producto,producto)
	  sql="SELECT ref,descripcion,precio,f.nombre,e.stock_logico,e.stock_fisico from productos, familias as f, existencia as e where familia=f.id %s and e.producto=ref %s  %s order by %s limit %s"%(producto,inventario,self.filde,self.orden,','.join(self.limite))
	  #sql="SELECT ref,descripcion,precio,f.nombre,e.stock_logico,e.stock_fisico from productos, familias as f, existencia as e where familia=f.id and e.producto=ref and inventario=%s order by "%self.inventario
	  #print sql
	  #print "Contando ",producto, sql

	  self.curser.execute(sql)
	  resul=self.curser.fetchone()
	  if resul !=None:
	    self.producto=resul
	    self.lbCProducto.setText(resul['descripcion'])
	    self.lbCProducto.setToolTip(resul['descripcion'])
	    self.lbCPrecio.setText("<b>Familia: </b>%s<br/><b>Precio: </b>%s"%(resul['nombre'],resul['precio']))
	    self.leExistencias.setText(str(resul['stock_fisico']))
	    self.leExistencias.selectAll ()
	    self.leExistencias.setFocus()

    def sigProd(self):#Carga el siguiente producto sin contar en conteo automatico
	#if int(self.limite[0])-1==0:
	  #self.tbSigProd.setEnabled(False)
	self.limite[0]=str(int(self.limite[0])+1)
	self.iniConteo()
	
    def antProd(self):#Carga el siguiente producto sin contar en conteo automatico
      if int(self.limite[0])-1==0:
	self.tbAntProd.setEnabled(False)
      else:
	self.limite[0]=str(int(self.limite[0])-1)
	self.iniConteo()	
    
    def listarDepartamentos(self):
	sql="SELECT * FROM departamentos;"
	self.cursor.execute(sql)
	qry=self.cursor.fetchall()
	if qry !=None:
	   ut.entablar(self.tablaDeps,qry,['id','Nombre'])
	   
    def cancelar(self):
      self.ui.conexion.rollback()
      self.done(2)
      
    def setStock(self):
      if self.producto!=None:
	self.cursor.execute("UPDATE existencia SET inventario=%s, stock_fisico='%s', inconsistencia=stock_fisico-stock_logico WHERE producto=%s"%(self.inventario,float(self.leExistencias.text()),self.producto['ref']))
	self.ui.conexion.commit()
	if self.modo==0:
	  self.sigProd()
	else:
	  self.leFiltro.setFocus()
	

    def imprimir(self):
      self.setCursor(QtGui.QCursor(16))
      lista="<table width='90%%' border='0' cellspacing=1 align='center'><tr><td><b>%s</b><br/><b>Departamentos:</b> %s<br/><b>Fecha:</b> %s</H4></td><TD> <H2>Lista de productos</H2></TD></tr></table><table width='100%%' border='0' cellspacing=1>"%(self.cfg.getDato('empresa','nombre'),','.join(self.deps),self.fecha)
      #print ','.join(self.deps)
      self.cursor.execute(self.query)
      res=self.cursor.fetchall()
      head="</table><table width='100%%' border='0' cellpadding=3 cellspacing=1 align='center'><tr bgcolor='#358' style='color:#fff'  width='100%%'><TH>#</TH>"
      for col in self.cols.split(','):
	head+="<TH ><span style=\" font-size:8px;\"> %s </span></TH>"%col.upper()
      head+="<TH style=\"font-size:8px;\">EXISTENCIAS</TH><TH style=\"font-size:8px;\">EXTRA</TH></tr>"
      for i,prod in enumerate(res):
	 if (i>41 and (i+2)%39==0) or i==37 or i==0:
	   lista+=head
	 if  i%2==0 :
	  lista+="<tr bgcolor=\"#ddd\" valign='middle'  >"
	 else:lista+="<tr valign='middle'>"
	 lista+="<td width='5%%' align=\"right\"><span style=\" font-size:8px;\">%s</span></td>"%i
	 for i,col in enumerate(self.cols.split(',')):
	  if type(prod[i])==str:
	    lista+="<td width='100%%'><span style=\" font-size:7px;\"> %s</span></td>"%prod[i]
	  else:
	    lista+="<td width='7%%' align=\"right\"><span style=\" font-size:8px;\"> %s </span></td>"%prod[i]
	 lista+="<td>        </td><td>        </td></tr>" 
      lista+="</table>"
      libutil.printa(lista,"Lista_de_productos-%s"%self.fecha,self)
      self.setCursor(QtGui.QCursor(0))
      

      
    def printInc(self):
      html=libutil.listaHtml(self.incos,"Inconsistencias", ['Ref','Descripcion','Falte/Sobrante','Costo','Monto'],anchos=[10,40,15,15,20])
      libutil.printa(html,"Inconsistencias",self)
      
    def autoGuardar(self):
      #self.timer.start(10000)
      #self.ui.conexion.commit()
      print "Aplicando cambios"
      
    def seleccionar(self,index):
      #print self.modelo.getCell(index,0)
      self.limite[0]='0'
      self.iniConteo(self.modelo.getCell(index,0))
      
    def buscar(self,texto):
	texto=str(texto)
	if len(texto)>0:
	  if texto[0].isdigit()==False:
	    #sql="SELECT ref,descripcion,precio,e.stock_fisico from productos, familias as f, existencia as e where familia=f.id and e.producto=ref and  (ref=%s or codigo like '%s%%') %s order by descripcion"%(texto,texto,self.filde)
	  #else:
	    sql="SELECT ref,descripcion,precio,e.stock_fisico from productos, familias as f, existencia as e where familia=f.id and e.producto=ref and  descripcion like '%%%s%%' %s order by descripcion"%(texto,self.filde)
	    try:
	      self.cursor.execute(sql)
	      lista=self.cursor.fetchall()
	    except:
	      print "No se encontro el producto"
	    else:

	      if lista!=None:
		if self.modelo==None:
		  self.modelo = ut.MyTableModel(lista, ['Ref','Descripcion','Precio','Conteo'], self) 
		  self.tabla.setModel(self.modelo)
		else:
		  self.modelo.setVector(lista)
		self.tabla.resizeColumnsToContents()
		#self.leFiltro.clear()

    def contar(self):
	txt=str(self.leFiltro.text())
	if txt[0].isdigit():
	  try:
	    ref=int(txt)
	  except:
	    pass
	  else:
	    self.limite=['0','1']
	    self.leFiltro.clear()
	    self.iniConteo(txt)
	    
    def manual(self,modo):
      if modo==0:
	self.leExistencias.setFocus()
	self.leExistencias.selectAll()
      elif modo==2:
	self.leFiltro.setFocus()
	self.leFiltro.selectAll()
      self.modo=modo
      
    def listarIncon(self):
	self.stack.setCurrentIndex(5)
	head=('Ref','Descripcion','Falte/Sobrante','Costo','Monto')
	sql="SELECT ref,descripcion,inconsistencia,costo, inconsistencia*costo FROM productos,existencia WHERE producto=ref and inconsistencia!=0 and inventario=%s order by ref ;"%self.inventario
	modelo=self.ui.entabla(self.tvInconsistencias,head,sql)    
	self.tvInconsistencias.resizeColumnsToContents()  
	self.incos=modelo.getVector()
	return modelo
	      
    def autentificacion(self,nivel):
	dlg=ut.Seguridad(self)
	acceso=dlg.exec_()
	if acceso>-1 and dlg.usuario['nivel']>=nivel:
	  return dlg.usuario
	else:
	  return False
	  
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    app.processEvents()
    aw = AsistInventario()
    aw.show()
    app.exec_()
    
