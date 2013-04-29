#!/usr/bin/python
# -*- coding: utf-8 -*-

# colors.py

import sys, random
from PyQt4 import QtGui, QtCore


class chart(QtGui.QWidget):
    def __init__(self,x,y,data):
    #x es el tipo de valores que representan las barras
    #y es el valor a escala de cada item
    #Data es un arreglo donde el primer nivel contiene los valores a graficas y la segunda el nombre de cada iten e.g [[1,2,3],[uno,dos,tres]]
        QtGui.QWidget.__init__(self)
	self.data=data
	self.xlabel=x
	self.ylabel=y
        self.setGeometry(300, 30, 500, 500)
        self.setWindowTitle('Grafica de ventas')
    def _reload(self,data):
	self.data=data
	self.repaint()
    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        color = QtGui.QColor(255, 255, 255)
        color.setNamedColor('#FFF')
        paint.setPen(color)
	paint.setBrush(QtGui.QColor('#0C4361'))
	paint.drawRect(1,1,self.width(),self.height())
       
	matrix=[23,45,56,78,2,65]
	ancho=(self.width()-100)/len(self.data[0])
	paint.drawLine(1,self.height()-50,self.width()+50,self.height()-50) 
	paint.drawText(2, self.height()-50,80, 100,0x1000,str(self.xlabel))	    

	#colori=[,QtGui.QColor(230, 200, 30, 100),QtGui.QColor(0, 150, 190,100),QtGui.QColor(30, 100, 150, 100),QtGui.QColor(150, 50, 0, 100)]
	i=0
	maxim=max(self.data[0])
	if (maxim>0):
	  for val in self.data[0]:
	    scale=(float(val)/float(maxim))*(self.height()-80)
	    paint.setBrush(QtGui.QColor(30, 100, 150, 255))
	    rect=QtCore.QRect((ancho*i)+80, (self.height()-50)-scale,ancho, scale)
	    paint.drawLine((ancho*i)+80,(self.height()-50),ancho*(i)+80,self.height()-30)
	    paint.drawText((ancho*i)+80, self.height()-30,ancho, 30,4,str(self.data[1][i]))	    
	    paint.drawRect(rect)
	    paint.drawText( rect.x()+6,rect.y()-5, str(val));
	    i+=1
        paint.end()
#app = QtGui.QApplication(sys.argv)
#datos=[[8,20,40,10,16,25.5,12,6],['uno','dos','tres','cuatro','cinco','seis','siete','ocho']]
#dt = chart(None,datos)
#dt.show()
#app.exec_()