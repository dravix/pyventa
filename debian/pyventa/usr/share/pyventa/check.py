#!/usr/bin/env python
import sys, os
#aqui=os.getcwd()
#sys.path.append(os.path.join(aqui,'dialogos'))
aqui="/usr/share/pyventa/"    
home=os.path.join(os.path.expanduser('~'),"pyventa")
if sys.platform == 'linux2':
    home=os.path.join(os.path.expanduser('~'),".pyventa")

    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, 'Checador\0')
    except:
        pass
else:
	pass
	#home=os.path.join(aqui,'perfil')
sys.path.append(os.path.join(aqui,'lib'))
sys.path.append(os.path.join(aqui,'ui'))
#import MySQLdb as My, ConfigParser as Cp
from PyQt4 import QtCore
from PyQt4 import QtGui
#from PyQt4.QtCore import *
from ui_checador import Ui_MainWindow
from utileria import conexion
	
class Checador(QtGui.QMainWindow, Ui_MainWindow):  
    def __init__(self):
	QtGui.QDialog.__init__(self)
	self.setupUi(self)
	self.con=conexion()
	self.curser=self.con.curser
	self.cursor=self.con.cursor
	#self.db=QtSql.QSqlDatabase.addDatabase("QMYSQL")
	#self.db.setHostName(QString(host.data()));
	#self.db.setDatabaseName(QString(dba.data()));
	#self.db.setUserName(QString(user.data()));
	#self.db.setPassword(QString(pass.data()));
	self.full=False
	self.stack.setCurrentIndex(0)
	self.codigo.setFocus(True)
	self.connect(self.tbTop, QtCore.SIGNAL("clicked()"), self.pantalla)
	self.connect(self.codigo, QtCore.SIGNAL("returnPressed()"), self.checar)
	

    def pantalla(self):
	if self.full==True:
	  self.showNormal()
	  self.full=False
	else:
	  self.showFullScreen()
	  self.full=True

    def checar(self):
	line=str(self.codigo.text())
	if len(line)>0:
	  self.curser.execute('SELECT ref,`descripcion`, `precio`, nombre as unidad from productos,unidades as u where unidad=u.id and codigo='+line+' or ref='+line+' limit 1;')
	  prod=None
	  prod=self.curser.fetchone()
	  cad=''
	  if prod!=None:
	    promos=self.checkAllPromos(prod['ref'])#Devuelve una lista [(nombre, minimo,descuento,precio-descuento)]
	    if len(promos)>0:
	      for promo in promos:
		cad+="A partir de %s %s : <b>$%s</b><br/>"%(promo[1],prod['unidad'],promo[3])
	      cad="<p style=\"font-size:17px\">%s</p>"%cad
	  else:
	    prod={"descripcion":"Lo sentimos, pero este producto no fue encontrado, verifique nuevamente o pregunte en cajas.",'precio':''}
	  self.lblInfo.setText(prod['descripcion'])
	  self.stack.setCurrentIndex(1)  
	  self.lblPrecio.setText("<h2>Precio: $%s</h2>%s"%(prod['precio'],cad))
	  self.codigo.clear()
	  self.codigo.setFocus(True)
	

    def checkAllPromos(self,ref):
	  promos=[]
	  self.curser.execute("SELECT `ref`,`precio`, familia, departamento  FROM productos,familias where ref=%s AND familia=familias.id   AND familia=familias.id limit 1"%ref)
	  prod = self.curser.fetchone()
	  if prod!=None:
	    self.cursor.execute("SELECT nombre,minimo, descuento, %s-(%s*descuento*0.01) FROM ofertas as O,promociones as P WHERE ((tipo=0 and conjunto=%s) OR (tipo=1 and conjunto=%s) OR (tipo=2 and conjunto=%s)) AND O.promocion=P.id AND curdate() BETWEEN P.inicio AND P.fin  order by P.descuento desc "%(prod['precio'],prod['precio'],prod['ref'],prod['familia'],prod['departamento']))
	    oferta=self.cursor.fetchall()
	    if oferta !=None:
	      oferta=list(oferta)
	      promos.extend(oferta)
	    return promos
	    
if __name__=="__main__":

    app = QtGui.QApplication(sys.argv)
    app.processEvents()
    aw = Checador()
    aw.show()
    app.exec_()