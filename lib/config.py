# -*- coding: utf-8 -*-
import sys,os, base64, datetime, tarfile, ftplib
from os import listdir
from os.path import isfile, join, expanduser, exists, basename
from PyQt4 import QtCore, QtGui
from ui.ui_config import Ui_Form
from lib.utileria import Respaldo, editorSimple
from lib.librerias.configurador import Configurador
import MySQLdb
import ConfigParser
from ui.ui_editor_ticket import Ui_Dialog as Editor
from lib.buscador_pop import buscadorPop
import cups

class Configs(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id=0):
	QtGui.QDialog.__init__(self)
	self.setupUi(self)
	self.stack.setCurrentIndex(0)
	self.curser=parent.curser
	self.cursor=parent.cursor
	self.datos={'nombre':"Configurador",'descripcion':"Configura el funcionamiento del programa, ademas de guardar las personalizaciones .",'version':"0.05",'id':id,'nivel':2}
	self.id=id
	self.parent=parent
	self.action = QtGui.QAction(self)
	self.action.setObjectName(self.datos['nombre']+str(id))
	self.action.setToolTip("Configuraciones globales de este punto de venta.") 
	#self.action.setShortcut("F4")
	#self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
	icono = QtGui.QIcon()
	icono.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/config.png"), 0, QtGui.QIcon.Off)
	self.icono=":/modulos/images/png/elegant/config.png"
	icono.addPixmap(QtGui.QPixmap(self.icono), 2, QtGui.QIcon.Off)
	self.action.setIcon(icono)
	self.action.setIconVisibleInMenu(True)

	self.action.setText(self.datos['nombre'])
	#self.connect(self.action, QtCore.SIGNAL("triggered()"), lambda: parent.stackMove(self.id) )
	self.connect(self.action, QtCore.SIGNAL("triggered()"), self.launch )

	#self.connect(self.benter, QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(1) )
	#self.connect(self.bdata, QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(0) )
	#self.connect(self.bpyventa, QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(2) )
	#self.connect(self.tbFormas, QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(3) )
	#self.connect(self.bRespaldo, QtCore.SIGNAL("clicked()"), lambda: self.stack.setCurrentIndex(4) )
	self.connect(self.cbPath, QtCore.SIGNAL("clicked()"),  self.cambiarFolderFacturas )
	self.connect(self.ctPrinter, QtCore.SIGNAL("clicked()"),  self.cambiarImpresoraTickets )
	self.connect(self.pbEditar, QtCore.SIGNAL("clicked()"),  self.editar )
	
	#self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),lambda: parent.aut(self.id,2) )
	#self.connect(self.tablaImpuestos, QtCore.SIGNAL("currentItemChanged(QTableWidgetItem*,QTableWidgetItem*)"), self.cambiarImp)
	#self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"), self.inicia)
	self.connect(self.rlBackup, QtCore.SIGNAL("clicked()"), self.respaldarLocal)
	self.connect(self.cpgrespaldo, QtCore.SIGNAL("clicked()"), self.respaldarRemoto)
	self.connect(self.rsServer, QtCore.SIGNAL("editingFinished ()"), lambda: self.setCambio('respaldo','server',self.rsServer.text()))
	self.connect(self.rsUser, QtCore.SIGNAL("editingFinished ()"), lambda: self.setCambio('respaldo','user',self.rsUser.text()))
	self.connect(self.rsPass, QtCore.SIGNAL("editingFinished ()"), lambda: self.setCambio('respaldo','pass',self.rsPass.text()))
	self.connect(self.rsPath, QtCore.SIGNAL("editingFinished ()"), lambda: self.setCambio('respaldo','rpath',self.rsPath.text()))
	self.connect(self.rlPeriod, QtCore.SIGNAL("valueChanged ( int )"), lambda: self.setCambio('respaldo','autolocal',self.rlPeriod.value()))
	self.connect(self.rsPeriod, QtCore.SIGNAL("valueChanged ( int )"), lambda: self.setCambio('respaldo','autoremoto',self.rsPeriod.value()))
	self.connect(self.bprobar, QtCore.SIGNAL("clicked()"), self.conexion )
	self.connect(self.bset, QtCore.SIGNAL("clicked()"), self.setDB )
	self.connect(self.bclose, QtCore.SIGNAL("clicked()"), self.close )
	self.connect(self.bcreate, QtCore.SIGNAL("clicked()"), self.crearDB )
	self.connect(self.brecargar, QtCore.SIGNAL("clicked()"),lambda: self.recargar('empresa') )
	self.connect(self.cbEstilos,QtCore.SIGNAL("activated(const QString)"),self.cambiarEstilo)
	self.connect(self.cbPrinters,QtCore.SIGNAL("activated(const QString)"),self.setPrinter)
	self.connect(self.cbDrivers,QtCore.SIGNAL("activated(const QString)"),self.setDriver)
	self.connect(self.clrExplorar,QtCore.SIGNAL("clicked()"),self.cambiarFolderRespaldo)
	self.connect(self.cbpreview,QtCore.SIGNAL("clicked()"),self.editarTicket)
	self.connect(self.pbfEditar,QtCore.SIGNAL("clicked()"),self.editarFactura)
	self.connect(self.pbpEditar_,QtCore.SIGNAL("clicked()"),self.editarPresupuesto)
	self.connect(self.pbEditarCorte,QtCore.SIGNAL("clicked()"),self.editarCorte)
	self.connect(self.rlRestore,QtCore.SIGNAL("clicked()"),self.restaurar)
	self.connect(self.rlRestoreDB,QtCore.SIGNAL("clicked()"),lambda:self.restaurar(True,False))		
	self.connect(self.rlRestoreConf,QtCore.SIGNAL("clicked()"),lambda:self.restaurar(False,True))		
	self.connect(self.sbCaja,QtCore.SIGNAL("editingFinished ()"),lambda: self.setCambio('pyventa','caja',self.sbCaja.value()))		
	self.connect(self.tbBuscarCaja,QtCore.SIGNAL("clicked()"),self.buscador)
	self.connect(self.tbLogo,QtCore.SIGNAL("clicked()"),self.cambiarLogo)
	self.connect(self.tbRecargarEstilo,QtCore.SIGNAL("clicked()"),self.parent.iniciarEstilo)
	self.connect(self.chbRecibePagos,QtCore.SIGNAL("stateChanged ( int  )"),self.setRecibePagos)
	self.connect(self.chbImprimirCopia,QtCore.SIGNAL("stateChanged ( int  )"),self.setImprimeCopiaRecibo)
	self.connect(self.chbImprimirTicket,QtCore.SIGNAL("stateChanged ( int  )"),self.setImprimeTicket)
	self.connect(self.dsbTicketTigger,QtCore.SIGNAL("valueChanged ( float  )"),self.setTicketTrigger)
	self.connect(self.dsbCopia,QtCore.SIGNAL("valueChanged ( float  )"),self.setCopiaTrigger)
      
	#self.connect(self.gbTickets,QtCore.SIGNAL("clicked()"),lambda: self.setCambio('ticket','default',self.boolint(self.gbTickets.isChecked())))
	#self.connect(self.gbFacturas,QtCore.SIGNAL("clicked()"),lambda: self.setCambio('facturas','default',self.boolint(self.gbFacturas.isChecked())))		#self.connect(self.bfSave, QtCore.SIGNAL("clicked()"), self.cambiarFolderFacturas )
	self.mysql={'host':'','user':'','pass':'','db':'tpv'}
	self.mysql['db']='tpv'
	self.ruta=join(self.parent.home,"config.cfg")
	#self.cfg = ConfigParser.ConfigParser()
	self.modulos={'empresa':{},'respaldo':{},'mysql':{},'ticket':{},'factura':{},'nota':{},'pyventa':{}}
	self.inicia()

	self.checkRespaldo()
	self.setupMenus()
	#self.listarImp()
		
    def launch(self):
      if self.parent.aut(self.datos['nivel'])>0:
	self.show()
	self.activateWindow ()

    def inicia(self):
	self.kfg=self.parent.cfg
	if (self.kfg.cfg!=None):
	    self.cfg=self.kfg
	    mysql=['host','user','pass','db']
	    for key in mysql:
	      if self.cfg.has_option("mysql", key):
		self.mysql[key]=self.kfg.getDato('mysql',key)

	    self.modulos['empresa']['nombre']=self.lenombre
	    self.modulos['empresa']['rfc']=self.lerfc
	    self.modulos['empresa']['slogan']=self.leslogan
	    self.modulos['empresa']['direccion']=self.ledir
	    self.modulos['empresa']['ciudad']=self.leciudad
	    self.modulos['empresa']['estado']=self.leestado
	    self.modulos['empresa']['cp']=self.lecp
	    self.modulos['empresa']['email']=self.lemail
	    self.modulos['empresa']['telefono']=self.letel
	    self.modulos['empresa']['pagina']=self.leweb
	    self.modulos['empresa']['logo']=self.leLogo
	    
	    self.lblLogo.setPixmap(QtGui.QPixmap(self.kfg.getDato('empresa','logo')))
	    
	    self.modulos['mysql']['host']=self.tserver
	    self.modulos['mysql']['user']=self.tuser
	    self.modulos['mysql']['pass']=self.tpass
	    self.modulos['mysql']['db']=self.tdb

	    self.modulos['respaldo']['lpath']=self.rlPath
	    self.modulos['respaldo']['server']=self.rsServer
	    self.modulos['respaldo']['user']=self.rsUser
	    self.modulos['respaldo']['pass']=self.rsPass
	    self.modulos['respaldo']['rpath']=self.rsPath

	    remoto=self.kfg.getDato('respaldo','remoto')
	    local=self.kfg.getDato('respaldo','local')
	    #if (remoto!=1):
		#self.gbRemoto.setChecked(False)
	    #if local!=1:
		#self.gbLocal.setChecked(False)
	      
	    for modulo in self.modulos:
	      for key in self.modulos[modulo]:
		try:
		  self.modulos[modulo][key].setText(self.kfg.getDato(modulo,key))
		except:
		  pass
	    self.sbCaja.setValue(float(self.kfg.getDato("pyventa","caja")))
	    self.chbRecibePagos.setCheckState(int(self.kfg.getDato("pyventa","cobra")))
	    #self.gbTickets.setChecked(bool(int(self.kfg.getDato("ticket","default"))))
	    #self.gbFacturas.setChecked(bool(int(self.kfg.getDato("factura","default"))))
	    self.gbBox.setChecked(bool(int(self.kfg.getDato("pyventa","caja"))))
	for  files in os.walk(join(self.parent.home,"estilos")):
	    for i,name in enumerate(files[2]):
		  tipo=name.split('.')
		  if tipo[1]=='css':
		    self.cbEstilos.addItem(str(name))

	#----Impresiones
	self.cbPath.setText(self.kfg.getDato("factura","ruta"))
	try:
	  conn = cups.Connection ()
	  printers = conn.getPrinters()
	  self.cbPrinters.addItems([str(p) for p in conn.getPrinters ()])
	  self.cbPrinters.setCurrentIndex(self.cbPrinters.findText(self.kfg.getDato("ticket","impresora")))
	except:
	  self.cbPrinters.addItem("Predeterminada")
	  
	self.dsbCopia.setValue(float(self.kfg.getDato("ticket","copia-trigger")))  
	self.dsbTicketTigger.setValue(float(self.kfg.getDato("ticket","trigger")))  	

	self.chbImprimirCopia.setCheckState(int(self.kfg.getDato("ticket","copia")))  
	self.chbImprimirTicket.setCheckState(int(self.kfg.getDato("ticket","default"))) 
	
	driverpath=join(self.parent.home,'drivers')
	self.cbDrivers.addItems([ f[0:-3] for f in os.listdir(driverpath) if isfile(join(driverpath,f)) and f[-1]=='y' ])

	self.cbDrivers.setCurrentIndex(self.cbDrivers.findText(self.kfg.getDato("ticket","driver")))


	
    def setupMenus(self):
      respaldos=self.parent.menuPyventa.addMenu("Respaldos")
      respaldos.addAction("Generar respaldo",self.respaldarLocal)
      respaldos.addAction("Restaurar todo",lambda:self.restaurar(True,True))
      
      respaldos.addSeparator()
      respaldos.addAction("Restaurar base de datos",lambda:self.restaurar(True,False))
      respaldos.addAction("Restaurar configuraciones",lambda:self.restaurar(False,True))
      
      self.parent.menuHerramientas.addAction("Configuraciones",self.launch)

      
    def cambiarLogo(self):
	  File = QtGui.QFileDialog()
	  saveFile = str(File.getOpenFileName(self, "Seleccione la imagen",expanduser("~"),self.tr("Imagenes (*.png *.jpg *.jpeg)")))
	  if (saveFile!=""):
	    self.lblLogo.setPixmap(QtGui.QPixmap(saveFile))
	    self.leLogo.setText(saveFile)
	    self.setCambio('empresa','logo',saveFile)
	    
    def recargar(self,modulo):
	  for key in self.modulos[modulo]:
	      try:
		print self.modulos[modulo][key].text()
		self.cfg.set(modulo,key,str(self.modulos[modulo][key].text()))
	      except:
		pass
	  self.cfg.guardar()
	  self.kfg=Configurador()
	  msgBox=QtGui.QMessageBox()
	  msgBox.setText("Se han guardado las configuraciones")	
	  msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
	  msgBox.exec_()
	  
    def setCambio(self,modulo,propiedad,valor):
	      try:
		self.cfg.set(str(modulo),str(propiedad),str(valor))
	      except ConfigParser.Error,e:
		print "({0},{1},{2}), No se guardo la configuracion".format(modulo,propiedad,valor),e
	      else:
		#self.cfg.guardar()
		self.parent.cfg=self.cfg
		
    def setDB(self):
	if self.cfg!=None:
	  pass
	else:
	  self.cfg.add_section('mysql')
	self.cfg.set('mysql','host',self.mysql['host'])
	self.cfg.set('mysql','user',self.mysql['user'])
	self.cfg.set('mysql','pass',base64.b64encode(self.mysql['pass']))
	self.cfg.set('mysql','db',self.mysql['db'])
	self.cfg.guardar()
	self.parent.conexion()
	self.display.setText("<h1>Se ha guardado correctamente.</h1><p>Su conexion ha sido guardada y esta lista para su uso. </p>")
	msgBox=QtGui.QMessageBox()
	msgBox.setText("Se ha establecido la base de datos.")
	msgBox.setInformativeText("Desea usted empezar a trabajar con este punto venta? <br> <i>Si desea continuar configurando pulse cancelar<i>")
	msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
	ret=msgBox.exec_()
	if ret==QtGui.QMessageBox.Ok:
	  self.parent.insert()
	    
    def crearDB(self):
		fi=open('./perfil/db.sql')
		tpv=fi.read()
		self.mysql['host']=str(self.tserver.text())
		self.mysql['user']=str(self.tuser.text())
		self.mysql['pass']=str(self.tpass.text())  
                db = MySQLdb.connect(self.mysql['host'], self.mysql['user'], self.mysql['pass'])
		stout=db.query(tpv)
               	self.display.setText('<p>'+str(stout)+'</p>')
               	
    def conexion(self):
		host=str(self.tserver.text())
		user=str(self.tuser.text())
		password=str(self.tpass.text())
		db=str(self.tdb.text())
		try:
	            db = MySQLdb.connect(host, user, password,db)
		except MySQLdb.Error, e:
		    if (e.args[0]==1049):
			  self.bcreate.setEnabled(True)
			  self.display.setText('<h1>No se encontro ninguna base de datos en el servidor.</h1>\
 </br> <ol><li>Puede crear una pulsando el boton de CREAR BASE DE DATOS</li>\
<li>Puede buscar en otro servidor</li></ol>')
		    if (e.args[0]==1045):
			  self.display.setText('<h1>Acceso denegado, Usuario y/o contrasena incorrecta.</h1>\
 </br> <ol><li>Es posible que solo tenga que intentar con otra contrasena</li>\
<li>O que la contrasena no sea para este usuario</li></ol>')
		    if (e.args[0]==2005):
			  self.display.setText('<h1>No se encontro al servidor.</h1>\
 </br> <ol><li>Pruebe cambiando el nombre del servidor, puede ser  IP, o su nombre DNS en la red local</li>\
<li>Averigue si el servidor esta disponible en red</li></ol>')

                
        	else:                
                	self.bset.setEnabled(True)
                	self.display.setText('<h1>Conectado.</h1><p>Guarde esta configuracion para que Pyventa se conecte usando esta base de datos</p>')
                	self.mysql['host']=str(self.tserver.text())
			self.mysql['user']=str(self.tuser.text())
			self.mysql['pass']=str(self.tpass.text())       
			self.mysql['db']=str(self.tdb.text())       
    def explorer(self):
	File = QtGui.QFileDialog()
	return File.getExistingDirectory(self, "Escoga un directorio.",expanduser('~'))

    def listarImp(self):
	    head=('Nombre','Porciento')
	    col='`'
	    col+='`,`'.join(head)
	    col+='`'
	    sql="SELECT "+col+" FROM impuestos; "
	    self.parent.cursor.execute(sql)
	    result = self.parent.cursor.fetchall()
	    self.tablaImpuestos.setColumnCount(len(head))
	    self.tablaImpuestos.setRowCount(len(result))	 
	 
	    for i,data in enumerate(head):
	    	item = QTableWidgetItem(1)
		item.setText(str(data))
		self.tablaImpuestos.setHorizontalHeaderItem(i,item)
	    for i,elem in enumerate(result):
		for j,data in enumerate(elem):
		  item = QTableWidgetItem(1)
		  item.setText(str(data))
		  self.tablaImpuestos.setItem(i,j,item)
	    self.tablaImpuestos.resizeColumnsToContents() 	

    def cambiarImpresoraTickets(self):
	printer=QtGui.QPrinter()
	dlg=QtGui.QPrintDialog(printer, self)
	if dlg.exec_()==QtGui.QDialog.Accepted:
	    self.setCambio("ticket","impresora",str(printer.printerName()))

    def cambiarFolderFacturas(self):
	folder=self.explorer()
	self.setCambio("factura","ruta",folder)
	self.cbPath.setText(folder)

    def cambiarEstilo(self,index):
	  self.setCambio("pyventa","estilo",index)
	  kcss = open("%s/estilos/%s"%(self.parent.home,index),"r")
	  styname=index.split('.')[0]
	  if exists("/usr/share/pyventa/images/png/%s"%styname):
	      self.setCambio("pyventa","resolucion",styname)
	  estilo=kcss.read()
	  self.parent.setStyleSheet(estilo)
	  kcss.close()	

    def cambiarFolderRespaldo(self):
	folder=self.explorer()
	self.setCambio("respaldo","lpath",folder)
	self.rlPath.setText(folder)
	
    def respaldarLocal(self):
      if self.parent.aut(2)>0:
	RES=Respaldo()
	out=RES.respaldarLocal()
	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"El respaldo fue generado.","Se ha creado el respaldo  %s."%out,QtGui.QMessageBox.Close,self)
	msgBox.exec_()
	return out

    def respaldarRemoto(self):
	ftp_servidor = self.kfg.getDato('respaldo','server')
	ftp_usuario  = self.kfg.getDato('respaldo','user')
	ftp_clave    = self.kfg.getDato('respaldo','pass')
	ftp_raiz     = self.kfg.getDato('respaldo','rpath')
	fichero_origen = self.respaldarLocal()	# Ruta al fichero que vamos a subir
	fichero_destino = basename(fichero_origen) # Nombre que tendrá el fichero en el servidor
  # Conectamos con el servidor
	try:
	  s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
	  try:
	    f = open(fichero_origen, 'rb')
	    s.cwd(ftp_raiz)
	    s.storbinary('STOR ' + fichero_destino, f)
	    f.close()
	    s.quit()
	  except:
	    print "No se ha podido encontrar el fichero " + fichero_origen
	except:
	    print "No se ha podido conectar al servidor " + ftp_servidor

    def checkRespaldo(self):
	hoy=datetime.date.today()
	self.dia=int(hoy.strftime("%d"))
	if exists(join(str(self.kfg.getDato('respaldo','lpath')),"respaldo_"+self.kfg.getDato("empresa","nombre")+"-pyventa_"+str(hoy.strftime("%d-%m-%Y"))+".tar.bz2"))==False:
	  autolocal=int(self.kfg.getDato("respaldo","autolocal"))
	  autoremoto=int(self.kfg.getDato("respaldo","autoremoto"))
	  if autoremoto!=0 :
	      if self.dia%autoremoto==0:
		self.respaldarRemoto()
	  elif autolocal!=0 :
	      if self.dia%autolocal==0:
		self.respaldarLocal()

    def restaurar(self,database=True,config=True):
	  File = QtGui.QFileDialog()
	  saveFile = File.getOpenFileName(self, "Escoga el archivo de respaldo",self.kfg.getDato('respaldo','lpath'),self.tr("Respaldos (*.tar.gz *.tar.bz2 *.zip)"))
	  if (saveFile!=""):
	    rs=Respaldo()
	    self.setCursor(QtGui.QCursor(3))
	    if rs.restaurar(saveFile,database,config):
		self.setCursor(QtGui.QCursor(0))
	      	msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"El respaldo ha sido restaurado.","La base de datos ha sido restaurada, todos los cambios hechos desde la fecha del respaldo, han sido eliminados.",QtGui.QMessageBox.Close,self)
		msgBox.exec_()

    def editarTicket(self):
	editor=editorSimple(self.parent,join(self.parent.home,"ticket.xml"))
	editor.exec_()
	self.cfg.recargar()
	
    def editarFactura(self):
	editor=editorSimple(self.parent,join(self.parent.home,"formas","factura.cfg"))
	editor.exec_()	
	self.cfg.recargar()
	
    def editarPresupuesto(self):
	editor=editorSimple(self.parent,join(self.parent.home,"formas","presupuesto.xml"))
	editor.exec_()	
	self.cfg.recargar()
	
    def editar(self):
	editor=editorSimple(self.parent,join(self.parent.home,"config.cfg"))
	editor.exec_()
	self.cfg.recargar()
	
    def editarCorte(self):
	editor=editorSimple(self.parent,join(self.parent.home,"corte.xml"))
	editor.exec_()  
	self.cfg.recargar()
	
    def buscador(self):
      sql="SELECT num_caja, caja, maquina from cajas;"
      app=buscadorPop(self,'',1,['Num_caja','Nombre','Maquina'],'cajas')
      #Proceso padre, texto a buscar, numero de columna, arreglo de columnas, tabla sql, seleccion multiple bool
      ret=app.exec_()
      if ret>0:
	caja=app.selected()
	if len(caja)>0 and len(caja[0])>0:
	  self.sbCaja.setValue(int(caja[0][0]))
	  self.setCambio('pyventa','caja',self.sbCaja.value())		
	
      #print app.getFilas()
	
	#====SETTERS===
	
    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def setRecibePagos(self,bo):
	self.setCambio('pyventa','cobra',bo)		
	
    def setPrinter(self,st):
	self.setCambio('ticket','impresora',st)
	
    def setDriver(self,st):
	self.setCambio('ticket','driver',st)
	
    def setTicketTrigger(self,num):
	self.setCambio('ticket','trigger',str(num))		
	
    def setImprimeCopiaRecibo(self,bo):
	self.setCambio('ticket','copia',bo)
	if bo:
	  self.setCambio('ticket','copia-trigger',str(self.dsbCopia.value()))
	  
    def setImprimeTicket(self,bo):
	self.setCambio('ticket','default',bo)
	if bo:
	  self.setCambio('ticket','trigger',str(self.dsbTicketTigger.value()))
	  
    def setTicketTrigger(self,val):
      self.setCambio('ticket','trigger',str(self.dsbTicketTigger.value()))
      
    def setCopiaTrigger(self, val):
       self.setCambio('ticket','copia-trigger',str(self.dsbCopia.value()))
      
      #====GETTERS====
	
    def datos(self):
      return self.datos
    
    def boolint(self,boo=True):
    #recibe un booleano y lo transforma en 1 o 0
      if not boo: return 0
      else: return 1
      
    def closeEvent(self,event):
      self.cfg.guardar()
      
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = modulo(app,1)
    aw.show()
    sys.exit(app.exec_())
	
