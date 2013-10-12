from ui.ui_marcar_faltante import  Ui_Faltante
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QDialog
import MySQLdb
class Faltante(QDialog, Ui_Faltante):
    def __init__(self,parent,ide=-1,usuario=0, editar=False, producto="Seleccion de productos"):
      QDialog.__init__(self,parent)
      self.setupUi(self)
      self.parent=parent
      self.cursor=parent.cursor
      self.ide=ide 
      self.editar=editar
      self.usuario=usuario 
      self.connect(self.tbMarcar, SIGNAL("clicked()"), self.agregar)    
      self.connect(self.tbCerrar, SIGNAL("clicked()"), self.reject) 
      self.lbProducto.setText(producto)
      if type(ide)==list and len(ide)>0:
	self.cursor.execute("SELECT descripcion,  cantidad, prioridad FROM productos, faltantes where producto=ref and ref={0}".format(ide[0]))
	prod=self.cursor.fetchone()
	#print prod
	if prod!=None:
	  self.lbProducto.setText("{0}<br/><strong>Ya fue marcado, se editara marcacion.</strong>".format(prod[0]))
	  self.dsbCantidad.setValue(prod[1])
	  self.cbPrioridad.setCurrentIndex(prod[2])
	else:
	  self.reject
      else:
	self.ide=[self.ide]
	self.lbProducto.setText("Productos seleccionados")
      self.dsbCantidad.setFocus(True)
      self.dsbCantidad.selectAll()
      self.setWindowFlags(self.windowFlags()|Qt.FramelessWindowHint)
      #self.dsbCantidad.setValue()
      
    def agregar(self):
	for ref in self.ide:
	  if self.editar==False:
	    try:
	      sql="INSERT INTO faltantes VALUES(%s,%s,%s,%s,CURDATE());"%(ref,self.usuario,float(self.dsbCantidad.value()),int(self.cbPrioridad.currentIndex()))
	      #print sql
	      delete="DELETE FROM faltantes where producto='%s'"%ref
	      #print delete
	      self.cursor.execute(delete)
	      self.cursor.execute(sql)
	    except MySQLdb.Error, e:
	      print "Error al marcar como faltante",e
	    else:
	      pass
	  
	  else:
	      try:
		sql="UPDATE faltantes set usuario=%s, cantidad=%s,prioridad=%s,fecha=CURDATE() where producto=%s;"%(self.usuario,float(self.dsbCantidad.value()),int(self.cbPrioridad.currentIndex()),ref)
		self.cursor.execute(sql)
	      except MySQLdb.Error, e:
		print "Error al marcar como faltante",e
	      else:
		pass
	self.accept()