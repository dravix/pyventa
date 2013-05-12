#Modulos de cuentas pendientes
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QWidget, QAction, QIcon
from lib.modelos.qmodelotablasql import QModeloTablaSql

from ui.ui_pendientes import Ui_Form
class Pendientes(QWidget, Ui_Form):
  def __init__(self,parent,id):
	  QWidget.__init__(self)
	  self.setupUi(self)
	  self.datos={'nombre':"Pendientes",'descripcion':"Control de cuentas pendientes",'version':"0.7",'id':id,'nivel':3}
	  self.id=id
	  self.action = QAction(self)
	  self.parent=parent
	  self.action.setIcon(QIcon(":/modulos/images/png/elegant/pending.png"))
	  self.action.setIconVisibleInMenu(True)
	  self.action.setText(self.datos['nombre'])
	  self.connect(self.action, SIGNAL("triggered()"), self.ver )
	  self.modelo=QModeloTablaSql(parent.cursor,self)
	  self.tvCuentas.setModel(self.modelo)
	  self.init()
	  self.setupEvents()
	  
	  
  def init(self):
    self.ids=False
    self.cliente=False
    
    
    
  def ver(self):
    self.parent.move(self.datos['nombre'])
    self.listar()
    
  def listar(self):
    if self.cbTipo.currentIndex()==1: #Cuando se seleccione "Notas" 
      head=['Id','Total','Fecha','Cliente','Vendedor','Caja']    
      sql="""SELECT notas.id,total , fecha,  SUBSTR(clientes.nombre,1,12), usuarios.usuario,
      caja FROM notas, clientes, usuarios where notas.usuario=usuarios.id_usuario and cliente=clientes.id 
      and status=0 and tipo=0 order by fecha"""
    else: #Cuando se seleccione "Todas las ventas"    
      sql="""SELECT notas.id, total,fecha,ELT(notas.tipo+1,'Nota','Factura'),SUBSTR(clientes.nombre,1,12), usuarios.usuario, caja   FROM notas, clientes, usuarios where notas.usuario=usuarios.id_usuario and cliente=clientes.id and status=0 order by fecha"""
      head=['Id','Total','Fecha','Tipo','Cliente','Vendedor','Caja']
    self.modelo.query(sql,head)
    self.tvCuentas.resizeColumnsToContents()
    
  def setupEvents(self):
    self.connect(self.ncactualizar,SIGNAL("clicked()"), self.listar)