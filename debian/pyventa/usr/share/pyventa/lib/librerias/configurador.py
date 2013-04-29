#!/usr/bin/env python
#Configurador global de Pyventa . Manipula el archivo de configuracion
import ConfigParser as Cp, os
from lib.librerias.comun import *
class Configurador:
#Esta clase se encarga de hacer la interfaz del archivo de configuracion
	def __init__(self):
		self.cfg=None
		self.ruta=os.path.join(home,"config.cfg")
		os.stat(self.ruta)
		cfg = Cp.ConfigParser()
		if cfg.read([self.ruta]):
			self.cfg=cfg
			
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
