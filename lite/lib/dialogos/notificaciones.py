from PyQt4.QtGui import QMessageBox, QDialog
from PyQt4.QtCore import  Qt,QTimer

def notify(parent,tipo,event,info='', detail="",time=5, coords=False):
	dia=QMessageBox(parent)
	timer=QTimer.singleShot(time*1000,dia.accept)
	# dia=QtGui.QDialog(parent)
	dia.setText(event)
	dia.setInformativeText(info)
	dia.setDetailedText(detail)
	dia.setWindowModality(0)
	dia.setStandardButtons(QMessageBox.NoButton)
	if tipo=='error':
		dia.setStyleSheet(".QMessageBox{background:rgba(250,30,10,255);color:#fff}QLabel{background:transparent;color:#fff}")
		dia.setIcon(QMessageBox.Critical)
	elif tipo=='info':
		dia.setStyleSheet(".QMessageBox{background:rgba(255,255,255,255);color:#333}QLabel{background:transparent;color:#333;border:0;}")	
		dia.setIcon(QMessageBox.Information)
	elif tipo=='advertencia':
		dia.setStyleSheet(".QMessageBox{background:rgba(255,200,0,255);color:#fff}QLabel{background:transparent;color:#fff}")	
		dia.setIcon(QMessageBox.Warning)
	elif tipo=='exito':	
		dia.setStyleSheet(".QMessageBox{background:rgba(0,128,0,255);color:#fff}QLabel{background:transparent;color:#fff}")	
		dia.setIcon(QMessageBox.Information)
	if coords:	
	  dia.move(coords[0],coords[1])
	# dia.addWidget(QLabel(event))
	dia.setWindowFlags(dia.windowFlags()|Qt.FramelessWindowHint)
	dia.show()