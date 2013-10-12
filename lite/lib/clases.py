from PyQt4 import QtCore, QtGui#,  Qt
import MySQLdb as My, os, sys
import lib.libutil,tarfile,datetime, csv 


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
    

