# -*- coding: utf-8 -*-
import sys,os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from dl_scliente import Ui_Seleccion
import MySQLdb, ConfigParser

class scliente(QtWidgets.QDialog, Ui_Seleccion):  
    def __init__(self,parent,tipo=0):
                QtWidgets.QDialog.__init__(self)
                self.setupUi(self)
                self.parent=parent
                self.cursor=parent.cursor
                self.tipo=tipo
                self.bbuscar.clicked.connect(self.buscar)
                self.texto.textChanged.connect(self.buscar)
                #self.tabla.doubleClicked.connect(self.retorno)
                self.tabla.itemActivated.connect(self.retorno)
                self.texto.setFocus(True)  
                self.Id=10
                #self.busk.clicked.connect(self.saludar)
        
    def buscar(self):
        txt=str(self.texto.text())
        self.cursor.execute("SELECT `id`,`nombre`,`rfc` FROM clientes where `nombre` like '%%%s%%' and tipo=%d limit 15"%(txt,self.tipo))
        result = self.cursor.fetchall()
        self.tabular(result)

    def tabular(self,datos):
    #Datos es una tupla resultado de un fetchall()
          
          self.tabla.setRowCount(len(datos)+1)
          for i,data in enumerate(datos):
            item=[]
            for j in range(len(data)):
              item.append( QtWidgets.QTableWidgetItem(1))
              item.append( QtWidgets.QTableWidgetItem(1))
              item.append( QtWidgets.QTableWidgetItem(1))
            for j in range(len(data)):
              item[j].setText(str(data[j]))
              self.tabla.setItem(i,j ,item[j])
          self.tabla.resizeColumnsToContents()   

    def retorno(self):
        self.parent.cliente={'id':int(self.tabla.item(self.tabla.currentRow(),0).text()),'nombre':str(self.tabla.item(self.tabla.currentRow(),1).text()),'rfc': str(self.tabla.item(self.tabla.currentRow(),2).text())}
        self.parent.csCliente.setText(self.parent.cliente['nombre'])
        self.done(int(self.tabla.item(self.tabla.currentRow(),0).text()))
        #print self.tabla.item(0,1).text()
        #self.hide()
        #return self.ret

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    aw = scliente()
    aw.show()
    sys.exit(app.exec())
        
