# -*- coding: utf-8 -*-
import sys,random,os
from os.path import join,expanduser
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox
from lib.utileria import Documento, MyTableModel
from ui.ui_reportes import Ui_Form
from datetime import  datetime
import MySQLdb,  tempfile
from lib import libutil
from lib.librepo import Chart, Ventas as RVentas
from lib.modelos.qmodelotablasql import QModeloTablaSql
from lib.libutil import printa
from lib.factura import Factura
from lib.modelos.venta import Venta
from lib.dialogos.cobrador import Cobrador
from lib.dialogos.agrega_gasto import AgregaGasto
#from lib.librerias.docx.docx import *
from lib.modelos.gasto import Gasto 
from lib.modelos.compra import Compra 
from lib.modelos.caja import Caja 
from lib.modelos.retiro import Retiro 
from lib.modelos.deposito import Deposito 
from lib.modelos.movimiento import Movimiento 
from lib.selector import Selector
from lib.dialogos.visor_venta import VisorVenta 
from lib.librerias.conexion import dicursor

class Reportes(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.curser=parent.curser
		self.cursor=parent.cursor
		self.datos={'nombre':"Reportes",'descripcion':"Muestra el todo lo relacionado con ventas.",'version':"0.05",'id':id,'nivel':2}
		self.id=id
		self.parent=parent
		self.moventas=QModeloTablaSql(self.parent.cursor,self)
		self.tVentas.setModel(self.moventas)
		self.efectivo=0
		self.action = QtGui.QAction(self)
		self.action.setObjectName(self.datos['nombre']+str(id))
		#self.action.setShortcut("F4")
		#self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
		icono = QtGui.QIcon()
		icono.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/report.png"), 0, QtGui.QIcon.Off)
		self.icono=":/modulos/images/png/elegant/report.png"
		icono.addPixmap(QtGui.QPixmap(self.icono), 2, QtGui.QIcon.Off)
		self.action.setIcon(icono)
		self.action.setText(self.datos['nombre'])
		#self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.stackMove(self.id))
		self.connect(self.action, QtCore.SIGNAL("triggered()"), self.inicia )
		
        	#self.connect(self.verGrafica, QtCore.SIGNAL("clicked()"), self.graficar)
        	self.connect(self.tbGraficas, QtCore.SIGNAL("clicked()"), self.graficar)
        	self.connect(self.tbGColorear, QtCore.SIGNAL("clicked()"), self.selecColor)
        	self.connect(self.tbRExportar, QtCore.SIGNAL("clicked()"), self.exportar)
        	self.connect(self.tbLExportar, QtCore.SIGNAL("clicked()"), self.exportar)
		#self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),lambda: parent.aut(self.id,2) )
        	#self.connect(self.bvShowinfo, QtCore.SIGNAL("clicked()"), self.weekPlot)
        	self.connect(self.tVentas, QtCore.SIGNAL("activated(const QModelIndex&)"), self.mostrarResumen)
        	self.connect(self.cbCaja, QtCore.SIGNAL("currentIndexChanged(int )"), self.setCaja)
        	self.connect(self.cbListas, QtCore.SIGNAL("currentIndexChanged(int )"), self.tablarVentas)
        	self.connect(self.pbListaVentas, QtCore.SIGNAL("clicked()"),  self.actualizar)
        	self.connect(self.bCorteT, QtCore.SIGNAL("clicked()"), self.corte)
        	self.connect(self.tbGImprimir, QtCore.SIGNAL("clicked()"), self.imprimirGrafica)
        	self.connect(self.tbGGuardar, QtCore.SIGNAL("clicked()"), self.guardarGrafica)
        	self.connect(self.tbListar, QtCore.SIGNAL("clicked()"), lambda:self.stackReportes.setCurrentIndex(0))
        	self.connect(self.tbImprimir, QtCore.SIGNAL("clicked()"), self.tbImprimir.showMenu)
		self.tVentas.setContextMenuPolicy(3)
		self.connect(self.tVentas,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
        	self.connect(self.deFrom, QtCore.SIGNAL("dateChanged ( const QDate)"), self.cambiarFecha)
        	self.connect(self.deTo, QtCore.SIGNAL("dateChanged ( const QDate)"), self.cambiarFecha)
		
		self.listing=False ##Bandera de si se esta viendo una lista especial
        	self.html=False
		self.makeMenu()
		self.fecha='CURDATE()'
		#self.splitter.moveSplitter(300,0)
        	self.deFrom.setDate(QtCore.QDate.currentDate())  
        	self.deTo.setDate(QtCore.QDate.currentDate())  
		self.tbImprimir.setMenu(self.menuImpresion)
		modelo=QModeloTablaSql(self.parent.cursor,self)
		self.parent.cursor.execute("SELECT num_caja, nombre from cajas")
		res=self.parent.cursor.fetchall()
		self.cbCaja.addItem("Todas",0)
		for c in res:
		  self.cbCaja.addItem(c[1],c[0])
		self.chart=False
		self.tbRExportar.setEnabled(True)
		

        	#self.graf=QWidget(self)
       		#self.vlVentas1.addWidget(self.graf)
    def inicia(self):
      if self.parent.aut(self.datos['nivel'])>0:
	if self.parent.sesion['usuario']['nivel']<3:
	  self.caja=" caja=%s "%self.parent.caja
	  self.cbCaja.setEnabled(False)
	elif  self.parent.sesion['usuario']['nivel']>=3:
	  self.caja="1"
	  self.cbCaja.setEnabled(True)
	self.parent.stack.setCurrentIndex(self.datos['id'])
	self.actualizar()
	self.verReportes()

    def makeMenu(self):
      self.menuVentas = QtGui.QMenu(self)
      self.menuCompras = QtGui.QMenu(self)
      self.menuImpresion = QtGui.QMenu(self)
      self.menuGastos = QtGui.QMenu(self)
      menuDetalles = QtGui.QMenu(self)
      #Menu contextual de tipos de impresion
      aPrintR=self.menuImpresion.addAction("Resumen (PDF) ")
      aPrintC=self.menuImpresion.addAction("Corte total (Ticket)")
      #Menu contextual del listado de ventas
      aAbrirNota=self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/file.png"),"Abrir venta ")
      aAbrirNota.setIconVisibleInMenu(True)
      aignorar=self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/cancel.png"),"Ignorar ")
      aignorar.setIconVisibleInMenu(True)
      aCobrarNota=self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/thunder.png"),"Liquidar ",self.cobrar)
      aCobrarNota.setIconVisibleInMenu(True)      
      aReimprimir=self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/print.png"),"Reimprimir copia ")
      aReimprimir.setIconVisibleInMenu(True)
      aReimprimir=self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/bookmark.png"),"Facturar venta",self.facturar)
      self.menuVentas.addAction(QtGui.QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar venta",self.eliminarVentas)
      
      #Menu contextual del listado de ventas
      aNuevaCompra=self.menuCompras.addAction(QtGui.QIcon(":/actions/images/actions/black_18/add.png")," Nueva compra")
      aNuevaCompra.setIconVisibleInMenu(True)
      aEditarCompra=self.menuCompras.addAction(QtGui.QIcon(":/actions/images/actions/black_18/pencil.png")," Editar compra")
      aEditarCompra.setIconVisibleInMenu(True)  
      aEliminarCompra=self.menuCompras.addAction(QtGui.QIcon(":/actions/images/actions/black_18/delete.png")," Eliminar compra")
      aEliminarCompra.setIconVisibleInMenu(True)
      
      aNuevoGasto=self.menuGastos.addAction(QtGui.QIcon(":/actions/images/actions/black_18/add.png")," Agregar",self.agregar)
      aEliminarGasto=self.menuGastos.addAction(QtGui.QIcon(":/actions/images/actions/black_18/delete.png")," Eliminar",self.remover)
      
      menuDetalles.addAction(QtGui.QIcon(":/actions/images/actions/black_18/clipboard.png"),"Detalle general",self.detallar)
      menuDetalles.addAction(QtGui.QIcon(":/actions/images/actions/black_18/clipboard.png"),"Detalle de movimientos",self.detallarMovimientos)
      menuDetalles.addAction(QtGui.QIcon(":/actions/images/actions/black_18/clipboard.png"),"Mejores productos",self.detallarProds)
      menuDetalles.addAction(QtGui.QIcon(":/actions/images/actions/black_18/clipboard.png"),"Detallar por familia",self.detallarFamilia)
      
      self.tbDetallar.setMenu(menuDetalles)
      
      self.connect(aPrintR, QtCore.SIGNAL("triggered()"), self.imprimir)
      self.connect(aPrintC, QtCore.SIGNAL("triggered()"), self.imprimirCorte)
      self.connect(aignorar, QtCore.SIGNAL("triggered()"), self.ignorarVentas)
      self.connect(aReimprimir, QtCore.SIGNAL("triggered()"), self.imprimirTicket)            		
      self.connect(aAbrirNota, QtCore.SIGNAL("triggered()"), self.abrirVenta)            		
      #self.connect(aCobrarNota, QtCore.SIGNAL("triggered()"), self.abrirCobrarVenta)            		
      self.connect(aNuevaCompra, QtCore.SIGNAL("triggered()"), self.nuevaCompra)
      self.connect(aEditarCompra, QtCore.SIGNAL("triggered()"), self.editarCompra)   
      self.connect(aEliminarCompra, QtCore.SIGNAL("triggered()"), self.eliminarCompra)   

      
    def actualizar(self):
      	self.setCursor(QtGui.QCursor(3))
	self.cambiarFecha()
	self.tablarVentas()
	self.parcial()
	self.setCursor(QtGui.QCursor(0))
	
    def graficar(self):
	w=self.stackReportes.width()
	h=self.stackReportes.height()
	chart=Chart(self.parent,w-20,h-40)
	inicio=str(self.deFrom.date().toString('yyyy-MM-dd'))
	fin=str(self.deTo.date().toString('yyyy-MM-dd'))
	
	if inicio==fin:
	  chart.hoursPlot(self.periodo)	
	  chart.setTitle("Ventas horas del dia")	    
	else:
	  dformat="%Y-%m-%d"
	  i=datetime.strptime(inicio,dformat)
	  f=datetime.strptime(fin,dformat)
	  ndays=(f-i).days
	  if ndays in range(7):
	    chart.xPlot('%w','%w',self.periodo)
	    chart.setTitle("Ventas por dias de la semana")	    
	  elif ndays in range(7,15): #Si son de 1 a 15 dias grafica por dias
	    chart.dayPlot(self.periodo)
	    chart.setTitle("Ventas por dias")	    
	  elif ndays in range(15,60):
	    chart.xPlot('%U/%M','%U',self.periodo) 
	    chart.setTitle("Ventas por semanas")
	  elif ndays in range(60,365):
	    chart.xPlot('%m','%m',self.periodo) 
	    chart.setTitle("Ventas por meses")
	  else:
	    chart.xPlot('%m.%y','%m%y',self.periodo)
	    chart.setTitle("Ventas por meses")
	    
	self.grafica.setScene(chart.escena)
	self.chart=chart
	self.stackReportes.setCurrentIndex(1)

    def verReportes(self):
      self.stackReportes.setCurrentIndex(0)
      
    def verGraficas(self):
      #### Deprecated
	self.graficar()


    def cambiarFecha(self,date=False):
	if date!=False:
	  self.fecha="'%s'"%date.toString('yyyy-MM-dd')
	inicio=str(self.deFrom.date().toString('yyyy-MM-dd'))
	fin=str(self.deTo.date().toString('yyyy-MM-dd'))
	if (inicio==fin):
	  self.periodo=" date(fecha)='%s'"%inicio
	  self.bCorteT.setEnabled(True)
	else:
	  self.periodo=" date(fecha) BETWEEN '%s' and  '%s' "%(inicio,fin)
	  self.bCorteT.setEnabled(False)
	#self.actualizar()
	
    def detallar(self):
      	self.setCursor(QtGui.QCursor(3))
	ventas=RVentas(self.parent,self.periodo)
	(lista,resumen)=ventas.resumir(self.periodo,self.caja)
	movimientos=libutil.listaHtml(lista,'Entradas y salidas',['Concepto','Monto'],'#fff','#1162A7',14,anchos=[70,30])
	tventas=ventas.detallarVentas(caja=self.caja)+"<br/>"
	tcajas=ventas.detallarCajas(caja=self.caja)
	tusuarios=ventas.detallarUsuarios(caja=self.caja)
	tdeptos=ventas.detallarDeptos(caja=self.caja)
	tprods=ventas.detallarProds(caja=self.caja)
	tabla2=libutil.listaHtml([[tventas+tusuarios+tcajas,movimientos+tdeptos]],titulo="Resumen de movimientos",color='#fff',fondo='#1162A7',opc="000",anchos=[50,50])
	self.html=tabla2+tprods
	self.tbRExportar.setEnabled(False)
	self.teResumen.setHtml(tabla2+tprods)	
	self.stackReportes.setCurrentIndex(2)
	self.setCursor(QtGui.QCursor(0))
	
    def detallarProds(self):
      self.setCursor(QtGui.QCursor(3))
      vs=RVentas(self.parent,self.periodo)
      num=QtGui.QInputDialog.getInt(self, self.parent.tr("Limite de articulos"),self.parent.tr("Limite de articulos a mostrar:"))
      lista=vs.detallarProdsVendidos(limit=num[0])
      #tabla=libutil.listaHtml(lista[2:],lista[0],lista[1],'#fff',"#239AB1", 12,anchos=[35,10,15,10,10,10,10]) 
      #self.teResumen.setHtml(tabla)
      self.moventas.setVector(lista[2:],lista[1])
      self.tVentas.resizeColumnsToContents()
      #self.html=tabla
      self.lista=lista
      self.listing=True
      #self.tbRExportar.setEnabled(True)
      self.stackReportes.setCurrentIndex(0)
      self.setCursor(QtGui.QCursor(0))	
      
    def detallarMovimientos(self):
      """Escribe una tabla en html de los movimientos de entradas y salidas """
      self.setCursor(QtGui.QCursor(3))
      ventas=RVentas(self.parent,self.periodo)
      head="id_movimiento,usuarios.nombre,cajas.nombre,detalle,tipo, monto,fecha"
      lista=list(Movimiento(self.parent.conexion).buscar(head,self.periodo+" order by tipo"))
      tabla=libutil.listaHtml(lista,'Tabla de movimientos de efectivo',
	"#,Usuario,Caja,Detalle,Tipo, Monto,Fecha".split(','),'#fff','#1162A7',10,opc="110",anchos=[5,15,15,22,13,15,15])
      self.teResumen.setHtml(tabla)
      lista.insert(0,"#,Usuario,Caja,Detalle,Tipo, Monto,Fecha".split(','))
      lista.insert(0,"Movimientos de efectivo")
      self.lista=lista
      self.html=tabla
      self.tbRExportar.setEnabled(True)
      self.stackReportes.setCurrentIndex(2)
      self.setCursor(QtGui.QCursor(0))	
      
    def detallarFamilia(self):
      	app=Selector(self,"Familia",'familias','id,nombre',"Id,Nombre","`nombre` like '%{0}%' order by nombre ")
	done=app.exec_()
	if done==1:
	  familia=app.retorno[0]
	  self.setCursor(QtGui.QCursor(3))
	  ventas=RVentas(self.parent,self.periodo)
	  lista=ventas.detallarFamilia(ide=familia[0],nombre=familia[1],caja=self.caja)
	  tabla=libutil.listaHtml(lista[2:],lista[0],lista[1],'#fff',"#239AB1", 12,anchos=[35,10,15,10,10,10,10]) 
	  self.teResumen.setHtml(tabla)
	  self.lista=lista
	  self.html=tabla
	  self.tbRExportar.setEnabled(True)
	  self.stackReportes.setCurrentIndex(2)
	  self.setCursor(QtGui.QCursor(0))	
	  

    def tablarVentas(self): 
      self.listing=False
      if self.cbListas.currentIndex()==0:
	head=('Id','Usuario','Cliente','Id Caja','Hora',"Formato","Estado",'Total')
	sql="""select n.id,u.usuario, clientes.nombre,caja,time(fecha),ELT(n.tipo+1,'Nota','Factura') ,
	ELT(status+1,'Sin pagar','Pagadas','En credito'), Total  from notas as n,usuarios as u, clientes 
	where {periodo} and {caja} and n.usuario=u.id_usuario and cliente=clientes.id order by n.id; """.format(periodo=self.periodo,caja=self.caja)
	#print sql
      elif self.cbListas.currentIndex()==1:
	head=('Id','Fecha','Comprador','Total')
	sql="select id, fecha, nombre, total  from compras,usuarios where id_usuario=comprador and {periodo}  order by id; ".format(periodo=self.periodo)	
      elif self.cbListas.currentIndex()==2:
	head=('Num','Usuario','Caja','Detalle','Tipo','Monto','Fecha')
	sql="select id_movimiento, usuarios.nombre, cajas.nombre, detalle, tipo, monto, fecha  from movimientos as m,usuarios, cajas where tipo='gasto' and id_usuario=m.usuario and cajas.num_caja=caja and  {periodo} and {caja} order by fecha; ".format(periodo=self.periodo,caja=self.caja)	
      elif self.cbListas.currentIndex()==3:
	head=('Num','Usuario','Caja','Detalle','Tipo','Monto','Fecha')
	sql="select id_movimiento, usuarios.nombre, cajas.nombre, detalle, tipo, monto, fecha  from movimientos as m,usuarios, cajas where tipo='retiro' and id_usuario=m.usuario and cajas.num_caja=caja and  {periodo} and {caja} order by fecha; ".format(periodo=self.periodo,caja=self.caja)	
      elif self.cbListas.currentIndex()==4:
	head=('Num','Usuario','Caja','Detalle','Tipo','Monto','Fecha')
	sql="select id_movimiento, usuarios.nombre, cajas.nombre, detalle, tipo, monto, fecha  from movimientos as m,usuarios, cajas where tipo='deposito' and id_usuario=m.usuario and cajas.num_caja=caja and {periodo} and {caja} order by fecha; ".format(periodo=self.periodo,caja=self.caja)	
      else:
	return False
      #print sql
      self.moventas.query(sql,head)      
      self.tVentas.resizeColumnsToContents()  
	
	
    def parcial(self):
	vs=RVentas(self.parent,self.periodo)
	tabla=vs.detallarVentas(caja=self.caja)
	self.teDetalles.setText(tabla)

	
    def resumir(self,fecha='CURDATE()'):
	rvs=RVentas(self.parent,fecha)
	(lista,resumen)=rvs.resumir("date(fecha)={0}".format(fecha),self.caja)
	self.efectivo=resumen['efectivo']
	tabla=libutil.listaHtml(lista,'Tabla de movimientos de dinero',['Concepto','Monto'],'#333','#E2E6E7',14,anchos=[70,30])
	return tabla

    def corte(self):
	msgBox=QtGui.QMessageBox()
	msgBox.setWindowTitle("Corte de ventas.")
	#self.cursor.execute("SELECT count(C.id) from notas as N,notas_cobradas as C where C.nota=N.id and date(N.fecha)="+self.fecha)
	#nc=int(self.cursor.fetchone()[0])
	#if nc==0:
	self.curser.execute("SELECT id from notas where tipo=0 and status=1 and %s;"%self.periodo)
	notas=self.curser.fetchall()
	if notas!=None:
	    notas=dicursor(self.curser,notas)
	    for item in notas:
	      try:
		self.cursor.execute("INSERT INTO notas_cobradas VALUES(NULL, %s)"%item['id'])
	      except:
		print "Error, nota ",item['id']
	try:
	  self.parcial()
	  self.cursor.execute("INSERT INTO ventas VALUES(%s,(select sum(total) from notas where date(fecha)=%s),0,(select sum(total) from notas_cobradas,notas where nota=notas.id and date(fecha)=%s), %s  )"%(self.fecha,self.fecha,self.fecha,self.efectivo))
	except MySQLdb.Error, e:
	  if (e.args[0]==1062):#Si hay un error por duplicacion de fila solo se actualiza
	    try:
	      self.cursor.execute("UPDATE ventas set total=(select sum(total) from notas where %s) where %s"%(self.periodo,self.periodo))
	    except MySQLdb.Error, e:
	      msgBox.setText("Error al guardar valores.")
	      print e
	    else:
	      msgBox.setText("Se ha realizado el corte caja.")
	      msgBox.setInformativeText("Desea imprimir el reporte?")
	  else:
	    print e
	else:
	    msgBox.setText("Se ha realizado el corte caja.")
	    msgBox.setInformativeText("Desea imprimir el reporte?")

      #else:
	#msgBox.setText("El Corte ya se habia realizado, solo se imprimira...")
	msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
	if msgBox.exec_()==QtGui.QMessageBox.Ok:
	  self.imprimirCorte() 
	  
    def imprimirTicket(self):
	refs=[]
	lastrow=-1
	ref=self.moventas.getCell(self.tVentas.selectedIndexes()[0],0)
	nota=self.parent.abrirNota(ref)
	if nota!=False:
	  self.parent.imprimirTicket()
	#for ref in refs:

    def abrirNota(self,ide):
	try:
	  self.curser.execute("select cliente, nombre, rfc, C.tipo, date_format(fecha,'%d-%m-%Y') as fecha, total  from notas as N, clientes as C where  N.`id`="+str(ide)+"  AND C.id=N.cliente and N.tipo=0;")
	  nota=self.curser.fetchone()
	  self.curser.execute("SELECT ref,`descripcion`,precio,cantidad,mayoreo, minimo, V.total as st FROM notas as N, vendidos as V, productos as P, familias as F where V.venta=N.id AND P.ref=V.producto AND familia=F.id AND  N.id="+str(ide)+" ;")
	  productos=self.curser.fetchall()	  
	except MySQLdb.Error, e:
	   print e
	   return False
	else:
	  if productos!=None:
	    prods=''
	    tags={}	    
	    try:
	      self.cursor.execute('select nc.id from notas_cobradas as nc, notas where nc.nota='+str(ide)+' and nc.nota=notas.id')
	      nc=self.cursor.fetchone() 
	    except MySQLdb.Error, e:
	      pass
	    else:
	      if nc!=None:
		tags['<nota/>']=str(nc[0])
	      else:
		tags['<nota/>']=str(ide)
	    for prod in productos:	       
		  prods+=str(prod['desc'])+" \n"+str(prod['cantidad'])+"  x  "+str(prod['precio'])+"\t\t\t  "+str(prod['st'])+'\n'
	    tags['<productos/>']=prods
	    tags['<subtotal/>']=str(nota['total'])
	    tags['<impuestos/>']='16%'#self.cfg.get('empresa','impuestos')+"%"
	    tags['<descuento/>']='0.0'
	    tags['<total/>']=str(nota['total'])
	    tags['<fecha/>']=str(nota['fecha'])
	    tags['<tletra>']=str(self.parent.nletra(nota['total']))
	    #tags['<usuario/>']=self.sesion['usuario']['name']
	    return tags
	  else:
	    return False
	    
    def imprimirCorte(self):
	#try:
	  sql="select C.id,N.total  from notas_cobradas as C, notas as N where %s and C.nota=N.id order by C.id; "%self.periodo
	  self.cursor.execute(sql)
	  result = self.cursor.fetchall()
	  notas=' Numero de venta    Total\n'
	  notas+='---------------------------------\n'
	  tax="---------------------------------\nTotal separado por tipos de impuestos.\nImpuesto  |  Total en ventas\n"
	  suma=i=0
	  for item in result:
	    notas+="%s  %s \n"%(item[0],item[1])
	    suma+=float(item[1])
	    i+=1
	  self.cursor.execute("SELECT sum(V.total), I.nombre from vendidos as V, notas_cobradas as C,notas as N, productos as P, impuestos as I WHERE V.venta=N.id  AND V.producto=P.ref  AND N.id=C.nota AND P.impuesto=I.id  AND date(N.fecha)="+self.fecha+"  group by P.impuesto;")
	  qry=self.cursor.fetchall()
	  for item in qry:
	      tax+="%s   <h2>$%s</h2> \n"%(item[1],item[0])
	  tax+="---------------------------------\n"
	  f=open(os.path.join(self.parent.home,'corte.xml'),'r+')
	  ticket=f.read()
	  f.close()
	  tags=self.parent.ticketDriver.etiquetas
	  tags['<fecha/>']=str(self.fecha)
	  tags['<notas/>']=notas
	  tags['<total/>']=str(round(suma,1))
	  tags['<num/>']=str(i)	  
	  tags['<impuestos/>']=tax
	  for key in self.parent.modulos['config'].modulos['empresa']:
	      try: 
		tags['<'+key+'/>']=self.parent.cfg.get('empresa',key)
	      except:
		pass
	  for key,item in tags.iteritems():
	      ticket=ticket.replace(key,item)
	  for key,item in tags.iteritems():
	      ticket=ticket.replace(key,item)
	  if sys.platform == 'linux2':
	    f=tempfile.NamedTemporaryFile(delete=False)
	  else:
	    f=open(os.path.normpath(os.path.join(self.parent.home,"tmp.txt")),"w+")
	  f.write(ticket)
	  f.close()
	  self.parent.imprimir(f,self.parent.cfg.get('ticket','impresora'))

    def mostrarResumen(self,index):
      if self.cbListas.currentIndex()==0:
	dlg=VisorVenta(self.parent,self.moventas.getCell(index,0))
	dlg.exec_()
      elif self.cbListas.currentIndex()==1:
	self.editarCompra()

    def guardarGrafica(self):
      File = QtGui.QFileDialog.getSaveFileName (self,"Guardar imagen",self.parent.home+'/grafica.png',self.tr("Imagenes (*.png)"))
      if File != '':
	self.chart.toPixmap().save(File)
      
    def imprimirGrafica(self):

	printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
	printer.setPaperSize(QtGui.QPrinter.Letter)   
	printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
	printer.setOutputFileName(self.parent.home+"/Grafica.pdf")
	prev=QtGui.QPrintDialog(printer,self.parent)
	if prev.exec_()==QtGui.QDialog.Accepted:
		paint=QtGui.QPainter()
		paint.begin(printer)
		self.escena.render(paint)
		paint.end()

    def fechas(self):
      inicio=str(self.deFrom.date().toString('dd-MM-yy'))
      fin=str(self.deTo.date().toString('dd-MM-yy'))
      if inicio==fin:
	periodo=inicio
      else:
	periodo="{0}_{1}".format(inicio,fin)
      return periodo
    
    def imprimir(self):
      if not self.html:
	self.detallar()      
      inicio=str(self.deFrom.date().toString('dd MMMM.yy'))
      fin=str(self.deTo.date().toString('dd MMMM.yy'))
      if inicio==fin:
	periodo=inicio
      else:
	periodo="{0} al {1}".format(inicio,fin)
      head="""<h2 align="center">Reporte de ventas</h2><center><b>Del {periodo}</b></center>""".format(periodo=periodo)
      printa(head+self.html,titulo="Reporte de ventas {periodo}".format(periodo=periodo),orientacion=0)
      self.html=False	
	
    def ignorarVentas(self):
	refs=libutil.seleccionar(self.tVentas, self.moventas)
	for ref in refs:
	  self.cursor.execute("update notas set status=0 where id="+ref)
	self.tablarVentas()
	
    def abrirVenta(self):
      keys=libutil.seleccionar(self.tVentas, self.moventas)
      self.parent.abrirNota(keys[0])
      self.parent.insert()
      
    def abrirCobrarVenta(self):
      ide=str(self.tVentas.selectedIndexes()[0].data().toString())
      self.parent.abrirNota(ide)
      self.parent.modulos["cventa"].ver()
      self.tablarVentas()

      
    def nuevaCompra(self):
      self.parent.nuevaCompra()
      self.parent.insert()


      
    def editarCompra(self):
      keys=libutil.seleccionar(self.tVentas, self.moventas)
      self.parent.abrirCompra(keys[0])
      self.parent.insert()
    
    def eliminarCompra(self):
      keys=libutil.seleccionar(self.tVentas, self.moventas)
      ret=self.parent.eliminarCompra(keys[0])
      if ret!=True:
	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Error al eliminar","La compra no fue eliminada.",QtGui.QMessageBox.Close,self)
      else:
	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Eliminacion correcta","Se ha eliminado la compra.",QtGui.QMessageBox.Close,self)
	self.tablarVentas()
      msgBox.exec_()  
    
    def getEntidadMovimiento(self):
      if self.cbListas.currentIndex()==2:
	entidad=('gasto',Gasto)
      elif self.cbListas.currentIndex()==3:
	entidad=('retiro',Retiro)
      elif self.cbListas.currentIndex()==4:
	entidad=('deposito',Deposito)
      return entidad
	
    def agregar(self): 
      entidad=self.getEntidadMovimiento()
      ag=AgregaGasto(self.parent,self.parent.sesion['usuario']['id_usuario'],entidad[0])
      if ag.exec_()>0:
	self.tablarVentas()
	self.parcial()       
    
    def remover(self):
	entidad=self.getEntidadMovimiento()
	msgBox=QMessageBox(QMessageBox.Question,"Eliminar movimiento(s)",
	"Confirme para eliminar los {mov}(s) seleccionado(s)".format(mov=entidad[0]),QMessageBox.Yes|QMessageBox.No,self.parent)
	ret=msgBox.exec_()
	if ret==QMessageBox.Yes:
	  obj=entidad[1](self.parent.conexion)
	  if obj.eliminar(','.join(map(str,libutil.seleccionar(self.tVentas, self.moventas)[0]))):
	    self.tablarVentas()
	    self.parcial()      
	      
    def ocm(self, point):
      if self.listing:
	return False
      else:
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         if self.cbListas.currentIndex()==0:
	  self.menuVentas.exec_(self.tVentas.mapToGlobal(point) )	
         elif self.cbListas.currentIndex()==1:
	  self.menuCompras.exec_(self.tVentas.mapToGlobal(point) )		  
         elif self.cbListas.currentIndex() in (2,3,4):
	  self.menuGastos.exec_(self.tVentas.mapToGlobal(point) )
	  
    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos

    def setCaja(self,index):
      if index==0:
	self.caja=" 1 "
      else:
	self.caja=" caja={0} ".format(str(self.cbCaja.itemData(index).toString()))
    
    def facturar(self):
	ide=str(self.tVentas.selectedIndexes()[0].data().toString())
	venta=Venta(self.parent.conexion)
	venta.cambiarTipo(ide,1)
	F=Factura(self.parent, ide)
	F.imprimir()
	self.actualizar()
	
    def cobrar(self):
	notas=libutil.seleccionar(self.tVentas, self.moventas)
	status=libutil.seleccionar(self.tVentas, self.moventas,6)
	if 'Sin pagar' in status:
	  cobra=Cobrador(conexion=self.parent.conexion,ventas=notas,usuario=self.parent.sesion['usuario']['id_usuario'],
	  cliente=self.parent.cliente['id'],caja=self.parent.caja)
	  if cobra.exec_()==QtGui.QDialog.Accepted:
	    self.actualizar()
	    
    def selecColor(self):
	col = QtGui.QColorDialog.getColor()
        if col.isValid():
	  col.setAlpha(100)
	  self.chart.changeColor(col)
	  
    def exportar(self):
      if self.stackReportes.currentIndex()==1 or self.listing:
	if self.lista:
	  lista=self.lista
      else:
	  lista=list(self.moventas.getVector())
	  lista.insert(0,['Id','Usuario','Cliente','Id Caja','Hora',"Formato","Estado",'Total'])
	  lista.insert(0,str(self.cbListas.currentText()))
      File = QtGui.QFileDialog.getSaveFileName (self,"Exportar como hoja de calculo",join(expanduser('~'),lista[0]+" "+self.fechas()+'.xls'),self.tr("Hojas de calculo (*.xls)"))
      if File!='' and len(lista)>3:
	#print self.lista
	libutil.toxls(lista[2:],File,lista[1],lista[0]+" "+self.fechas())	
	
    def eliminarVentas(self):
	selected=[item.data().toInt()[0] for item in self.tVentas.selectionModel().selectedRows(0)]
	msgBox=QMessageBox(QMessageBox.Question,"Eliminar ventas(s)",
	"Esta operacion no se puede deshacer. \nContinuar?",QMessageBox.Yes|QMessageBox.No,self.parent)
	if msgBox.exec_()==QMessageBox.Yes:
	  venta=Venta(self.parent.conexion)
	  venta.eliminarMuchas(selected)
	  self.actualizar()
	  
    #def exportarListado(self):
	#lista=self.moventas.getVector()
	#File = QtGui.QFileDialog.getSaveFileName (self,"Exportar como hoja de calculo",
	#join(expanduser('~'),'Listado.xls'),
	#self.tr("Hojas de calculo (*.xls)"))
	#if File!='':
	  ##print self.lista
	  #libutil.toxls(self.lista[2:],File,self.lista[1],"")

    #def export(self):
      #relationships = relationshiplist()
    ## Make a new document tree - this is the main part of a Word document
      #document = newdocument()
      ## This xpath location is where most interesting content lives
      #body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]
      

		  
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = modulo(app,1)
    aw.show()
    sys.exit(app.exec_())
	
