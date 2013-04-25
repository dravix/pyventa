#!/usr/bin/env python
### Librerias.common.py ###
### Este modulo incluye las variables y funciones de acceso comun
import os,sys
home=os.path.join(os.path.expanduser('~'),"pyventa")
if sys.platform == 'linux2':
	home=os.path.join(os.path.expanduser('~'),".pyventa")
