from PyQt4 import  QtGui, QtCore
from ui.ui_control1 import Ui_Masul as Form
from lib import utileria 
from lib import libutil
from PyQt4.QtCore import QDate
import sqlite3
#from utileria import MyTableModel
class Admin1(QtGui.QDialog,Form):
    def __init__(self,padre,objeto,campos,info="",logo=-1,ide=-1,ancla=False,cond=""):
      #Padre:  	es el objeto principal padre del que puede extraer conexiones y recursos
      #Objeto:	Es el nombre del objeto o tvTabla que se estara manipulando "familias", "unidades", "impuestos", etc
      #Campos:	Es un diccionario con las columnas de la tvTabla apuntando a un tipo de dato
#		[['columna','Label','tipo',ui=QtGui.*,enabled=None]] ;tipos={str, int, double, date, combo}
#	Ide:	En el caso de que le pasen ide significa que editara un objeto en particular y solo se realizara una accion (modificar, agregar)
	      QtGui.QDialog.__init__(self,padre)
	      self.setupUi(self)
	      self.ide=['',ide]
	      self.padre=padre
	      obj=objeto.split(',')

	      self.objeto=obj[0]
	      objeto=obj[len(obj)-1]
	      self.campos=campos
	      self.anclado=ancla
	      self.cond=cond
	      self.curser=self.padre.curser
	      self.cursor=self.padre.cursor
	      self.lblDatos.setText("Administracion de %s"%objeto)
	      self.leTitulo.setText("%s"%objeto.upper())
	      #self.lblDatos.setText("Datos de %s\b "%self.objeto)
	      ###Aqui se generan automaticamente los campos
	      self.header=[]
	      self.modelo=None
	      for key, item in enumerate(campos):
		if key==0:
		  self.ide[0]=item[0]
		if self.campos[key][3]==None:

		  if item[2]=='hide':
		    self.campos[key][3]=item[3]
		  elif item[2]=='str':
		    self.campos[key][3]=QtGui.QLineEdit(self)
		    self.campos[key][3].setAlignment(QtCore.Qt.AlignLeft)
		  elif item[2]=='pass':
		    self.campos[key][3]=QtGui.QLineEdit(self)
		    self.campos[key][3].setAlignment(QtCore.Qt.AlignCenter)
		    self.campos[key][3].setEchoMode(2)
		  elif item[2]=='int':
		    self.campos[key][3]=QtGui.QSpinBox(self)
		    self.campos[key][3].setAlignment(QtCore.Qt.AlignRight)
		    self.campos[key][3].setButtonSymbols(2)
		    self.campos[key][3].setMaximum(10000)
		    self.campos[key][3].setMinimum(0)
		  elif item[2]=='double':
		    self.campos[key][3]=QtGui.QDoubleSpinBox(self)
		    self.campos[key][3].setAlignment(QtCore.Qt.AlignRight)
		    self.campos[key][3].setButtonSymbols(2)	
		    self.campos[key][3].setMaximum(10000)
		    self.campos[key][3].setMinimum(0)		    
		  elif item[2]=='date':
		    self.campos[key][3]=QtGui.QDateEdit(self)
		    self.campos[key][3].setDate(QDate.currentDate())
		    self.campos[key][3].setCalendarPopup (True)
		    self.campos[key][3].setButtonSymbols(2)
		    self.campos[key][3].setAlignment(QtCore.Qt.AlignRight)
		    
		if  item[2]!='hide':
		  self.campos[key][3].setEnabled(item[4])
		  self.formLay.addRow(item[1],self.campos[key][3])	
		  
		self.header.append(campos[key][1])
	      ### -------------------------------------
	      self.tvTabla.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
	      self.popMenu=QtGui.QMenu(self)
	      self.lblInfo.setText(info)
	      if logo!=-1:
		#self.lblLogo.setI(QtGui.QPixmap(logo))
		self.tbHome.setIcon(QtGui.QIcon(logo))
	      #self.connect(self.tbCerrar, QtCore.SIGNAL("clicked()"), lambda:self.done(-1))
	      self.connect(self.tbHome, QtCore.SIGNAL("clicked()"), self.listar)
	      self.connect(self.tbModif, QtCore.SIGNAL("clicked()"), self.guardar)
	      self.connect(self.tbLimpiar, QtCore.SIGNAL("clicked()"), self.limpiar)
	      #self.connect(self.tvTabla,QtCore.SIGNAL('cellDoubleClicked (int, int)'),self.seleccionar)
	      self.connect(self.tvTabla, QtCore.SIGNAL("activated(const QModelIndex&)"), self.seleccionar)
	      self.connect(self.tvTabla,QtCore.SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
	      self.cargarMenu()	      
	      #self.anclar()
	      self.editando=False
	      self.listar()
	      if ide!=-1:
		self.cargar(self.ide[1])
		
    def anclar(self,bol=True):
      self.anclado=bol
      if self.anclado==False:
	  self.padre.stack.removeWidget(self)
      else:
	  self.padre.stack.addWidget(self)
	  self.num=self.padre.stack.count()-1 
    
    def iniciar(self):
	if self.anclado==True:
	  self.padre.stack.setCurrentIndex(self.num)
	else:
	  self.exec_()
	
    def setDatos(self,padre,objeto,campos,ide):
	self.padre=padre
	self.objeto=objeto
	self.campos=campos
	self.ide=['',ide]
    
    def cargarMenu(self):
	action=self.popMenu.addAction(QtGui.QIcon(":/actions/images/actions/black_18/pencil.png"),"Editar ")
	action.setIconVisibleInMenu(True)
	self.connect(action, QtCore.SIGNAL("triggered()"), lambda:self.cargar(self.getKey()))
	action=self.popMenu.addAction(QtGui.QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar")
	action.setIconVisibleInMenu(True)
	self.connect(action, QtCore.SIGNAL("triggered()"), self.eliminar)

	
    def getDato(self,key):
	if self.campos[key][2]=='hide':
	  return self.campos[key][3]
	elif self.campos[key][2]=='str':
	  return self.campos[key][3].text()
	elif self.campos[key][2]=='pass':
	  return self.campos[key][3].text()	  
	elif self.campos[key][2]=='int':
	  return self.campos[key][3].value()
	elif self.campos[key][2]=='double':
	  return self.campos[key][3].value()
	elif self.campos[key][2]=='date':
	  return self.campos[key][3].date().toString('yyyy-MM-dd')
	elif self.campos[key][2]=='combo':
	  #print self.campos[key][3].model().celda(self.campos[key][3].currentIndex(),0)
	  return self.campos[key][3].model().celda(self.campos[key][3].currentIndex(),0)	  

    def setDato(self,key,dato):
	if self.campos[key][2]=='hide':
	  self.campos[key][3]=dato
	elif self.campos[key][2]=='str':
	   self.campos[key][3].setText(str(dato))
	elif self.campos[key][2]=='pass':
	   self.campos[key][3].setText(str(dato))	   
	elif self.campos[key][2]=='int':
	   self.campos[key][3].setValue(int(dato))
	elif self.campos[key][2]=='double':
	   self.campos[key][3].setValue(float(dato))
	elif self.campos[key][2]=='date':
	   self.campos[key][3].setDate(QDate.currentDate())
	elif self.campos[key][2]=='combo':
	   self.campos[key][3].setCurrentIndex ( self.campos[key][3].model().buscarKey(dato,0) )
	  
    def cargar(self,ide):
      	self.cursor.execute("SELECT * FROM %s WHERE `%s`=%s limit 1; "%(self.objeto,self.ide[0],ide))
      	objeto=self.cursor.fetchone()
      	if objeto!=None:
	  self.ide[1]=ide
	  for key,item in enumerate(self.campos):
	    self.setDato(key,objeto[key])
	  self.editando=True
	else:
	  print "No se encontro una unidad con la Id %s"%self.ide[1]
	  
    def seleccionar(self,modelIndex):
	#key=self.tvTabla.item(y,0).text()
	#self.modix=modelIndex
	key=self.modelo.getCell(modelIndex,0)
	self.cargar(key)

    def getKey(self): #Esta funcion devuelve la llave primaria del primer elemento seleccionado
	#return str(self.tvTabla.item(self.tvTabla.currentRow(),0).text()) #QTableWidget
	#self.modix=self.tvTabla.selectedIndexes ()[0]
	return self.modelo.getCell(self.tvTabla.selectedIndexes ()[0],0)
	
    def listar(self):
	sql=str("SELECT * FROM %s %s;"%(self.objeto,self.cond))
	try:
	  self.cursor.execute(sql)
	  lista=self.cursor.fetchall()
	except:
	  print "Error al obtener la lista de elementos"
	else:
	  if lista!=None:
	    if self.modelo==None:
	      self.modelo = utileria.MyTableModel(lista, self.header, self) 
	      self.tvTabla.setModel(self.modelo)
	    else:
	      self.modelo.setVector(lista)
	      
	    self.tvTabla.resizeColumnsToContents()
	    #self.modelo=utileria.tabular(self.tvTabla,lista,self.header,self)  

    def getModelo(self):
      if self.modelo==None:
	self.listar()
      return self.modelo
     
    def guardar(self): 
     if self.editando:
       self.editar()
     else:
       self.agregar()
     
    def editar(self):
	campos=[]
	for key,item in enumerate(self.campos):
	  campos.append(" `%s`='%s' "%(item[0],self.getDato(key)))
	sql="UPDATE %s SET %s  WHERE %s=%s"%(self.objeto,','.join(campos),self.ide[0],self.ide[1])
	try:
	  self.cursor.execute(sql)
	except:
	  print sql
	  error="No se actualizo correctamente, verifique el log"
	  print error
	  return error
	else:
	  self.ui.conexion.commit()  
	  self.limpiar()  
	  self.listar()
	  
    def eliminar(self,ide=-1):
	if ide>0:
	  ides=[int(ide)]
	else:
	  indexes=self.tvTabla.selectedIndexes()
	  ides=[]
	  for indice in indexes:
	    if indice.column()==0:
	      ides.append(int(indice.data().toString()))
	for ide in ides:
	  if int(ide)>1:
	    sql="DELETE FROM %s  WHERE %s=%s"%(self.objeto,self.ide[0],ide)
	    try:
	      self.cursor.execute(sql)
	    except:
	      print sql
	      error="No se elimino correctamente, verifique el log"
	      print error
	      return error
	    else:
	      self.ui.conexion.commit()  
	      self.limpiar()  
	      self.listar()
	  else:
	    msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"No se puede eliminar","No se puede eliminar este elemento porque es el registro por default.",QtGui.QMessageBox.Ok,self.padre)
	    msgBox.exec_()
	
    def agregar(self):
	campos=[]
	for key,item in enumerate(self.campos):
	  if key>0:
	    campos.append(" '%s' "%(self.getDato(key)))      
	sql="INSERT INTO %s VALUES(NULL,%s)"%(self.objeto,','.join(campos))
	try:
	  self.cursor.execute(sql)
	except sqlite3.Error,e:
	  print sql
	  raise(e)
	  return False
	except :
	  #print sql
	  error="No se agrego correctamente, verifique el log"
	  print error
	  return error
	else:
	  self.ui.conexion.commit()
	  self.limpiar()  
	  self.listar()

	
    def limpiar(self):
      self.ide[1]=-1
      self.editando=False
      for item in self.campos:
	if item[2]=='str':
	   item[3].clear()
	elif item[2]=='int':
	   item[3].setValue(0)
	elif item[2]=='double':
	   item[3].setValue(0)
	elif item[2]=='date':
	   item[3].setDate(QDate.currentDate())
	   
    def ocm(self, point):
	 point.setY(point.y()+25)
	 point.setX(point.x()+30)
         self.popMenu.exec_(self.tvTabla.mapToGlobal(point) )	
    

      
      
