import libutil
from PyQt4 import QtCore, QtGui#,  Qt
from PyQt4.QtCore import Qt
from lib.modelos.gasto import Gasto 
from lib.modelos.compra import Compra 
from lib.modelos.venta import Venta 
from lib.modelos.caja import Caja 
class Chart:
  def __init__(self,parent,w=650,h=500):
    self.parent=parent
    self.cursor=parent.cursor
    self.width=w
    self.height=h
    #self.grafica=self.parent.vgrafica
    #self.grafica.setSceneRect(0,0,w,h)

  def toPix(self,name):
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

      
  def setGrafica(self,datos,w=450,h=200):
	if len(datos[0])>0:
    	  self.escena=QtGui.QGraphicsScene()
    	  self.escena.setBackgroundBrush(QtGui.QColor('#fff'))
    	  pen=QtGui.QPen()
    	  pen.setWidth(2)
    	  pen.setColor(QtGui.QColor('#0C4361'))
    	  rBrush=QtGui.QBrush(QtGui.QColor(101, 163, 255, 100))
    	  grid=QtGui.QPen(QtGui.QColor("#999"),1,Qt.DashLine)
    	  gridThick=QtGui.QPen(QtGui.QColor("#AAA"),2,Qt.SolidLine)
    	  top=200
    	  alto=h
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

	  for i,val in enumerate(datos[0]):
	    if maxim>0:
	      scale=(float(val)/float(maxim))*(alto-50)
	      #self.escena.addRect((ancho*i)+80, (alto-50)-scale,ancho,scale,pen,rBrush)
	      if len(datos[0])>10:
		  n=round(len(datos[0])*.05)
	      else:
		  n=1
	      if i>0:
		self.escena.addLine(ax,ay,(ancho*i)+85,alto-50-scale,pen)
		#self.escena.addEllipse((ancho*i)+84,alto-51-scale,4,4,pen)
	      self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,alto-50-scale,grid)
	      if i%n==0:
		text=self.escena.addSimpleText(str(datos[1][i]))
		text.setPos((ancho*i)+85,alto-35)
		self.escena.addLine((ancho*i)+85,alto-40,(ancho*i)+85,alto-35,gridThick)
	      ax=(ancho*i)+85
	      ay=alto-50-scale    
	  #self.grafica.setScene(self.escena)  
      
#--------------------------------------------------------      
  def dayPlot(self,fecha='DATE(fecha)=date(current_timestamp)'):
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

  def daysPlot(self,fecha='DATE(fecha)=date(current_timestamp)'):
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


class Ventas:
    def __init__(self,parent,periodo):
      self.cursor=parent.cursor
      self.curser=parent.curser
      self.periodo=periodo
      self.ventas={}
      
    def resumir(self,fecha='date(current_timestamp)',caja='1'):
	resumen={'ventas':0,'gastos':0,'compras':0, 'inicial':0.0}
	con=self.parent.conexion
	resumen['ventas']=Venta(con).suma("date(fecha)={0} and {1}".format(fecha,caja))
	resumen['gastos']=Gasto(con).suma("date(fecha)={0} and {1}".format(fecha,caja))
	resumen['compras']=Compra(con).suma("date(fecha)={0} and {1}".format(fecha,caja))
	resumen['inicial']=Caja(con).saldo_inicial(self.parent.caja)	
	self.efectivo=(resumen['ventas']-resumen['compras']-resumen['gastos']+resumen['inicial'])
	lista=[
	  ['Ventas:',resumen['ventas']],
	  ['Compras:',resumen['compras']],
	  ['Gastos:',resumen['gastos']],
	  ['Efectivo inicial:',resumen['inicial']],
	  ['Efectivo final:',self.efectivo]
	  ]
	tabla=libutil.listaHtml(lista,'Tabla de movimientos de dinero',['Concepto','Monto'],'#333','#E2E6E7',14,anchos=[70,30])
	return tabla
      
    def detallarVentas(self):
      self.cursor.execute("SELECT tipo , count(id), ROUND(sum(total),2) from notas where "+self.periodo+" and status>0  group by tipo ")
      rows=self.cursor.fetchall()
      self.ventas['general']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['general'],"Ventas cobradas",['Tipo','Ventas realizadas','Monto'],anchos=[50,50])
      return tabla

    def detallarCajas(self):
      self.cursor.execute("SELECT nombre, tipo , count(id), ROUND(sum(total),2) from notas,cajas where %s and num_caja=caja group by tipo,caja order by caja;"%self.periodo)
      rows=self.cursor.fetchall()
      self.ventas['general']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['general'],"Ventas cobradas por cajas",['Caja','Tipo','Ventas realizadas','Monto'],anchos=[40,10,20,20])
      return tabla
      
    def detallarUsuarios(self):
      self.cursor.execute("select nombre,count(N.id), ROUND(sum(total),2) from notas as N, usuarios as U where "+self.periodo+" and status=1 and N.usuario=U.id_usuario group by N.usuario order by ROUND(sum(total),2) desc;")
      rows=self.cursor.fetchall()
      self.ventas['usuarios']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['usuarios'],"Total de ventas por usuarios",['Usuario','Ventas realizadas','Monto total'],anchos=[70,30]) 
      return tabla
     
      
    def detallarDeptos(self):
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT d.nombre,count(n.id),ROUND(sum(v.total),2) from productos as p, notas as n, vendidos as v, familias as f, departamentos as d where "+periodo+"  and v.venta=n.id and p.ref=v.producto and f.id=p.familia  and d.id=f.departamento  group by d.id order by ROUND(sum(v.total),2) desc;")
      rows=self.cursor.fetchall()
      self.ventas['deptos']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['deptos'],"Total de ventas por departamento",['Departamento','Ventas realizadas','Monto total'],anchos=[50,50]) 
      return tabla
      
    def detallarProds(self,limit=20):
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT ref,descripcion,ROUND(sum(v.total),2),ROUND(sum(v.cantidad),2), count(n.id), stock_logico, ROUND(stock_logico-sum(v.cantidad),2)*-1,u.nombre  from productos as p, notas as n, vendidos as v, existencia as e, unidades as u where %s  and v.venta=n.id and p.ref=v.producto and e.producto=ref and u.id=unidad group by ref order by count(n.id) desc limit %s;"%(periodo,limit))
      rows=self.cursor.fetchall()
      self.ventas['prods']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['prods'],"Total de ventas por mejores productos",['Ref.','Producto','Monto total','Vendidas','Ventas','Stock <br/>actual','Requeridas','Unidad'],'#fff',"#239AB1", 12,anchos=[6,30,14,10,6,10,10,10]) 
      return tabla
      
    def detallarProdsVendidos(self,limit=20):
      periodo=self.periodo.replace("fecha", "n.fecha")
      self.cursor.execute("select DISTINCT descripcion,count(n.id),ROUND(sum(v.cantidad),2),u.nombre, ROUND(sum(v.total),2), stock_logico, ROUND(stock_logico-sum(v.cantidad),2)  from productos as p, notas as n, vendidos as v, existencia as e, unidades as u where %s  and v.venta=n.id and p.ref=v.producto and e.producto=ref and u.id=unidad group by ref order by count(n.id) desc limit %s;"%(periodo,limit))
      rows=self.cursor.fetchall()
      self.ventas['prods']=list([list(a) for a in rows])
      tabla=libutil.listaHtml(self.ventas['prods'],"Total de ventas por mejores productos",['Producto','# Ventas','U. Vendidas','Unidad','Monto total','Stock <br/>actual','Requeridas'],'#fff',"#239AB1", 12,anchos=[30,10,10,10,10,10,10]) 
      return tabla      