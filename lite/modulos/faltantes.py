from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb as my
from lib import libutil
from lib.dialogos.marca_faltante import Faltante
from lib.selector import Selector

class Faltantes:
    def __init__(self,parent):
      self.ui=parent
      self.curser=parent.curser
      self.cursor=parent.cursor
      self.ui.tvFaltantes.setContextMenuPolicy(Qt.CustomContextMenu)
      self.ui.deFFecha.setDate(QDate.currentDate())
      self.popMenu=QMenu(self.ui)
      self.cargarMenu()
      self.ui.connect(self.ui.tFaltantes,SIGNAL("clicked()"), self.iniciar)
      self.ui.connect(self.ui.actionFaltantes,SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tbFImprimir,SIGNAL("clicked()"), self.imprimir)
      self.ui.connect(self.ui.pbListaFaltantes,SIGNAL("clicked()"), self.listar)
      self.ui.connect(self.ui.tbFLista,SIGNAL("clicked()"), self.verOrdenCompra)
      self.ui.connect(self.ui.deFFecha, SIGNAL("dateChanged ( const QDate)"), self.listar)

      self.ui.connect(self.ui.tbfAgregarProducto,SIGNAL("clicked()"), self.agregarProducto)
      self.ui.connect(self.ui.tbFaltantes,SIGNAL("clicked()"), lambda:self.ui.stackFaltantes.setCurrentIndex(0))
      self.ui.connect(self.ui.tvFaltantes,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
     
      self.modelo=None
      #self.ui.tvFaltantes()
      
    def iniciar(self):
      self.ui.stack.setCurrentIndex(4)
      self.ui.stackFaltantes.setCurrentIndex(0)
      self.listar()	
      
    def agregarProducto(self):
      app=Selector(self.ui,"Producto",'productos','ref,descripcion,precio',"Ref,Descripcion, Precio ","descripcion like '%{0}%' order by descripcion ")
      done=app.exec_()
      if done==1:
	refs=app.retorno
	prods=[ref[0] for ref in refs]
	lis=Faltante(self.ui,prods,self.ui.usuario['id_usuario'])	
	if lis.exec_()>0:
	  self.listar()
	
      
    def listar(self):
	fecha=str(self.ui.deFFecha.date().toString('yyyy-MM-dd'))
	head=('Ref','Cantidad','Producto','Prioridad','Usuario','Fecha')
	sql="SELECT ref,cantidad,descripcion,  prioridad, usuarios.nombre, fecha FROM faltantes, productos,usuarios  WHERE fecha>=date('%s') and ref=producto and  id_usuario=faltantes.usuario order by prioridad ;"%fecha
	self.modelo=self.ui.entabla(self.ui.tvFaltantes,head,sql,self.modelo)    
	self.ui.tvFaltantes.resizeColumnsToContents() 
	
    def imprimir(self):
      titulo="Lista completa de faltantes %s"%self.ui.deFFecha.date().toString('MMM dd')
      html=libutil.listaHtml(self.modelo.getVector(),titulo, ['Ref','Cantidad','Producto','Prioridad','Usuario','Fecha'],'#FFF',"#639639",10,anchos=[5,5,30,15,15,25,20])
      libutil.printa(html,titulo,self.ui)
      
    def eliminar(self):
      ide=libutil.seleccionar(self.ui.tvFaltantes,self.modelo)
      for i in ide:
	self.cursor.execute("DELETE FROM faltantes where producto=%s"%i)
      self.listar()

    def editar(self):
      refs=libutil.seleccionar(self.ui.tvFaltantes,self.modelo)
      lis=Faltante(self.ui,refs,self.ui.usuario,True)	
      lis.exec_()
      self.listar()

  
      
    def cargarMenu(self):
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/pencil.png"),"Editar ",self.editar)
	action.setIconVisibleInMenu(True)
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/cancel.png"),"Quitar",self.eliminar)
  	action.setIconVisibleInMenu(True)

	
    def verOrdenCompra(self):
      self.ui.stackFaltantes.setCurrentIndex(2)
      
	
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.ui.tvFaltantes.mapToGlobal(point) )
      
      
