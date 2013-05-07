# -*- coding: utf-8 -*-
import sys,os,random
from PyQt4 import QtCore, QtGui
from qt import Qt
import  datetime
#from chart import chart
class Modulo():
    def __init__(self,parent,nombre):
		self.curser=parent.curser
		self.cursor=parent.cursor
		self.datos={'nombre':"Reportes",'descripcion':"Muestra el todo lo relacionado con ventas.",'version':"0.05",'id':id,'nivel':2}
		self.id=id
		self.parent=parent
		self.action = QtGui.QAction(self)
		self.action.setObjectName(self.datos['nombre']+str(id))
		#self.action.setShortcut("F4")
		#self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
		icon28 = QtGui.QIcon()
		icon28.addPixmap(QtGui.QPixmap("/usr/share/pyventa/images/32/silver/ptch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.action.setIcon(icon28)
		self.action.setText(self.datos['nombre'])
		#self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.stackMove(self.id))
		self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.move(self.datos['nombre']) )

        	self.connect(self.verGrafica, QtCore.SIGNAL("clicked()"), self.graficar)
		#self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),lambda: parent.aut(self.id,2) )
        	#self.connect(self.bvShowinfo, QtCore.SIGNAL("clicked()"), self.weekPlot)
        	self.connect(self.tVentas, QtCore.SIGNAL("itemActivated(QTableWidgetItem* )"), self.mostrarResumen)
        	self.connect(self.pbListaVentas, QtCore.SIGNAL("clicked()"),  self.tablarVentas)
        	self.connect(self.bCorteT, QtCore.SIGNAL("clicked()"), self.corte)
        	self.connect(self.bCorteP, QtCore.SIGNAL("clicked()"), self.parcial)
        	self.connect(self.rbHoy, QtCore.SIGNAL("clicked()"), self.dayPlot)
        	self.connect(self.rbSemana, QtCore.SIGNAL("clicked()"), self.weekPlot)
        	self.connect(self.rbMes, QtCore.SIGNAL("clicked()"), self.monthPlot)
        	self.connect(self.rbAnio, QtCore.SIGNAL("clicked()"), self.yearPlot)
        	self.connect(self.tbPrint, QtCore.SIGNAL("clicked()"), self.imprimirGrafica)
        	self.connect(self.tbImprimir, QtCore.SIGNAL("clicked()"), self.imprimir)
		self.tVentas.setContextMenuPolicy(3)
		self.connect(self.tVentas,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
        	self.connect(self.deCorte, QtCore.SIGNAL("dateChanged ( const QDate)"), self.cambiarFecha)
		self.popMenu = QtGui.QMenu(self)
		action=self.popMenu.addAction(QtGui.QIcon("/usr/share/pyventa/images/16/block_16.png")," Ignorar ")
		action.setIconVisibleInMenu(True)
		action2=self.popMenu.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/receipt.png")," Reimprimir copia ")
		action2.setIconVisibleInMenu(True)
		self.connect(action, QtCore.SIGNAL("triggered()"), self.ignorarVentas)
		self.connect(action2, QtCore.SIGNAL("triggered()"), self.imprimirTicket)
		self.fecha='date(current_timestamp)'
        	self.deDesde.setDate(QtCore.QDate.currentDate())
        	self.deHasta.setDate(QtCore.QDate.currentDate())
        	self.deCorte.setDate(QtCore.QDate.currentDate())
		self.cbEscala.addItem("Hora",'%H')
		self.cbEscala.addItem("Dia",'%j')
		self.cbEscala.addItem("Dia de la semana",'%w')
		self.cbEscala.addItem("Semana",'%u')
		self.cbEscala.addItem("Mes",'%m')
		self.cbEscala.addItem("Anualidad",'%Y')        	
        	#self.graf=QWidget(self)
       		#self.vlVentas1.addWidget(self.graf)


    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos
      

	
