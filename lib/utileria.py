#Utileria es una libreria de clases reusables en Pyventa y sus subsecuentes paquetes
import os,sys, datetime, operator
from shutil import copy2
from PyQt4 import QtCore, QtGui#,  Qt
from PyQt4.QtCore import Qt, QAbstractTableModel, QVariant

#from PyQt4.QtGui import *
#from PyQt4.QtGui import *

from lib.db_conf import configurador
import MySQLdb as My, ConfigParser as Cp
import base64, tarfile
from ui.ui_editor_ticket import Ui_Dialog as Editor
from ui.ui_acceso import Ui_Acceso
from ui.dl_resumen_venta import Ui_Dialog as Ui_Resumen
from ui.ui_resumen import Ui_Form as Ui_RVenta
from lib.nletras import *
import _mysql, locale
from ui.ui_agregar_deposito import Ui_Dialog as Apertura
from subprocess import call
from lib.librerias.conexion import dicursor

aqui="/usr/share/pyventa/"
home=os.path.join(os.path.expanduser('~'),"pyventa")
if sys.platform == 'linux2':
    home=os.path.join(os.path.expanduser('~'),".pyventa")
#else:
    #home=os.path.join(aqui,'perfil')
    
#EL editorSimple  es una clase que lee un archivo de texto plano y lo muestra dando la posibilidad de modificarlo

def setIcono(widget,icono):
	icon= QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(icono), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	widget.setIcon(icon)
	
def odic(adict): ##Ordena los indices de un diccionacio
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)
    
def cifra(num):	
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    dato=num
    if (str(num)[0].isdigit() or str(num)[0]=='-' or str(num)[0]=='$' or str(num)[0]=='#') and str(num)[-1].isdigit() and len(str(num))<10:
    #cuando detecte que es un numero 
      if str(num)[0].isdigit() or str(num)[0]=='-':
	dato=locale.format("%.2f",float(num),grouping=True)
      elif str(num)[0]=='$':
	dato="$%s"%locale.format("%.2f",float(num[1:]),grouping=True)
    return dato 
    
def getComboModelKey( combo, col=0): #Esta funcion devuelve el valor de la columna del elemento seleccionado de un combo model
  combo.model().celda(combo.currentIndex(),col)
  #print combo.model().celda(combo.currentIndex(),col)

def setComboModelKey(combo, key): #Establece el combo en el valor de la llave
  combo.setCurrentIndex ( combo.model().buscarKey(key,0) )
  
class editorSimple(QtGui.QDialog, Editor):
    def __init__(self,parent, archivo):
	QtGui.QDialog.__init__(self)
	self.setupUi(self)
	self.parent=parent
	self.archivo=archivo
	self.connect(self, QtCore.SIGNAL("accepted()"), self.guardar)
	f=open(archivo,'r+')
	ticket=f.read()
	f.close()
	self.teTicket.insertPlainText(ticket)
	#self.imprimir()

    def guardar(self):
	print "Guardando cambios..."
      	f=open(self.archivo,'w+')
	ticket=self.teTicket.toPlainText()
	f.write(ticket)
	f.close()
    #Esta funcion lee el contenido del editor y lo pasa a un archivo de PDF 
    def imprimir(self, nombre='/tmp/editor.pdf'):
      printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
      printer.setPaperSize(QtGui.QPrinter.Letter)   
      printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
      printer.setCreator ("Pyventa : Software de punto de venta.")
      #nombre=os.path.join("/tmp","Editor.pdf")
      printer.setOutputFileName(nombre)
      self.teTicket.print_(printer)
      nombre=nombre.replace(" ","\\ ")
      #Esta instruccion se encarga llamar al sistema para que el archivo sea abierto por el programa designado para leer PDF
      if sys.platform == 'linux2':
	  os.system("gnome-open %s"%nombre)
      elif sys.platform == 'win32':
	  os.system("start %s"%nombre)
	
class Documento:
    #Esta es una clase generica para crear un documento en tamano carta, que se podra despues exporar a PDF o PS
    def __init__(self,padre,plantilla,campos):
    #padre es la instancia que invoca, esta debe tener una conexion establecida con la base de datos 
	#QtGui.QDialog.__init__(self)
	#self.setupUi(self)
	self.padre=padre
	self.cursor=padre.cursor
	self.curser=padre.curser
	self.plantilla=plantilla
	self.campos=campos
	self.pages=[]
	self.escena=QtGui.QGraphicsScene()
	self.iniciar()


    def iniciar(self):
      f=open(self.plantilla,"r+")
      self.plantilla=f.read()
      #campos={'%fecha%':self.parent.fecha}
      for key,item in self.campos.iteritems():
	  self.plantilla=self.plantilla.replace(key,item)
      #alto=765
      #ancho=765
      #self.escena.setSceneRect(0,0,ancho,alto)
      droid=QtGui.QFont("Droid Sans", 8, QtGui.QFont.Bold)
      productos=self.escena.addText(" ",droid)
      productos.setHtml(self.plantilla)
      productos.setPos(0,0)      
      #self.gvDocumento.setScene(self.escena)
      #self.guardarPDF()
      
    def br(self,texto):
	 offset=1
	 font=texto.font()
	 pos=texto.pos()
	 print "pos.y=%s font.pointSize=%s"%(pos.y(),font.pointSize())
	 return QPointF(pos.x(),float(pos.y())+float(font.pointSize())+offset)
	
    def addPixmap(self,pix,x=0,y=0):
	pix=self.escena.addPixmap(pix)
	pix.setPos(x,y)
	
    def addPage(self,scene):
	self.pages.append(scene)
    
    
    def guardarPDF(self):
      	printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
	printer.setPaperSize(QtGui.QPrinter.Letter)   
	printer.setColorMode(QtGui.QPrinter.Color)   
	printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
	printer.setCreator ("Pyventa : Software de punto de venta.")
	nombre=os.path.join(os.path.expanduser('~'),"%s.pdf"%self.campos['titulo'])
	File = QtGui.QFileDialog()
	saveFile = str(File.getSaveFileName(self.padre, "Guardar pdf",nombre))
	if (saveFile!=""):
	    printer.setOutputFileName(saveFile)
	#printer.setOutputFileName(nombre)
	    paint=QtGui.QPainter()
	    paint.begin(printer)
	    self.escena.render(paint)
	    for page in self.pages:
	      printer.newPage()
	      page.render(paint)
	    paint.end()
	    #nombre=nombre.replace(" ","\\ ")
	    if sys.platform == 'linux2':
		os.system("gnome-open '%s'"%saveFile)
	    elif sys.platform == 'win32':
		os.system("start '%s' "%saveFile)
	
    #def imprimir(self):
      	#printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
	#printer.setPaperSize(QtGui.QPrinter.Letter)   
	#printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
	#printer.setCreator ("Pyventa : Software de punto de venta.")
	#printer.newPage()
	
	#printer.setOutputFileName(os.path.join(home,"%s.pdf"%self.campos['titulo']))
	#prev=QtGui.QPrintDialog(printer,self.padre)
	#if prev.exec_()==QtGui.QDialog.Accepted:
		#paint=QtGui.QPainter()
		#paint.begin(printer)
		#self.escena.render(paint)
		#paint.end()
		#print "Imprimiendo..."
class Konfig:
  #Esta clase se encarga de hacer la interfaz del archivo de configuracion
  def __init__(self):
    self.cfg=None
    self.ruta=os.path.join(home,"config.cfg")
    try:
      os.stat(self.ruta)
    except:
      print "El archivo de configuracion no fue encontrado.\nCreando uno..."
      copy2("/usr/share/pyventa/perfil/config.cfg",self.ruta)
    else:  
      cfg = Cp.ConfigParser()
      if cfg.read([self.ruta]):
	  self.cfg=cfg

  def getDato(self,modulo,propiedad):
     if self.cfg.has_option(modulo,propiedad):
	return self.cfg.get(modulo,propiedad)
     else:
	self.setCambio(modulo,propiedad,0)
	return 0
      
  def config(self):
      return self.cfg
      
  def guardar(self):
  #Escribe todo el archivo con los cambios que se hayan realizado
      self.cfg.write(open(self.ruta,"w+"))

  def setCambio(self,modulo,propiedad,valor):
  #Registra el valor de un campo(propiedad) de un modulo  
      try:
	self.cfg.set(str(modulo),str(propiedad),str(valor))
      except:
	print "No se guardo la configuracion"
      else:
	self.guardar()
	
	
      
class conexion:
    def __init__(self):
	self.cfg = Cp.ConfigParser()
	if self.cfg.read([os.path.join(home,"config.cfg")]):
	  if self.cfg.has_option("mysql", "user"):
	    try:
	      self.host = self.cfg.get("mysql", "host")  
	      self.user = self.cfg.get("mysql", "user")  
	      self.password = base64.b64decode(self.cfg.get("mysql", "pass"))
	      self.data = self.cfg.get("mysql", "db")
	    except:
		  print "Error, no se pudieron leer los datos de configuracion"
	    else:                
		self.conectar()
	  else:
		  print "Error al conectarse con la base de dato, datos insuficientes en el archivo de configuraciones"

	else:  
	      print "No se encontro el nombre en el archivo de configuracion."    

    def asistente(self):
	print "Configurando base de datos"
	ui = configurador(os.path.join(home,"config.cfg"))
	dialog=ui.exec_()
	if (dialog==1):
	  self.__init__()  
	  
    def conectar(self):
      try:
	self.db = My.connect(self.host, self.user, self.password,self.data)
      except:
	    print "Error al conectar a la base de datos"
	    self.asistente()
      else:                
	  self.cursor = self.db.cursor()
	  self.curser=  self.db.cursor(My.cursors.DictCursor)	


    def close(self):
	self.db.close()
	
    def query(self,string,single=False,tipo=0):
      if tipo==0: #Tipos{ 0:Tupla,1:Diccionario} 
	cursor=self.cursor
      else:
	cursor=self.curser  
      try: 
	cursor.execute(string)
      except My.Error, e:
	if (e.args[0]==2006):
	  self.conectar()
	elif (e.args[0]==1054):
	  print "La version de la base de datos es incorrecta. Configure nuevamente la base de datos"
	  print e
	  self.asistente()
	else:
	  print e
	  return None
      else:
	ret=None
	if single: #Single es en caso de que se requiera solo un resultado devuelve una tupla, caso contrario una lista de tupla
	  ret=cursor.fetchone()
	  return ret
	else:
	  ret=cursor.fetchall()
	  return ret
	  
class Respaldo:

    def __init__(self,conn=False):
        if not conn:
	  self.con=conexion()
	else:
	  self.con=conn

    def restaurar(self,File,database=True, config=True):
    #Esta funcion procesa un archivo de respaldo y establece los cambios en la base de datos y la configuracion
    #File es la nombre extendido del archivo de configuracion y db establece que tambien se restaure la base de datos del respaldo
    #en caso contrario(False) solo restaurara los archivos de configuracion
	print "Restaurando ",File
	#Extrae el paquete de respaldo
	tar = tarfile.open(str(File), "r:bz2") 
	if config:#Para el caso que se quiera restaurar las personalizaciones
	  tar.extractall(os.path.split(home)[0])
	  #print os.path.basename(home),home
	if database: #En el caso que se quiera restaurar la base de datos
	  tar.extract("respaldo.sql",home)
	  #Se conecta con el servidor
	  host = self.con.host 
	  user = self.con.user
	  password =self.con.password
	  data = self.con.data
	  respaldo=os.path.join(home,"respaldo.sql")
	  if os.path.exists(respaldo):
	    try:
		retcode = call("cat {4} | mysql -u{0} -h{1} -p{2} {3} ".format(user,host,password,data,respaldo), shell=True)
		if retcode < 0:
		    print >>sys.stderr, "Child was terminated by signal", -retcode
		    return False
		else:
		    print >>sys.stderr, "Child returned", retcode
		    #os.unlink(respaldo)
		    return True
	    except OSError as e:
		print >>sys.stderr, "Execution failed:", e
		return False
		#print "No se ha restaurado la base de datos, asegurese que tiene instalado mysql y que esta en variables globales de su sistema operativo."
		#os.unlink(respaldo)
	    ##Importacion de base de datos
	    #try:
	      #if sys.platform == 'linux2':
		
		##os.system("mysql -u%s -h%s -p%s %s < %s"%(user,host,password,data,respaldo))
	      #else:
		#os.system("%MYSQL% -u%s -h%s -p%s %s < %s"%(user,host,password,data,respaldo))	  
	    #except:
	      #ret=False
	      #print "No se ha restaurado la base de datos, asegurese que tiene instalado mysql y que esta en variables globales de su sistema operativo."
	    #else:
	      #os.unlink(respaldo)
	      #return True
	  else: 
	      print "El archivo de configuracion no es valido"
	      return False
	else:
	  return True
	tar.close()
	


    def respaldarLocal(self):
	lpath=str(self.con.cfg.get('respaldo','lpath'))
	if len(lpath)<1:
	  print "No se ha definido una ruta valida"
	  return	
	fecha= datetime.date.today()
	hoy= fecha.strftime("%d-%m-%Y")
	host = self.con.host 
	user = self.con.user
	password =self.con.password
	data = self.con.data
	print "Guardando..."
	respaldo=os.path.join(str(lpath),"respaldo.sql")
	ret=os.system("mysqldump -u%s -h%s -p%s %s --add-drop-table > %s"%(user,host,password,data,respaldo))
	tarname=os.path.join(str(lpath),"respaldo_"+self.con.cfg.get("empresa","nombre")+"-pyventa_"+str(hoy)+".tar.bz2")
	out = tarfile.TarFile.open(tarname,'w:bz2')
	out.add(respaldo,arcname=os.path.basename(respaldo))
	out.add(home,arcname=os.path.basename(home))
	os.unlink(respaldo)
	out.close()
	return tarname

class AperturaCaja(QtGui.QDialog, Apertura):
    def __init__(self,parent=None):
    		QtGui.QDialog.__init__(self,parent)
		self.setupUi(self)
		self.cursor=parent.cursor
		self.parent=parent
        	self.connect(self, QtCore.SIGNAL("accepted()"), self.setInicial)  
        	
    def setInicial(self):
      if self.parent.caja>0:
	inic=float(self.dsbInicial.value())
	sql="UPDATE cajas set saldo_inicial=%s WHERE num_caja=%s;"%(inic,self.parent.caja)
	self.cursor.execute(sql)
	self.parent.conexion.commit()
	
        	
class Seguridad(QtGui.QDialog, Ui_Acceso):
    def __init__(self,parent=None):
    		QtGui.QDialog.__init__(self,parent)
		#self.con=conexion()
		#self.curser=self.con.curser
		self.setupUi(self)
		self.cursor=parent.cursor
		self.curser=parent.curser
		self.con=conexion()
		self.home=home
		self.count=0
		self.usuario={'nivel':0,'nombre':'Pyventa','usuario':'Pyventa','id_usuario':1}
		self.pbAceptar.setDefault(True)
		self.pbCerrar.setVisible(False)
        	self.connect(self.leClave, QtCore.SIGNAL("returnPressed()"), self.autentificar)
        	self.connect(self.pbAceptar, QtCore.SIGNAL("clicked()"), self.autentificar)
        	self.connect(self, QtCore.SIGNAL("reject()"), self.getUser)
        	self.connect(self.pbCerrar, QtCore.SIGNAL("clicked()"), lambda:self.done(-1))
        	
    def getUser(self):
      return self.usuario
      
    def autentificar(self):
	usuario=str(self.leUsuario.text())
	clave=str(self.leClave.text())
	
	if len(usuario)>0:
	  #try:
	    #self.curser.execute("SELECT * from usuarios where user='"+str(usuario)+"' and pass=MD5('"+str(clave)+"')")
	  #except My.Error, e:
	    #if (e.args[0]==2006):
	      #self.parent.conexion()
	      #self.autentificar()
	    #else:
	      #print e
	      #self.lbInfo.setText("Hay un problema con la base de datos, es posible que sus datos sean incorrectos")
	      #print "Hay un problema con la base de datos, es posible que sus datos sean incorrectos"
	  #else:
	    #user=self.curser.fetchone()
	    user=self.con.query("SELECT * from usuarios where usuario='"+str(usuario)+"' and clave=MD5('"+str(clave)+"')",True,1)
	    if user!=None:
	      if user['nivel']>0:
		self.lbInfo.setText("<h2>Bienvenido %s </h2>"%user['nombre'])
		print "Bienvenido %s "%user['nombre']
		self.usuario=user
		self.done(int(user['id_usuario']))
	    else:
		if self.count<2:
		  self.lbInfo.setText("<h3>El usuario/clave son incorrectos</h3> Intentelo nuevamente.")
		  self.count+=1
		else:
		  self.done(-1)

class VisorNotas(QtGui.QDialog, Ui_Resumen):
    def __init__(self,parent,ide=-1):
    		QtGui.QDialog.__init__(self,parent)
		self.setupUi(self)
		self.parent=parent
		self.ide=ide
		tipo=['Nota','Factura']
		status=['Sin pagar','Efectivo','Credito']
		if self.ide!=-1:
		  self.parent.curser.execute("select id,cliente,tipo, status, total from  notas where id="+str(ide))
		  nota=self.parent.curser.fetchone()
		  if nota!=None:
		    self.lbResumen.setText("<b>Venta:</b> %s    <b>Cliente:</b> %s <br><b>Tipo de venta:</b> %s    <b>Forma de pago:</b> %s <br> <h2>Total: %s </h2>"%(nota['id'],nota['cliente'],tipo[int(nota['tipo'])],status[int(nota['status'])],nota['total']))
		    head=['ref','Descripcion','Cantidad','Precio','Total']
		    col=','.join(head).lower()
		    sql="select "+col+" from productos,vendidos where ref=producto and venta="+str(ide)
		    tabular(self.twProductos,sql,head)
		    self.nota=nota
		  else:
		    self.lbResumen.setText("No se encontro la nota")
		    self.nota=False
    
    def getDatos(self):
     #Devuelve una tupla con del tipo [id, cliente, tipo, status, total]
      return self.nota
      
class ResumenVenta(QtGui.QDialog, Ui_RVenta):
    def __init__(self,parent=None,datos={'total':0,'modo':'efectivo','recibido':0,'cambio':0,'articulos':0}):
	QtGui.QDialog.__init__(self,parent)
	self.setupUi(self)
	self.info.setText("""<table width="100%%" cellpading="0" cellspacing="5">
 <tr>
  <td width="70%%"><h1>Total</h1></td>  <td width="30%%" align="right"><h1>$%s</h1></td>
</tr>
 <tr>
  <td width="70%%"><h2>Monto recibido: </h2></td>  <td width="30%%" align="right"><h2>$%s</h2></td>
</tr>
 <tr>
  <td width="70%%"><h2>Num. de articulos: </h2></td>  <td width="30%%" align="right"><h2>#%s</h2></td>
</tr>
</table>"""%(cifra(datos['total']),cifra(datos['recibido']),datos['articulos']))
	self.cambio.setText(str(cifra(datos['cambio'])))
	self.connect(self.aceptar, QtCore.SIGNAL("clicked()"), self.accept)    
	
class Factura:
    def __init__(self,padre,num):
	self.padre=padre
	self.cursor=padre.cursor
	self.curser=padre.curser
	self.parent=padre
	self.num=num
	self.escena=QtGui.QGraphicsScene()
	self.gvDocumento=QtGui.QGraphicsView()
	self.iniciar()

    def iniciar(self):
      if self.cargarPlantilla():
	iva=0
	subtotal=0
	total=0
	alto=int(self.cfg.get("documento", "alto"))
	ancho=int(self.cfg.get("documento", "ancho"))
	cfont=QtGui.QFont("Droid Sans", int(self.cfg.get("cliente", "fuente")), int(self.cfg.get("cliente", "peso") ))
	pfont=QtGui.QFont("Droid Sans", int(self.cfg.get("productos", "fuente")), int(self.cfg.get("productos", "peso") ))
	ffont=QtGui.QFont("Droid Sans", int(self.cfg.get("fecha", "fuente")), int(self.cfg.get("fecha", "peso") ))
	tfont=QtGui.QFont("Droid Sans", int(self.cfg.get("totales", "fuente")), int(self.cfg.get("totales", "peso") ))
	self.escena.setSceneRect(-int(self.cfg.get("documento", "x")),-int(self.cfg.get("documento", "y")),ancho,alto)
	fuente=QtGui.QFont("Droid Sans", int(self.cfg.get("documento", "fuente")), int(self.cfg.get("documento", "peso") ))
	smallDroid=QtGui.QFont("Droid Sans", 9)
	self.curser.execute("""SELECT * FROM clientes as C, notas WHERE notas.id=%s and notas.cliente=C.id;"""%self.num)
	cliente=self.curser.fetchone()
	if cliente!=None:
	  cliente=dicursor(self.curser,cliente)
	datos=self.escena.addText("",cfont)
	datos.setHtml("<p><b>Nombre:</b> %s<br><b>Direccion:</b>  %s, C.P %s %s, %s.<br><b>RFC:</b>  %s</p>"%(cliente['nombre'],cliente['direccion'],cliente['correo'],cliente['poblacion'],cliente['estado'],cliente['rfc']))
	datos.setPos(int(self.cfg.get("cliente", "x")) ,int(self.cfg.get("cliente", "y")))
	datos.setTextWidth(int(self.cfg.get("cliente", "ancho")))
	self.curser.execute("SELECT cantidad, `descripcion`,precio,total,porcentaje as imp from productos,vendidos, impuestos where ref=producto and venta="+str(self.num)+" and impuestos.id=impuesto group by ref")
	fecha=self.escena.addText("",ffont)
	fecha.setHtml(datetime.datetime.strptime(cliente['fecha'],'%Y-%m-%d').strftime(self.cfg.get("fecha", "formato")))
	fecha.setPos(int(self.cfg.get("fecha", "x")),int(self.cfg.get("fecha", "y")))
	fecha.setTextWidth(int(self.cfg.get("fecha", "ancho")))
	#print "SELECT cantidad, `descripcion`,precio,total from productos,vendidos where ref=producto and venta="+str(self.num)+" group by ref"
	arts=self.curser.fetchall()
	col=[[],[],[],[]]
	#dict(arts)
	for item in arts:
	  imp=0;porc=0
	  imp=item['total']/float("1.%d"%item['imp'])
	  porc=imp*(int(item['imp'])*.01)
	  #imp=round(imp,2)
	  #porc=round(porc,2)
	  #porc+=item['total']-(imp+porc)
	  total+=item['total']
	  item['precio']=round(imp/item['cantidad'],2)
	  item['total']=round(imp,2) 
	  iva+=porc
	  subtotal+=imp
	subtotal=round(subtotal,2)
	iva=round(iva,2)
	for item in arts:
	    col[0].append("%.2f"%float(item['cantidad']))
	    col[1].append(str(item['descripcion']))
	    col[2].append("%.2f"%float(item['precio']))
	    col[3].append("%.2f"%float(item['total']))
	#tbl="<table width='%s%%' border='0' cellpadding=3 cellspacing=1 align='center'>"%self.cfg.get("productos", "ancho")
	#tbl+="<tr bgcolor=\"#ddd\" valign='middle' width='100%%' > <TH>1</TH><TH>2</TH><TH>3</TH><TH>4</TH></TR>"

	#for item in arts:
	  #tbl+="<tr bgcolor=\"#ddd\" valign='middle' width='100%%' >"
	  #tbl+="<td width='%s%%' align=\"right\"><span> %3.2f </span></td>"%(self.cfg.get("cantidad", "ancho"),float(item['cantidad']))
	  #tbl+="<td width='%s%%' align=\"center\"> <span> %s </span> </td>"%(self.cfg.get("desc", "ancho"),item['descripcion'])
	  #tbl+="<td width='%s%%' align=\"right\"><span> %3.2f </span> </td>"%(self.cfg.get("precio", "ancho"),float(item['precio']))
	  #tbl+="<td width='%s%%' align=\"right\"> <span> %3.2f </span></td>"%(self.cfg.get("total", "ancho"),float(item['total']))
	  #tbl+="</tr>"	  
	#tbl+="</table>"
	#print tbl
	#tabla=self.escena.addText("",pfont)  
	#tabla.setHtml(tbl)
	#tabla.setPos(int(self.cfg.get("productos", "x")),int(self.cfg.get("productos", "y")))   
	#cnt=
	cant=self.escena.addText("",pfont)
	cant.setHtml("<p ALIGN=right>%s</p>"%('<br>'.join(col[0])))
	cant.setPos(int(self.cfg.get("cantidad", "x")),int(self.cfg.get("productos", "y")))
	cant.setTextWidth(int(self.cfg.get("cantidad", "ancho")))

	desc=self.escena.addText('\n'.join(col[1]),pfont)
	desc.setPos(int(self.cfg.get("desc", "x")),int(self.cfg.get("productos", "y")))
	#desc.setTextWidth(int(self.cfg.get("desc", "ancho")))

	precio=self.escena.addText("",pfont)
	precio.setHtml("<p ALIGN=right>%s</p>"%('<br>'.join(col[2])))
	precio.setPos(int(self.cfg.get("precio", "x")),int(self.cfg.get("productos", "y")))
	precio.setTextWidth(int(self.cfg.get("precio", "ancho")))
	
	imp=self.escena.addText("",pfont)
	imp.setHtml("<p ALIGN=right>%s</p>"%('<br>'.join(col[3])))
	imp.setPos(int(self.cfg.get("total", "x")),int(self.cfg.get("productos", "y")))
	imp.setTextWidth(int(self.cfg.get("total", "ancho")))
	
	#col[1]=self.escena.addText('\n'.join(col[1]),pfont)
	#col[1].setPos(int(self.cfg.get("desc", "x")),int(self.cfg.get("productos", "y")))
	#col[2]=self.escena.addText('\n'.join(col[2]),pfont)
	#col[2].setPos(int(self.cfg.get("precio", "x")),int(self.cfg.get("productos", "y")))
	#col[3]=self.escena.addText('\n'.join(col[3]),pfont)
	#col[3].setPos(int(self.cfg.get("total", "x")),int(self.cfg.get("productos", "y")))
	cantidad=self.escena.addText("",pfont)
	cantidad.setHtml("<center>%s</center>"%nletra(total))
	cantidad.setPos(int(self.cfg.get("nletra", "x")),int(self.cfg.get("nletra", "y")))
	cantidad.setTextWidth(int(self.cfg.get("nletra", "ancho")))
	totales=self.escena.addText("",tfont)
	totales.setHtml("<p ALIGN=right>%.2f</p><p ALIGN=right>%.2f</p><p ALIGN=right>%.2f</p>"%(float(subtotal),float(iva),float(total)))
	totales.setPos(int(self.cfg.get("totales", "x")),int(self.cfg.get("totales", "y")))
	totales.setTextWidth(int(self.cfg.get("totales", "ancho")))
	#self.curser.execute("SELECT cantidad, `descripcion`,precio,total from productos,vendidos where ref=producto and venta="+str(self.num)+" group by ref")
	
	self.gvDocumento.setScene(self.escena)
      else:
	print "Error al cargar plantilla"
	
    def alinear(self,item):
      formato=QtGui.QTextBlockFormat()
      formato.setAlignment(Qt.AlignRight)
      cursor = item.textCursor()
      cursor.select(QTextCursor.Document)
      cursor.mergeBlockFormat(formato)
      cursor.clearSelection()
      item.setTextCursor(cursor)

    def cargarPlantilla(self):
	self.cfg = Cp.ConfigParser()
	if self.cfg.read([os.path.join(home,"formas","factura.cfg")]):
	  if self.cfg.has_option("documento", "version"):
	    return True
	else:
	  return False
    
	
    def br(self,texto):
	 offset=1
	 font=texto.font()
	 pos=texto.pos()
	 return QPointF(pos.x(),float(pos.y())+float(font.pointSize())+offset)

    def imprimir(self):
      	printer=QtGui.QPrinter(QtGui.QPrinter.HighResolution)
	printer.setPaperSize(QtGui.QPrinter.Letter)   
	printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
	ruta=os.path.join(self.parent.cfg.get("factura", "ruta"),'Factura-'+str(self.num)+'.pdf')
	printer.setOutputFileName(ruta)
	prev=QtGui.QPrintDialog(printer,self.padre)
	if prev.exec_()==QtGui.QDialog.Accepted:
	    paint=QtGui.QPainter()
	    paint.begin(printer)
	    self.escena.render(paint)
	    paint.end()
	    print "Imprimiendo..."
	    
	if sys.platform == 'linux2':
	    os.system("gnome-open '%s'"%ruta)
	elif sys.platform == 'win32':
	    os.system("start '%s'"%ruta)
	  

	
		

#from ui_documento import Ui_Form
#class Documento(QtGui.QDialog, Ui_Form):	
  
def nletra(numero): #Traduce un entero en letra
    print numero
    numero=round(numero,2)
    print numero
    
    num=str(numero)
    num=num.split('.')
    if len(num[1])<2:
      num[1]+='0'
    ret="***( "+numerals(int(num[0]),0)+" PESOS "+num[1]+"/100 M.N)***"    
    #ret="***( "+numerals(int(num[0]),0)+" PESOS "+num[1]*10+"/100 M.N)***"
    #print num[1]*10
    return ret.upper()
    
def tabular(tabla, vector,head, padre):
      modelo = MyTableModel(vector, head, padre) 
      tabla.setModel(modelo)
      #self.tabular(tabla,sql,head)
      #tabla.setColumnHidden(0,True)
      tabla.resizeColumnsToContents()
      return modelo
	      
def entablar(tabla,lista,head):
	    #Cumple la misma funcion que tabular, con la diferencia que esta recibe una lista de tuplas 
	      tabla.clear()
	      tabla.setColumnCount(len(head))
	      tabla.setRowCount(len(lista))	 	 
	      for i,data in enumerate(head):
		  item = QtGui.QTableWidgetItem(1)
		  item.setText(str(data))
		  tabla.setHorizontalHeaderItem(i,item)
	      for i,elem in enumerate(lista):
		  for j,data in enumerate(elem):
		    item = QtGui.QTableWidgetItem(1)
		    item.setText(str(data))
		    tabla.setItem(i,j,item)
	      tabla.resizeColumnsToContents()       
	      
class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        QAbstractTableModel.__init__(self, parent, *args) 
        self.parent=parent
        self.arraydata = datain
        self.headerdata = headerdata
        
    def addRow(self,row):
	self.beginInsertRows ()
	self.arraydata.append(row)
	self.endInsertRows ()
	
    def delRow(self,row):
      self.arraydata.remove(row)
      
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.headerdata) 
        
    def getVector(self):
	return self.arraydata
	
    def setVector(self, vector):
	self.arraydata=vector
	self.reset()
	
    def getRowCount(self):
	return len(self.arraydata)
	
    def getParticion(self,a=0,b=1):
	tmp=[]
	for item in self.arraydata:
	  tmp.append(item[a:b])
	return MyTableModel(tmp,self.headerdata,self.parent)
	
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        #elif role != Qt.DisplayRole: 
            #return QVariant() 
	#elif role == Qt.TextAlignmentRole:
	  #return Qt.AlignCenter    
	##print index.row(),index.column(),len(self.arraydata)
        #return QVariant(self.arraydata[index.row()][index.column()]) 
        try:
	  col=self.arraydata[index.row()][index.column()]
	  if role == Qt.DisplayRole and str(type(self.arraydata[index.row()][index.column()]))!='<type \'date\'>':
	      return QVariant(str(self.arraydata[index.row()][index.column()]))
	      
	  elif role == Qt.TextAlignmentRole and (str(col)[0].isdigit() or str(col)[0]=='-' or str(col)[0]=='$' or str(col)[0]=='#') and str(col)[-1].isdigit() and len(str(col))<10:
	   #cuando detecte que es un numero 
	    return QVariant(Qt.AlignRight | Qt.AlignVCenter)
	except:
	    pass
	    #return QVariant() 

    def getFila(self, index): 
        if not index.isValid(): 
            return QVariant() 
	#if str(type(self.arraydata[index.row()][col]))=="<type 'datetime'>":
	          #return self.arraydata[index.row()][col]
	#else:
	return self.arraydata[index.row()]
	
    def getCell(self, index,col): 
        if not index.isValid(): 
            return QVariant() 
	#if str(type(self.arraydata[index.row()][col]))=="<type 'datetime'>":
	          #return self.arraydata[index.row()][col]
	#else:
	return self.arraydata[index.row()][col]
        
    def celda(self, row,col): 
	#print row,col,self.arraydata[row][col]
        return str(self.arraydata[row][col]) 
        
    def buscarKey(self, valor,col): #Busca un valor en el numero de columna
	for i,fila in enumerate(self.arraydata):
	  if str(fila[0])==str(valor):
	    return i
        return -1    
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])	

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))
        
class MyListModel(QtCore.QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()])
        else: 
            return QVariant()
            




