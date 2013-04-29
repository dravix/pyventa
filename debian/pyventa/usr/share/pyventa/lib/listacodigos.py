from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QMessageBox, QInputDialog
from ui.ui_lista import Ui_Listado
from lib.libutil import seleccionar
class ListadorCodigos(QDialog, Ui_Listado):
    def __init__(self,parent,ide=-1,lista=[]):
      QDialog.__init__(self,parent)
      self.setupUi(self)
      self.parent=parent
      self.cursor=parent.cursor
      self.ide=ide 
      self.modelo=None
      self.codes=lista
      self.connect(self.tbMas, SIGNAL("clicked()"), self.nuevo)    
      self.connect(self.tbMenos, SIGNAL("clicked()"), self.eliminar)    
      #if self.ide>0:
      self.listar()
      #else:
	#self.modelo=MyTableModel([],["codigo"], self)
	#self.lvLista.setModel(self.modelo)
	##self.stat.setText("No ha seleccionado un producto.")
	
    def listar(self):
      if self.ide>0:
	head=["producto","codigo"]
	sql="SELECT * FROM codigos where producto=%s"%self.ide
	#print sql
	self.modelo=self.parent.entabla(self.lvLista,head,sql,self.modelo)      
	self.lvLista.setColumnHidden(0,True)
      else:
	self.modelo=self.parent.listaTabla(self.lvLista,["codigo"],self.codes,self.modelo)      
	#self.lvLista.setColumnHidden(0,True)
    
    def modificar(self,code=''):
      code=str(code)
      if len(code>0):
	ref=seleccionar(self.lvLista,self.modelo)[0]
	sql="UPDATE codigos set codigo=%s where producto=%s"%(code,self.ide)
	try:
	   self.cursor.execute(sql)
	except:
	  print "No fue posible actualizar el codigo asociado al producto %s"%self.ide
	  return False
	else:
	  return True

    def eliminar(self):
      #msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Question,"e ",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,self, Qt.WindowStaysOnTopHint)
      #ret=msgBox.exec_()
      #if ret!=QtGui.QMessageBox.Yes:
      ref=seleccionar(self.lvLista,self.modelo,1)[0]
      if self.ide>0:
	sql="DELETE FROM  codigos WHERE codigo=%s"%(ref)
	try:
	   self.cursor.execute(sql)
	except:
	  print "No fue posible ELIMINAR el codigo %s"%ref
	  return False
	else:
	  self.listar()	
	  return True
      else:
	self.codes.remove([ref])
	  
    def nuevo(self):
	dsc=QInputDialog.getText(self, self.tr("Agregar codigo alterno"),self.tr("Pase ahora el codigo de barras por el lector \no escribalo manualmente. (Solo se aceptan numeros)"))
	code=str(dsc[0])
	#print self.ide

	if len(code)>0:
	  prev=self.parent.productos.buscarProd(code)
	  if prev!=None:
	    QMessageBox.critical (self, "Codigo duplicado", "Este codigo ya ha sido asignado a\n%s."%prev) 
	  elif self.ide>0:
	    try:
	      sql="INSERT INTO codigos values (%s,%s)"%(self.ide,code)
	      self.cursor.execute(sql)
	    except:
	      print "No fue posible ingresar el codigo asociado al producto %s"%self.ide
	      #print sql
	      return False
	    else:
	      self.listar()
	      return True
	  else:
	    self.codes.append([code])
	    self.listar()