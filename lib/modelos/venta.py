import sqlite3,MySQLdb

class Venta:
  def __init__(self,conexion):
    self.conexion=conexion
    self.cursor=conexion.cursor
    
    def eliminar(self,nota):
      try:
	self.cursor.execute( "select v.producto,stock_logico+cantidad from vendidos as v,existencia as e where venta={0} and v.producto=e.producto; ".format(ide))
	ff=self.cursor.fetchall()
	for f in ff:
	  self.cursor.execute("UPDATE existencia set stock_logico={1} WHERE producto={0}".format(*f))
	self.cursor.execute("DELETE FROM vendidos where venta={venta}".format(venta=nota))  
	self.cursor.execute("DELETE FROM notas where `id`={venta}".format(venta=nota))
      except MySQLdb.Error, e:
	print "Error al eliminar nota %s"%nota,e
	return False
      except:
	return False
      else:	
	self.conexion.commit()
	return True

  def guardarVendidos(self,ide,canasta):
      for item in canasta:
	  try:
	    sql="""INSERT INTO `vendidos` VALUES({ide},{0},{tipo},{1},{5})""".format(ide=ide,tipo=0,*item)
	    self.cursor.execute(sql)
	    self.cursor.execute("UPDATE existencia SET stock_logico=stock_logico-{1} where producto={0}".format(*item))		
	    self.cursor.execute("UPDATE productos set vendidas=vendidas+1, ultima_modificacion=NOW() WHERE ref={0}".format(item[0]))
	  except sqlite3.Error,e:
	    raise(e)
	    self.conexion.rollback()
	    return False
	  except MySQLdb.Error, e:
	    raise(e)
	    self.conexion.rollback()
	    return False	  
	  except:
	    print "Error al guardar el producto ",item[0]
	    self.conexion.rollback()
	    return False
      self.conexion.commit()
      return True
	  
  def totalizar(self,canasta):
    total=0.0
    for item in canasta:
      total+=item[5]
    return total
  
  def actualizar(self,ide,canasta,cliente,usuario, caja, tipo,status):
    try:
      self.cursor.execute( "select v.producto,stock_logico+cantidad from vendidos as v,existencia as e where venta={0} and v.producto=e.producto; ".format(ide))
      ff=self.cursor.fetchall()
      for f in ff:
	self.cursor.execute("UPDATE existencia set stock_logico={1} WHERE producto={0}".format(*f))
      self.cursor.execute("""DELETE FROM vendidos where venta=%s """%ide)	    
    except sqlite3.Error,e:
      raise(e)
      return False
    except MySQLdb.Error, e:
      raise(e)
      return False
    except:
      return False
    else:
      self.conexion.commit()
      self.cursor.execute("UPDATE `notas` SET cliente={cliente}, usuario={vendedor}, caja={caja}, total={total}, tipo={tipo}, status={estado} WHERE id={ide}".format(cliente=cliente,vendedor=usuario,caja=caja,tipo=tipo,estado=status,total=self.totalizar(canasta), ide=ide))  
      self.guardarVendidos(ide,canasta)
      return ide
      
  def guardar(self,canasta,cliente,usuario, caja, tipo,status):
    try:      
      self.cursor.execute("INSERT INTO `notas`  VALUES(NULL,{cliente},{vendedor},{caja},{total},NOW(),{tipo},{status})".format(cliente=cliente,vendedor=usuario,caja=caja,total=self.totalizar(canasta),tipo=tipo,status=status))
    except sqlite3.Error,e:
      raise(e)
      return False
    except MySQLdb.Error, e:
      raise(e)
      return False      
    except:
      print "Error al guardar la venta"
      return False
    else:
      self.cursor.execute(self.conexion.lastId())
      last=int(self.cursor.fetchone()[0])
      if self.guardarVendidos(last,canasta):
	return last 
      
  def cambiarTipo(self,ide,tipo):
    try:
      self.cursor.execute("UPDATE notas set tipo={tipo} WHERE id={ide}".format(ide=ide,tipo=tipo))
    except:
      return False
    else:
      self.conexion.commit()
      return True
      
  def cambiarEstado(self,ide,estado):
    #ide puede ser uno o una lista de ides
    if isinstance(ide,list):
      ide=','.join(ide)
    try:
      self.cursor.execute("UPDATE notas set status={estado} WHERE id in ({ide})".format(estado=estado,ide=ide))
    except:
      return False
    else:
      self.conexion.commit()
      return True      

  def sumaTotales(self,condicion):
    self.cursor.execute("SELECT SUM(total) from notas where {condicion}".format(condicion=condicion))
    return self.cursor.fetchone()
    

  def suma(self, condicion):
    try:
      self.cursor.execute("""SELECT ROUND(SUM(total),2) FROM compras WHERE {condicion}""".format(condicion=condicion))
    except:
      return 0
    else:
      ff=self.cursor.fetchone()
      if ff!=None and ff[0]!=None:
	return float(ff[0])    
      else:
	return 0       
