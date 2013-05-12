# -*- coding: utf-8 -*-
import sys,os
from PyQt4 import QtCore, QtGui
from ui.ui_cobro import Ui_Form
from lib.selector import Selector
from lib.utileria import VisorNotas as NotaViewer, ResumenVenta as Resumen
import  datetime
import MySQLdb
class Cobros(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
	  QtGui.QDialog.__init__(self)
	  self.setupUi(self)
	  self.twNotas.setContextMenuPolicy(3)
	  self.connect(self.twNotas,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)

	  self.connect(self.twNotas, QtCore.SIGNAL("itemActivated(QTableWidgetItem* )"), self.ncInfo)
	  self.connect(self.ncactualizar, QtCore.SIGNAL("clicked()"), self.actualizarNotas)
	  self.connect(self.nccobrar, QtCore.SIGNAL("clicked()"), self.ncCobrar)
	  self.connect(self.BClientSelect, QtCore.SIGNAL("clicked()"), self.seleccionarCliente)
	  self.connect(self.bScliente, QtCore.SIGNAL("clicked()"), self.cuentasPendientes)
	  self.connect(self.pbLimpiar, QtCore.SIGNAL("clicked()"), self.limpiar)
	  self.connect(self.cbTipo, QtCore.SIGNAL("activated(const QString)"), self.actualizarNotas)
	  self.connect(self.leNumero, QtCore.SIGNAL("returnPressed()"), self.addNota)

	  self.connect(self.ncrecibo, QtCore.SIGNAL("returnPressed()"), self.ncCobrar) 

	  self.curser=parent.curser
	  self.cursor=parent.cursor
	  self.datos={'nombre':"Cobros",'descripcion':"Cobro de notas pendientes por pagar",'version':"0.04",'id':id,'nivel':2}
	  self.id=id
	  self.action = QtGui.QAction(self)
	  self.action.setObjectName(self.datos['nombre']+str(id))
	  #self.action.setShortcut("F4")
	  self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
	  self.parent=parent
	  icon28 = QtGui.QIcon()
	  icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/pending.png"), 0, QtGui.QIcon.Off)
	  icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/pending.png"), 2, QtGui.QIcon.Off)
	  self.action.setIcon(icon28)
	  self.action.setIconVisibleInMenu(True)
	  self.action.setText(self.datos['nombre'])
	  #self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.stackMove(self.id) )
	  self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.move(self.datos['nombre']) )

	  self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),self.inicio )
	  self.tmp={'notas':[],'clientes':[],'total':0}
	  self.cliente=0
	  self.popMenu = QtGui.QMenu(self)
	  action=self.popMenu.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/receipt.png"),"Ver detalle de venta")
	  action.setIconVisibleInMenu(True)
	  self.connect(action, QtCore.SIGNAL("triggered()"), self.verDetalle)
	  actionAgregar=self.popMenu.addAction(QtGui.QIcon("/usr/share/pyventa/images/32/Add-32.png"),"Cobrar venta")
	  actionAgregar.setIconVisibleInMenu(True)
	  self.connect(actionAgregar, QtCore.SIGNAL("triggered()"), lambda: self.addNota(str(self.twNotas.item(self.twNotas.currentRow(),0).text())))
	  self.leNumero.setFocus(True)
    
    def addNota(self,ide=-1): 
    #Esta funcion es llamada para agregar una nota con su numero de id
      if ide==-1:
	ide=str(self.leNumero.text())
	self.leNumero.clear()
      if len(ide)>0:
	try:
	  a=self.tmp['notas'].index(ide)
	except:
	  Res=NotaViewer(self.parent,ide)
	  nota=Res.getDatos()
	  app=self.verDetalle(ide)
	  if app!=0:
	    if nota!=False:
		self.tmp['notas'].append(ide)
		self.tmp['clientes'].append(nota['cliente'])
		self.tmp['total']+=float(nota['total'])
		self.nctotal.setText("Total:  %s"%self.tmp['total'])
		self.ncnotas.setText("Nota(s): %s "%','.join(self.tmp['notas']))
		self.leNumero.setFocus(True)
      else:
	self.ncrecibo.setFocus(True)
    
    def verDetalle(self,ide=-1):
      if ide==-1:
	ide=str(self.twNotas.item(self.twNotas.currentRow(),0).text())
      Res=NotaViewer(self.parent,ide)
      Res.show()

	  
    def ncInfo(self):
	self.tmp={'notas':[],'clientes':[],'total':0}
	items=self.twNotas.selectedItems()
	ids=''
	total=0	
	for item in items:
	  if self.twNotas.column(item)==0:
	      self.tmp['notas'].append(str(item.text()))
	  if self.twNotas.column(item)==1:
	      self.tmp['clientes'].append(str(item.text()))
	  if self.twNotas.column(item)==3:
	      self.tmp['total']+=float(str(item.text()))
	  self.nctotal.setText("Total:  %s"%self.tmp['total'])
	  self.ncnotas.setText("Nota(s): %s "%','.join(self.tmp['notas']))
	self.ncrecibo.setFocus()

    def ncCobrar(self):
	if self.rbCredito.isChecked():
	  for ide in self.tmp['notas']:
	    if (ide!=' '):
	      self.cursor.execute("""UPDATE clientes set credito=credito-%s, caja=%s where  id=%s """%(self.tmp['total'],self.parent.caja,self.cliente))
	      self.cursor.execute("""UPDATE notas SET status=2, cliente=%s,caja=%s where  id=%s """%(self.cliente,ide, self.parent.caja))
	else:
	  if self.cliente!=0:
	      self.cursor.execute("""UPDATE clientes set credito=credito+%s, caja=%s where  id=%s """%(self.tmp['total'],self.parent.caja,self.cliente))
	  for ide in self.tmp['notas']:
	    if (ide!=' '):
	      self.cursor.execute("UPDATE notas SET status=1, caja=%s where  id=%s"%(self.parent.caja,ide))
	  display=Resumen(self.parent,{'total':float(self.tmp['total']),'modo':'efectivo','recibido':float(self.ncrecibo.text()),'cambio':str(float(self.ncrecibo.text())-float(self.tmp['total']))})
	  display.exec_()
	  self.limpiar()
    
    def limpiar(self):
	self.tmp={'notas':[],'clientes':[],'total':0}
        self.ncrecibo.setText("")
        self.actualizarNotas()	
        self.rbCredito.setEnabled(False)
        self.rbCredito.setChecked(False)
        self.ncrecibo.setEnabled(True)
        self.cliente=0
        self.ncnotas.clear()
        self.leNumero.setFocus(True)
        
    def inicio(self,ind):
      if ind==self.id:
	self.actualizarNotas()
	self.leNumero.setFocus(True)

    def actualizarNotas(self):
      #self.cursor.execute("SELECT count(fecha) from ventas where fecha=CURDATE() ")
      #qry=self.cursor.fetchone()
      #if (qry[0]==0):
	head=('Id','Cliente','time(fecha)','Total')
	col=''
	col+=','.join(head)
	col+=''
	if self.cbTipo.currentIndex()==0:
	  tipo=''
	else:
	  tipo=" and tipo="+str(self.cbTipo.currentIndex()-1)
	sql="select "+col+"  from notas where date(fecha)=CURDATE()  "+str(tipo)+" and status=0 order by id; "
	self.parent.tabular(self.twNotas,sql,head) 

    def cuentasPendientes(self):
	 app=scliente(self.parent)
	 self.cliente=app.exec_()
	 self.parent.cliente={'id':0,'nombre':"Normal mostrador",'rfc':''}
	 head=('Id','Cliente','time(fecha)','Total')
	 col=''
	 col+=','.join(head)
	 col+=''
	 sql="select "+col+"  from notas where  status=2 and cliente="+str(self.cliente)+" order by fecha desc; "
	 self.parent.tabular(self.twNotas,sql,head)
	
    def seleccionarCliente(self):
	 app=scliente(self.parent)
	 app=Selector(self,'Clientes','clientes','id,nombre,rfc','Id,Nombre del cliente,RFC',"(`nombre` like '%{0}%' or `rfc` like '{0}%') order by nombre desc ")
	 if app.exec_()>0:
	  self.cliente=app.retorno[0][0]
	  #self.parent.cliente={'id':0,'nombre':"Normal mostrador",'rfc':''}
	  self.rbCredito.setEnabled(True)
	  self.rbCredito.setChecked(True)
	  self.checkCredito()
	 
    def checkCredito(self):
#Esta funcion debe ser llamada una vez que se tenga seleccionado un cliente al que se cargara la(s) nota(s)
#Verifica si el cliente tiene fondos para cargar a su cuenta la deuda de nota actual
	self.cursor.execute("""SELECT credito FROM clientes where id=%s """%[self.cliente])
	qry=self.cursor.fetchone()[0]
	if qry!=None:
	  if float(qry)>self.tmp['total']:
	      self.ncrecibo.setEnabled(False)
	      return True
	  else:
	    msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Critical,"No existen fondos suficientes!","El cliente seleccionado no cuenta con credito suficiente para cargar con el total de las ventas. El pago tendra que ser en efectivo",QtGui.QMessageBox.Close,self)
	    msgBox.exec_()
	    self.rbCredito.setEnabled(False)
	    self.ncrecibo.setEnabled(True)
	    return False	 
	    
    def ocm(self, point):
	 #point.setY(point.y())
	 point.setX(point.x()+20)
         self.popMenu.exec_(self.twNotas.mapToGlobal(point) )

    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = caja(app,1)
    aw.show()
    sys.exit(app.exec_())
	
