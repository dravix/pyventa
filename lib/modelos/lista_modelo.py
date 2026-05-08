from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
class ListaModelo(QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self.listdata[index.row()]
        else: 
            return 