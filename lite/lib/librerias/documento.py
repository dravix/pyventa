class Documento:
  
  def __init__(self,ruta,campos):
    self.abrir(ruta,campos)
    
    
  def abrir(self,ruta=False,campos=False):
    
    try:
      f=open(ruta,"r")
    except:
      print "EL archivo '{0}'  no se encontro".format(ruta)
    else:
      plantilla=f.read().format(**campos)
      f.close()
      plantilla
    
  

