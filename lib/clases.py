from PyQt4 import QtCore, QtGui#,  Qt
from ui.ui_agregar_gasto import Ui_Form as Ui_Gasto
import MySQLdb as My, os, sys
import lib.libutil,tarfile,datetime, csv 
from lib.modelos.gasto import Gasto 
from lib.modelos.compra import Compra 
from lib.modelos.venta import Venta 
from lib.modelos.caja import Caja 
class Gasto:
    def __init__(self, parent):
      self.parent=parent
      self.cursor=self.parent.cursor
    
    def agregar(self):
	usuario=self.parent.aut(2)
	if int(usuario)>0:
	    nuevo=NuevoGasto(self.parent,usuario)
	    if nuevo.exec_()>0:
	      return True 
	    else:
	      False
	else:
	  False
	      
    def eliminar(self,ide):
      if ide>0:
	try:
	  self.cursor.execute("DELETE FROM gastos where num_gasto=%s;"%ide)
	except:
	  return False
	else:
	  self.parent.conexion.commit()
	  return True
	  
class NuevoGasto(QtGui.QDialog, Ui_Gasto):
    def __init__(self, parent,usuario):
    		QtGui.QDialog.__init__(self)
		self.parent=parent
		self.usuario=usuario
		self.caja=self.parent.caja
		self.cursor=self.parent.cursor
		self.setupUi(self)
        	#self.connect(self.leClave, SIGNAL("returnPressed()"), self.autentificar)
        	self.connect(self.tbDone, QtCore.SIGNAL("clicked()"), self.agregar)
        	self.connect(self.tbCancelar, QtCore.SIGNAL("clicked()"), lambda:self.done(-1))
        	self.leConcepto.setFocus()

		if self.caja<1:
		  #print self.caja
		  self.lbinfo.setText('<h3 style="color:#C00">Este punto de venta no es Caja.</h3> \nLos gastos deben ser manejados desde una caja')
		  self.dsbCantidad.setEnabled(False)
		  self.leConcepto.setEnabled(False)

    def agregar(self):
      if self.caja>1:
	try:
	  self.cursor.execute("""INSERT INTO gastos VALUES(NULL,%s,%s,NOW(),%s,%s) """%(self.usuario,self.caja,self.leConcepto.text(),self.dsbCantidad.value()))
	except:
	  self.info.setText('Ha ocurrido un error, verifique los datos e intente mas tarde')
	else:
	    self.done(1)
      else:
	self.lbinfo.setText('Este punto de venta no es Caja. \nLos gastos deben ser manejados desde una caja')

class Mantenimiento:
  def __init__(self):
    self.cursor=libutil.conectar()
    
  def crearPefil(self):
      if sys.platform == 'linux2':   
	os.system("cp -r /usr/share/pyventa/perfil/* "+libutil.home())
      else:
	os.system("xcopy \usr\share\pyventa\perfil \"%s\" /i /a /e /k"%self.home)
      msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Reinicio programado","<h2>La operacion ha tenido exito</h2><br><p>Ahora se recopilaran los datos necesarios para la base de datos, despues de eso el programa se cerrara para establecer las configuraciones.</p>.",QtGui.QMessageBox.Close,self)
      msgBox.exec_()
      
  
  def tablaACsv(self,nombre,ruta):	#exporta una tabla a csv
      tabla=os.path.join(ruta,"%s.csv"%nombre)
      tablaF=open(tabla,'wb')
      chivo = csv.writer(tablaF, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
      sql="DESCRIBE %s"%nombre
      self.cursor.execute(sql)
      result = self.cursor.fetchall()
      chivo.writerow([col[0] for col in result])
      sql="SELECT * FROM %s  "%(nombre)
      self.consulta(sql)
      ff=self.cursor.fetchall()
      for row in ff:
	chivo.writerow(row)
      tablaF.close()
      return tabla
  
  def respaldo(self):
    sql="SHOW TABLES;"
    self.cursor.execute(sql)
    tabs=self.cursor.fetchall()
    fecha=str(datetime.date.today().strftime("%d.%m.%Y"))
    home=libutil.home()
    files=[]
    out = tarfile.TarFile.open(os.path.join(home,"bd.respaldo.%s.tar.bz2"%fecha),'w:bz2')
    for i,tab in enumerate(tabs):
      tabla=self.tablaACsv(tab[0],home)
      files.append(tabla)
      out.add(tabla,arcname="%s.csv"%tab[0])
      os.unlink(tabla)
      print "Progreso: ",(i+1)*100/len(tabs),"%"
    out.close()
      
      
  def limpiarVentas(self,fecha):
    sql="DELETE FROM notas as n,notas_cobradas as nc,vendidos as v where date(fecha)<%s and nc.nota=n.id and v.venta=n.id;"%fecha
    return self.consulta(sql)
      
  def limpiarProductos(self):
    sql="UPDATE productos SET vendidas=0, ultima_modificacion=current_timestamp"
    return self.consulta(sql)  
  
  def limpiarExistencias(self):
    sql="INSERT INTO existencia SELECT ref,1,0,0,0 FROM productos WHERE ref NOT IN (SELECT producto from existencia)"
    return self.consulta(sql)  
    
  def consulta(self,sql):
    try:
      self.cursor.execute(sql)
    except My.Error, e:
      print e
      return False
    else:
      return True
    

