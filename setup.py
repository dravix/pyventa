#setup.py py2exe
import sys
from distutils.core import setup
#from setuptools import setup,find_packages
import py2exe
__author__="dave"

setup(name="Pyventa",
      version="2.7",
      description="Punto de venta",
      author="David Osorio",
      author_email="david@pyventa.com",
      url="http://pyventa.com/",
      license="GPLv3",
      windows=[{"script":"pyventa.py","icon_resources":[(1, "images/pyv.ico")]}],
      options={"py2exe":{"includes":["sip"],
                         "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
                         }}
#      options={"py2exe":{"includes":["sip","utileria"]}}
)
