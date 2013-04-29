import sys
from lib import  libutil
from ui.ui_swap import Ui_Swap
from PyQt4 import QtCore, QtGui

#cant=input("Ingrese la cantidad")
class Swaproductos(QtGui.QDialog, Ui_Swap): 
  def __init__(self, parent,ref=0):
    QtGui.QDialog.__init__(self)
    self.setupUi(self)
    self.cursor=parent.cursor
    self.curser=parent.curser
    self.parent=parent
    self.connect(self.leBusca, QtCore.SIGNAL("textChanged(QString)"), self.buscar)
    self.connect(self.tbAplicar, QtCore.SIGNAL("clicked()"), self.aplicar)
    self.connect(self.cbProd, QtCore.SIGNAL("activated (int )"), self.setProp)
    self.connect(self.tbRegresar, QtCore.SIGNAL("clicked()"), lambda:self.regresar())
    self.connect(self.tbConfirmar, QtCore.SIGNAL("clicked()"), self.commit)
    #self.connect(self.tbRegresar, QtCore.SIGNAL("clicked()"), lambda:self.stack.setCurrentIndex(0))

    
    self.modelo=None
    if ref>0:
      self.ref=ref
      self.buscarProd(ref)
    else:
      print "Referencia %s equivocada"%ref
    
  def buscar(self,txt):
    txt=str(txt)
    if len(txt)==3:
      self.acompleta(txt)

  def buscarProd(self,text):
    text=str(text)
    if len(text)>0 and text.isdigit():
      sql="SELECT ref,descripcion, stock_logico from productos, existencia where producto=ref and ref=%s "%(text)
    else:
      sql="SELECT ref, descripcion, stock_logico from productos, existencia where producto=ref and descripcion='%s' "%(text)
    self.curser.execute(sql)
    tup=self.curser.fetchone()
    self.producto=tup
    self.ref=tup['ref']
    self.leProd.setText(tup['descripcion'])
    self.dsbStock.setValue(float(tup['stock_logico'])) 
    self.prod=dict(tup)
    self.tabla=[]
    self.superior(self.ref)
    self.inferior(self.ref)
    self.dsbCant.setMinimum(1)
    self.listar()
    
  def acompleta(self,txt=' '):
    sql="select descripcion from productos, subproductos where (producto=ref or subproducto=ref) and descripcion like '%%%s%%' "%txt
    self.cursor.execute(sql)
    tup=self.cursor.fetchall()
    li=[row[0] for row  in tup]
    self.com=QtGui.QCompleter(li,self)
    self.com.setCaseSensitivity(0)
    self.leBusca.setCompleter(self.com)
    self.connect(self.com, QtCore.SIGNAL("activated (QString )"), self.buscarProd)

    
  def superior(self,ref):
    sql="select subproducto,descripcion,1/cantidad, cantidad,concat(cantidad,\":1\"), stock_logico from productos, subproductos as s, existencia as e where s.producto=%s and ref=subproducto and e.producto=ref"%(ref)
    self.cursor.execute(sql)
    tup=self.cursor.fetchall()
    if tup!=None:
      self.tabla.extend(list(tup))
    
  def inferior(self,ref):
    sql="select s.producto,descripcion,cantidad, cantidad, concat(\"1:\",cantidad),stock_logico from productos, subproductos as s,existencia as e  where subproducto=%s and ref=e.producto and ref=s.producto"%(ref)
    self.cursor.execute(sql)
    tup=self.cursor.fetchall()
    if tup!=None:
      self.tabla.extend(list(tup))
  
  def listar(self):
    
    for i,item in enumerate(self.tabla):
      self.tabla[i]=list(item)
    self.modelo=libutil.tabox(self.cbProd, self.tabla, 1, self)
    if self.modelo!=None:
      self.cbProd.setMaxVisibleItems(self.modelo.rowCount(self))
    else:
      self.cbProd.setMaxVisibleItems(0)

   
  def aplicar(self):
    nuevos=int(float(self.dsbCant.value())*float(self.sub['prop']))
    tmp=float(self.dsbCant.value())*float(self.sub['prop'])
    viejos=int(self.dsbCant.value())-((tmp-int(tmp))*float(self.sub['cantidad']))
    if float(self.producto['stock_logico'])>=viejos:
	antes=libutil.listaHtml([
	[self.prod['descripcion'],self.prod['stock_logico']],
	[self.sub['descripcion'],self.sub['stock_logico']]
	], "Existencias antes.",[[80,"Producto"],[20,"Existencias"]])

	despues=libutil.listaHtml([
	  [self.prod['descripcion'],self.prod['stock_logico']-viejos],
	  [self.sub['descripcion'],float(self.sub['stock_logico'])+(nuevos)]
	  ], "Existencias despues.",[[80,"Producto"],[20,"Existencias"]])
	  
	tabla=libutil.listaHtml([antes,despues],"Tabla comparativa",[],'#fff',"#239AB1", tfuente=10,opc="100")
	self.lbResulta.setText(str(self.lbResulta.text())%(viejos,self.prod['descripcion'],nuevos,self.sub['descripcion'],antes,despues))
	self.stack.setCurrentIndex(1)
    else:
      em=QtGui.QErrorMessage(self)
      em.showMessage( "No hay suficientes unidades, hay %s unidades se requieren %s"%(float(self.producto['stock_logico']),viejos))
      print "No hay suficientes unidades ",float(self.producto['stock_logico']),viejos
  
  def commit(self):
    nuevos=int(float(self.dsbCant.value())*float(self.sub['prop']))
    tmp=float(self.dsbCant.value())*float(self.sub['prop'])
    viejos=int(self.dsbCant.value())-((tmp-int(tmp))*float(self.sub['cantidad']))
    old="UPDATE existencia set stock_logico=stock_logico-%s WHERE producto=%s"%(viejos,self.prod['ref'])
    new="UPDATE existencia set stock_logico=stock_logico+%s WHERE producto=%s"%(nuevos,self.sub['ref'])
    self.cursor.execute(old)
    self.cursor.execute(new)
    self.cursor.execute("COMMIT")
    self.accept()

    
  def setProp(self,index):
    self.sub={}
    if self.modelo!=None:
      self.sub['ref']= self.modelo.celda(self.cbProd.currentIndex(),0)
      self.sub['descripcion']= self.modelo.celda(self.cbProd.currentIndex(),1)
      self.sub['prop']= self.modelo.celda(self.cbProd.currentIndex(),2)
      self.sub['cantidad']= self.modelo.celda(self.cbProd.currentIndex(),3)
      self.sub['proporcion']= self.modelo.celda(self.cbProd.currentIndex(),4)
      self.sub['stock_logico']= self.modelo.celda(self.cbProd.currentIndex(),5)
      self.leProp.setText(self.sub['proporcion'])
      self.dsbCant.setMinimum(float(self.sub['proporcion'].split(':')[0]))

  #def animar(self):
    #formerGeometry = QtCore.QRect(self.geometry()) # storing previous geometry in order to be able to restore it later
    #hideAnimation = QtCore.QPropertyAnimation(self, "geometry")
    #hideAnimation.setDuration(200) # chose the value that fits you
    #hideAnimation.setStartValue(formerGeometry)
    ##computing final geometry
    #endTopLeftCorner = QtCore.QPoint(self.pos() + QtCore.QPoint(0, self.height()))
    #finalGeometry = QtCore.QRect(endTopLeftCorner, QtCore.QSize(self.width(), 0))
    #hideAnimation.setEndValue(finalGeometry)

    #hideAnimation.start()
  def regresar(self):
    self.lbResulta.setText("""<p >Se tomaran <span style=" font-weight:600;">%s</span> unidades de %s y se agregaran como %s unidades de<span style=" font-weight:600;"> %s , </span>quedando de la siguiente manera:</p><p>%s</p><p>%s</p>""")
    self.stack.setCurrentIndex(0)
  
if __name__=="__main__":
  #ref=input("Ingrese la ref: ")
  #cant=input("Ingrese la cantidad: ")

  #superior(ref)
  #inferior(ref)
  #print tabla
  app = QtGui.QApplication(sys.argv)
  app.processEvents()
  aw = Swaproductos(11754)
  aw.show()
  app.exec_()

  