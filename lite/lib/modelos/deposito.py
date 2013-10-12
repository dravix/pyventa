import sqlite3,MySQLdb
from lib.modelos.movimiento import Movimiento
class Deposito(Movimiento):
  def __init__(self,conexion):
    Movimiento.__init__(self,conexion,'deposito')
    
    