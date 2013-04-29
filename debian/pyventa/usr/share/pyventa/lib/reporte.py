# -*- coding: utf-8 -*-
import sys,os,random
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from lib.utileria import Documento, MyTableModel
from ui.ui_corte import Ui_Form
import  datetime
import MySQLdb,  tempfile
from ui.dl_resumen_venta import Ui_Dialog 
from lib.clases import Gasto
from lib import libutil
from lib.librepo import Chart
from lib.qmodelotablasql import QModeloTablaSql

#from chart import chart
class Reportes(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.curser=parent.curser
		self.cursor=parent.cursor
		self.datos={'nombre':"Reportes",'descripcion':"Muestra el todo lo relacionado con ventas.",'version':"0.05",'id':id,'nivel':3}
		self.id=id
		self.parent=parent
		self.moventas=None
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
        	self.connect(self.tbGraficas, QtCore.SIGNAL("clicked()"), self.verGraficas)
		#self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),lambda: parent.aut(self.id,2) )
        	#self.connect(self.bvShowinfo, QtCore.SIGNAL("clicked()"), self.weekPlot)
        	self.connect(self.tVentas, QtCore.SIGNAL("activated(const QModelIndex&)"), self.mostrarResumen)
        	self.connect(self.cbCaja, QtCore.SIGNAL("activated (int)"), self.setCaja)
        	self.connect(self.cbListas, QtCore.SIGNAL("currentIndexChanged(int )"), self.tablarVentas)
        	self.connect(self.pbListaVentas, QtCore.SIGNAL("clicked()"),  self.actualizar)
        	self.connect(self.bCorteT, QtCore.SIGNAL("clicked()"), self.corte)
        	self.connect(self.tbListar, QtCore.SIGNAL("clicked()"), lambda:self.stackReportes.setCurrentIndex(0))
        	#self.connect(self.bCorteP, QtCore.SIGNAL("clicked()"), self.parcial)
        	#self.connect(self.rbHoy, QtCore.SIGNAL("clicked()"), self.dayPlot)
        	#self.connect(self.rbSemana, QtCore.SIGNAL("clicked()"), self.weekPlot)
        	#self.connect(self.rbMes, QtCore.SIGNAL("clicked()"), self.monthPlot)
        	#self.connect(self.rbAnio, QtCore.SIGNAL("clicked()"), self.yearPlot)
        	#self.connect(self.tbPrint, QtCore.SIGNAL("clicked()"), self.imprimirGrafica)
        	#self.connect(self.tbImprimir, QtCore.SIGNAL("clicked()"), self.imprimir)
        	self.connect(self.tbImprimir, QtCore.SIGNAL("clicked()"), self.tbImprimir.showMenu)
		self.tVentas.setContextMenuPolicy(3)
		self.connect(self.tVentas,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
        	self.connect(self.deFrom, QtCore.SIGNAL("dateChanged ( const QDate)"), self.cambiarFecha)
        	self.connect(self.deTo, QtCore.SIGNAL("dateChanged ( const QDate)"), self.cambiarFecha)
		self.makeMenu()
		self.fecha='CURDATE()'
		#self.splitter.moveSplitter(300,0)
        	self.deCorte.setDate(QtCore.QDate.currentDate())
        	self.deFrom.setDate(QtCore.QDate.currentDate())  
        	self.deTo.setDate(QtCore.QDate.currentDate())  
		self.tbImprimir.setMenu(self.menuImpresion)
		modelo=QModeloTablaSql(self.parent.cursor,self)
		self.parent.cursor.execute("SELECT num_caja, nombre from cajas")
		res=self.parent.cursor.fetchall()
		self.cbCaja.addItem("Todas",0)
		for c in res:
		  self.cbCaja.addItem(c[1],c[0])
		#self.cbCaja.setModel(modelo)
		#self.cbCaja.setModelColumn (1)
		
		self.caja="TRUE"

        	#self.graf=QWidget(self)
       		#self.vlVentas1.addWidget(self.graf)
    def inicia(self):
      if self.parent.aut(self.datos['nivel'])>0:
	  self.parent.stack.setCurrentIndex(self.datos['id'])
	  self.actualizar()
	  self.verReportes()

    def makeMenu(self):
      self.menuVentas = QtGui.QMenu(self)
      self.menuCompras = QtGui.QMenu(self)
      self.menuImpresion = QtGui.QMenu(self)
      self.menuGastos = QtGui.QMenu(self)
      #Menu contextual de tipos de impresion
      aPrintR=self.menuImpresion.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/application-pdf.png")," Resumen (PDF) ")
      aPrintR.setIconVisibleInMenu(True)
      aPrintC=self.menuImpresion.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/receipt.png"),"Corte total (Ticket)")
      aPrintC.setIconVisibleInMenu(True)	
      #Menu contextual del listado de ventas
      aAbrirNota=self.menuVentas.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/edit32.png")," Abrir venta ")
      aAbrirNota.setIconVisibleInMenu(True)
      aignorar=self.menuVentas.addAction(QtGui.QIcon("/usr/share/pyventa/images/16/block_16.png")," Ignorar ")
      aignorar.setIconVisibleInMenu(True)
      aCobrarNota=self.menuVentas.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/Lightning-32.png")," Liquidar ")
      aCobrarNota.setIconVisibleInMenu(True)      
      aReimprimir=self.menuVentas.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/receipt.png")," Reimprimir copia ")
      aReimprimir.setIconVisibleInMenu(True)
      #Menu contextual del listado de ventas
      aNuevaCompra=self.menuCompras.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/Add-32.png")," Nueva compra")
      aNuevaCompra.setIconVisibleInMenu(True)
      aEditarCompra=self.menuCompras.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/edit32.png")," Editar compra")
      aEditarCompra.setIconVisibleInMenu(True)  
      aEliminarCompra=self.menuCompras.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/list-remove.png")," Eliminar compra")
      aEliminarCompra.setIconVisibleInMenu(True)
      
      aNuevoGasto=self.menuGastos.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/Add-32.png")," Agregar gasto")
      aNuevoGasto.setIconVisibleInMenu(True)
      aEliminarGasto=self.menuGastos.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/list-remove.png")," Eliminar gasto")
      aEliminarGasto.setIconVisibleInMenu(True)
      
      self.connect(aPrintR, QtCore.SIGNAL("triggered()"), self.imprimir)
      self.connect(aPrintC, QtCore.SIGNAL("triggered()"), self.imprimirCorte)
      self.connect(aignorar, QtCore.SIGNAL("triggered()"), self.ignorarVentas)
      self.connect(aReimprimir, QtCore.SIGNAL("triggered()"), self.imprimirTicket)            		
      self.connect(aAbrirNota, QtCore.SIGNAL("triggered()"), self.abrirVenta)            		
      self.connect(aCobrarNota, QtCore.SIGNAL("triggered()"), self.abrirCobrarVenta)            		
      self.connect(aNuevaCompra, QtCore.SIGNAL("triggered()"), self.nuevaCompra)
      self.connect(aEditarCompra, QtCore.SIGNAL("triggered()"), self.editarCompra)   
      self.connect(aEliminarCompra, QtCore.SIGNAL("triggered()"), self.eliminarCompra)   
      self.connect(aNuevoGasto, QtCore.SIGNAL("triggered()"), self.agregarGasto)   
      self.connect(aEliminarGasto, QtCore.SIGNAL("triggered()"), self.eliminarGasto)   
      
    def graficar(self):
	  inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
	  fin=str(self.deHasta.date().toString('yyyy-MM-dd'))
	  #escalas=['%H','%j',%d,'%u','%m','%Y']

	  rango=self.getRango(inicio,fin,str(self.cbEscala.itemData(self.cbEscala.currentIndex()).toString()))
	  #self.graf=chart(self.cbEscala.currentText(),'Total',rango)
	  #self.graf.show()
	  self.setGrafica(rango)

    def verReportes(self):
      self.stackReportes.setCurrentIndex(0)
      
    def verGraficas(self):
      self.stackReportes.setCurrentIndex(1)    
      self.dayPlot(self.periodo)

      
    def setGrafica(self,datos):
	if len(datos[0])>0:
    	  self.escena=QtGui.QGraphicsScene()
    	  self.escena.setBackgroundBrush(QtGui.QColor('#fff'))
    	  pen=QtGui.QPen()
    	  pen.setWidth(2)
    	  pen.setColor(QtGui.QColor('#0C4361'))
    	  rBrush=QtGui.QBrush(QtGui.QColor(101, 163, 255, 250))
    	  blueb=QtGui.QBrush(QtGui.QColor(0, 118, 117, 50))
    	  grid=QtGui.QPen(QtGui.QColor("#999"),1,Qt.DashLine)
    	  top=200
    	  alto=self.grafica.height()
   	  ancho=(self.grafica.width()-60)/len(datos[1])
	  maxim=max(datos[0])
	  Y=alto-50
	  axe=ancho*len(datos[1])+85 #acho del eje x

	  self.escena.addLine(70,0,70,Y,pen)
	  self.escena.addLine(0,Y,axe,Y,pen)

  	  for i in range(5):
	    self.escena.addLine(60,Y*i*.25,self.grafica.width()-20,Y*i*.25,grid)
	    text=self.escena.addSimpleText(str(libutil.cifra(round(maxim*i*.25,1))))
	    text.setPos(5,Y-(Y*i*.25))
	    mi=80
	  dm=1 #num de dia
	  for i,val in enumerate(datos[0]):
	    if maxim>0:
	      dm+=1
	      if (int(datos[1][i])==1 or dm>31):
		self.escena.addRect(mi,0,axe-mi,alto-50,QtGui.QPen(QtGui.QColor("#fff")),QtGui.QBrush(QtGui.QColor(20, 110, 170,10)))
		mi=(ancho*i)+85
		dm=1
	      scale=(float(val)/float(maxim))*(alto-50)
	      #self.escena.addRect((ancho*i)+80, (alto-50)-scale,ancho,scale,pen,blueb)
	      if len(datos[0])>10:
		  n=round(len(datos[0])*.05)
	      else:
		  n=1
	      if i>0:
		self.escena.addLine(ax,ay,(ancho*i)+85,alto-50-scale,pen)
	      self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,alto-50-scale,grid)
	      if i%n==0:
		text=self.escena.addSimpleText(str(datos[1][i]))
		text.setPos((ancho*i)+85,alto-35)
		self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,alto-35,grid)

	      ax=(ancho*i)+85
	      ay=alto-50-scale

      
	  self.grafica.setScene(self.escena)
	
	
    def getRango(self,inicio,fin,escala='%j'):
    #recoge dos fechas inicio y fin en formato de cadena "yyyy-MM-dd" y una escala de dias, horas, semanas meses "%j" "%e" "%Y"
    #Devuelve un diccionario con X y Y datos
    	#print "SELECT sum(total), DATE_FORMAT(fecha,'"+escala+"') FROM `notas` where DATE(fecha)>'"+inicio+"' and DATE(fecha)<'"+fin+"' GROUP BY DATE_FORMAT(fecha,'"+escala+"') ORDER BY DATE_FORMAT(fecha,'"+escala+"');"
	self.parent.cursor.execute("SELECT ROUND(sum(total),2), DATE_FORMAT(fecha,'"+escala+"') FROM `notas` where DATE(fecha)>DATE('"+inicio+"') and DATE(fecha)<DATE('"+fin+"') GROUP BY DATE_FORMAT(fecha,'"+escala+"') ORDER BY DATE_FORMAT(fecha,'"+escala+"');")
	datos=self.parent.cursor.fetchall()
	total=[]
	escala=[]
	for fila in datos:
	    total.append(fila[0])
	    escala.append(fila[1])
	    print "%s  %s"%(fila[0],fila[1])
	return [total,escala]

    def weekPlot(self):
	dias=[]
	total=[]
	self.parent.cursor.execute(" SELECT ROUND(sum(total),2) as `total`, DATE_FORMAT(fecha,'%w') as `dia` FROM `notas` where MONTH(fecha)=MONTH(curdate()) and YEAR(fecha)=YEAR(curdate()) and WEEK(fecha)=WEEK(curdate()) GROUP BY DATE_FORMAT(fecha,'%w') ORDER BY DATE_FORMAT(fecha,'%w')")
	datos=self.parent.cursor.fetchall()
	Dias=['Domingo','Lunes','Martes', 'Miercoles','Jueves','Viernes','Sabado']
	for hora in datos:
	    total.append(round(float(hora[0]),1))
	    dias.append(Dias[int(hora[1])])
	data=[total,dias]
       	self.setGrafica(data)

	#self.graf=chart('Dias','total',data)
	#self.graf.show()
	#try: 
	  #self.vlVentas2.removeWidget(self.sc)
	#except:
	    #pass
	#self.sc=grafica(self, dias,total)
	#self.vlVentas2.addWidget(self.sc)

    def dayPlot(self,fecha='DATE(fecha)=curdate()'):
	hours=[]
	total=[]
	sql="SELECT ROUND(sum(total),2) as `total` ,DATE_FORMAT(fecha,'%%d') as `hora` FROM `notas` where %s GROUP BY DATE_FORMAT(fecha,'%%j')"%fecha
	self.parent.cursor.execute(sql)
	#print sql
	datos=self.parent.cursor.fetchall()
	for hora in datos:
	    hours.append(hora[1])
	    total.append(round(float(hora[0]),1))
	data=[total,hours]
       	self.setGrafica(data)


    def yearPlot(self):
	meses=[]
	total=[]
	self.cursor.execute("SELECT ROUND(sum(total),2) as `total`, DATE_FORMAT(fecha,'%m') as `mes` FROM `notas` where  YEAR(`fecha`)=YEAR(curdate()) GROUP BY DATE_FORMAT(fecha,'%m');")
	#self.cursor.execute("SELECT sum(`total`) as `total`, DATE_FORMAT(fecha,'%Y') as `mes` FROM `notas`  GROUP BY DATE_FORMAT(fecha,'%Y');")
	datos=self.cursor.fetchall()
	for mes in datos:
	    meses.append(mes[1])
	    total.append(round(float(mes[0]),1))
	data=[total,meses]
       	self.setGrafica(data)

    def monthPlot(self):
	meses=[]
	total=[]
	#self.cursor.execute("SELECT sum(`total`) as `total`, DATE_FORMAT(fecha,'%m') as `mes` FROM `notas` where  YEAR(`fecha`)=YEAR(curdate()) GROUP BY DATE_FORMAT(fecha,'%m');")
	self.cursor.execute("SELECT ROUND(sum(total),2) as `total`, DATE_FORMAT(fecha,'%d') as `mes` FROM `notas` where  YEAR(`fecha`)=YEAR(curdate()) and MONTH(fecha)=MONTH(curdate()) GROUP BY DATE_FORMAT(fecha,'%d') ORDER BY mes ;")
	datos=self.cursor.fetchall()
	for mes in datos:
	    meses.append(mes[1])
	    total.append(round(float(mes[0]),1))
	data=[total,meses]
       	self.setGrafica(data)


	#self.graf=chart('mes','total',data)
	#self.graf.show()
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
	
    def actualizar(self):
      	self.setCursor(QtGui.QCursor(3))
	self.cambiarFecha()
	self.tablarVentas()
	self.parcial()
	self.setCursor(QtGui.QCursor(0))

    def tablarVentas(self): 
      if self.cbListas.currentIndex()==0:
	head=('Id','Usuario','Cliente','Caja','Hora',"Formato","Estado",'Total')
	sql="select n.id,u.usuario, SUBSTRING(clientes.nombre,1,12),caja,time(fecha),ELT(n.tipo+1, 'Nota','Factura','Devolucion') ,ELT(status+1, 'Pendiente','Pagada','En credito', 'Devolucion'),Total  from notas as n,usuarios as u, clientes where %s and n.usuario=u.id_usuario and cliente=clientes.id order by n.id; "%(self.periodo)
	#print sql
      elif self.cbListas.currentIndex()==1:
	head=('Id','Fecha','Comprador','Total')
	sql="select id, fecha, nombre, total  from compras,usuarios where id_usuario=comprador and %s order by id; "%(self.periodo)	
      elif self.cbListas.currentIndex()==2:
	head=('Num','Usuario','Caja','Fecha','Concepto','Cantidad')
	sql="select num_gasto, nombre, caja, fecha, concepto, cantidad  from gastos as g,usuarios where id_usuario=g.usuario and %s order by fecha; "%self.periodo	
      else:
	return False
	##print sql
      self.moventas=self.parent.entabla(self.tVentas,head,sql)    
      self.tVentas.resizeColumnsToContents()  
	#entabla(self,tabla,header,query,modelo=None)
	
	
    def parcial(self):
	ventas={'realizadas':[],'cobradas':[],'facturas':[],'notas':[],'efectivo':[],'credito':[]}
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s "%self.periodo)
	row=self.cursor.fetchone()
	ventas['realizadas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s and status>0 "%self.periodo)
	row=self.cursor.fetchone()
	ventas['cobradas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s and tipo=1 "%self.periodo)
	row=self.cursor.fetchone()
	ventas['facturas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s and tipo=0 "%self.periodo)
	row=self.cursor.fetchone()
	ventas['notas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s and status=1 "%self.periodo)
	row=self.cursor.fetchone()
	ventas['efectivo']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where %s and status=2 "%self.periodo)
	row=self.cursor.fetchone()
	ventas['credito']=row
	tabla='<h3>Tabla general de ventas</h3>\
<table cellspacing="6px" width="100%%">\
<TR> <Th align=\"left\">Concepto</Th><TH width="12%%" align=\"right\">#</TH><th width="15%%" align=\"right\">Valor</th>	</TR>\
<tr> <TD>Ventas realizadas</TD>	<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
<tr> <TD>Ventas cobradas</TD>	<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
<tr> <TD>Facturas</TD>		<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
<tr> <TD>Notas</TD>		<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
<tr> <TD>En efectivo</TD>	<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
<tr> <TD>En credito</TD>	<TD width="12%%" align=\"right\">%s</TD>       <TD align=\"right\">%s</TD>      </tr>\
</table>'%(ventas['realizadas'][0],ventas['realizadas'][1],ventas['cobradas'][0],ventas['cobradas'][1],ventas['facturas'][0],ventas['facturas'][1],ventas['notas'][0],ventas['notas'][1],ventas['efectivo'][0],ventas['efectivo'][1],ventas['credito'][0],ventas['credito'][1])
	tabla+='<br>%s'%self.resumir(self.fecha);
	self.teDetalles.setText(tabla)
	#self.lVentas.setText(str(row[0]))
	#self.lEfectivo.setText(str(row[2]))
	#self.lTotal.setText(str(row[1]))
	
    def resumir(self,fecha='curdate()'):
	resumen={'ventas':0,'gastos':0,'compras':0, 'inicial':0.0}
	self.cursor.execute("select  IFNULL(ROUND(sum(total),2),0) from notas where date(fecha)="+fecha)
	resumen['ventas']=self.cursor.fetchone()[0]
	self.cursor.execute("select  IFNULL(ROUND(sum(cantidad),2),0) from gastos where date(fecha)="+fecha)
	resumen['gastos']=self.cursor.fetchone()[0]
	self.cursor.execute("select  IFNULL(ROUND(sum(total),2),0) from compras where date(fecha)="+fecha)
	resumen['compras']=self.cursor.fetchone()[0]
	self.cursor.execute("SELECT saldo_inicial from cajas where num_caja=%s and estado=curdate();"%self.parent.caja)
	res=self.cursor.fetchone()
	if res!=None:
	  resumen['inicial']=res[0]	
	#self.cursor.execute("select  IFNULL(inicial,0) from ventas where fecha=curdate() ")
	#row=self.cursor.fetchone()
	#if row!=None:
	  #resumen['inicial']=row[0]
	#else:
	  #resumen['inicial']=0  
	#tabla='<H2>Tabla de movimientos de dinero </H2>\
#<table cellspacing="6px" width="100%%">\
#<TR> <Th align=\"left\">Concepto</Th><TH>Cantidad</TH></TR>\
#<tr> <TD >Ventas:</TD><TD  align=\"right\" >%s		</TD></tr>\
#<tr> <TD>Compras:</TD><TD  align=\"right\" style="color:#F00">%s		</TD></tr>\
#<tr> <TD>Gastos:</TD><TD  align=\"right\" style="color:#F00">%s		</TD></tr>\
#<tr> <TD>Efectivo inicial:</TD><TD  align=\"right\">%s		</TD></tr>\
#<tr> <TD>Efectivo final:</TD><TD  align=\"right\" style="color:#000;font-weight:800;font-size:16px">%s		</TD></tr>\
#</table>'%(resumen['ventas'],resumen['compras'],resumen['gastos'],resumen['inicial'],(resumen['ventas']-resumen['compras']-resumen['gastos']+resumen['inicial']))
	self.efectivo=(resumen['ventas']-resumen['compras']-resumen['gastos']+resumen['inicial'])

	lista=[
	  ['Ventas:',resumen['ventas']],
	  ['Compras:',resumen['compras']],
	  ['Gastos:',resumen['gastos']],
	  ['Efectivo inicial:',resumen['inicial']],
	  ['Efectivo final:',self.efectivo]
	  ]
	tabla=libutil.listaHtml(lista,'Tabla de movimientos de dinero',[[48,'Concepto'],[48,'Monto']],'#333','#E2E6E7',14)
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
	  notas=' Numero de venta  |  Total\n'
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
	      tax+="%s  |  <h2>$%s</h2> \n"%(item[1],item[0])
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
	dlg=resumen(self.parent,self.moventas.getCell(index,0))
	dlg.exec_()
      elif self.cbListas.currentIndex()==1:
	self.editarCompra()

    def imprimirGrafica(self):
	#printer=QtGui.QPrinter(QtGui.QPrinter.PrinterResolution)
	#printer.setResolution(20)
	#printer.setPageMargins ( .5,0,.3,0,QtGui.QPrinter.Inch )
	#printer.setOutputFormat(QtGui.QPrinter.NativeFormat)

	printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
	printer.setPaperSize(QtGui.QPrinter.Letter)   
	printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
	printer.setOutputFileName("/tmp/Grafica.pdf")
	prev=QtGui.QPrintDialog(printer,self.parent)
	if prev.exec_()==QtGui.QDialog.Accepted:
		paint=QtGui.QPainter()
		paint.begin(printer)
		self.escena.render(paint)
		paint.end()
		print "Imprimiendo..."

    def imprimir(self):
	campos={'titulo':'reporte de ventas '+self.parent.fecha,'%fecha%':self.parent.fecha}
	for key in self.parent.modulos['config'].modulos['empresa']:
	    try:
	      campos['%'+key+'%']=self.parent.cfg.get('empresa',key)
	    except:
	      pass	
	    
	self.dayPlot(self.periodo)
	pixMap = QtGui.QPixmap.grabWidget(self.grafica)
	pixMap.save("/tmp/plot.png")
	campos['%detalles%']=str(self.teDetalles.toHtml())+"<img src='/tmp/plot.png'/>"
	doc=Documento(self.parent,os.path.join(self.parent.home,"formas","ventas.xml"),campos)
	doc.addPixmap(pixMap)

	
	
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
      keys=libutil.seleccionar(self.tVentas, self.moventas)
      self.parent.abrirNota(keys[0])
      self.parent.modulos["cventa"].inicia()
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
	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Error al eliminar",str(ret),QtGui.QMessageBox.Close,self)
      else:
	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Eliminacion correcta","Se ha eliminado la compra satisfactoriamente.",QtGui.QMessageBox.Close,self)
	self.tablarVentas()
      msgBox.exec_()  
   
    def agregarGasto(self):
	gasto=Gasto(self.parent)
	if gasto.agregar():
	  self.tablarVentas()
	  self.parcial() 
	      
    def eliminarGasto(self):
	gasto=Gasto(self.parent)
	if gasto.eliminar(libutil.seleccionar(self.tVentas, self.moventas)[0]):
	  self.tablarVentas()
	  self.parcial() 
	      
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         if self.cbListas.currentIndex()==0:
	  self.menuVentas.exec_(self.tVentas.mapToGlobal(point) )	
         elif self.cbListas.currentIndex()==1:
	  self.menuCompras.exec_(self.tVentas.mapToGlobal(point) )		  
         elif self.cbListas.currentIndex()==2:
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
	self.caja=" true "
      else:
	self.caja=" caja={0} ".format(str(self.cbCaja.itemData(index).toString()))
      print self.caja

	      
class resumen(QtGui.QDialog, Ui_Dialog):
    def __init__(self,parent,id=-1):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.parent=parent
		self.id=id
		tipo=['Nota','Factura']
		status=['Sin pagar','Efectivo','Credito']
		if self.id!=-1:
		  self.parent.cursor.execute("select id,cliente,tipo, status, total from  notas where id="+str(id))
		  nota=self.parent.cursor.fetchone()
		  self.lbResumen.setText("<b>Venta:</b> %s    <b>Cliente:</b> %s <br><b>Tipo de venta:</b> %s    <b>Forma de pago:</b> %s <br> <h2>Total: %s </h2>"%(nota[0],nota[1],tipo[int(nota[2])],status[int(nota[3])],nota[4]))
		  head=['ref','`Descripcion`','Cantidad','Precio','Total']
		  col=','.join(head)
		  sql="select "+col+" from productos,vendidos where ref=producto and venta="+str(id)
		  self.parent.tabular(self.twProductos,sql,head)
		  
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = modulo(app,1)
    aw.show()
    sys.exit(app.exec_())
	
