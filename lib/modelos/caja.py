import sqlite3,MySQLdb

class Caja:
  def __init__(self,conexion):
    self.conexion=conexion
    self.cursor=conexion.cursor
    
    
  def saldoInicial(self,caja):
    try:
      self.cursor.execute("""SELECT saldo_inicial from cajas where num_caja={caja} and estado=date(current_timestamp);""".format(caja=caja))
    except:
      return 0
    else:
      ff=self.cursor.fetchone()
      if ff!=None and ff[0]!=None:
	return float(ff[0])    
      else:
	return 0 
      
  def setSaldoInicial(self,caja,saldo):
    try:
      sql="UPDATE cajas SET estado=NOW(), saldo_inicial={saldo} where num_caja={caja};".format(saldo=saldo,caja=caja)
      self.cursor.execute(sql)
    except:
      return False
    else:
      return True
  