# -*- coding: utf-8 -*-
import sys,os
from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import QLocale 
from ui.ui_ventas import Ui_Form
from ui.ui_resumen import Ui_Form as Display
from lib.utileria import Documento
from lib.clases import Gasto
from lib import libutil
from lib.librepo import Ventas, Chart
import  datetime
import MySQLdb

class Cajas(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.datos={'nombre':"Ventas",'descripcion':"Gestion de ventas.",'version':"0.04",'id':id,'nivel':3}
		self.id=id
		self.action = QtGui.QAction(self)
		self.action.setObjectName(self.datos['nombre']+str(id))
		#self.action.setShortcut("F4")
		self.parent=parent
		self.curser=parent.curser
		self.cursor=parent.cursor
		icon28 = QtGui.QIcon()
		icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/sales.png"), 0, QtGui.QIcon.Off)
		icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/sales.png"), 2, QtGui.QIcon.Off)
		self.action.setIcon(icon28)
		self.action.setIconVisibleInMenu(True)
		self.action.setText(self.datos['nombre'])
		self.agasto=QtGui.QAction(self)
		self.agasto.setIcon(icon28)
		self.agasto.setIconVisibleInMenu(True)
		self.agasto.setText("Registrar gasto")
		self.agasto.setShortcut("Ctrl+H")
        	self.deDesde.setDate(QtCore.QDate.currentDate())
        	self.deHasta.setDate(QtCore.QDate.currentDate())		
		#self.connect(self.action, QtCore.SIGNAL("triggered()"), self.iniciar )
		self.connect(self.agasto, QtCore.SIGNAL("triggered()"), self.agregarGasto)
		self.connect(self.tboImprimir, QtCore.SIGNAL("clicked()"), self.imprimir)
		#self.connect(self.agasto, QtCore.SIGNAL("clicked()"), self.agregarGasto)
		self.connect(self.tbAgregar, QtCore.SIGNAL("clicked()"), self.agregarGasto)
		self.connect(self.pbVerResumen, QtCore.SIGNAL("clicked()"),lambda: self.stack.setCurrentIndex(0))
		self.connect(self.pbVerResumen_2, QtCore.SIGNAL("clicked()"),lambda: self.stack.setCurrentIndex(0))
		self.connect(self.action, QtCore.SIGNAL("triggered()"),self.iniciar )
		
		self.connect(self.pbVerDetallada,QtCore.SIGNAL("clicked()"), self.detallarGastos)
		self.connect(self.pbVerEnDetallada,QtCore.SIGNAL("clicked()"), self.detallarEntradas)
		#self.connect(self.tboHome,QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(0))
		self.connect(self.tboDetalles,QtCore.SIGNAL("clicked()"), self.detallarEntradas)
		self.connect(self.tboInicial, QtCore.SIGNAL("clicked()"), self.inicial)
		self.connect(self.tboActualizar, QtCore.SIGNAL("clicked()"), self.actualizar)
		self.parent.menuEdicion.addAction(self.agasto)
		self.tmp={'notas':[],'clientes':[],'total':0}
		self.tablas=[self.teDetalles,self.teDetalles_2,self.teDetalles_3]
		self.cliente=0
		#inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
		self.periodo=" date(fecha)=CURDATE()  "

    def iniciar(self):
      if self.parent.aut(self.datos['nivel'])>0:
	  self.parent.stack.setCurrentIndex(self.datos['id'])
	  self.setCursor(QtGui.QCursor(16))
	  self.entradas()
	  self.salidas()
	  self.resumir()
	  self.setCursor(QtGui.QCursor(0))
      
    def agregarGasto(self):
	gasto=Gasto(self.parent)
	if gasto.agregar():
	  self.salidas()
	  self.resumir()
	      
    def actualizar(self):
	self.setCursor(QtGui.QCursor(3))
	inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
	fin=str(self.deHasta.date().toString('yyyy-MM-dd'))
	if (inicio==fin):
	  self.periodo=" date(fecha)='%s'"%inicio
	else:
	  self.periodo=" date(fecha) BETWEEN '%s' and  '%s' "%(inicio,fin)
	self.salidas()
	self.resumir()
	self.entradas()
	self.setCursor(QtGui.QCursor(0))	
	
    def entradas(self):
	ventas={'realizadas':[],'cobradas':[],'facturas':[],'notas':[],'efectivo':[],'credito':[]}
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo)
	row=self.cursor.fetchone()
	ventas['realizadas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+" and status>0 ")
	row=self.cursor.fetchone()
	ventas['cobradas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and tipo=1 ")
	row=self.cursor.fetchone()
	ventas['facturas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and tipo=0 ")
	row=self.cursor.fetchone()
	ventas['notas']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and status=1 ")
	row=self.cursor.fetchone()
	ventas['efectivo']=row
	self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+" and status=2 ")
	row=self.cursor.fetchone()
	ventas['credito']=row
	tabla='<h2>Tabla general de ventas</h2>\
<table cellspacing="6px" width="100%%">\
<TR> <Th>Concepto</Th><TH>Cantidad</TH><th>Valor</th>	</TR>\
<tr> <TD>Ventas realizadas</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
<tr> <TD>Ventas cobradas</TD>	<TD >%s		</TD>       <TD	>		%s</TD>      </tr>\
<tr> <TD>En efectivo</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
<tr> <TD>En credito</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
</table>'%(ventas['realizadas'][0],ventas['realizadas'][1],ventas['cobradas'][0],ventas['cobradas'][1],ventas['efectivo'][0],ventas['efectivo'][1],ventas['credito'][0],ventas['credito'][1])
	self.teDetalles.setText(tabla)


      
    def detallarEntradas(self):
	self.setCursor(QtGui.QCursor(3))

	#ventas={'realizadas':[],'cobradas':[],'facturas':[],'notas':[],'efectivo':[],'credito':[]}
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+" ")
	#row=self.cursor.fetchone()
	#ventas['realizadas']=row
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and status>0 ")
	#row=self.cursor.fetchone()
	#ventas['cobradas']=row
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and tipo=1 ")
	#row=self.cursor.fetchone()
	#ventas['facturas']=row
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and tipo=0 ")
	#row=self.cursor.fetchone()
	#ventas['notas']=row
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+"  and status=1 ")
	#row=self.cursor.fetchone()
	#ventas['efectivo']=row
	#self.cursor.execute("select count(id), ROUND(sum(total),2) from notas where "+self.periodo+" and status=2 ")
	#row=self.cursor.fetchone()
	#ventas['credito']=row
	#tabla='<h2>Tabla general de ventas</h2>\
#<table cellspacing="6px" width="100%%">\
#<TR> <Th>Concepto</Th><TH>Cantidad</TH><th>Valor</th>	</TR>\
#<tr> <TD>Ventas realizadas</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
#<tr> <TD>Ventas cobradas</TD>	<TD >%s		</TD>       <TD	>		%s</TD>      </tr>\
#<tr> <TD>En efectivo</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
#<tr> <TD>En credito</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
#</table>'%(ventas['realizadas'][0],ventas['realizadas'][1],ventas['cobradas'][0],ventas['cobradas'][1],ventas['efectivo'][0],ventas['efectivo'][1],ventas['credito'][0],ventas['credito'][1])
	#self.teDetalles.setText(tabla)
	#rows=""
	#self.cursor.execute("select nombre,count(N.id), ROUND(sum(total),2) from notas as N, usuarios as U where "+self.periodo+" and status=1 and N.usuario=U.id_usuario group by N.usuario;")
	#ventas=self.cursor.fetchall()

	#for v in ventas:
	  #rows+='<tr> <TD>%s</TD>	<TD >%s	</TD>       <TD >	%s</TD>      </tr>'%v;
	#tabla+='<h2>Tabla de ventas por usuario</h2><table cellspacing="6px" width="100%%"><TR> <Th>Usuario</Th><TH>Num. ventas</TH><th>Cantidad cobrada</th></TR>%s</table>'%rows;
	#self.teDetalles.setText(tabla)
	##TABLA DE VENTAS POR DEP
	#periodo=self.periodo.replace("fecha", "n.fecha")
	#self.cursor.execute("select DISTINCT d.nombre,count(n.id),ROUND(sum(v.total),2) from productos as p, notas as n, vendidos as v, familias as f, departamentos as d where "+periodo+"  and v.venta=n.id and p.ref=v.producto and f.id=p.familia  and d.id=f.departamento  group by d.id;")
	#ventas=self.cursor.fetchall()
	#rows=""
	#for v in ventas:
	  #rows+='<tr> <TD>%s</TD>	<TD >%s	</TD>       <TD >	%s</TD>      </tr>'%v;
	#tabla+='<H2>Tabla de ventas por departamento</H2><table cellspacing="6px" width="100%%"><TR> <Th>Departamento</Th><TH>Num. ventas</TH><th>Cantidad cobrada</th></TR>%s</table>'%rows;
	ventas=Ventas(self.parent,self.periodo)
	tab=ventas.detallarVentas()
	tab+="<br/>%s"%ventas.detallarCajas()
	tabu=ventas.detallarUsuarios()
	tab+="<br/>%s"%ventas.detallarDeptos()
	tabu+="<br/>%s"%ventas.detallarProds()
	#tabla=tab
	tabla2=libutil.listaHtml([[tab,tabu]],"Detalle de ventas </span><br/><span>En el periodo del %s al %s <br/> "%(self.deDesde.date().toString("(dd 'de' MMM 'del' yyyy)"),self.deHasta.date().toString("(dd 'de' MMM 'del' yyyy)")),[['50%','Departamento'],['50%','Ventas realizadas']],"#1A4F67",'#eee',14,'100',"#totaldeventas > tr.odd{ background:rgba(0,0,0,0); }") 
	#print tabu

	#tabla2+="<br/><img src='/tmp/grafica.png'/>"
	self.teEntradasDetalle.setText(tabla2)	
	self.stack.setCurrentIndex(2)
	self.setCursor(QtGui.QCursor(0))
	
    def detallarGastos(self):
	self.stack.setCurrentIndex(1)
	head=['if','Fecha','Usuario','Concepto','Cantidad']
	periodo=self.periodo.replace("fecha", "G.fecha")
	self.parent.tabular(self.twGastos,sql,head)
	self.detallarCompras()
	
    def detallarCompras(self):
	self.stack.setCurrentIndex(1)
	head=['Id','Fecha','Proveedor','Total']
	sql="SELECT * FROM compras where "+self.periodo
	self.parent.tabular(self.twCompras,sql,head)


    def salidas(self):
	compras={'realizadas':[],'gastos':[]}
	self.cursor.execute("select count(id), ROUND(sum(total),2) from compras where "+self.periodo)
	row=self.cursor.fetchone()
	compras['realizadas']=row
	self.cursor.execute("select count(num_gasto), ROUND(sum(cantidad),2) from gastos where "+self.periodo)
	row=self.cursor.fetchone()
	compras['gastos']=row

	tabla='<H2>Tabla de salidas de dinero</H2>\
<table cellspacing="6px" width="100%%">\
<TR> <Th>Concepto</Th><TH>Cantidad</TH><th>Valor</th>	</TR>\
<tr> <TD>Compras recibidas:</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
<tr> <TD>Gastos pagados:</TD>	<TD >%s		</TD>       <TD >		%s</TD>      </tr>\
</table>'%(compras['realizadas'][0],compras['realizadas'][1],compras['gastos'][0],compras['gastos'][1])
	self.teDetalles_2.setText(tabla)	
	
    def resumir(self):
	resumen={'ventas':0,'gastos':0,'compras':0}
	self.cursor.execute("select  IFNULL(ROUND(sum(total),2),0) from notas where "+self.periodo)
	resumen['ventas']=self.cursor.fetchone()[0]
	self.cursor.execute("select  IFNULL(ROUND(sum(cantidad),2),0) from gastos where "+self.periodo)
	resumen['gastos']=self.cursor.fetchone()[0]
	self.cursor.execute("select  IFNULL(ROUND(sum(total),2),0) from compras where "+self.periodo)
	resumen['compras']=self.cursor.fetchone()[0]
	resumen['efectivo']=(resumen['ventas']-resumen['compras']-resumen['gastos'])
	tabla='<H2>Movimientos de dinero </H2>\
<table cellspacing="6px" width="100%%">\
<TR> <Th>Concepto</Th><TH>Cantidad</TH></TR>\
<tr> <TD>Ventas:</TD><TD >{ventas}		</TD></tr>\
<tr> <TD>Compras:</TD><TD >{compras}		</TD></tr>\
<tr> <TD>Gastos:</TD><TD >{gastos}		</TD></tr>\
<tr> <TD>Efectivo final:</TD><TD >{efectivo}		</TD></tr>\
</table>'.format(**resumen)
	self.teDetalles_3.setText(tabla)
	  
    def inicial(self):
	if self.parent.aut(2):
	  val=QtGui.QInputDialog.getDouble(self, self.tr("Establecer efectivo inicial"),self.tr("Ingrese la cantidad de efectivo<br> inicial al abrir las cajas."))
	  print val[0]
	  try:
	    self.cursor.execute("""INSERT INTO ventas VALUES(CURDATE(),%s,0)""",val[0])
	  except MySQLdb.Error, e:
	    if (e.args[0]==1062):#Si hay un error por duplicacion de fila solo se actualiza
	      try:
		self.cursor.execute("""UPDATE ventas set inicial=%s where fecha=curdate()""",val[0])
	      except MySQLdb.Error, e:
		print e
	      else:
		self.resumir()
	  else:
	    self.resumir()
	    
    def imprimir(self):
	fecha="%s-%s"%(self.deDesde.date().toString("(dd.MMM.yyyy)"),self.deHasta.date().toString("(dd.MMM.yyyy)"))
	campos={'titulo':'Reporte de ventas de %s'%fecha,'%fecha%':fecha}
	for key in self.parent.modulos['config'].modulos['empresa']:
	    try:
	      campos['%'+key+'%']=self.parent.cfg.get('empresa',key)
	    except:
	      pass
	campos['%detalles%']=str(self.teEntradasDetalle.toHtml())
	#libutil.printb(self.parent,'Reporte de ventas',os.path.join(self.parent.home,"formas","ventas.xml"),campos)
	#for tabla in self.tablas:
	  #campos['%detalles%']+=str(tabla.toHtml())+"<br>"
	doc=Documento(self.parent,os.path.join(self.parent.home,"formas","ventas.xml"),campos)
	ch=Chart(self.parent,700,300)
	ch.dayPlot(self.periodo)
	pix=ch.toPix('/tmp/grafica.png')
	doc.addPage(ch.escena)
	doc.guardarPDF()
	####! Cambiar apartir de aqui

	

    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos	
	

	  

	
