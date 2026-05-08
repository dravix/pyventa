# -*- coding: utf-8 -*-
import sys, os, datetime, urllib.request, tarfile, base64
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from dialogos.ui_acceso import Ui_Form
import  datetime
import MySQLdb, ConfigParser  
class acceso(QtWidgets.QDialog, Ui_Form):
    def __init__(self):
                QtWidgets.QDialog.__init__(self)
                self.setupUi(self)
                self.cursor=None
                self.home=home
                self.count=0
                self.pbAceptar.setDefault(True)
                #self.leClave.returnPressed.connect(self.autentificar)
                self.pbAceptar.clicked.connect(self.autentificar)
                self.connect(self.pbCerrar, SIGNAL("clicked()"), lambda:self.done(-1))
                self.conexion()

    def check(self):
        if os.path.exists(os.path.join(self.home,"config.cfg")):
          return True
        else:
          return False

    def conexion(self):
                self.cfg = ConfigParser.ConfigParser()
                if self.check():
                        self.cfg.read([os.path.join(self.home,"config.cfg")])
                        try:
                            host = self.cfg.get("mysql", "host")  
                            usuario = self.cfg.get("mysql", "usuario")  
                            claveword = base64.b64decode(self.cfg.get("mysql", "clave"))
                            data = self.cfg.get("mysql", "db")
                            self.db = MySQLdb.connect(host, usuario, claveword,data)
                        except:
                              print("Error: No fue posible establecer la conexion con la base de datos.")
                        else:                
                            self.cursor = self.db.cursor()
                            self.curser= self.db.cursor(MySQLdb.cursors.DictCursor)

                else:
                        print("Error: El archivo de configuracion no especifica los datos necesarios para la conexion")
          
    
    def autentificar(self):
        usuario=str(self.leUsuario.text())
        clave=str(self.leClave.text())
        
        if len(usuario)>0:
          self.curser.execute("SELECT * from usuarios where usuario='"+str(usuario)+"' and clave=MD5('"+str(clave)+"')")

          try:
            self.curser.execute("SELECT * from usuarios where usuario='"+str(usuario)+"' and clave=MD5('"+str(clave)+"')")
          except:
            self.lbInfo.setText("Hay un problema con la base de datos, es posible que sus datos sean incorrectos")
          else:
            usuario=self.curser.fetchone()
            if usuario!=None:
              if usuario['nivel']>2:
                self.lbInfo.setText("<h2>Bienvenido %s </h2>"%usuario['nombre'])
                self.done(int(usuario['id']))
              elif usuario['nivel']>0:
                self.lbInfo.setText("<h3>Su nivel de acceso no es suficiente.</h3>")
                self.leUsuario.setFocus(True)
            else:
                if self.count<2:
                  self.lbInfo.setText("<h3>El usuario/clave son incorrectos</h3> Intentelo nuevamente.")
                  self.count+=1
                else:
                  self.done(-1)

aqui="/usr/share/pyventa/"              
#if sys.platform == 'linux2':
    ## Set process nombre.  Only works on Linux >= 2.1.57.
home=os.path.join(os.path.expandusuario('~'),"pyventa/")
if sys.platform == 'linux2':
    home=os.path.join(os.path.expandusuario('~'),".pyventa")
#else:
    #home=os.path.join(aqui,'perfil')