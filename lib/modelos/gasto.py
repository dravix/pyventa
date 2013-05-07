import sqlite3,MySQLdb

class Gasto:
  def __init__(self,conexion):
    self.conexion=conexion
    self.cursor=conexion.cursor
  
  def agregar(self, usuario, caja,detalle, monto ):
    try:
      self.cursor.execute("""INSERT INTO movimientos VALUES(NULL, {usuario}, {caja},{detalle},'gasto', {monto},NOW())
      """.format(usuario=usuario, caja=caja, detalle=detalle, monto=monto))
    except:
      return False
    else:
      return self.conexion.ultimo()
    
  def eliminar(self,ide):
    try:
      self.cursor.execute("""DELETE FROM movimientos WHERE id_movimiento={ide} """.format(ide=ide))
    except:
      return False
    else:
      return True
    
  def buscar(self,condicion):
    try:
      self.cursor.execute("""SELECT * FROM movimientos WHERE tipo='gasto' and {condicion}""".format(condicion=condicion))
    except:
      return []
    else:
      return self.cursor.fetchall()
    
  def suma(self, condicion):
    try:
      self.cursor.execute("""SELECT ROUND(SUM(monto),2) FROM movimientos WHERE tipo='gasto' and {condicion}""".format(condicion=condicion))
    except:
      return 0
    else:
      ff=self.cursor.fetchone()
      if ff!=None and ff[0]!=None:
	return float(ff[0])    
      else:
	return 0
    