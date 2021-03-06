import os,sys
from PyQt4 import QtCore, QtGui#,  Qt
from PyQt4.QtCore import Qt, QAbstractTableModel, QVariant
import MySQLdb as My, ConfigParser as Cp
from utileria import MyTableModel, conexion
import csv
import locale
db=None
    
def conectar():  #Crea la conexion a la base de datos
  con=conexion()
  db=con.db
  cursor=con.cursor
  return cursor

def home():	
  home=os.path.join(os.path.expanduser('~'),"pyventa")
  if sys.platform == 'linux2':
      home=os.path.join(os.path.expanduser('~'),".pyventa")
  return home
 
	
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

def tabular(tabla, vector,head, padre=None): #Tabula con respecto a una lista
      if padre==None:
	padre=tabla.parent()
      modelo = MyTableModel(vector, head, padre) 
      tabla.setModel(modelo)
      #tabular(tabla,sql,head)
      #tabla.setColumnHidden(0,True)
      tabla.resizeColumnsToContents()
      return modelo
      
def tabox(widget, lista,columna, padre): #Tabula con respecto a una lista en un combo box
    if lista!=None and len(lista)>0:
      head=['1']*len(lista[0]) #Crea una arreglo vacio del tamano de columnas de lista
      modelo = MyTableModel(lista, head, padre) 
      widget.setModel(modelo)
      modelo.setVector(lista)
      
      widget.setModelColumn(columna)
      return modelo
    else:
      return None

def seleccionar(tabla,modelo,col=0): #regresa las referencias seleccionadas 
  refs=[]
  lista=tabla.selectedIndexes()
  lastrow=-1
  for li in lista:
      if (li.row()!=lastrow) :
	lastrow=li.row()
	refs.append(str(modelo.getCell(li,col)))      
  return list(set(refs))

def seleccionarFilas(tabla,modelo): #regresa las filas seleccionadas 
  refs=[]
  lista=tabla.selectedIndexes()
  lastrow=-1
  for li in lista:
      if (li.row()!=lastrow) :
	lastrow=li.row()
	refs.append(str(modelo.getFila(li)))      
  return list(set(refs))

def listaTabla(tabla,header,lista,padre,modelo=None):
  #tabla, header, lista, modelo
      if header==None:
	header=['1']*len(lista[0])
      if lista!=None:
	#print lista
	if modelo==None:
	  modelo = MyTableModel(lista, header, padre) 
	  tabla.setModel(modelo)
	else:
	  modelo.setVector(lista) 
	return modelo

def enTabla(tabla,lista,header=None,modelo=None):
  #tabla, header, lista, modelo
      if header==None:
	header=['Columna']*len(lista[0])
	if modelo==None:
	  modelo = MyTableModel(lista, header, tabla.parent()) 
	  tabla.setModel(modelo)
	else:
	  modelo.setVector(lista) 
	return modelo

 
#def entabla(tabla,header,query,modelo=None): #Tabula con respecto a un query
    #if db==None:
      #conectar()
    #sql=str(query)
    #try:
      #cursor.execute(sql)
      #lista=cursor.fetchall()
    #except:
      #print "Problema al ejecutar el query"
    #else:
      #if lista!=None:
	#if modelo==None:
	  #modelo = MyTableModel(lista, header, lista.) 
	  #tabla.setModel(modelo)
	#else:
	  #modelo.setVector(lista)
	##tabla.resizeColumnsToContents()  
    #return modelo	
    
def odic(adict): ##Ordena los indices de un diccionacio
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)  
    
def getComboModelKey( combo, col=0): #Esta funcion devuelve el valor de la columna del elemento seleccionado de un combo model
  return combo.model().celda(combo.currentIndex(),col)
  #print combo.model().celda(combo.currentIndex(),col)

def setComboModelKey(combo, key): #Establece el combo en el valor de la llave
  combo.setCurrentIndex ( combo.model().buscarKey(key,0) )      
  
  
  
def listaHtml(lista, titulo='', cabezas=[], color='#fff',fondo="#239AB1", tfuente=10,opc="110",css=""): #opc(titulo:true,cabezas:true,enumerado:false)
  ide=titulo.lower().replace(' ','')
  locale.setlocale(locale.LC_ALL, 'en_US.utf8')
  html="""<style type="text/css">
table{border-collapse:collapse;}
#%s .odd{background:#efefef}
#%s .cab{background:%s; color:%s;}
#%s .cabeza{background:%s; color:%s; font-weight:700;border:2px solid #333}
table{border-style:solid}
%s
</style>"""%(ide,ide,fondo,color,ide,fondo,color,css)
  if opc[0]=='1' and len(titulo)>0: #si se quiere mostrar el titulo
    html+="""<table id="%s" width="100%%" valign="top"  cellspacing="0" cellpadding="5"  ><tr class="cabeza" ><th colspan=%s><span style="font-size:%spx;">%s</span></th></tr>"""%(ide, len(cabezas),tfuente+4,titulo)
  #html+="""<table width="100%%" border="0" cellspacing="0" cellpadding="5">"""
  if opc[1]=='1' and len(cabezas)>0: #si se quiere mostrar las cabezas
    html+="""<tr class="cab"> """
    width=False
    if type(cabezas[0]) ==list:
      width=True
    for item in cabezas:
      if width:
	html+="""<th width="%s%%"><span style="font-size:%spx;">%s</span></th>"""%(item[0],tfuente+1,item[1])
      else:
	html+="""<th ><span style="font-size:%spx;">%s</span></th>"""%(tfuente+1,item)
    html+="""</tr>"""

  for i,li in enumerate(lista):
    if i%2==0  :
      html+="""<tr class="odd" valign='top'>"""
    else:
      html+="""<tr  valign='top'>"""
    for col in li:
      if col!=None :
	if isinstance(col,float):
	    dato=str(col)
	if isinstance(col,str) and len(col)>0 and (str(col)[0].isdigit() or str(col)[0]=='-' or str(col)[0]=='$' or str(col)[0]=='#') and str(col)[-1].isdigit() and len(str(col))<10:
	#cuando detecte que es un numero 
	  if isinstance(col,int):
	    dato=str(col)
	  if str(col)[0].isdigit() or str(col)[0]=='-':
	    dato=locale.format("%.2f",float(col),grouping=True)
	  elif str(col)[0]=='$':
	    dato="$ %s"%locale.format("%.2f",float(col[1:]),grouping=True)
	  else:
	    dato=col
	  html+="""<td align="right" ><span style="font-size:%spx;">%s</span></td>"""%(tfuente,dato)
	else: # Es una cadena
	  html+="""<td align="left"><span style="font-size:%spx;">%s</span></td>"""%(tfuente,col)
    html+="""</tr>"""
  html+="""</table>"""
  return html



def printb(parent,titulo,plantilla,campos):
    f=open(plantilla,"r+")
    plantilla=f.read()
    #campos={'%fecha%':self.parent.fecha}
    for key,item in campos.iteritems():
	plantilla=plantilla.replace(key,item)
    printa(plantilla,titulo,parent)

def printa(string,titulo="Lista",parent=None):
  tedit=QtGui.QTextEdit(string)
  printer=QtGui.QPrinter()
  printer.setOrientation(0)
  printer.setPaperSize(QtGui.QPrinter.Letter)
  #printer.setFullPage(True)
  #printer.setPageMargins(5,10,5,10,0)
  printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
  printer.setCreator ("Pyventa : Software de punto de venta.")
  nombre=os.path.join(os.path.expanduser('~'),"%s.pdf"%titulo)
  printer.setColorMode(QtGui.QPrinter.Color)
  File = QtGui.QFileDialog()
  saveFile = str(File.getSaveFileName(parent, "Guardar pdf",nombre))
  if (saveFile!=""):
      printer.setOutputFileName(saveFile)
      tedit.print_(printer)
      if sys.platform == 'linux2':
	  os.system("gnome-open '%s'"%saveFile)
      elif sys.platform == 'win32':
	  os.system("start '%s'"%saveFile)	
	  
  #paint=QtGui.QPainter(printer)
  #paint.begin(self.tablaProductos)
  #self.tablaProductos.render(printer)
  #saveFile=saveFile.replace(" ","\\ ")

    
def toCsv(tabla,parent):
  import csv
  File = QtGui.QFileDialog()
  save = str(File.getSaveFileName(parent, "Guardar csv",os.path.join(os.path.expanduser('~'),"tabla.csv")))
  if (save!=""):
    hoja = csv.writer(open(save, 'wb'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in tabla:
      hoja.writerow(row)
  

    

    
      
  
      