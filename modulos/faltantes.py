from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb as my
from lib import libutil
from lib.utileria import Faltante
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

      self.ui.connect(self.ui.tbFaltantes,SIGNAL("clicked()"), lambda:self.ui.stackFaltantes.setCurrentIndex(0))
      self.ui.connect(self.ui.tvFaltantes,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
     
      self.modelo=None
      #self.ui.tvFaltantes()
      
    def iniciar(self):
      self.ui.stack.setCurrentIndex(4)
      self.ui.stackFaltantes.setCurrentIndex(0)
      self.listar()	
      
    def listar(self):
	fecha=str(self.ui.deFFecha.date().toString('yyyy-MM-dd'))
	head=('Ref','Cantidad','Producto','Prioridad','Usuario','Fecha')
	sql="SELECT ref,cantidad,descripcion,  ELT(prioridad+1,'0 Urgente','1 Alta','2 Normal','3 Baja'), nombre, fecha FROM faltantes, productos,usuarios  WHERE fecha>=date('%s') and ref=producto and  id_usuario=faltantes.usuario order by prioridad ;"%fecha
	self.modelo=self.ui.entabla(self.ui.tvFaltantes,head,sql,self.modelo)    
	self.ui.tvFaltantes.resizeColumnsToContents() 
	
    def imprimir(self):
      titulo="Lista completa de faltantes del dia %s"%self.ui.deFFecha.date().toString('dd-MM-yyyy')
      html=libutil.listaHtml(self.modelo.getVector(),titulo, [[5,'Ref'],[5,'Cantidad'],[30,'Producto'],[15,'Prioridad'],[15,'Usuario'],[20,'Fecha']],'#FFF',"#639639",10)
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
      
      
