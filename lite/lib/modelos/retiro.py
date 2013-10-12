from lib.modelos.movimiento import Movimiento
class Retiro(Movimiento):
  def __init__(self,conexion):
    Movimiento.__init__(self,conexion,'retiro')
    
  def agregar(self, usuario, caja,detalle, monto ):
    return super(Retiro,self).agregar(usuario,caja,detalle,0-monto)
    