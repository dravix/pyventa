#!/bin/python
import sys,os,shutil, base64
sys.path.append(os.path.join('/usr','share','pyventa','import','Cventa'))
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer, SIGNAL
from ui.ui_cventa import Ui_Form
import MySQLdb, ConfigParser
from lib.selector import Selector
from lib.utileria import ResumenVenta as Resumen, Factura
class Cventa(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.datos={'nombre':"Registrar",'descripcion':"Registra o cierra la venta en proceso, dando opciones de pago.",'version':"0.05",'id':id,'nivel':1}
		self.id=id
		self.parent=parent
		self.kfg=parent.kfg
		self.data={'forma':0,'tipo':0,'recibido':0,'impresion':True}
		self.action = QtGui.QAction(self)
		self.action.setObjectName(self.datos['nombre']+str(id))
		self.action.setToolTip("<h1> F5 </h1>Cerrar venta actual") 
		#self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
		icon28 = QtGui.QIcon()
		icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.action.setIcon(icon28)
		self.action.setIconVisibleInMenu(True)
		self.action.setText(self.datos['nombre'])
		
		#icon28.addPixmap(QtGui.QPixmap("/usr/share/pyventa/images/png/%scventa.png"%parent.iconset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		#self.action.setIcon(icon28)
		#self.action.setIconVisibleInMenu(True)
		self.connect(self.action, QtCore.SIGNAL("triggered()"), self.ver )
		self.imp=True
		self.connect(self.parent.actionCerrar_nota, QtCore.SIGNAL("triggered()"), self.ver)

		self.connect(self.trecibo, QtCore.SIGNAL("editingFinished ()"), self.cerrar)
		self.connect(self.parent.dsbRecibido,SIGNAL("editingFinished ()"), self.cobrar)
		#self.connect(self.bPagoCredito, QtCore.SIGNAL("clicked ()"), self.pagoCredito)
		#self.tbAceptar.setDefault(True)
		#self.frTarjeta.setHidden(True)
		#self.inicia()
    def ver(self):
      if (len(self.parent.basket)>0):
	if self.parent.banderas['tipo']=='c' and self.parent.aut(2)>0: #si es compra
	    self.guardarCompra()
	elif self.parent.banderas['tipo']=='v' and self.parent.aut(1)>0:  #si es venta   
	    if int(self.kfg.getDato('pyventa','caja'))>0 and int(self.kfg.getDato("pyventa","cobra"))==2:	#Si puede cobrar la venta
	      
	      self.parent.wResumen.setVisible(True)
	      self.parent.dsbRecibido.setFocus()
	      self.parent.dsbRecibido.selectAll()
	    else:
	      ide=self.allocate(0,0)
	      if int(self.parent.cfg.get('ticket','default'))>1 and float(self.parent.cfg.get('ticket','trigger'))<self.parent.datos['total']:
		self.parent.imprimirTicket({"<nota/>":str(ide)})
		if int(self.parent.cfg.get('ticket','copia'))>1 and float(self.parent.cfg.get('ticket','copia-trigger'))<self.parent.datos['total']:
		  self.parent.imprimirTicket({"<nota/>":str(ide)})
	      self.parent.limpiar()	
	      
    def cobrar(self):
	  recibo=float(self.parent.dsbRecibido.value())
	  if recibo==0:
	    self.limpiar()
	  elif recibo>0 and recibo>=self.parent.datos['total']:
	    ide=self.allocate(self.data['tipo'],1) #Hasta este punto significa que se realizo la transaccion
	    if ide>0:
	      cambio=recibo-self.parent.datos['total']
	      self.parent.dsbCambio.setValue(cambio)
	      self.parent.dsbCambio.setVisible(True)
	      self.parent.lblCambio.setVisible(True)
	      self.parent.dsbRecibido.setEnabled(False)
	      timer=QTimer.singleShot(10000,self.limpiar)
	      tags={"<nota/>":str(ide),"<total/>":str(self.parent.datos['total']),"<modo/>":"efectivo","<recibido/>":str(recibo),"<cambio/>":str(cambio)}
	      self.parent.imprimirTicket(tags)
	      self.parent.limpiar()
	  
    def inicia(self, imp=True):
      if self.parent.banderas['tipo']=='c' and self.parent.aut(2)>0:
	  self.guardarCompra()
      elif self.parent.banderas['tipo']=='v' and self.parent.aut(1)>0:
	self.nr=True
	self.imp=imp
	self.trecibo.setFocus()
	if (len(self.parent.basket)>0):
	  #print self.parent.cfg.get('ticket','default')
	  if int(self.kfg.getDato('pyventa','caja'))>0 and int(self.kfg.getDato("pyventa","cobra"))==2:
	    self.total.setText(str(self.parent.datos['total']))
	    self.exec_()
	  else:
	    ide=self.allocate(0,0)
	    if int(self.parent.cfg.get('ticket','activo'))==1 and imp:
	      self.parent.imprimirTicket({"<nota/>":str(ide)})
	    self.parent.limpiar()
	    
    def limpiar(self):
      self.nr=True #No repeat option to avoid the recursive bug of doubleSpinbo
      self.total.clear()
      self.trecibo.setValue(0)
      self.trNoprint.setChecked(True)
      self.parent.dsbRecibido.setEnabled(True)
      self.parent.dsbRecibido.setValue(0)
      self.parent.dsbCambio.setValue(0)
      self.parent.dsbCambio.setVisible(False)
      self.parent.lblCambio.setVisible(False)
      self.parent.wResumen.setVisible(False)
      
    def anotar(self,ac):
	if ac:
	  self.data['tipo']=0;
	  
    def eliminarCompra(self,ide):
      try:
	self.cursor.execute( "UPDATE existencia as e, comprados as cc SET stock_logico=stock_logico-cantidad WHERE e.producto=cc.producto and compra=%s;"%ide)
	self.cursor.execute("""DELETE FROM comprados where compra=%s """,ide)
	self.cursor.execute("""DELETE FROM compras where id=%s """,ide)
      except:
	print "Problema al eliminar la compra, la operacion no se realizo."
	return False
      else:
	self.cursor.execute("COMMIT")
	return True

    def guardarCompra(self):
      if (self.parent.banderas['tipo']=='c'):
	if (self.parent.banderas['edicion']!=False):
	  ide=self.parent.banderas['edicion']
	  try:
	    self.cursor.execute("UPDATE existencia as e, comprados as cc SET stock_logico=stock_logico-cantidad WHERE e.producto=cc.producto and compra=%s;"%ide)
	    self.cursor.execute("""DELETE FROM comprados where compra=%s """,ide)
	    self.cursor.execute("COMMIT")
	  except:
	    return

	total=0.0
	for item in self.parent.basket:
	    total+=float(item[4])
	try:
	  if (self.parent.banderas['edicion']!=False):
	    self.cursor.execute("UPDATE compras SET proveedor=%s, comprador=%s, total=%s WHERE id=%s;"%(self.parent.cliente['id'],self.parent.sesion['usuario']['id_usuario'],total, ide))  
	    last=ide
	  else:
	    self.cursor.execute("INSERT INTO compras VALUES(NULL,NOW(),%s,%s, %s); "%(self.parent.cliente['id'],self.parent.sesion['usuario']['id_usuario'],total))
	    self.cursor.execute("SELECT LAST_INSERT_ID();")
	    last=int(self.cursor.fetchone()[0])
	except:
	  print "Problema para crear una compra.\n La operacion no se realizo"
	else:
	  self.cursor.execute("COMMIT")

	  for item in self.parent.basket:
	      try:
		self.cursor.execute("""insert into comprados values(%s,%s,%s,(SELECT costo from productos where ref=%s),%s)""",(last,item[0],item[1],item[0],item[4]))
		sql="UPDATE existencia SET stock_logico=stock_logico+%s where producto=%s"%(item[1],item[0])
		self.cursor.execute(sql)		
	      except:
		print "Error al guardar el producto ",(last,item[0],item[1],item[0],item[4])

	  self.cursor.execute("COMMIT") 
	self.parent.banderas['edicion']=False
	self.parent.banderas['tipo']='v'
	self.limpiar()
	self.parent.limpiar()


    def cobro(self,ac):
	if ac:
	  self.data['forma']=1;
	  self.cobro.setEnable(True)
	  self.trecibo.setFocus()

    def checkCliente(self):
	if (self.parent.cliente['id']==0):
		msgBox=QtGui.QMessageBox()
		msgBox.setText("No se ha seleccionado un cliente.")
		msgBox.setInformativeText("Es necesario que seleccione un cliente para esta operacion.")
		msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		ret=msgBox.exec_()
		if ret==QtGui.QMessageBox.Ok:
		      if self.parent.selCliente()>0:
			return True
		else: 
		      return False
	else:
	    return True
	    
    def facturar(self):	
      if self.parent.cliente['id']<2:
	  if self.parent.selCliente()>0:
	    self.facturar()
      else:
	#self.facturar(self.modulos["cventa"].allocate(1,0))
	ide=self.allocate(1,0)
	#fac=factura(self.parent,id)
	F=Factura(self.parent,ide)
	F.imprimir()
	self.parent.limpiar()

	
	
	
    def cerrar(self):
	if float(self.trecibo.value())>0 and float(self.trecibo.value())>=self.parent.datos['total'] and self.nr:
	   self.nr=False
	   if self.data['forma']==0:
	    #msgBox=QMessageBox(QMessageBox.Information,"Detalles de cobro","<p style='font-size:34px;font-weight:800'>Total: %s</p><p style='font-size:34px;font-weight:800'>Recibido: %s</p><p style='font-size:40px;font-weight:800;color:#cc0000'>Cambio: $%s</p>"%(self.parent.datos['total'],self.trecibo.text(),float(self.trecibo.text())-self.parent.datos['total']),QMessageBox.Ok,self.parent)
	    #msgBox.exec_()

	    ide=self.allocate(self.data['tipo'],1) #Hasta este punto significa que se realizo la transaccion
	    #self.cursor.execute("UPDATE notas set status=1 where id="+str(ide))
	    if self.data['tipo']!=1:
		if self.trNoprint.checkState()==2 and self.imp:
		  tags={"<nota/>":str(ide),"<total/>":str(self.parent.datos['total']),"<modo/>":"efectivo","<recibido/>":str(self.trecibo.value()),"<cambio/>":str(float(self.trecibo.value())-self.parent.datos['total'])}
		  #print tags
		  self.parent.imprimirTicket(tags)
		else:
		  pass
	    elif self.data['tipo']==1:
	      	if self.trNoprint.checkState()==2:
		  fac=factura(self.parent,ide)
		  self.parent.facturar(ide)
	    self.done(1)
	    display=Resumen(self.parent,{'total':self.parent.datos['total'],'modo':'efectivo','recibido':self.trecibo.text(),'articulos':self.parent.datos['narticulos'],'cambio':float(self.trecibo.text())-self.parent.datos['total']})
	    display.exec_()
	    self.retorno()

    def retorno(self):
	    self.limpiar()
	    #self.trecibo.setValue(0)
	    #self.total.clear()
      	    self.parent.limpiar()
      	    
    def guardarPresupuesto(self):
	paper=QtGui.QGraphicsScene()
	



    def allocate(self,tipo,forma):
#Almacena en la base de datos, l nota con todos sus elementos
      #self.cursor.execute("SELECT count(fecha) from ventas where fecha=curdate();")
      #qry=self.cursor.fetchone()
      last=0
      #if (qry[0]==1):
	  #print "Esta nota no entrara en la venta de hoy pues ya se hizo un corte."
      try:
	    if (self.parent.banderas['edicion']!=False):#Si se esta guardando una nota que se reedito
	      last=self.parent.banderas['edicion']
	      self.parent.banderas['edicion']=False
	      print "Editando nota %s "%last
	      #self.cursor.execute("SELECT cantidad, producto FROM vendidos, notas WHERE venta=id AND  `id`=%s"%last)
	      #lista=self.cursor.fetchall()
	      #if lista!=None:
	      self.cursor.execute("""UPDATE `notas` SET cliente=%s, usuario=%s, caja=%s, total=%s, tipo=%s, status=%s WHERE id=%s""",(self.parent.cliente['id'],self.parent.sesion['usuario']['id_usuario'], self.parent.caja,self.parent.grant()[2],tipo,forma,last))
	      self.cursor.execute("""UPDATE existencia as e, vendidos as v SET stock_logico=stock_logico+cantidad WHERE e.producto=v.producto and venta=%s;""",(last))
	      self.cursor.execute("DELETE FROM vendidos where venta="+str(last)+";") 

	    else: 		#en el caso que se trate de guardar una venta por primera vez
	      last=False  	#Se creara una nueva nota
	      self.cursor.execute("""INSERT INTO `notas`  VALUES(NULL,%s,%s,%s,%s,NOW(),%s,%s)""",(self.parent.cliente['id'],self.parent.sesion['usuario']['id_usuario'], self.parent.caja,self.parent.grant()[2],tipo,forma))
	      
	    #last='LAST_INSERT_ID()'
#+str(ref)+","+str(self.parent.cliente['id'])+","+str(self.parent.grant()[2])+",now(),"+str(tipo)+","+str(forma)+")")

      except MySQLdb.Error, e:
     	    mb=QtGui.QMessageBox.critical(self, "Error!", "La nota no pudo ser registrada !!")
     	    print e
	    return False
      else:
	if last==False:
      	    self.cursor.execute("SELECT LAST_INSERT_ID() from notas;")
	    last=self.cursor.fetchone()[0]
#['Ref','Ctd','Descripcion del producto','Precio','Importe','C/Dcto']	      	      
	for aux in self.parent.basket:
	  self.cursor.execute("""INSERT INTO `vendidos` VALUES(%s,%s,%s,%s,%s)""",(last,aux[0],tipo,aux[1],aux[5]))
	  self.cursor.execute("UPDATE productos set `vendidas`=`vendidas`+1, ultima_modificacion=now() WHERE ref="+str(aux[0]))
	  self.cursor.execute("""UPDATE existencia SET stock_logico=stock_logico-%s WHERE producto=%s""",(aux[1],aux[0]))
	self.cursor.execute("COMMIT")
	return last 
	
    def eliminarNota(self,nota):
      if self.parent.aut(2):
	try:
	  self.cursor.execute("""UPDATE existencia as e, vendidos as v SET stock_logico=stock_logico+cantidad WHERE e.producto=v.producto and venta=%s;""",(nota))
	  self.cursor.execute("DELETE FROM vendidos where venta=%s"%nota)  
	  self.cursor.execute("DELETE FROM notas where `id`=%s"%nota)
	except MySQLdb.Error, e:
	  print "Error al eliminar nota %s"%nota,e
	  QtGui.QMessageBox.critical(self, "Error!", "No fue posible eliminar la nota")
	else:	
	  self.cursor.execute("COMMIT")
	  QtGui.QMessageBox.informative(self, "Error!", "La nota no pudo ser registrada !!")

    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos

