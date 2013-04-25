import operator
from PyQt4.QtCore import Qt, QAbstractTableModel, QVariant,SIGNAL
class QModeloTablaSql(QAbstractTableModel): 
	def __init__(self, cursor, parent=None, *args): 
		QAbstractTableModel.__init__(self,parent, *args) 
		self.cursor = cursor
		self.arraydata=[]
		self.headerdata =[]
        
	def query(self,qry,header):
		self.headerdata = header
		qry=qry.replace('\\\'','').replace('`','').replace('\\','')
		nres=self.cursor.execute(qry)
		if nres>0:
			table=self.cursor.fetchall()
			if table!=None:
				self.arraydata=table
				self.reset()
				

         
	def rowCount(self,parent): 
		return len(self.arraydata) 
 
	def columnCount(self,parent): 
		return len(self.headerdata) 
        
	def getVector(self):
		return self.arraydata
	
	def setVector(self, vector):
		self.arraydata=vector
		self.reset()
	
	def getRowCount(self):
		return len(self.arraydata)
	

	
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
			elif role==Qt.ForegroundRole and str(col)[0]=='-':
					return QColor(Qt.red)
		except:
			return QVariant() 

	
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
		"""Sort table by given column number."""
		self.emit(SIGNAL("layoutAboutToBeChanged()"))
		self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
		if order == Qt.DescendingOrder:
			self.arraydata.reverse()
		self.emit(SIGNAL("layoutChanged()"))
