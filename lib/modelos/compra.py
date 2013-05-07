import sqlite3,MySQLdb
class Compra:
  def __init__(self,conexion):
    self.conexion=conexion
    self.cursor=conexion.cursor
    
  def eliminarCompra(self,ide):
    try:
      #Corrige el stock_logico 
      self.cursor.execute( "select c.producto,stock_logico-cantidad from comprados as c,existencia as e where compra={0} and c.producto=e.producto; ".format(ide))
      ff=self.cursor.fetchall()
      for f in ff:
	self.cursor.execute("UPDATE existencia set stock_logico={1} WHERE producto={0}".format(*f))
      #Eliminacion de los articulos comprados y de la compra en su
      self.cursor.execute("""DELETE FROM comprados where compra={0} """.format(ide))
      self.cursor.execute("""DELETE FROM compras where id={0} """.format(ide))
    except:
      print "Problema al eliminar la compra, la operacion no se realizo."
      return False
    else:
      self.conexion.commit()
      return True

  def actualizar(self,ide,canasta,usuario,proveedor):
    try:
      self.cursor.execute( "select c.producto,stock_logico-cantidad from comprados as c,existencia as e where compra={0} and c.producto=e.producto; ".format(ide))
      ff=self.cursor.fetchall()
      for f in ff:
	self.cursor.execute("UPDATE existencia set stock_logico={1} WHERE producto={0}".format(*f))
      self.cursor.execute("""DELETE FROM comprados where compra=%s """%ide)	    
    except sqlite3.Error,e:
      raise(e)
      return False
    except:
      return False
    else:
      self.conexion.commit()
      self.totalizar(canasta)
      self.cursor.execute("UPDATE compras SET proveedor={proveedor}, comprador={comprador}, total={total} WHERE id={id};".format(proveedor=proveedor,comprador=usuario,total=self.totalizar(canasta), id=ide))  
      self.guardarComprados(ide,canasta)
      return True
    
  def guardarComprados(self,ide,canasta):

      for item in canasta:
	  try:
	    self.cursor.execute("""insert into comprados values({compra},{0},{1},{7},{4})""".format(compra=ide,*item))
	    sql="UPDATE existencia SET stock_logico=stock_logico+{1} where producto={0}".format(*item)
	    self.cursor.execute(sql)		
	  except:
	    print "Error al guardar el producto ",item[0]
	    self.conexion.rollback()
	    return False
	  else:
	    self.conexion.commit()
	    return True
	  
  def totalizar(self,canasta):
    total=0.0
    for item in canasta:
      total+=float(item[1]*item[7])
    return total
  
  def guardar(self,canasta,usuario,proveedor):
    try:      
      self.cursor.execute("INSERT INTO compras VALUES(NULL,NOW(),{proveedor},{comprador}, {total},0); ".format(proveedor=proveedor,comprador=usuario,total=self.totalizar(canasta)))
    except:
      print "Error al guardar la compra"
      return False
    else:
      self.cursor.execute(self.conexion.lastId())
      last=int(self.cursor.fetchone()[0])
      if self.guardarComprados(last,canasta):
	return last
	
  def obtener(self,ide):
    self.cursor.execute("SELECT * FROM compras WHERE id={0};".format(ide))
    compra=self.cursor.fetchone()
    if compra!=None:
      self.cursor.execute("SELECT * FROM comprados WHERE compra={0};".format(compra[0]))
      comprados=self.cursor.fetchall()
      return {'compra':compra,'articulos':comprados}
    else:
      return False
    
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