import sqlite3,MySQLdb
#		id_movimiento, usuario, caja,'detalle','tipo', monto,fecha
class Movimiento(object):
  def __init__(self,conexion,tipo=''):
    self.conexion=conexion
    self.cursor=conexion.cursor
    self.tipo=tipo
    
    
  def agregar(self, usuario, caja,detalle, monto ):
    try:
      self.cursor.execute("""INSERT INTO movimientos VALUES(NULL, {usuario}, {caja},'{detalle}','{tipo}', {monto},NOW())
      """.format(usuario=usuario, caja=caja, detalle=detalle, monto=monto, tipo=self.tipo))
    except:
      return False
    else:
      return self.conexion.ultimo()
    
  def eliminar(self,ide):
    try:
      self.cursor.execute("""DELETE FROM movimientos WHERE id_movimiento in ({ide}) """.format(ide=ide))
    except:
      return False
    else:
      return True
    
  def buscar(self,columnas="*",condicion=""):
    try:
      if self.tipo!='':
	tipo=" tipo= '{0}' and ".format(self.tipo)
      else:
	tipo=''	
      sql="""SELECT {columnas} FROM movimientos,usuarios,cajas WHERE {tipo} usuarios.id_usuario=movimientos.usuario and 
       cajas.num_caja=caja and {condicion}
      """.format(columnas=columnas,condicion=condicion,tipo=tipo)
      self.cursor.execute(sql)
    except sqlite3.Error,e:
      raise(e)
      return []
    except:
      #print sql
      return []
    else:
      return self.cursor.fetchall()    
    
  def suma(self, condicion):
    try:
      if self.tipo!='':
	tipo=" tipo ='{0}' and ".format(self.tipo)
      else:
	tipo=''
      sql="""SELECT ROUND(SUM(monto),2) FROM movimientos WHERE {tipo} {condicion}""".format(condicion=condicion,tipo=tipo)
      #print sql
      self.cursor.execute(sql)
    except sqlite3.Error,e:
      raise(e)
      return 0
    except MySQLdb.Error,e:
      raise(e)
      return 0
    except:
      return 0
    else:
      ff=self.cursor.fetchone()
      if ff!=None and ff[0]!=None:
	return float(ff[0])    
      else:
	return 0