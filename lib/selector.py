
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL
from ui.ui_selector import Ui_Seleccion
from lib.modelos.qmodelotablasql import QModeloTablaSql
class Selector(QDialog,Ui_Seleccion):
  def __init__(self,parent, entidad,tablename=False,columnas=False,heads=False,filtros=True):
    #I.E. Selector(self,'proveedores','clientes','id,nombre,email','Id,Nombre del proveedor,E-Mail',"`nombre` like '%%%s%%' order by nombre desc limit 100")
    #Tablename, columnas y filtros vienen dadas por una cadena de elementos separados por comas y es lo que se pasa al query
    QDialog.__init__(self)
    self.setupUi(self)
    self.parent=parent
    self.nombre=entidad.capitalize()
    self.tablename=tablename.lower()
    self.columnas=columnas
    self.filtros=filtros
    if heads: self.heads=heads.split(',')
    else: self.heads=columnas.split(',')
    #print self.heads
    self.leEntidad.setText(self.nombre+':')
    self.setWindowTitle("Seleccionador de {0}".format(self.nombre))
    self.modelo=QModeloTablaSql(self.parent.cursor,self)
    self.tabla.setModel(self.modelo)
    self.connect(self.texto,SIGNAL("textChanged(QString)"),self.buscar)
    self.connect(self.tabla,SIGNAL("activated(const QModelIndex&)"),self.seleccionado)
    
  def buscar(self,texto=False):
    texto=str(texto)
    if len(texto)>3 or texto=='*':
      if texto=='*':
	sql="SELECT {0} FROM {1};".format(self.columnas,self.tablename)
      else:
	sql="SELECT {0} FROM {1} where {2} ;".format(self.columnas,self.tablename,self.filtros.format(texto))
      #print sql
      self.modelo.query(sql,self.heads)
      self.tabla.resizeColumnsToContents()
  

  def seleccionado(self):
    ret=[]
    for index in self.tabla.selectedIndexes():
      if index.column()==0:
	ret.append([str(index.data().toString())])
      else:
	ret[len(ret)-1].append(str(index.data().toString()))
    self.retorno=ret
    self.done(1)