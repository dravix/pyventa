from lib.librerias.configurador import Configurador
from lib.db_conf import configurador as BDConfig
from lib.librerias.comun import *
import base64
from datetime import datetime
from os.path import join,exists
import MySQLdb
from PyQt4.QtCore import QTimer
from lib.dialogos.notificaciones import notify
from lib.librerias.comun import *
import sqlite3,shutil,hashlib
class Conexion:
    def __init__(self, parent, config=False,datos=False,driver=False):
	self.parent=parent
	if datos and isinstance(datos,dict) and len(datos)>0:
	  self._host=datos['host']
	  self._user=datos['user']
	  self._pass=datos['pass']
	  self._schema=datos['schema']
	  self.driver='mysql'
	  self.conectar()
	else:
	  if not config:
	    self.cfg = Configurador(parent)
	  else :
	    self.cfg=config
	  if self.cfg.stat:
	    if not driver:
		driver=self.cfg.getDato('pyventa','motor')
	    self.driver=driver
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
    
    def lastId(self):
      if self.driver=='sqlite3':
       return "SELECT last_insert_rowid();"
      else:
	return "SELECT LAST_INSERT_ID();"
      

    def conectar(self):
      if self.driver=='sqlite3':
	dbpath=join(home,"pyventa.db")
	if exists(dbpath):
	  self.db=sqlite3.connect(dbpath)
	  self.db.create_function("NOW", 0, ahora)
	  self.db.create_function("CURDATE", 0, hoy)
	  self.db.create_function("DATE_FORMAT", 2, dateformat)
	  self.db.create_function("ELT", -1, elt)
	  self.db.create_function("MD5", 1, md5)
	  self.cursor=self.db.cursor()
	  self.curser=self.db.cursor()
	  self.stat=True
	else:
	  try:
	    shutil.copy(join(self.parent.raiz,"perfil","pyventa.db"),dbpath)
	  except shutil.Error, e:
	    print "No se encontro el archivo de la base de datos y no se pudo copiar una nueva"
	    raise(e)
	  else:
	    self.conectar()
      else:
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

    def commit(self):
      if self.driver=='sqlite3':
	self.db.commit()
      else:
	pass
	#self.cursor.execute("COMMIT")
    def affected(self):
      if self.driver=='sqlite3':
	return self.cursor.rowcount
	
    def ultimo(self):
      if self.driver=='sqlite3':	
	  return self.cursor.lastrowid
      else:
	return self.db.insert_id()
      
	
    def rollback(self):
      if self.driver=='sqlite3':
	self.db.rollback() 
      else:
	pass
	#self.cursor.execute("ROLLBACK")

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
	
def ahora():
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def md5(string):  
  return hashlib.md5(string).hexdigest()

def hoy():
  return datetime.now().strftime("%Y-%m-%d")

def elt(n,*args):
  #tupla=tupla.replace('(','').replace(')','').split(',')
  n-=1
  if n<=len(args):
    return args[n]
  else:
    return ''

def dateformat(fecha,formato):
  return datetime.strptime(fecha,"%Y-%m-%d %H:%M:%S").strftime(formato)
	
def dicursor(cursor,row):
      if isinstance(cursor,sqlite3.Cursor):
	if isinstance(row, list):
	  li=[]
	  for item in row:
	    li.append(dicursor2(cursor,item))
	  return li
	elif isinstance(row, tuple):
	  return dicursor2(cursor,row)
      else:
	return row
	  
def dicursor2(cursor,row):
    if isinstance(cursor,sqlite3.Cursor):
      d = {}
      for idx,col in enumerate(cursor.description):
	      d[col[0]] = row[idx]
      return d 	  	
    else:
      return row
