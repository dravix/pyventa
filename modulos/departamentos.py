# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QMessageBox
from modulos.control1 import Admin1
class Departamentos(Admin1):
    def __init__(self,parent,attached=False):
      info="Las familias se agrupan de manera semantica en departamentos que son basicamente areas dentro de la misma tienda."
      logo=":/actions/images/actions/color_18/pyramid.png"      
      Admin1.__init__(self,parent,'departamentos',[['id','Id','str',None,False],['nombre','Nombre','str',None,True]],info,logo,cond=" ORDER BY nombre ")
      self.ui=parent
      self.ui.connect(self.ui.verDepartamentos, SIGNAL("triggered()"), self.iniciar)
      self.ui.connect(self.ui.tDepartamentos, SIGNAL("clicked()"), self.iniciar)
      #self.ui.tbrProductos.addAction(self.ui.verDepartamentos)
      self.anclar(not attached)
      
    def eliminar(self,ide=-1):
	#msgBox=QMessageBox(QMessageBox.Question,"Eliminar relacionados","Desea eliminar las familias relacionadas con este departamento?"%key,QMessageBox.Yes|QMessageBox.No,self.ui, Qt.WindowStaysOnTopHint)
	#ret=msgBox.exec_()
	if ide>0:
	  ides=[int(ide)]
	else:
	  indexes=self.tvTabla.selectedIndexes()
	  ides=[]
	  for indice in indexes:
	    if indice.column()==0:
	      ides.append(int(indice.data().toString()))
	for ide in ides:
	  if ide>1:
	    sql="DELETE FROM departamentos  WHERE id ={0}".format(ide)
	    try:
	      self.cursor.execute(sql)
	      #if ret==QMessageBox.Yes:
		#self.cursor.execute("DELETE FROM familias where ")
	    except:
	      error="No se elimino correctamente, verifique el log"
	      print error
	      return error
	    else:
	      self.ui.conexion.commit()  
	      self.limpiar()  
	      self.listar()
	  else:
	    msgBox=QMessageBox(QMessageBox.Information,"No se puede eliminar","No se puede eliminar este elemento porque es el registro por default.",QMessageBox.Ok,self.padre)
	    msgBox.exec_()
	