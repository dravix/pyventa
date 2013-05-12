from ui.ui_agregar_gasto import Ui_Form as Ui_Gasto
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import SIGNAL
from lib.modelos.retiro import Retiro
from lib.modelos.gasto import Gasto
from lib.modelos.deposito import Deposito

class AgregaGasto(QDialog, Ui_Gasto):
    def __init__(self, parent,usuario, entidad='gasto'):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.parent=parent
		self.usuario=usuario
		if entidad=='gasto':
		  self.entidad=Gasto(self.parent.conexion)
		elif entidad=='retiro':
		  self.entidad=Retiro(self.parent.conexion)
		  self.setWindowTitle("Retiro de efectivo")
		elif entidad=='deposito':
		  
		  self.setWindowTitle("Deposito de efectivo")
		  self.entidad=Deposito(self.parent.conexion)
		elif entidad=='inicial':
		  self.entidad=Deposito(self.parent.conexion)
		  self.setWindowTitle("Deposito inicial de efectivo")
		  self.leConcepto.setText("Efectivo inicial")
		  self.leConcepto.setEnabled(False)
		self.caja=self.parent.caja
		self.cursor=self.parent.cursor
        	#self.connect(self.leClave, SIGNAL("returnPressed()"), self.autentificar)
        	self.connect(self.tbDone, SIGNAL("clicked()"), self.agregar)
        	self.connect(self.tbCancelar, SIGNAL("clicked()"), lambda:self.done(-1))
        	self.leConcepto.setFocus()

		if self.caja<1:
		  #print self.caja
		  self.lbinfo.setText('<h3 style="color:#C00">Este punto de venta no es Caja.</h3> \nLos movimientos de efectivo deben ser manejados desde una caja')
		  self.dsbCantidad.setEnabled(False)
		  self.leConcepto.setEnabled(False)

    def agregar(self):
      if self.caja>1:
	ret=self.entidad.agregar(usuario=self.usuario,caja=self.caja,
	detalle=self.leConcepto.text(),monto=self.dsbCantidad.value())
	if ret!=False:
	  self.done(ret)
	else:	
	  self.lbinfo.setText('No se registro el movimiento compruebe que los datos sean correctos.')
	  
      else:
	self.lbinfo.setText('Este punto de venta no esta registrado como "caja". \nLos movimientos de efectivo deben ser manejados desde una caja')