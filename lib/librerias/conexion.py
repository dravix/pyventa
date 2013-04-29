from lib.librerias.configurador import Configurador
from lib.db_conf import configurador as BDConfig
from lib.librerias.comun import *
import base64
from os.path import join
import MySQLdb
from PyQt4.QtCore import QTimer
from lib.dialogos.notificaciones import notify
class Conexion:
    def __init__(self, parent, config=False,datos=False):
	self.parent=parent
	if datos and isinstance(datos,dict) and len(datos)>0:
	  self._host=datos['host']
	  self._user=datos['user']
	  self._pass=datos['pass']
	  self._schema=datos['schema']
	  self.conectar()
	else:
	  if not config:
	    self.cfg = Configurador(parent)
	  else :
	    self.cfg=config
	  if self.cfg.stat:
	    self._host=self.cfg.getDato('mysql','host')
	    self._user=self.cfg.getDato('mysql','user')
	    self._pass=base64.b64decode(self.cfg.getDato('mysql','pass'))
	    self._schema=self.cfg.getDato('mysql','db')
	    self.conectar()
	  else:
	    self.stat=False

    def asistente(self):
	print "Configurando base de datos"
	ui = BDConfig(self.cfg)
	dialog=ui.exec_()
	if (dialog==1):
	  self.__init__(self.parent)  
	else:
	  self.stat=False
	  
    def conectar(self):
      try:
	self.db = MySQLdb.connect(self._host, self._user, self._pass,self._schema)
      except MySQLdb.Error,e:
	    if e.args[0]==2006: #Cuando el servidor se ha ido
	      notify(self.parent,'error','El servidor se ha ido', "El servidor ha cerrado la conexion, reconectando en 10 segundos")
	      QTimer.singleShot(10000,self.conectar)
	    else:
	      print e,"\nError al conectar a la base de datos"#,(self._host, self._user, self._pass,self._schema)
	      self.asistente()
      else:                
	  self.cursor = self.db.cursor()
	  self.curser=  self.db.cursor(MySQLdb.cursors.DictCursor)	
	  self.stat=True


    def close(self):
	self.db.close()
	
    def ejecutar(self,sql,dic=False):
      if dic:
	cursor=self.curser
      else:
	cursor=self.cursor
      try:
	cursor.execute(sql)
      except MySQLdb.Error, e:
	if e.args[0] in (2006,2013):
	  print "Se perdio la conexion al intentar executar una consulta"
	  self.conectar
	else:
	  raise(e)
	
    def query(self,string,single=False,tipo=0):
      if tipo==0: #Tipos{ 0:Tupla,1:Diccionario} 
	cursor=self.cursor
      else:
	cursor=self.curser  
      try: 
	cursor.execute(string)
      except MySQLdb.Error, e:
	if (e.args[0]==2006):
	  self.conectar()
	elif (e.args[0]==1054):
	  print "La version de la base de datos es incorrecta. Configure nuevamente la base de datos"
	  print e
	  self.asistente()
	else:
	  print e
	  return None
      else:
	ret=None
	if single: #Single es en caso de que se requiera solo un resultado devuelve una tupla, caso contrario una lista de tupla
	  ret=cursor.fetchone()
	  return ret
	else:
	  ret=cursor.fetchall()
	  return ret
	
