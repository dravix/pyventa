from PyQt4.QtGui import QGraphicsScene,QGraphicsView, QFont, QTextBlockFormat, QPrinter, QPrintDialog, QDialog, QPainter
from lib.librerias.conexion import dicursor 
from lib.librerias.comun import * 
import ConfigParser as Cp
import datetime, time
from lib.libutil import listaHtml
from lib.nletras import nletra

class Factura:
    def __init__(self,padre,num):
	self.padre=padre
	self.cursor=padre.cursor
	self.curser=padre.curser
	self.parent=padre
	self.num=num
	self.escena=QGraphicsScene()
	self.gvDocumento=QGraphicsView()
	#self.cfg=padre.cfg
	self.iniciar()

    def iniciar(self):
      if self.cargarPlantilla():
	iva=0
	subtotal=0
	total=0
	alto=int(self.cfg.get("documento", "alto"))
	ancho=int(self.cfg.get("documento", "ancho"))
	cfont=QFont("Droid Sans", int(self.cfg.get("cliente", "fuente")), int(self.cfg.get("cliente", "peso") ))
	pfont=QFont("Droid Sans", int(self.cfg.get("productos", "fuente")), int(self.cfg.get("productos", "peso") ))
	ffont=QFont("Droid Sans", int(self.cfg.get("fecha", "fuente")), int(self.cfg.get("fecha", "peso") ))
	tfont=QFont("Droid Sans", int(self.cfg.get("totales", "fuente")), int(self.cfg.get("totales", "peso") ))
	self.escena.setSceneRect(-int(self.cfg.get("documento", "x")),-int(self.cfg.get("documento", "y")),ancho,alto)
	fuente=QFont("Droid Sans", int(self.cfg.get("documento", "fuente")), int(self.cfg.get("documento", "peso") ))
	smallDroid=QFont("Droid Sans", 9)
	sql="""SELECT * FROM clientes as C, notas WHERE notas.id=%s and notas.cliente=C.id;"""%self.num
	self.curser.execute(sql)
	cliente=self.curser.fetchone()
	if cliente!=None:
	  cliente=dicursor(self.curser,cliente)
	datos=self.escena.addText("",cfont)
	datos.setHtml("<p><b>Nombre:</b> %s<br><b>Direccion:</b>  %s, C.P %s %s, %s.<br><b>RFC:</b>  %s</p>"%(cliente['nombre'],cliente['direccion'],cliente['correo'],cliente['poblacion'],cliente['estado'],cliente['rfc']))
	datos.setPos(int(self.cfg.get("cliente", "x")) ,int(self.cfg.get("cliente", "y")))
	datos.setTextWidth(int(self.cfg.get("cliente", "ancho")))
	self.curser.execute("SELECT cantidad, `descripcion`,total/cantidad as precio,total,porcentaje as imp,unidades.nombre as unidad, ' ' as espacio  from productos,vendidos, impuestos , unidades where ref=producto and venta="+str(self.num)+" and impuestos.id=impuesto and unidades.id=unidad group by ref")
	fecha=self.escena.addText("",ffont)
	if isinstance(cliente['fecha'],datetime.datetime):
	  fecha.setHtml(cliente['fecha'].strftime(self.cfg.get("fecha", "formato")))
	else:
	  fecha.setHtml(datetime.datetime.strptime(cliente['fecha'],'%Y-%m-%d %H:%M:%S').strftime(self.cfg.get("fecha", "formato")))
	fecha.setPos(int(self.cfg.get("fecha", "x")),int(self.cfg.get("fecha", "y")))
	fecha.setTextWidth(int(self.cfg.get("fecha", "ancho")))
	#print "SELECT cantidad, `descripcion`,precio,total from productos,vendidos where ref=producto and venta="+str(self.num)+" group by ref"
	arts=self.curser.fetchall()
	if arts!=None:
	  arts=dicursor(self.curser,arts)
	  col=[[],[],[],[],[]]
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
	  filas=[]
	  campos=self.cfg.get("productos", "campos").replace(" ","").split(",")
	  heads="{%s}"%"},{".join(campos)
	  anchos=self.cfg.get("productos", "anchos").replace(" ","").split(",")
	  #cabezas=heads.replace("{","").replace("}","").split(",")
	  for item in arts:
	      row=heads.format(**item)
	      filas.append(row.split(','))

	  heads=heads.replace("{","").replace("}","") 
	  tabla=self.escena.addText("",pfont)
	  tabla.setHtml(listaHtml(filas,cabezas=campos,color='#fff',fondo="#FFF", tfuente=11,opc="101",css="th{color:#FFF} .celda{margin:10px;padding:5px;}",anchos=anchos))
	  tabla.setPos(int(self.cfg.get("productos", "x")),int(self.cfg.get("productos", "y")))
	  tabla.setTextWidth(int(self.cfg.get("productos", "ancho")))

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
      formato=QTextBlockFormat()
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
      	printer=QPrinter(QPrinter.HighResolution)
	printer.setPaperSize(QPrinter.Letter)   
	printer.setOutputFormat(QPrinter.PdfFormat)
	ruta=os.path.join(self.parent.cfg.get("factura", "ruta"),'Factura-'+str(self.num)+'.pdf')
	printer.setOutputFileName(ruta)
	prev=QPrintDialog(printer,self.padre)
	if prev.exec_()==QDialog.Accepted:
	    paint=QPainter()
	    paint.begin(printer)
	    self.escena.render(paint)
	    paint.end()
	    print "Imprimiendo..."
	    
	#if sys.platform == 'linux2':
	    #os.system("gnome-open '%s' "%ruta)
	#elif sys.platform == 'win32':
	    #os.system("start '%s'"%ruta)
	  