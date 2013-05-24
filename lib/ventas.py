# -*- coding: utf-8 -*-
import os
from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import QLocale 
from ui.ui_ventas import Ui_Form
from lib.utileria import Documento
from lib.dialogos.agrega_gasto import AgregaGasto
from lib import libutil
from lib.librepo import Ventas, Chart
from lib.modelos.gasto import Gasto 
from lib.modelos.caja import Caja 
from lib.modelos.retiro import Retiro 
from lib.modelos.deposito import Deposito 
from lib.modelos.movimiento import Movimiento 
from lib.librerias.comun import *

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
        	copy=QtGui.QAction(QtGui.QIcon(":/actions/images/actions/black_18/copy.png"),"Copiar",self)
		self.connect(copy, QtCore.SIGNAL("triggered()"), self.teEntradasDetalle.copy)

        	self.teEntradasDetalle.addAction(copy)
		self.connect(self.tboImprimir, QtCore.SIGNAL("clicked()"), self.imprimir)
		self.connect(self.tboActualizar, QtCore.SIGNAL("clicked()"), self.actualizar)
		self.connect(self.agasto, QtCore.SIGNAL("triggered()"), self.gastar)
		self.connect(self.tboInicial, QtCore.SIGNAL("clicked()"), self.inicial)
		self.connect(self.pbDepositar, QtCore.SIGNAL("clicked()"), self.depositar)
		self.connect(self.tbRetirar, QtCore.SIGNAL("clicked()"), self.retirar)
		self.connect(self.pbAgregarGasto, QtCore.SIGNAL("clicked()"), self.gastar)
		self.connect(self.pbDetallarProds, QtCore.SIGNAL("clicked()"), self.detallarProds)
		self.connect(self.pbVerResumen, QtCore.SIGNAL("clicked()"),lambda: self.stack.setCurrentIndex(0))
		self.connect(self.action, QtCore.SIGNAL("triggered()"),self.iniciar )
		
		self.connect(self.pbVerEnDetallada,QtCore.SIGNAL("clicked()"), self.detallarEntradas)
		self.connect(self.tboDetalles,QtCore.SIGNAL("clicked()"), self.detallarEntradas)
		self.connect(self.tbGraficar,QtCore.SIGNAL("clicked()"), self.graficar)
		self.parent.menuEdicion.addAction(self.agasto)
		self.tmp={'notas':[],'clientes':[],'total':0}
		#self.tablas=[self.teDetalles,self.teDetalles_2,self.teDetalles_3]
		self.cliente=0
		#inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
		self.periodo=" date(fecha)=CURDATE()  "
		self.grafica=False

    def iniciar(self):
      if self.parent.aut(self.datos['nivel'])>0:
	  self.parent.stack.setCurrentIndex(self.datos['id'])
	  self.setCursor(QtGui.QCursor(16))
	  self.entradas()
	  #self.salidas()
	  self.resumir()
	  self.setCursor(QtGui.QCursor(0))
      
 
	  
	      
    def actualizar(self):
	self.setCursor(QtGui.QCursor(3))
	inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
	fin=str(self.deHasta.date().toString('yyyy-MM-dd'))
	if (inicio==fin):
	  self.periodo=" date(fecha)='%s'"%inicio
	else:
	  self.periodo=" date(fecha) BETWEEN '%s' and  '%s' "%(inicio,fin)
	#self.salidas()
	self.resumir()
	self.entradas()
	self.setCursor(QtGui.QCursor(0))	
	
    def entradas(self):
      pass

    def graficar(self):
      	inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
	fin=str(self.deHasta.date().toString('yyyy-MM-dd'))
	ch=Chart(self.parent,700,300)
	if (inicio==fin):
	  ch.hoursPlot(self.periodo)	
	else:
	  ch.dayPlot(self.periodo)	
	pix=ch.toPix(home+'/grafica.png')
	self.grafica=pix
	self.lblGrafica.setPixmap(pix)
	self.stack.setCurrentIndex(2)
	
	#ch.popGrafica(pix)  
	  
      
    def detallarEntradas(self):
	self.setCursor(QtGui.QCursor(3))
	ventas=Ventas(self.parent,self.periodo)
	tventas=ventas.detallarVentas(caja=self.parent.caja)+"<br/>"
	tcajas=ventas.detallarCajas()
	tusuarios=ventas.detallarUsuarios()
	tdeptos=ventas.detallarDeptos()
	tprods=ventas.detallarProds()
	tabla2=libutil.listaHtml([[tventas+tusuarios+tcajas,tdeptos]],titulo="Resumen de movimientos",opc="000",anchos=[40,60])
	self.teEntradasDetalle.setText(tabla2+tprods)	
	self.detalle=tabla2+tprods
	self.stack.setCurrentIndex(1)
	self.setCursor(QtGui.QCursor(0))
	
    def detallarCompras(self):
	self.stack.setCurrentIndex(1)
	head=['Id','Fecha','Proveedor','Total']
	sql="SELECT * FROM compras where "+self.periodo
	self.parent.tabular(self.twCompras,sql,head)


    def salidas(self):
	pass
	
    def resumir(self):
	vs=Ventas(self.parent,self.periodo)
	(lista,resumen)=vs.resumir(self.periodo,self.parent.caja)
	self.efectivo=resumen['efectivo']
	movimientos=libutil.listaHtml(lista,'Tabla de movimientos',['Concepto','Monto'],'#fff','#1162A7',14,anchos=[70,30])
	head="id_movimiento,usuarios.nombre,cajas.nombre,detalle,tipo, monto,fecha"
	lista=Movimiento(self.parent.conexion).buscar(head,self.periodo+" order by tipo")
	movs=libutil.listaHtml(lista,'Tabla de movimientos de efectivo',
	"#,Usuario,Caja,Detalle,Tipo, Monto,Fecha".split(','),'#fff','#1162A7',10,opc="110",anchos=[5,15,15,22,13,15,15])
	ventas=vs.detallarVentas(caja=self.parent.caja,color='#fff',fondo='#1162A7')
	#dns=vs.detalleNotas(periodo=self.periodo,caja=self.parent.caja)
	#ventas=libutil.listaHtml(dns,'Detalle de ventas',['Tipo','Estado','Valor'],'#fff','#1162A7',12,anchos=[40,30,30])
	tabla=libutil.listaHtml([[movimientos+ventas,movs]],color='#fff',fondo='#1162A7',opc="000",anchos=[40,60])
	self.resumen=tabla
	self.teResumen.setHtml(tabla)
	
    def detallarProds(self):
      self.setCursor(QtGui.QCursor(3))
      vs=Ventas(self.parent,self.periodo)
      num=QtGui.QInputDialog.getInt(self, self.parent.tr("Limite de articulos"),self.parent.tr("Limite de articulos a mostrar:"))
      tabla=vs.detallarProdsVendidos(num[0])
      self.teEntradasDetalle.setHtml(tabla)
      self.detalle=tabla
      self.stack.setCurrentIndex(1)
      self.setCursor(QtGui.QCursor(0))
	  
    def inicial(self):
	self.hacerMovimiento('inicial')
	    
    def depositar(self):
	self.hacerMovimiento('deposito')

    def retirar(self):
	self.hacerMovimiento('retiro')

    def gastar(self):
	self.hacerMovimiento('gasto')
	    
    def hacerMovimiento(self,tipo=''):
	if self.parent.aut(2):
	  ag=AgregaGasto(self.parent,self.parent.sesion['usuario']['id_usuario'],tipo)
	  if ag.exec_()>0:
	    self.resumir()
	    
    def imprimir(self):
      inicio=str(self.deDesde.date().toString('dd MMMM.yy'))
      fin=str(self.deHasta.date().toString('dd MMMM.yy'))
      if inicio==fin:
	periodo=inicio
      else:
	periodo="{0} al {1}".format(inicio,fin)
      head="""<h2 align="center">Reporte de ventas</h2><center><b>Del {periodo}</b></center>""".format(periodo=periodo)
      libutil.printa(head+self.resumen+self.detalle,titulo="Reporte de ventas {periodo}".format(periodo=periodo),orientacion=1)

    #def imprimir(self):
	#fecha="%s a %s"%(self.deDesde.date().toString("(dd.MMM.yyyy)"),self.deHasta.date().toString("(dd.MMM.yyyy)"))
	#campos={'titulo':'Reporte de ventas de %s'%fecha,'%fecha%':fecha}
	#for key in self.parent.modulos['config'].modulos['empresa']:
	    #try:
	      #campos['%'+key+'%']=self.parent.cfg.get('empresa',key)
	    #except:
	      #pass
	
	#campos['%detalles%']=self.html
	##libutil.printb(self.parent,'Reporte de ventas',os.path.join(self.parent.home,"formas","ventas.xml"),campos)
	##for tabla in self.tablas:
	  ##campos['%detalles%']+=str(tabla.toHtml())+"<br>"
	#doc=Documento(self.parent,os.path.join(self.parent.home,"formas","ventas.xml"),campos)
	#if self.grafica:
	  #doc.addPage(self.grafica)
	#doc.guardarPDF()
	#####! Cambiar apartir de aqui

	

    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos	
	

	  

	
