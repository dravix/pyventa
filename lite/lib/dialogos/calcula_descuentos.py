from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import   QDialog
from ui.ui_calculo_descuentos import Ui_Calculo

class CalculaDescuentos(QDialog, Ui_Calculo):
    def __init__(self,parent,ide=-1):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.parent=parent
		self.ide=ide
    		self.connect(self.dsbPrecioDesc, SIGNAL("editingFinished ()"), self.calcularDesc)
    		self.connect(self.dsbDescuento, SIGNAL("editingFinished ()"), self.calcularPrecio)
    		self.show()
    		#print self.isModal ()

    def iniciar(self):
      if ide>0:
	self.cursor.execute("""SELECT precio FROM productos where ref=%s """%self.ide)
	qry=self.cursor.fetchone()
	if qry!=None:
	  self.dsbPrecio.setValue(qry)
	  
    def calcularDesc(self):
      precio=self.dsbPrecio.value()
      if precio>0:
	pcd=self.dsbPrecioDesc.value()
	self.dsbDescuento.setValue((precio-pcd)*100/precio)
      
    def calcularPrecio(self):
      desc=self.dsbDescuento.value()      
      precio=self.dsbPrecio.value()
      self.dsbPrecioDesc.setValue(precio-(precio*desc*0.01))