import libutil
from PyQt4 import QtCore, QtGui#,  Qt
from PyQt4.QtCore import Qt,QPointF
from PyQt4.QtGui import QPolygonF, QFont, QColor
from lib.modelos.gasto import Gasto 
from lib.modelos.compra import Compra 
from lib.modelos.venta import Venta 
from lib.modelos.caja import Caja 
from lib.modelos.retiro import Retiro 
from lib.modelos.deposito import Deposito 
from lib.modelos.movimiento import Movimiento 

class Chart:
  def __init__(self,parent,w=650,h=500):
    self.parent=parent
    self.cursor=parent.cursor
    self.width=w
    self.height=h
    self.area=False
    #self.grafica=self.parent.vgrafica
    #self.grafica.setSceneRect(0,0,w,h)

  def toPixmap(self):
    #image=QtGui.QImage()
    #painter=QtGui.QPainter(image)
    #painter.setRenderHint(QtGui.QPainter.Antialiasing)
    #self.escena.render(painter)
    #image.save(name)
    #return image
    pixMap=QtGui.QPixmap(self.width,self.height);
    pixMap.fill(Qt.white)
    p=QtGui.QPainter(pixMap);
    self.escena.render(p);
    p.end();
    return pixMap
  
  def popGrafica(self,pixMap):
    dia=QtGui.QDialog(self.parent)
    #pix=QtGui.QLabel(self.parent).setPixmap(pixMap)
    #dia.addWidget(pix)
    #dia.setLayout(QtGui.QHBoxLayout(self.parent).addWidget())
    dia.show()

      
  def setGrafica(self,datos,w=450,h=200,label=True):
	if len(datos[0])>0:
    	  self.escena=QtGui.QGraphicsScene()
    	  self.escena.setBackgroundBrush(QtGui.QColor('#fff'))
    	  rBrush=QtGui.QBrush(QtGui.QColor(101, 163, 255, 100))
    	  area=QtGui.QBrush(QtGui.QColor(135, 190, 80, 100))
    	  #area=QtGui.QBrush(QtGui.QColor("#500"))
    	  pen=QtGui.QPen()
    	  pen.setWidth(2)
    	  pen.setCosmetic(True)
    	  shadow=QtGui.QPen()
    	  shadow.setColor(QtGui.QColor('#555'))
    	  pen.setColor(QtGui.QColor('#333'))
    	  grid=QtGui.QPen(QtGui.QColor("#999"),1,Qt.DashLine)
    	  gridThick=QtGui.QPen(QtGui.QColor("#AAA"),2,Qt.SolidLine)
    	  top=200
    	  alto=h-20
    	  width=w
   	  ancho=(width-100)/len(datos[1])
	  maxim=max(datos[0])
	  Y=alto-50
	  self.escena.addLine(70,0,70,Y,pen)
	  self.escena.addLine(0,Y,width-10,Y,pen)
  	  for i in range(5):
	    self.escena.addLine(60,Y*i*.25,width-20,Y*i*.25,grid)
	    text=self.escena.addSimpleText(str(round(maxim*i*.25,1)))
	    text.setPos(5,Y-(Y*i*.25))
	  puntos=[]
	  for i,val in enumerate(datos[0]):
	    if maxim>0:
	      scale=(float(val)/float(maxim))*(alto-50)
	      #self.escena.addRect((ancho*i)+80, (alto-50)-scale,ancho,scale,pen,rBrush)
	      if len(datos[0])>10:
		  n=round(len(datos[0])*.05)
	      else:
		  n=1
	      if i>0:
		(x1,y1)=(ax,ay)
		(x2,y2)=((ancho*i)+85,alto-50-scale)
		#self.escena.addLine(x1,y1,x2,y2,shadow)
		#self.escena.addLine(ax,ay,(ancho*i)+85,alto-50-scale,pen)
		#self.escena.addEllipse((ancho*i)+84,alto-51-scale,4,4,shadow)
	      (x,y)=(ancho*i)+85,alto-50-scale
	      puntos.append(QPointF(x,y))
	      self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,y,grid)
	      if i%n==0:
		text=self.escena.addSimpleText(str(datos[1][i]))
		text.setPos((ancho*i)+85,alto-35)
		self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,alto-35,gridThick)
	      ax=(ancho*i)+85
	      ay=alto-50-scale
	  puntos.append(QPointF(puntos[-1].x(),Y))
	  puntos.append(QPointF(puntos[0].x(),Y))
	  self.area= self.escena.addPolygon(QPolygonF(puntos),pen,area)
	  if label:
	    for i,p in enumerate(puntos[:-2]):
		lbl=self.escena.addSimpleText("{0:,.2f}".format(datos[0][i]),QFont("Serif", 8, QFont.Bold))
		lbl.setPos(p.x()+4,p.y())
		
	  #self.grafica.setScene(self.escena)  
  def changeColor(self,color):
    if self.area:
      self.area.setBrush(color)
    
#--------------------------------------------------------      
  def hoursPlot(self,fecha='DATE(fecha)=CURDATE()'):
	hours=[]
	total=[]
	sql="SELECT ROUND(sum(total),2) as `total` ,DATE_FORMAT(fecha,'%H') as `hora` FROM `notas` where {fecha} GROUP BY DATE_FORMAT(fecha,'%H')".format(fecha=fecha)
	#print sql
	self.parent.cursor.execute(sql)
	datos=self.parent.cursor.fetchall()
	for hora in datos:
	    hours.append(hora[1])
	    total.append(round(float(hora[0]),1))
	data=[total,hours]
       	self.setGrafica(data,self.width,self.height)
       	
  def dayPlot(self,fecha='DATE(fecha)=CURDATE()'):
	hours=[]
	total=[]
	sql="SELECT ROUND(sum(total),2) as `total` ,DATE_FORMAT(fecha,'%%d') as `hora` FROM `notas` where %s GROUP BY DATE_FORMAT(fecha,'%%j')"%fecha
	#print sql
	self.parent.cursor.execute(sql)
	datos=self.parent.cursor.fetchall()
	for hora in datos:
	    hours.append(hora[1])
	    total.append(round(float(hora[0]),1))
	data=[total,hours]
       	self.setGrafica(data,self.width,self.height)

  def daysPlot(self,fecha='DATE(fecha)=CURDATE()'):
	hours=[]
	total=[]
	sql="""SELECT ROUND(sum(total),2) as `total` ,DATE_FORMAT(fecha,'%d')  FROM `notas`
	where {fecha} GROUP BY DATE_FORMAT(fecha,'%j')""".format(fecha)
	self.parent.cursor.execute(sql)
	datos=self.parent.cursor.fetchall()
	for hora in datos:
	    hours.append(hora[1])
	    total.append(round(float(hora[0]),1))
	data=[total,hours]
       	self.setGrafica(data,self.width,self.height)
       	
  def xPlot(self,formato,group,fecha='DATE(fecha)=CURDATE()'):
	hours=[]
	total=[]
	sql="""SELECT ROUND(sum(total),2) as `total` ,DATE_FORMAT(fecha,'{formato}')  FROM `notas`
	where {fecha} GROUP BY DATE_FORMAT(fecha,'{formato}')""".format(fecha=fecha,formato=formato)
	self.parent.cursor.execute(sql)
	datos=self.parent.cursor.fetchall()
	for hora in datos:
	    hours.append(hora[1])
	    total.append(round(float(hora[0]),1))
	data=[total,hours]
       	self.setGrafica(data,self.width,self.height)
  
  def setTitle(self,titulo):
    text=self.escena.addText(titulo,QFont("Arial", 12, QFont.Bold))
    text.setPos(1,self.height-20)

class Ventas:
    def __init__(self,parent,periodo):
      self.cursor=parent.cursor
      self.curser=parent.curser
      self.conexion=parent.conexion
      self.periodo=periodo
      self.ventas={}
      
    def resumir(self,fecha='date(fecha)=CURDATE()',caja='1'):
	resumen={'ventas':0,'gastos':0,'compras':0, 'inicial':0.0}
	con=self.conexion
	resumen['ventas']=Venta(con).suma(" {0} and {1} and status>0".format(fecha,caja))
	resumen['retiros']=Retiro(con).suma("{0} and {1}".format(fecha,caja))
	resumen['depositos']=Deposito(con).suma("{0} and {1}".format(fecha,caja))
	resumen['gastos']=Gasto(con).suma("{0} and {1}".format(fecha,caja))
	resumen['efectivo']=(resumen['ventas']+resumen['compras']+resumen['gastos']+resumen['retiros']+resumen['depositos'])
	lista=[
	  ['Ventas cobradas:',resumen['ventas']],
	  ['Retiros:',resumen['retiros']],
	  ['Gastos:',resumen['gastos']],
	  ['Depositos:',resumen['depositos']],
	  ['Efectivo final:',resumen['efectivo']]
	  ]
	return (lista,resumen)
      
    def detalleNotas(self,periodo,caja):
	sql="""SELECT ELT(tipo+1,'Notas de venta','Factura'),ELT(status+1,'Sin pagar','Pagadas','En credito'),
	sum(total) from notas where {periodo} and {caja} group by status,tipo;""".format(periodo=self.periodo,caja=caja)
	self.cursor.execute(sql)
	return self.cursor.fetchall()


    def detallarVentas(self,caja='1',color="#fff",fondo="#1162A7"):
      self.cursor.execute("SELECT ROUND(sum(total),2) from notas where {periodo} and {caja}  ".format(periodo=self.periodo,caja=caja))
      rows=self.cursor.fetchone()
      total=rows[0]
      if total==None:
	  total=0
      dns=self.detalleNotas(periodo=self.periodo,caja=caja)
      ventas=libutil.listaHtml(dns,'Detalle de ventas',['Tipo','Estado','Valor'],color,fondo,12,anchos=[40,30,30])	
      tabla=libutil.listaHtml([],"",['SUMA TOTAL:','$ {0:,.2f}'.format(total)],opc="010",anchos=[70,30])
      return ventas+"\n\n"+tabla

    def detallarCajas(self,caja='1'):
      self.cursor.execute("SELECT nombre, ELT(tipo+1,'Nota','Factura') , count(id), ROUND(sum(total),2) from notas,cajas where {periodo} and {caja} and status>0 and num_caja=caja group by tipo,caja order by caja;".format(periodo=self.periodo,caja=caja))
      rows=self.cursor.fetchall()
      self.ventas['general']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['general'],"Ventas cobradas por cajas",['Caja','Tipo','#','Valor'],anchos=[40,20,20,20])
      return tabla
      
    def detallarUsuarios(self,caja='1'):
      self.cursor.execute("select nombre,count(N.id), ROUND(sum(total),2) from notas as N, usuarios as U where {periodo} and status=1 and N.usuario=U.id_usuario and {caja} group by N.usuario order by ROUND(sum(total),2) desc;".format(periodo=self.periodo,caja=caja))
      rows=self.cursor.fetchall()
      self.ventas['usuarios']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['usuarios'],"Total de ventas por usuarios",['Usuario','#','Valor total'],anchos=[60,10,30]) 
      return tabla
     
      
    def detallarDeptos(self,caja='1'):
      periodo=self.periodo.replace("fecha", "n.fecha")
      
      self.cursor.execute("select DISTINCT d.nombre,count(n.id),ROUND(sum(v.total),2) from productos as p, notas as n, vendidos as v, familias as f, departamentos as d where {periodo}  and v.venta=n.id and p.ref=v.producto and f.id=p.familia  and d.id=f.departamento and {caja} group by d.id order by ROUND(sum(v.total),2) desc;".format(periodo=periodo,caja=caja))
      rows=self.cursor.fetchall()
      self.ventas['deptos']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['deptos'],"Total de ventas por departamento",['Departamento','#','Valor total'],anchos=[50,50]) 
      return tabla
      
    def detallarProds(self,caja='1',limit=20):
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT ref,descripcion,ROUND(sum(v.total),2),ROUND(sum(v.cantidad),2), count(n.id), stock_logico, ROUND(stock_logico-sum(v.cantidad),2)*-1,u.nombre  from productos as p, notas as n, vendidos as v, existencia as e, unidades as u where {periodo} and {caja} and v.venta=n.id and p.ref=v.producto and e.producto=ref and u.id=unidad group by ref order by count(n.id) desc limit {limit};".format(periodo=periodo,caja=caja,limit=limit))
      rows=self.cursor.fetchall()
      self.ventas['prods']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['prods'],"Total de ventas por mejores productos",['Ref.','Producto','Monto total','Vendidas','Ventas','Stock <br/>actual','Requeridas','Unidad'],'#fff',"#239AB1", 12,anchos=[6,30,14,10,6,10,10,10]) 
      return tabla
      
    def detallarProdsVendidos(self,caja='1',limit=20):
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT descripcion,count(n.id), ROUND(sum(v.total),2),ROUND(sum(v.cantidad),2),u.nombre, stock_logico, ROUND(stock_logico-sum(v.cantidad),2)  from productos as p, notas as n, vendidos as v, existencia as e, unidades as u where {periodo} and {caja}  and v.venta=n.id and p.ref=v.producto and e.producto=ref and u.id=unidad group by ref order by count(n.id) desc limit {limit};".format(periodo=periodo,caja=caja,limit=limit))
      rows=self.cursor.fetchall()
      heads=['Producto','# Ventas','Monto total','U. Vendidas','Unidad','Stock actual','Requeridas']
      titulo="Productos mejor vendidos"
      lista=list([list(a) for a in rows])
      lista.insert(0,heads)
      lista.insert(0,titulo)
      return lista     
    
    def detallarFamilia(self,ide,nombre="",caja='1'):
      """Devuelve la lista de productos pertenecientes a la familia vendidos en el periodo"""
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT descripcion,count(n.id), ROUND(sum(v.total),2),ROUND(sum(v.cantidad),2),u.nombre, stock_logico, ROUND(stock_logico-sum(v.cantidad),2)  from productos as p, notas as n, vendidos as v, existencia as e, unidades as u where {periodo} and {caja} and familia={familia} and v.venta=n.id and p.ref=v.producto and e.producto=ref and u.id=unidad group by ref order by descripcion ".format(familia=ide,periodo=periodo,caja=caja))

      rows=self.cursor.fetchall()
      heads=['Producto','# Ventas','Monto total','U. Vendidas','Unidad','Stock actual','Requeridas']
      titulo="Productos de la familia {0}".format(nombre)
      lista=list([list(a) for a in rows])
      lista.insert(0,heads)
      lista.insert(0,titulo)
      return lista      


    def imprimir(self,html):
	campos={'fecha':self.parent.fecha}
	for key in self.parent.modulos['config'].modulos['empresa']:
	    try:
	      campos[key]=self.parent.cfg.get('empresa',key)
	    except:
	      pass
	#print campos
	#self.dayPlot(self.periodo)
	#pixMap = QtGui.QPixmap.grabWidget(self.grafica)
	#pixMap.save("/tmp/plot.png")

	head="""<table border="0" width="100%" cellspacing="5px" cellpadding="5px">
		<tr valign='top'>
			<td width="75%"><img src="{logo}" align="left" valign="top" style="float:left;margin-right:20px;display:inline" />
			    <span style=" font-size:large; font-weight:800; 
			    color:#222;">{nombre}</span><br/>
			    <span>{slogan}</span></td>
		  <td width=25%>
		  <span style=" font-size:x-large; font-weight:800; color:#294e5e;text-align:right">Reporte de ventas</span><br/>
		  <span style=" font-size:normal; font-weight:600; color:#294e5e;">Fecha: {fecha}</span></td></tr></table>	""".format(**campos)
	foot="""	<hr align="center"/>
			<p style="font-size:10px; color:#999;text-align:center" align="center">{nombre}, {slogan}<br/>{direccion} {ciudad}, C.P {cp}<br>{email} Tel: {telefono}<br/>{pagina}</p>
			<br/><br/>""".format(**campos)
	libutil.printa(head+html+foot,"Reporte de ventas",self)    