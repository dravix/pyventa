# -*- coding: utf-8 -*-
import sys,os,base64, time
from PyQt4 import QtCore, QtGui
from ui.ui_bd_config import Ui_Dialog
import MySQLdb, ConfigParser
class configurador(QtGui.QDialog, Ui_Dialog):  
    def __init__(self,configFile=-1):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.connect(self.bprobar, QtCore.SIGNAL("clicked()"), self.conexion )
		self.connect(self.bset, QtCore.SIGNAL("clicked()"), self.setDB )
		self.connect(self.bclose, QtCore.SIGNAL("clicked()"), self.close )
		self.connect(self.bcreate, QtCore.SIGNAL("clicked()"), self.crearDB )
		self.bcreate.setEnabled(False)
		self.host=''
		self.user=''
		self.password=''
		self.db='tpv'
		if configFile!=-1:
		  self.cfg=configFile
		  self.iniciar()

    def iniciar(self):
	  self.tserver.setText(self.cfg.get('mysql','host'))
	  self.tuser.setText(self.cfg.get('mysql','user'))
	  self.tpass.setText(self.cfg.get('mysql','pass'))
	  self.tdb.setText(self.cfg.get('mysql','db'))

	  
    def setDB(self):

	  self.cfg.set('mysql','host',self.host)
	  self.cfg.set('mysql','user',self.user)
	  self.cfg.set('mysql','pass',base64.b64encode(self.password))
	  self.cfg.set('mysql','db',self.db)
	  self.cfg.guardar()
	  self.done(1)

	  
    def crearDB(self):
		progress=QtGui.QProgressDialog("Cargando la base de datos","Cerrar", 0, 4, self)
		#progress.setWindowModality(Qt.WindowModal)
		fi=open('/usr/share/pyventa/perfil/db.sql')
		tpv=fi.read()
		progress.setValue(1)
		progress.setLabelText("Verificando BD anteriores")
		self.host=str(self.tserver.text())
		self.user=str(self.tuser.text())
		self.password=str(self.tpass.text())  
		self.db=str(self.tdb.text())
		try:
		  db = MySQLdb.connect(self.host, self.user, self.password,self.db)
		except MySQLdb.Error, e:
		  if (e.args[0]==1049):
		    try:
		      db = MySQLdb.connect(self.host, self.user, self.password)
		      c=db.cursor()
		      stout=c.execute("CREATE DATABASE %s;"%self.db)
		      self.crearDB()
		      return
		    except:
		      print "Error al tratar de crear una base de datos"
		      return
		else:
		  c=db.cursor()
		  stout=None
		  progress.setValue(2)
		  progress.setLabelText("Volcando la base de datos por defecto.")
		  c.execute(tpv)	
		  for i in range(15):
		    time.sleep(.4)#
		  progress.setValue(3)
		  progress.setLabelText("Estableciendo administrador")
		  self.configAdmin(c)
		  progress.setValue(4)
		  self.setDB()
		    
    def configAdmin(self, cursor):
	try:
	  cursor.execute("UPDATE usuarios  set clave=MD5('%s') where usuario='admin' "%self.password)
	  cursor.execute("INSERT INTO `usuarios` (`id_usuario`, `nombre`, `usuario`, `clave`, `nivel`) VALUES (1, 'Usuario Administrador', '%s', '%s', 5); "%(self.user,self.password))
	except MySQLdb.Error, e:
	  print e,"Linea 88"
	else:
	  self.display.setText('<h2>Se creo la base de datos</h2><h2>Cuenta de administrador</h2><p>Se ha establecido como administrador el usuario <b>admin</b> con la misma clave de acceso que tu base de datos, es recomendable que la cambies desde el adminstrador para mejorar la seguridad.</p>')
	  
    def conexion(self):
		host=str(self.tserver.text())
		user=str(self.tuser.text())
		password=str(self.tpass.text())
		base=str(self.tdb.text())
		try:
	            db = MySQLdb.connect(host, user, password,base)
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
                	self.bcreate.setEnabled(True)
                	self.display.setText('<h1>Conectado.</h1><p>Guarde esta configuracion para que Pyventa se conecte usando esta base de datos</p>')
                	self.host=str(self.tserver.text())
			self.user=str(self.tuser.text())
			self.password=str(self.tpass.text())
			self.db=base   

    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = configurador()
    aw.show()
    sys.exit(app.exec_())
	
