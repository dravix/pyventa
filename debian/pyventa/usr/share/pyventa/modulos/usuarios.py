# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.ui_editor_usuarios import Ui_Dialog
from ui.ui_editor_claves import Ui_Claves
import MySQLdb
class Usuarios:
    def __init__(self,parent):
		self.ui=parent
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.parent=parent
		self.ui.twUsuarios.setContextMenuPolicy(Qt.CustomContextMenu)
		self.index=8
        	self.ui.connect(self.ui.tUsuarios, SIGNAL("clicked()"), self.ver)		
        	self.ui.connect(self.ui.verUsuarios, SIGNAL("triggered()"), self.ver)		
		self.ui.connect(self.ui.tbuCambiar, SIGNAL("clicked()"), self.cambiarClaves)
		self.ui.connect(self.ui.tbpActualizar, SIGNAL("clicked()"), self.listar)
        	self.ui.connect(self.ui.tbAgregarUsuario, SIGNAL("clicked()"), self.nuevo)		
        	self.ui.connect(self.ui.tbuGuardar, SIGNAL("clicked()"), self.guardar)		
        	self.ui.connect(self.ui.leuFiltro, SIGNAL("returnPressed()"), lambda: self.listar(self.ui.leuFiltro.text()))
		self.ui.connect(self.ui.twUsuarios,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
		self.ui.connect(self.ui.twUsuarios,SIGNAL('cellDoubleClicked (int, int)'),self.editar)
		
		#self.ui.connect(self.ui.twUsuarios,SIGNAL('cellDoubleClicked (int, int)'),self.editar)
		self.iniciarActions()
		self.ide=-1
		self.nivel={0:'Reserva',1:'Vendedor',2:'Cajero',3:'Gerente',6:'Auditor',5:'Administrador',4:'Manager'}		
		self.iniciar()

		#self.ui.wuControls.setVisible(False)



    def iniciar(self):
	for key,item in self.nivel.iteritems():
	  self.ui.cbNivel.addItem(item,key)
	  self.ui.leClave.setEnabled(True)
	self.listar()      


    def ver(self):
	self.ui.stack.setCurrentIndex(self.index)
	

    def iniciarActions(self):
	self.popMenu = QMenu(self.ui)
	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/add.png"),"Nuevo Usuario")
	self.ui.connect(action, SIGNAL("triggered()"), self.nuevo)
	#self.ui.menuPersonal.addAction(action)

	action= self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/pencil.png"),"Editar ")
	self.ui.connect(action, SIGNAL("triggered()"), lambda: self.editar(self.ui.twUsuarios.currentRow(),self.ui.twUsuarios.currentColumn()))
	#self.ui.menuPersonal.addAction(action)

	action= self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/password.png"),"Cambiar clave ")
	self.ui.connect(action, SIGNAL("triggered()"), lambda: self.cambiarClaves(self.ui.twUsuarios.currentRow(),self.ui.twUsuarios.currentColumn()))
	#self.ui.menuPersonal.addAction(action)

	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar")
	self.ui.connect(action, SIGNAL("triggered()"), self.eliminar)
	#self.ui.menuPersonal.addAction(action)

	  
    def listar(self,texto=''):
	if texto!='':
	    texto=" WHERE nombre like '%"+str(texto)+"%'"
	head=['Id','Nombre','Usuario','Nivel']
	self.cursor.execute(" SELECT id_usuario,nombre,usuario,nivel FROM usuarios %s"%texto)
	query=self.cursor.fetchall()
	lista=[]
	for item in query:
	    tmp=list(item)
	    if tmp[3]>6: lev=6
	    else: lev=int(tmp[3])
	    tmp[3]=self.nivel[lev]
	    lista.append(tmp)
	self.ui.entablar(self.ui.twUsuarios,lista,head)

    def nuevo(self):
      #self.ui.wuControls.setVisible(True)
      self.limpiar()
      self.ui.leNombre.setFocus()
	#editor=editorUsuarios(self.ui)
	#if editor.exec_()>0:
	  #self.listar()

    def eliminar(self):
	msgBox=QMessageBox(QMessageBox.Question,"Confirmar dar de baja?","Esta a punto de eliminar un usuario .Desea continuar?",QMessageBox.Yes|QMessageBox.No,self.ui, Qt.WindowStaysOnTopHint)
	if msgBox.exec_()==QMessageBox.Yes:
	  lista=self.ui.twUsuarios.selectedItems()
	  for item in lista:
	    if self.ui.twUsuarios.column(item)==0:
	      key=str(item.text())
	  #dep=self.ui.twFamilias.item(self.ui.twFamilias.currentRow(),0).text()
	      #self.ui.cursor.execute("UPDATE productos set familia=0 where familia="+str(dep))
	      self.ui.cursor.execute("delete from usuarios where id_usuario="+str(key))
	      self.ui.cursor.execute("COMMIT")
	  self.listar()

    def editar(self,y,x):
	#head=['id','nombre']
	key=self.ui.twUsuarios.item(y,0).text()
	self.ide=key
	self.curser.execute("SELECT * FROM usuarios where id_usuario=%s"%key)
	usuario=self.curser.fetchone()
	self.ui.leNombre.setText(str(usuario['nombre']))
	self.ui.leUsuario.setText(str(usuario['usuario']))
	self.ui.leClave.setEnabled(False)
	self.ui.cbNivel.setCurrentIndex(self.ui.cbNivel.findData(QVariant(usuario['nivel'])))
	#self.ui.wuControls.setVisible(True)
	  
    def guardar(self):
	  nivel=int(self.ui.cbNivel.itemData(self.ui.cbNivel.currentIndex()).toString())
	  try:
	    if self.ide!=-1:
	      familia=(self.ui.leNombre.text(),self.ui.leUsuario.text(),nivel,self.ide)
	      self.curser.execute("""UPDATE usuarios set nombre=%s, usuario=%s, nivel=%s where id_usuario=%s""",familia)
	    else:
	      familia=(self.ui.leNombre.text(),self.ui.leUsuario.text(),self.ui.leClave.text(),nivel)
	      self.curser.execute("""INSERT INTO usuarios value (NULL,%s, %s,MD5(%s),%s )""",familia)
	  except MySQLdb.Error, e:
	    if e.args[0]==1062:
	      self.parent.notify("error","No se registro el usuario","El nombre de usuario ya existe, elija otro.",7)
	    else:
	      print e
	  except:
	      self.parent.notify("error","No se registro el usuario","Compruebe sus datos",5)

	  else:
	    self.curser.execute("COMMIT")
	    self.limpiar()
	    self.listar()
	  
    def limpiar(self):
	self.ui.leNombre.setText('')
	self.ui.leUsuario.setText('')
	self.ui.leClave.setText('')
	self.ui.leClave.setEnabled(True)
	self.ui.cbNivel.setCurrentIndex(0)
	self.ide=-1

    def cambiarClaves(self,y=-1,x=-1):
	if self.ide==-1 or (y>-1 and x>-1):
	  key=self.ui.twUsuarios.item(y,0).text()
	else:
	  key=self.ide
	editor=editorClaves(self.ui,key)
	editor.exec_()

    def ocm(self, point):
         self.popMenu.exec_(self.ui.twUsuarios.mapToGlobal(point) )





class editorUsuarios(QDialog, Ui_Dialog):
  
    def __init__(self,parent,ide=-1):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.curser=parent.curser
		self.parent=parent
		self.ide=ide
		#self.connect(self, SIGNAL("accepted()"), self.guardar)
		self.cx=0
		self.nivel={0:'Reserva',1:'Vendedor',2:'Cajero',3:'Gerente',6:'Auditor',5:'Administrador',4:'Manager'}		
		self.iniciar()

    def iniciar(self):
	for key,item in self.nivel.iteritems():
	  self.cbNivel.addItem(item,key)
	  self.leClave.setEnabled(True)
	if self.ide!=-1:
	  self.curser.execute("SELECT * FROM usuarios where id_usuario="+str(self.ide))
	  usuario=self.curser.fetchone()
	  self.leNombre.setText(str(usuario['nombre']))
	  self.leUsuario.setText(str(usuario['usuario']))
	  self.leClave.setEnabled(False)
	  self.cbNivel.setCurrentIndex(self.cbNivel.findData(QVariant(usuario['nivel'])))

  
    def guardar(self):
	  nivel=int(self.cbNivel.itemData(self.cbNivel.currentIndex()).toString())
	  try:
	    if self.ide!=-1:
	      familia=(self.leNombre.text(),self.leUsuario.text(),nivel,self.ide)
	      self.curser.execute("""UPDATE usuarios set nombre=%s, usuario=%s, nivel=%s where id_usuario=%s""",familia)
	    else:
	      familia=(self.leNombre.text(),self.leUsuario.text(),self.leClave.text(),nivel)
	      self.curser.execute("""INSERT INTO usuarios value (NULL,%s, %s,MD5(%s),%s )""",familia)
	  except:
	      pass
	  else:
	    self.curser.execute("COMMIT")
	      


class editorClaves(QDialog, Ui_Claves):
    def __init__(self,parent,ide):
    		QDialog.__init__(self)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.parent=parent
		self.ide=ide
		self.time=QTimer(self)
		self.connect(self, SIGNAL("accepted()"), self.guardar)
		self.connect(self.leActual, SIGNAL("editingFinished ()"), self.checarActual)
		self.connect(self.leRepeticion, SIGNAL("editingFinished ()"), self.checarRepeticion)
		self.connect(self.leRepeticion, SIGNAL("returnPressed () "), self.checarRepeticion)
		self.connect(self.time, SIGNAL("timeout()"), self.limpiarAlerta)
		self.cursor.execute("""SELECT usuario from usuarios where id_usuario=%s""",self.ide)
		usuario=self.cursor.fetchone()[0]
		self.lbUsuario.setText("Usuario: %s "%str(usuario))
		self.bandera={'actual':False,'repeat':False,}

    def checarActual(self):
	actual=str(self.leActual.text())
	self.cursor.execute("""SELECT COUNT(id_usuario) from usuarios where id_usuario=%s and clave=MD5(%s) """,(self.ide,actual))
	qry=self.cursor.fetchone()[0]
	if qry>0 :
	  self.bandera['actual']=True
	else:
	    self.lbAlerta.setText("La clave actual no es correcta.")
	    self.time.start(5000)

    def checarRepeticion(self):
	nueva=str(self.leNueva.text())
	repeticion=str(self.leRepeticion.text())
	if len(nueva)>0 and len(repeticion)>0:
	    if nueva!=repeticion:
		self.lbAlerta.setText("Las claves no coinciden.")
		self.time.start(5000)
	    else:
		self.bandera['repeat']=True


    def guardar(self):
	nueva=str(self.leNueva.text())
	self.checarRepeticion()
	if self.bandera['actual']==True:
	  if self.bandera['repeat']==True:
	    print """UPDATE usuarios set clave=MD5(%s) WHERE id_usuario=%s"""%(nueva,self.ide)

	    self.cursor.execute("""UPDATE usuarios set clave=MD5(%s) WHERE id_usuario=%s""",(nueva,self.ide))
	    self.cursor.execute("COMMIT")

    def limpiarAlerta(self):
	self.lbAlerta.clear()

