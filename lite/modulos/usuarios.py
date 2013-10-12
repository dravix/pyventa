# -*- coding: utf-8 -*-
from PyQt4 import  Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.ui_editor_usuarios import Ui_Dialog
from ui.ui_editor_claves import Ui_Claves
import MySQLdb
import md5, sqlite3
from lib.librerias.conexion import dicursor
from lib.modelos.qmodelotablasql import QModeloTablaSql

class Usuarios:
    def __init__(self,parent):
		self.ui=parent
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.parent=parent
		self.ui.tvUsuarios.setContextMenuPolicy(Qt.CustomContextMenu)
		self.index=8
        	self.ui.connect(self.ui.tUsuarios, SIGNAL("clicked()"), self.ver)		
        	self.ui.connect(self.ui.verUsuarios, SIGNAL("triggered()"), self.ver)		
		self.ui.connect(self.ui.tbuCambiar, SIGNAL("clicked()"), self.cambiarClaves)
		self.ui.connect(self.ui.tbpActualizar, SIGNAL("clicked()"), self.listar)
        	self.ui.connect(self.ui.tbAgregarUsuario, SIGNAL("clicked()"), self.nuevo)		
        	self.ui.connect(self.ui.tbuGuardar, SIGNAL("clicked()"), self.guardar)		
        	self.ui.connect(self.ui.leuFiltro, SIGNAL("returnPressed()"), lambda: self.listar(self.ui.leuFiltro.text()))
		self.ui.connect(self.ui.tvUsuarios,SIGNAL('customContextMenuRequested(const QPoint)'),self.ocm)
		self.ui.connect(self.ui.tvUsuarios,SIGNAL("activated(const QModelIndex&)"),self.editar)

		#self.ui.connect(self.ui.tvUsuarios,SIGNAL('cellDoubleClicked (int, int)'),self.editar)
		self.ui.wuControls.setVisible(False)
		self.modelo=QModeloTablaSql(self.cursor,self.ui)
		self.ui.tvUsuarios.setModel(self.modelo)
		#self.ui.connect(self.ui.tvUsuarios,SIGNAL('cellDoubleClicked (int, int)'),self.editar)
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
	self.ui.connect(action, SIGNAL("triggered()"), self.editar)
	#self.ui.menuPersonal.addAction(action)

	action= self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/password.png"),"Cambiar clave ")
	self.ui.connect(action, SIGNAL("triggered()"), self.cambiarClaves)

	action=self.popMenu.addAction(QIcon(":/actions/images/actions/black_18/delete.png"),"Eliminar")
	self.ui.connect(action, SIGNAL("triggered()"), self.eliminar)
	#self.ui.menuPersonal.addAction(action)

	  
    def listar(self,texto=''):
	if texto!='':
	    texto=" WHERE nombre like '%"+str(texto)+"%'"
	head=['Id','Nombre','Usuario','Nivel']
	sql=""" SELECT id_usuario,nombre,usuario,ELT(nivel+1,'Reserva','Vendedor','Cajero','Gerente','Manager','Administrador','Auditor')
	FROM usuarios %s"""%texto
	self.modelo.query(sql,head)

    def nuevo(self):
      self.limpiar()
      self.ui.wuControls.setVisible(True)
      self.ui.leNombre.setFocus()
	#editor=editorUsuarios(self.ui)
	#if editor.exec_()>0:
	  #self.listar()

    def eliminar(self):
	msgBox=QMessageBox(QMessageBox.Question,"Confirmar dar de baja?","Esta a punto de eliminar un usuario .Desea continuar?",QMessageBox.Yes|QMessageBox.No,self.ui, Qt.WindowStaysOnTopHint)
	if msgBox.exec_()==QMessageBox.Yes:
	  keys=[item.data().toInt()[0] for item in self.ui.tvUsuarios.selectionModel().selectedRows()]
	  keys=map(str,keys)
	  self.ui.cursor.execute("delete from usuarios where id_usuario in (%s) "%(','.join(keys)))
	  self.ui.conexion.commit()
	  self.listar()

    def editar(self):
	#head=['id','nombre']
	key=self.ui.tvUsuarios.selectionModel().selectedRows()[0].data().toInt()[0]
	self.ide=key
	self.curser.execute("SELECT * FROM usuarios where id_usuario=%s"%key)
	usuario=self.curser.fetchone()
	if usuario!=None:
	  usuario=dicursor(self.curser,usuario)
	  self.ui.leNombre.setText(str(usuario['nombre']))
	  self.ui.leUsuario.setText(str(usuario['usuario']))
	  self.ui.leClave.setEnabled(False)
	  self.ui.cbNivel.setCurrentIndex(self.ui.cbNivel.findData(QVariant(usuario['nivel'])))
	  self.ui.wuControls.setVisible(True)
	  
    def guardar(self):
	  nivel=int(self.ui.cbNivel.itemData(self.ui.cbNivel.currentIndex()).toString())
	  flag=0
	  try:
	    if self.ide!=-1:
	      familia=(self.ui.leNombre.text(),self.ui.leUsuario.text(),nivel,self.ide)
	      self.curser.execute("""UPDATE usuarios set nombre='%s', usuario='%s', nivel=%s where id_usuario=%s"""%familia)
	      flag=1
	    else:
	      m=md5.new(str(self.ui.leClave.text()))
	      familia=(self.ui.leNombre.text(),self.ui.leUsuario.text(),m.hexdigest(),nivel)
	      self.curser.execute("""INSERT INTO usuarios values (NULL,'%s', '%s','%s',%s )"""%familia)
	      flag=2
	  except MySQLdb.Error, e:
	    if e.args[0]==1062:
	      self.parent.notify("error","No se registro el usuario","El nombre de usuario ya existe, elija otro.",7)
	    else:
	      print e
	  except sqlite3.Error, e:
	      self.parent.notify("error","No se registro el usuario","Compruebe sus datos",5)
	      raise(e)
	  else:
	    if flag==1:
	      self.parent.notify("info","Los datos de usuario {0} fueron actualizados".format(familia[0]),"",5)
	    elif flag==2:
	      self.parent.notify("info","Nuevo usuario","Se ha registrado un nuevo usuario,%s "%familia[0],5)
	    self.ui.conexion.commit()
	    self.limpiar()
	    self.listar()
	  
    def limpiar(self):
	self.ui.leNombre.setText('')
	self.ui.leUsuario.setText('')
	self.ui.leClave.setText('')
	self.ui.leClave.setEnabled(True)
	self.ui.cbNivel.setCurrentIndex(0)
	self.ui.wuControls.setVisible(False)
	self.ide=-1

    def cambiarClaves(self):
      if not self.ui.wuControls.isVisible():
	  key=self.ui.tvUsuarios.selectionModel().selectedRows()[0].data().toInt()[0]
      else:
	  key=self.ide
      editor=editorClaves(self.ui,key)
      editor.exec_()

    def ocm(self, point):
         self.popMenu.exec_(self.ui.tvUsuarios.mapToGlobal(point) )





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
	      self.curser.execute("""UPDATE usuarios set nombre=%s, usuario=%s, nivel=%s where id_usuario=%s"""%familia)
	    else:
	      familia=(self.leNombre.text(),self.leUsuario.text(),self.leClave.text(),nivel)
	      self.curser.execute("""INSERT INTO usuarios values (NULL,'%s', '%s','%s',%s )"""%familia)
	  except sqlite3.Error,e:
	      raise(e)
	  else:
	    self.ui.conexion.commit()
	      


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
		self.cursor.execute("""SELECT usuario from usuarios where id_usuario=%s"""%self.ide)
		usuario=self.cursor.fetchone()[0]
		self.lbUsuario.setText("Usuario: %s "%str(usuario))
		self.bandera={'actual':False,'repeat':False,}

    def checarActual(self):
	actual=str(self.leActual.text())
	m=md5.new(actual)
	
	self.cursor.execute("""SELECT COUNT(id_usuario) from usuarios where id_usuario=%s and clave='%s' """%(self.ide,m.hexdigest()))
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
	    #print """UPDATE usuarios set clave=MD5(%s) WHERE id_usuario=%s"""%(nueva,self.ide)
	    m=md5.new(nueva)
	    try:
	      self.cursor.execute("""UPDATE usuarios set clave='%s' WHERE id_usuario=%s"""%(m.hexdigest(),self.ide))
	    except  :
		self.parent.notify("error","Error al cambia la clave","Compruebe sus datos",5)
	    else:
	      self.parent.conexion.commit()
	      self.parent.notify("info","Se ha cambiado la clave","",5)

    def limpiarAlerta(self):
	self.lbAlerta.clear()

