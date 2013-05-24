#Modulos de cuentas pendientes
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QWidget, QAction, QIcon, QDialog, QMenu, QMessageBox
from lib.modelos.qmodelotablasql import QModeloTablaSql
from lib.dialogos.agrega_gasto import AgregaGasto
from lib.dialogos.cobrador import Cobrador
from ui.ui_caja import Ui_Form
from lib.selector import Selector
from lib.dialogos.visor_venta import VisorVenta 


class Caja(QWidget, Ui_Form):
  def __init__(self,parent,id):
	  QWidget.__init__(self)
	  self.setupUi(self)
	  self.datos={'nombre':"Caja",'descripcion':"Control de cuentas pendientes",'version':"0.7",'id':id,'nivel':3}
	  self.id=id
	  self.action = QAction(self)
	  self.parent=parent
	  self.action.setIcon(QIcon(":/modulos/images/png/elegant/sales.png"))
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
    
  def setupEvents(self):
    self.connect(self.ncactualizar,SIGNAL("clicked()"), self.listar)
    self.connect(self.tbRetirar,SIGNAL("clicked()"), self.retirar)
    self.connect(self.tbDepositar,SIGNAL("clicked()"), self.depositar)
    self.connect(self.tbGastar,SIGNAL("clicked()"), self.gastar)
    self.connect(self.tbInicial,SIGNAL("clicked()"), self.inicial)
    self.connect(self.tbScliente,SIGNAL("clicked()"), self.seleccionarCliente)
    self.connect(self.tvCuentas,SIGNAL("activated(const QModelIndex&)"),self.cobrar)
    self.connect(self.cbTipo,SIGNAL("currentIndexChanged ( int )"),self.listar)
    self.connect(self.leNumero, SIGNAL("returnPressed()"),self.cobrarNota)
    self.tvCuentas.setContextMenuPolicy(Qt.ActionsContextMenu)
    menu=QMenu(self)
    cobra=menu.addAction(QIcon(":/actions/images/actions/color_18/coin.png"),"Cobrar ventas",self.cobrar)
    ver=menu.addAction(QIcon(":/actions/images/actions/color_18/binoculars.png"),"Visualizar",self.verVenta)
    suma=menu.addAction(QIcon(":/actions/images/actions/color_18/add.png"),"Sumar totales",self.sumarizar)
    self.tvCuentas.addAction(ver)
    self.tvCuentas.addAction(cobra)
    self.tvCuentas.addAction(suma)
    
 
  def ver(self):
    self.parent.move(self.datos['nombre'])
    self.listar()
    
  def cobrarNota(self):
    """Cobra el numero de nota que tenga el buscador"""
    txt=str(self.leNumero.text())
    if len(txt) in range(3,12):
	cobra=Cobrador(conexion=self.parent.conexion,ventas=txt,usuario=self.parent.sesion['usuario']['id_usuario'],
	cliente=self.parent.cliente['id'],caja=self.parent.caja)
	if cobra.exec_()==QDialog.Accepted:
	  self.leNumero.setText('')
	  self.listar()	       
    self.leNumero.selectAll()
    
  def listar(self):
    if self.cbTipo.currentIndex()==0: #Cuando se seleccione "Notas" 
      filtro="1"
    else:
      filtro="notas.tipo={0}".format(self.cbTipo.currentIndex()-1)
    sql="""SELECT notas.id, total,fecha,ELT(notas.tipo+1,'Nota','Factura'),SUBSTR(clientes.nombre,1,12), usuarios.usuario, caja   FROM notas, clientes, usuarios where notas.usuario=usuarios.id_usuario and cliente=clientes.id and status=0 and date(fecha)=CURDATE() and {filtro} order by fecha""".format(filtro=filtro)
    head=['Id','Total','Fecha','Tipo','Cliente','Vendedor','Caja']
    self.modelo.query(sql,head)
    self.tvCuentas.resizeColumnsToContents()
    
  def listarCliente(self,cliente):
    sql="""SELECT notas.id, total,fecha,ELT(notas.tipo+1,'Nota','Factura'),SUBSTR(clientes.nombre,1,12), usuarios.usuario, caja   FROM notas, clientes, usuarios where notas.usuario=usuarios.id_usuario and cliente=clientes.id and status=0  and cliente={cliente} order by fecha""".format(cliente=cliente)
    head=['Id','Total','Fecha','Tipo','Cliente','Vendedor','Caja']
    self.modelo.query(sql,head)
    self.tvCuentas.resizeColumnsToContents()
	
    
  def inicial(self):
      self.hacerMovimiento('inicial')
	  
  def depositar(self):
      self.hacerMovimiento('deposito')

  def retirar(self):
      self.hacerMovimiento('retiro')

  def gastar(self):
      self.hacerMovimiento('gasto')
	  
  def hacerMovimiento(self,tipo=''):
      if self.parent.aut(2):
	ag=AgregaGasto(self.parent,self.parent.sesion['usuario']['id_usuario'],tipo)
	if ag.exec_()>0:
	  self.resumir()
	
  def cobrar(self):
      notas= [item.data().toInt()[0] for item in self.tvCuentas.selectionModel().selectedRows()]
      if len(notas)>0:
	cobra=Cobrador(conexion=self.parent.conexion,ventas=notas,usuario=self.parent.sesion['usuario']['id_usuario'],
	cliente=self.parent.cliente['id'],caja=self.parent.caja)
	if cobra.exec_()==QDialog.Accepted:
	  self.listar()	  
	  
  def seleccionarCliente(self):
      app=Selector(self.parent,"Cliente",'clientes','id,nombre,rfc','Id,Nombre ,RFC',
      "(`nombre` like '%{0}%' or `rfc` like '{0}%') order by nombre  ")
      done=app.exec_()
      if done==1:
	cliente=app.retorno[0]
	self.tbScliente.setText(cliente[1])
	self.listarCliente(cliente[0])
	
  def verVenta(self):
    nota=self.tvCuentas.selectionModel().selectedRows()[0].data().toInt()[0]
    app=VisorVenta(self.parent,nota)
    app.exec_()
    
  def sumarizar(self):
    """Suma los totales y los demuestra en un dialogo"""
    suma=sum([item.data().toDouble()[0] for item in self.tvCuentas.selectionModel().selectedRows(1)])
    QMessageBox.information(self.parent,"Suma de totales","""<h1 align="right">${0:,.2f}</h1>""".format(suma))

    
	