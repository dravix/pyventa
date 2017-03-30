#setup.py py2exe
import sys
sys.path.append('./import')
sys.path.append('./plugins')
sys.path.append('./ui')
sys.path.append('./admin')
from distutils.core import setup
#from setuptools import setup,find_packages
import py2exe
__author__="dave"

setup(name="Pyventa",
      version="0.8",
      description="Punto de venta",
      author="David Osorio",
      author_email="david@pyventa.com",
      url="http://pyventa.com/",
      license="GPLv3",
      windows=[{"script":"pyventa.py","icon_resources":[(1, "images/pv-32.ico")]}],
      options={"py2exe":{"includes":["sip"]}}
#      options={"py2exe":{"includes":["sip","utileria"]}}
)
