from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog
from ui.ui_cambia_precios import Ui_Form
from lib.modelos.qmodelotabla import QModeloTabla
from copy import deepcopy
from MySQLdb import Error
class CambiaPrecios(QDialog, Ui_Form):
  def __init__(self,parent,productos):
    #Productos debe ser una lista de productos con la forma [ref,descripcion,costo,ganancia,precio]
    QDialog.__init__(self,parent)
    self.setupUi(self)
    self.parent=parent
    self.cursor=parent.cursor
    self.productos=productos
    self.modelo=QModeloTabla(self.productos,["Ref","Descripcion","Costo","Ganancia","Precio"],self.parent)
    self.tvProductos.setModel(self.modelo)
    self.tvProductos.resizeColumnsToContents()
    self.connect(self.pbProbar, SIGNAL("clicked()"), self.aplicar)
    self.connect(self.pbRestaurar, SIGNAL("clicked()"), self.restaurar)
    self.connect(self.pbGuardar, SIGNAL("clicked()"), self.guardar)
    
  def aplicar(self):
    if self.chbCosto.checkState()==2:
      self.aplicarCosto()
    if self.chbGanancia.checkState()==2:
      self.aplicarGanancia()
    if self.chbPrecio.checkState()==2:
      self.aplicarPrecio()
    if self.chbIncremento.checkState()==2:
      self.aplicarIncremento()
      
  def restaurar(self):
    self.aplicarLista(self.productos)
  
  def aplicarCosto(self):
    self.tmps=deepcopy(self.productos)
    for item in self.tmps:
      item[2]=str(self.dsbCosto.value())
    self.aplicarLista(self.tmps)

    
  def aplicarGanancia(self):
    self.tmps=deepcopy(self.productos)
    for item in self.tmps:
      item[3]=str(self.dsbCosto.value())
      item[4]=float(item[2])+(float(self.dsbGanancia.value())*.01*float(item[2]))
    self.aplicarLista(self.tmps)
    
  def aplicarIncremento(self):
    self.tmps=deepcopy(self.productos)
    for item in self.tmps:
      item[2]=float(item[2])+(float(self.dsbIncremento.value())*.01*float(item[2]))
      item[4]=float(item[4])+(float(self.dsbIncremento.value())*.01*float(item[4]))
    self.aplicarLista(self.tmps)
    
  def aplicarPrecio(self):
    self.tmps=deepcopy(self.productos)
    for item in self.tmps:
      item[4]=str(self.dsbPreciop.value())
    self.aplicarLista(self.tmps)    
    
  def aplicarLista(self,lista):
    modelo=QModeloTabla(lista,["Ref","Descripcion","Costo","Ganancia","Precio"],self.parent)
    self.tvProductos.setModel(modelo)
    self.tvProductos.resizeColumnsToContents()
    
  def guardar(self):

    for item in self.tmps:
      try:
	sql="UPDATE productos set costo='{2}' , ganancia='{3}' , precio='{4}' WHERE ref={0}".format(*item)
	self.cursor.execute(sql)
      except Error, e:
	print "Error en el producto {0}, e={1}".format(item[0],e.args[0]),e
      else:
	self.cursor.execute("COMMIT")
#	print sql
	
      self.done(1)

  
    
    
