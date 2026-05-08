
from PyQt6.QtCore import Qt, QAbstractTableModel, SIGNAL
class QModeloTabla(QAbstractTableModel): 
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
            return  
        #elif role != QtCore.Qt.ItemDataRole.DisplayRole: 
            #return  
        #elif role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
          #return QtCore.Qt.AlignmentFlag.AlignCenter    
        ##print index.row(),index.column(),len(self.arraydata)
        #return self.arraydata[index.row()][index.column()] 
        try:
          col=self.arraydata[index.row()][index.column()]
          if role == QtCore.Qt.ItemDataRole.DisplayRole and str(type(self.arraydata[index.row()][index.column()]))!='<type \'date\'>':
              return str(self.arraydata[index.row()][index.column()])
              
          elif role == QtCore.Qt.ItemDataRole.TextAlignmentRole and (str(col)[0].isdigit() or str(col)[0]=='-' or str(col)[0]=='$' or str(col)[0]=='#') and str(col)[-1].isdigit() and len(str(col))<10:
           #cuando detecte que es un numero 
            return QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter
        except:
            pass
            #return  

    def getFila(self, index): 
        if not index.isValid(): 
            return  
        #if str(type(self.arraydata[index.row()][col]))=="<type 'datetime'>":
                  #return self.arraydata[index.row()][col]
        #else:
        return self.arraydata[index.row()]
        
    def getCell(self, index,col): 
        if not index.isValid(): 
            return  
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
        if orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.headerdata[col]       

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == QtCore.Qt.SortOrder.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
