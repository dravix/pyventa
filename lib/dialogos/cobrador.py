
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL,QTimer
from ui.ui_cobrador import Ui_Cobrador
from lib.modelos.qmodelotablasql import QModeloTablaSql
from lib.modelos.venta import Venta
class Cobrador(QDialog,Ui_Cobrador):
  def __init__(self,conexion,ventas,usuario,cliente,caja):
    #I.E. Selector(self,'proveedores','clientes','id,nombre,email','Id,Nombre del proveedor,E-Mail',"`nombre` like '%%%s%%' order by nombre desc limit 100")
    #Tablename, columnas y filtros vienen dadas por una cadena de elementos separados por comas y es lo que se pasa al query
    QDialog.__init__(self)
    self.setupUi(self)
    self.conexion=conexion
    self.wCambio.setVisible(False)
    self.ventas=ventas
    self.modelo=QModeloTablaSql(self.conexion.cursor,self)
    self.tabla.setModel(self.modelo)
    self.connect(self.leRecibo,SIGNAL("returnPressed()"),self.cobrar)
    self.connect(self.tbCobrar,SIGNAL("clicked()"),self.cobrar)
    self.iniciar()

    
  def iniciar(self):
    self.retorno=False
    venta=Venta(self.conexion)
    total=venta.sumaTotales(" id in ({ide}) and status=0".format(ide=",".join(self.ventas)))
    if total!=None:
      if total[0]==None:
	print "Todas las ventas ya estan pagadas"
	self.reject()
      else:
	self.total=float(total[0])
	self.dsbTotal.setValue(self.total)
	self.modelo.query("""Select notas.id, usuarios.usuario, cajas.nombre,total from notas,usuarios,cajas 
	where status=0 and notas.id in ({ide}) and id_usuario=notas.usuario and cajas.num_caja=caja """.format(ide=",".join(self.ventas)),
	    "id,usuario,caja,total".split(','))
	self.tabla.resizeColumnsToContents()  
	self.leRecibo.selectAll()


  def cobrar(self):
    if len(str(self.leRecibo.text()))>0:
      recibo=float(self.leRecibo.text())
      cambio=recibo-self.total
      if cambio<0:
	self.leRecibo.selectAll()
      else:
	venta=Venta(self.conexion)
	self.retorno=venta.cambiarEstado(self.ventas,1)
	if self.retorno:
	  self.dsbCambio.setValue(cambio)
	  self.wCambio.setVisible(True)
	  self.leRecibo.setEnabled(False)
	  self.tbCobrar.setEnabled(False)
	  #self.tbCerrar.setFocus(True)
	  QTimer.singleShot(10000,self.accept)
  
    
  #def seleccionado(self):
    #if len(self.tabla.selectedIndexes())>0:
      #nrow=(len(self.tabla.selectedIndexes())/self.modelo.columnCount(self))
      #ret = [range(self.modelo.columnCount(self)) for i in range(nrow)]
      #offset=self.tabla.selectedIndexes()[0].row()
      #for index in self.tabla.selectedIndexes():
	  ##print index.row(),index.column()
	  #ret[index.row()-offset][index.column()]=str(index.data().toString())
      #self.retorno=ret
      #self.done(1)