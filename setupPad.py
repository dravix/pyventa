from distutils.core import setup
#from setuptools import setup,find_packages
import py2exe
import sys, os
sys.path.append('./admin')

__author__="dave"

setup(name="Padmin",
      version="0.75",
      description="Administrador de Pyventa",
      author="David Osorio",
      author_email="david@ladosmil.com",
      url="http://ottarw.com/pyventa/",
      license="GPL",
      windows=[{"script":"admin/main.py","icon_resources":[(1, "padmin.ico")]}],
      options={"py2exe":{"includes":["sip"]}},
      zipfile="lib.admin.zip",
      #install_requires=['MySQL>=3'],
      #packages=["plugins"]

)
