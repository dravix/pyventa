from ui.ui_acceso import Ui_Acceso
from PyQt4.QtCore import SIGNAL, QTimer
from PyQt4.QtGui import QDialog, QPixmap, QCursor
from lib.librerias.conexion import Conexion
from lib.librerias.comun import *
import MySQLdb
class Seguridad(QDialog, Ui_Acceso):
    def __init__(self,parent=None, nivel=1,logo=False, nombre="Pyventa"):
    		QDialog.__init__(self,parent)
		#self.con=conexion()
		#self.curser=self.con.curser
		self.setupUi(self)
		self.nivel=nivel
		self.parent=parent
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.lbInfo.setText("<h4>{0}</h4>".format(nombre.capitalize()))
		if logo:
		  self.logo.setPixmap(QPixmap(logo))
		self.home=home
		self.count=0
		self.usuario={'nivel':0,'nombre':'Pyventa','usuario':'Pyventa','id_usuario':1}
		self.pbAceptar.setDefault(True)
		self.pbCerrar.setVisible(True)
		self.lblServidor.setVisible(False)
		self.cbServidores.setVisible(False)
		self.leClaveServidor.setVisible(False)
		self.lblClaveServidor.setVisible(False)
		self.lblAlerta.setVisible(False)
		self.updateGeometry()
		try:
		  self.cursor.execute("SELECT * from conexiones")
		  self.conexiones=self.cursor.fetchall()
		  self.cbServidores.addItem("Local",0)
		  for c in self.conexiones:
		    self.cbServidores.addItem(c[1],c[0])
		except:
		  self.pbRemoto.setVisible(False)
		else:
		  self.pbRemoto.setVisible(True)
        	self.connect(self.leClave, SIGNAL("returnPressed()"), self.autentificar)
        	self.connect(self.pbAceptar, SIGNAL("clicked()"), self.autentificar)
        	self.connect(self, SIGNAL("reject()"), self.getUser)
        	self.connect(self.pbCerrar, SIGNAL("clicked()"), lambda:self.done(-1))
        	self.connect(self.pbRemoto, SIGNAL("toggled(bool)"), self.activateRemote)
        	#self.connect(self.cbServidores, SIGNAL("currentIndexChanged ( int  )"), self.changeConection)
        	
        	
    def getUser(self):
      return self.usuario
      
    def activateRemote(self,boo):
	  self.lblServidor.setVisible(boo)
	  self.cbServidores.setVisible(boo)
	  self.leClaveServidor.setVisible(boo)
	  self.lblClaveServidor.setVisible(boo)
	  self.adjustSize()
      
    def changeConection(self, index):
      self.setCursor(QCursor(3))
      if index>0:#Si no es local
	conexion=self.conexiones[index-1]
	#if 
	conn={'host':conexion[2],'schema':conexion[3],'user':conexion[5],'pass':str(self.leClaveServidor.text())}
	try:
	  db = MySQLdb.connect(conn['host'], conn['user'], conn['pass'],conn['schema'])
	except MySQLdb.Error,e:
	  self.setCursor(QCursor(0))
	  if (e.args[0]==1045):
	    self.notify("Acceso denegado. \nPor favor verifique su clave de servidor")
	  elif (e.args[0] in range(2001,2006)):
	    self.notify("Acceso denegado. \nEl servidor no se encuentra disponible")
	  elif (e.args[0] ==1049):
	    self.notify("Acceso denegado. \nLa base de datos no fue localizada, es posible que no exista")
	  else:
	    print e.args[0],"\nError al conectar a la base de datos"#,(self._host, self._user, self._pass,self._schema)
	  return False
	else: 
	  self.setCursor(QCursor(0))
	  self.cursor = db.cursor()
	  self.curser=  db.cursor(MySQLdb.cursors.DictCursor)	
	  return True
      return True
    
    def notify(self,info):
	  QTimer.singleShot(50000,self.ocultarAlerta )
	  self.lblAlerta.setVisible(True)
	  self.lblAlerta.setText(info)
	  
    def ocultarAlerta(self):
      self.lblAlerta.setVisible(False)

    def autentificar(self):
	if self.changeConection(self.cbServidores.currentIndex()):
	  usuario=str(self.leUsuario.text())
	  clave=str(self.leClave.text())
	  
	  if len(usuario)>0:
	      self.curser.execute("SELECT * from usuarios where usuario='{0}' and clave=MD5('{1}')".format(usuario,clave))    
	      user=self.curser.fetchone()
	      if user!=None:
		if user['nivel']>=self.nivel:
		  self.lbInfo.setText("<h2>Bienvenido %s </h2>"%user['nombre'])
		  print "Bienvenido %s "%user['nombre']
		  self.usuario=user
		  self.done(int(user['id_usuario']))
		else:
		    self.notify("Su nivel de acceso es menor al necesario, consulte con su superior.")
	      else:
		  if self.count<2:
		    self.notify("El usuario/clave son incorrectos\nIntentelo nuevamente (Intentos {0}).".format(self.count))
		    self.count+=1
		  else:
		    self.done(-1)
