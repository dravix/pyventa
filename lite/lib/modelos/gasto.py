from lib.modelos.movimiento import Movimiento
class Gasto(Movimiento):
  def __init__(self,conexion):
    Movimiento.__init__(self,conexion,'gasto')
    
  def agregar(self, usuario, caja,detalle, monto ):
    return super(Gasto,self).agregar(usuario,caja,detalle,0-monto)