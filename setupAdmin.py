from distutils.core import setup
#from setuptools import setup,find_packages
import py2exe

__author__="dave"

setup(name="Padmin",
      version="0.75",
      description="Administrador de Pyventa",
      author="David Osorio",
      author_email="david@ladosmil.com",
      url="http://ottarw.com/pyventa/",
      license="GPL",
      windows=[{"script":"padmin.py","icon_resources":[(1, "images/padmin.ico")]}],
      options={"py2exe":{"includes":["sip"],
                         "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
                         }},      
      #install_requires=['MySQL>=3'],
      packages=["modulos", "ui"]

)
