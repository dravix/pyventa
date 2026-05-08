from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_nueva_lista import Ui_Form as Form
import utileria 

#from utileria import MyTableModel
class nuevaLista(QtWidgets.QDialog,Form):
    def __init__(self,padre):
      #Padre:   es el objeto principal padre del que puede extraer conexiones y recursos
      #Objeto:  Es el nombre del objeto o tabla que se estara manipulando "familias", "unidades", "impuestos", etc
      #Campos:  Es un diccionario con las columnas de la tabla apuntando a un tipo de dato
#               [['columna','Label','tipo',ui=QtGui.*,enabled=None]] ;tipos={str, int, double, date, combo}
#       Ide:    En el caso de que le pasen ide significa que editara un objeto en particular y solo se realizara una accion (modificar, agregar)
              QtWidgets.QDialog.__init__(self,padre)
              self.setupUi(self)
              self.ide=['',-1]
              self.padre=padre
              self.curser=self.padre.curser
              self.cursor=self.padre.cursor
              titulo="Nueva compra"
              self.setWindowTitle(titulo)
              self.lbTitulo.setText(titulo)
              #self.lblDatos.setText("Datos de %s\b "%self.objeto)
              ###Aqui se generan automaticamente los campos
              self.header=['ref','descripcion','cantidad','unidad','costo','importe']
              self.modelo=None
      

              self.producto=[]
              ### -------------------------------------
              self.tabla.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
              self.popMenu=QtWidgets.QMenu(self)
              self.lblLogo.setPixmap(QtGui.QPixmap("/usr/share/pyventa/images/png/Basket-64.png"))
              ##self.connect(self.tbCerrar, QtCore.SIGNAL("clicked()"), lambda:self.done(-1))
              #self.tbModif.clicked.connect(self.editar)
              #self.tbAgregar.clicked.connect(self.agregar)
              #self.leCodigo.textChanged.connect(self.buscar)
              self.leCodigo.returnPressed.connect(self.buscar)
              #self.leCodigo.returnPressed.connect(self.detallar)
              ##self.connect(self.tabla,QtCore.SIGNAL('cellDoubleClicked (int, int)'),self.seleccionar)
              #self.tabla.activated.connect(self.seleccionar)
              #self.tabla.customContextMenuRequested.connect(self.ocm)

    def buscar(self,texto=''):
      if texto=='':
        texto=str(self.leCodigo.text())
      texto=str(texto)
      if len(texto)>0:
        if texto[0].isdigit():
          print(texto,type(texto))

          #sql="SELECT ref,descripcion,  unidad, costo from producto where ref=%s or codigo like '%s%%';"%( texto,texto)
        elif len(texto)>2:
          sql="SELECT ref,descripcion from productos where descripcion like '%%%s%%'"%(texto)
          print(sql)
          try:
            self.cursor.execute(sql)
            lista=self.cursor.fetchall()
          except:
            print("No se pudo seleccionar la columna")
          else:
            if lista!=None:
              if self.modelo==None:
                self.modelo = utileria.MyTableModel(lista, self.header, self) 
                self.completer=QtWidgets.QCompleter(self.modelo,self)
                self.completer.setCompletionColumn(1)
                #self.completer.setCompletionMode(0)
                #self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
                #self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                self.leCodigo.setCompleter(self.completer)
                self.leCantidad.setCompleter(self.completer)            
              else:
                self.modelo.setVector(lista)    
                self.tabla.setModel(self.completer.model())
                
    def detallar(self,ref=''):
        if ref=='':
           ref=str(self.leCodigo.text())
        sql="SELECT ref,descripcion, 1 as cantidad,  unidad, costo, costo as importe from productos where ref=%s or codigo like '%s%%';"%( texto,texto)
        self.curser.execute(sql)
        qry=self.curser.fetchone()
        self.leCodigo.setText(qry['descripcion'])
        self.leCantidad.setFocus(True)
        