# -*- coding: utf-8 -*-
import sys,os,base64, time
from PyQt4 import QtCore, QtGui
from ui_bd_config import Ui_Dialog
import MySQLdb, ConfigParser
class configurador(QtGui.QDialog, Ui_Dialog):  
    def __init__(self,configFile):
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
		self.configFile=configFile
		print self.configFile

    def setDB(self):
	print self.configFile
	self.cfg = ConfigParser.ConfigParser()
	if(self.cfg.read([self.configFile])):
	  self.cfg.set('mysql','host',self.host)
	  self.cfg.set('mysql','user',self.user)
	  self.cfg.set('mysql','pass',base64.b64encode(self.password))
	  self.cfg.set('mysql','db',self.db)
	  self.cfg.write(open(self.configFile,"w+"))
	  self.done(1)
	else:
	  print "No se encontro"+self.configFile
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
                db = MySQLdb.connect(self.host, self.user, self.password)
		c=db.cursor()
		stout=None
		try:
		  stout=c.execute(tpv)		#
		except MySQLdb.Error, e:
		  if (e.args[0]==1007):
		    print "Ya existe una base de datos con el nombre de tpv"
		else:
		  progress.setValue(2)
		  progress.setLabelText("Volcando la base de datos por defecto.")
		  for i in range(15):
		    time.sleep(.4)
		  progress.setValue(3)
		  progress.setLabelText("Estableciendo administrador")
		#
		try:
		    self.db="tpv"
	            db = MySQLdb.connect(self.host, self.user, self.password,self.db)
		except MySQLdb.Error, e:
		  print e
		else:
		  cursor=db.cursor()
		  cursor.execute("update usuarios  set pass=MD5('%s') where user like 'admin'"%self.password)
		  print self.password
		  self.display.setText('<h2>Se creo la base de datos</h2><p>'+str(stout)+'</p><h2>Cuenta de administrador</h2><p>Se ha establecido como administrador el usuario <b>admin</b> con la misma clave de acceso que tu base de datos, es recomendable que la cambies desde el adminstrador para mejorar la seguridad.</p>')
		  progress.setValue(4)
		  time.sleep(5)
		  self.setDB()
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

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = configurador()
    aw.show()
    sys.exit(app.exec_())
	
