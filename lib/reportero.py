import sys
sys.path.append('/home/dave/Dropbox/Pyventa/pyventa-2.3/lib')
sys.path.append('/home/dave/Dropbox/Pyventa/pyventa-2.3/ui')
#import MySQLdb
from utileria import conexion
import  libutil
from librepo import Ventas, Chart
from ui_reportero import Ui_Reporte
from PyQt4 import QtCore, QtGui

#cant=input("Ingrese la cantidad")
class Reporte(QtGui.QDialog, Ui_Reporte): 
  def __init__(self):
    QtGui.QDialog.__init__(self)
    self.setupUi(self)
    self.deDesde.setDate(QtCore.QDate.currentDate())
    self.deHasta.setDate(QtCore.QDate.currentDate())
    self.connect(self.tbVer, QtCore.SIGNAL("clicked()"), self.ejecutar)
    self.connect(self.tbPrint, QtCore.SIGNAL("clicked()"), self.imprimir)
    self.con=conexion()
    self.consulta={'titulo':'Mejores productos Temporada','descripcion':'Productos con mas ventas','fecha':''}
    
  def getPeriodo(self,campo='fecha'):
      inicio=str(self.deDesde.date().toString('yyyy-MM-dd'))
      fin=str(self.deHasta.date().toString('yyyy-MM-dd'))
      if (inicio==fin):
	self.periodo=" date(%s)='%s'"%(campo,inicio)
      else:
	self.periodo=" date(%s) BETWEEN '%s' and  '%s' "%(campo,inicio,fin)
      return self.periodo
    
  def ejecutar(self):
      qry=str(self.pteQuery.toPlainText() )
      tup=self.con.query(qry.replace('<rango>',self.getPeriodo('fecha')))
      self.header= [key[0] for key in self.con.cursor.description]
      if tup!=None:
	self.modelo=libutil.tabular(self.tvTabla, tup,self.header)

	#for item in tup:
	  #print item
  def imprimir(self):
      vector=self.modelo.getVector()
      #head=[[len(row),row] for row in self.header]
      tabla=libutil.listaHtml(vector,self.consulta['descripcion'],self.header,'#001931',"#eee", 10) 
      libutil.printa(tabla,"%s %s-%s"%(self.consulta['titulo'],self.deDesde.date().toString('dd.MMM.yy'),self.deHasta.date().toString('dd.MMM.yy')))
    
if __name__=="__main__":
  #ref=input("Ingrese la ref: ")
  #cant=input("Ingrese la cantidad: ")

  #superior(ref)
  #inferior(ref)
  #print tabla
  app = QtGui.QApplication(sys.argv)
  app.processEvents()
  aw = Reporte()
  aw.show()
  app.exec_()
    