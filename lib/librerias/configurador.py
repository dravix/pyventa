#!/usr/bin/env python
#Configurador global de Pyventa . Manipula el archivo de configuracion
import ConfigParser as Cp, os
from lib.librerias.comun import *
from PyQt4.QtGui import QMessageBox
class Configurador():
#Esta clase se encarga de hacer la interfaz del archivo de configuracion
    def __init__(self,parent, configFile=False):
      self.parent=parent
      if not configFile:
	self.ruta=os.path.join(home,"config.cfg")
      else:
	self.ruta=configFile
      cfg = Cp.ConfigParser()
      if  os.path.exists(self.ruta) and cfg.read([self.ruta]):
	self.cfg=cfg   
	self.stat=True
      else:
	self.stat=self.setupInitConfig()


    def setupInitConfig(self):
      	if not os.path.exists(self.ruta):
	    	msgBox=QMessageBox(QMessageBox.Question,"No se ha detectado el archivo de configuracion","Desea que el sistema asigne  una configuracion por defecto? ",QMessageBox.Yes|QMessageBox.No,self.parent)
		ret=msgBox.exec_()
		if ret==QMessageBox.Yes:
		    if sys.platform == 'linux2':   
			  os.system("cp -r perfil {0}".format(home))
		    else:
			  os.system("xcopy perfil \"%s\" /i /a /e /k"%self.home)
		    msgBox=QMessageBox(QMessageBox.Information,"Reinicio programado","<h2>La operacion ha tenido exito</h2><br><p>Se han cargado las configuraciones por defecto, ahora usted puede configurar el sistema. Gracias.</p>.",QMessageBox.Close,self.parent)
		    msgBox.exec_()
		    self.__init__(self.parent)
		    return True
		else:
		    print "El programa no puede continuar porque no existe el archivo de configuracion."
		    return False

    def add_section(self,section):
      self.cfg.add_section(section)
   
    def has_option(self,modulo,propiedad):
	    return self.cfg.get(modulo,propiedad)
    
    def get(self,modulo,propiedad):
	    if self.cfg.has_option(modulo,propiedad):
		    return self.cfg.get(modulo,propiedad)
	    else:
		    self.setCambio(modulo,propiedad,0)
		    return 'False'

    def set(self,modulo,propiedad,valor):
#Registra el valor de un campo(propiedad) de un modulo  
	    try:
		    self.cfg.set(str(modulo),str(propiedad),str(valor))
	    except ConfigParser.Error,e: 
		    raise(e)
	    else:
		    self.guardar()	
	    
    def getDato(self,modulo,propiedad):
	    if self.cfg.has_option(modulo,propiedad):
		    return self.cfg.get(modulo,propiedad)
	    else:
		    self.setCambio(modulo,propiedad,0)
		    return False  
      
    def config(self):
	    return self.cfg
  
    def guardar(self):
#Escribe todo el archivo con los cambios que se hayan realizado
	    self.cfg.write(open(self.ruta,"w+"))

    def setCambio(self,modulo,propiedad,valor):
#Registra el valor de un campo(propiedad) de un modulo  
	    try:
		    self.cfg.set(str(modulo),str(propiedad),str(valor))
	    except Cp.Error,e:
		    print "No se guardo la configuracion",e
	    else:
		    self.guardar()
