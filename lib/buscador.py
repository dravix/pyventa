#!/bin/python
import sys,os
#sys.path.append("/usr/share/pyventa/ui")
from PyQt4 import QtCore, QtGui
import MySQLdb
from ui.ui_buscar import Ui_Form
from lib import utileria
class Buscador(QtGui.QDialog, Ui_Form):
    def __init__(self,parent,id):
    		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.curser=parent.curser
		self.cursor=parent.cursor
		self.datos={'nombre':"Buscador",'descripcion':"Buscador de productos",'version':"0.06",'id':id,'nivel':1}
		self.id=id
		self.parent=parent
		self.modelo=None
		self.header=['Ref','Descripcion','Familia','Precio','Existencias']
		self.action = QtGui.QAction(self)
		self.action.setObjectName(self.datos['nombre']+str(id))
		self.action.setShortcut("F3")
		#self.action.setShortcut(QtGui.QApplication.translate("Principal", "F4", None, QtGui.QApplication.UnicodeUTF8))
		icon28 = QtGui.QIcon()
		icon28.addPixmap(QtGui.QPixmap(":/modulos/images/png/elegant/search.png"),0)
		self.action.setIcon(icon28)
		self.action.setIconVisibleInMenu(True)
		self.action.setText(self.datos['nombre'])
		self.action.setToolTip("<h1> F3 </h1>Buscador") 
		self.connect(self.action, QtCore.SIGNAL("triggered()"), self.ver )
		self.connect(self.tbusk, QtCore.SIGNAL("activated(const QModelIndex&)"), self.adomatic)
		self.connect(parent.stack, QtCore.SIGNAL("currentChanged(int)"),self.inicio )
		self.connect(self.cbDepartamentos, QtCore.SIGNAL("activated(int)"), self.buscar)

		self.cbDepartamentos.clear()
		self.cbDepartamentos.addItem("Todos",-1)
		self.cursor.execute("SELECT id,nombre FROM departamentos order by nombre;")
		todos=self.cursor.fetchall()
		for fila in todos:
		    self.cbDepartamentos.addItem(str(fila[1]),fila[0])
		      
    def ver(self):
      self.parent.move(self.datos['nombre'])
      codigo=str(self.parent.codigo)
      if self.parent.moli2!=None:
	self.tbusk.setModel(self.parent.moli2)
	self.tbusk.resizeColumnsToContents()

    def inicio(self,i):
	if(i==self.id):
	  self.parent.codigo.setText(self.parent.codigo.text())
	  self.parent.codigo.setFocus()
	   

    def buscar(self,texto=False):
	  if not texto:
	    texto=str(self.parent.codigo.text())
	  txt=str(texto)
	  dep=self.cbDepartamentos.itemData(self.cbDepartamentos.currentIndex()).toString()
	  familia=""
	  if int(dep)>0:
	      familia=" and familias.departamento={0} ".format(dep)
	  if len(txt)>2:
	    if txt[0].isdigit():
	      sql="SELECT  ref,descripcion,familias.nombre,  `precio`, `stock_logico` from productos,familias, existencia where (ref={0} or codigo like '{0}%') {1} and ref=producto and familia=familias.id order by `vendidas` desc;".format( txt,familia)
	    else:
	      li=txt.split(' ')
	      fil=[]
	      for l in li:
		    fil.append(" descripcion like '%{0}%' ".format(l))
	      sql="SELECT `ref`,`descripcion`,familias.nombre,`precio`, `stock_logico` FROM productos, existencia,familias where {0} {1} and ref=producto and familia=familias.id order by `vendidas` desc;".format("and".join(fil),familia)
	    head=('Ref','Descripcion','Familia','Precio', 'Existencias')
	    try:
	      self.cursor.execute(sql)
	    except:
		print 'No se encontro el articulo'
	    else:
	      result = self.cursor.fetchall()
	      if result!=None:
		if self.modelo==None:
		  #print "tabulando por primera vez",result
		  self.modelo = utileria.MyTableModel(result, head, self.parent) 
		  #self.tbusk.setModel(self.modelo)
		else:
		  self.modelo.setVector(result)
		self.tbusk.setModel(self.modelo)
		self.tbusk.resizeColumnsToContents()

    def adomatic(self, index):
	ref=self.modelo.getCell(index,0)
	self.parent.stack.setCurrentIndex(0)
	self.parent.codigo.clear()
	self.parent.adomatic(str(ref))
		  
    def setId(self,ide):
      self.id=ide
      self.datos['id']=ide
      
    def setNivel(self,nivel):
      self.datos['nivel']=nivel
    
    def datos(self):
      return self.datos

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    aw = modulo(app,1)
    aw.show()
    sys.exit(app.exec_())
	
