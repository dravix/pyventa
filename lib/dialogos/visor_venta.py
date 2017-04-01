from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QDialog
from ui.ui_visor_venta import Ui_Dialog
from lib.modelos.qmodelotablasql import QModeloTablaSql

class VisorVenta(QDialog, Ui_Dialog):
    def __init__(self, parent, ide=-1):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.ide = ide
        modelo = QModeloTablaSql(self.parent.cursor, self)
        self.tvProductos.setModel(modelo)
        tipo = ['Nota', 'Factura']
        if self.ide != -1:
            self.parent.cursor.execute("""select notas.id,clientes.nombre,ELT(notas.tipo+1,'Nota de venta','Factura'),
	   ELT(status+1,'Sin pagar','Pagada','En credito'), total, DATE_FORMAT(fecha,"%d/%M/%y"), usuarios.nombre from  notas, clientes,usuarios where clientes.id=cliente and id_usuario=notas.usuario and  notas.id={ide} """.format(ide=ide))
            nota = self.parent.cursor.fetchone()
            self.lbResumen.setText("""<table width="100%"><tr><td>
	  <b>Venta:</b> {0}<br/>
	  <b>Cliente:</b> {1} <br>
	  <b>Tipo de venta:</b> {2}<br/>
	  <b>Forma de pago:</b> {3} <br/> 
	  </td><td style="text-align:right">
	  <b>Fecha: </b>{5}<br/>
	  <b>Vendedor: </b>{6} <br/>
	  <b align="right" style="font-size:24px">Total: {4} </b>
	  </td><tr/></table>
	  
	  """.format(*nota)
            )
            head = ['Ref', 'Descripcion', 'Cantidad', 'Precio', 'Subtotal']
            sql = "select ref,descripcion,cantidad,ROUND(total/cantidad,2),total from productos,vendidos where ref=producto and venta=%s " % (
                ide)
            modelo.query(sql, head)
            self.tvProductos.resizeColumnsToContents()
