#!/usr/bin/env python
import sys
import os
import datetime
import base64
import locale
import md5
from re import sub
from lib.librerias.comun import *

version = 2.340
aqui = os.getcwd()
# aqui="/usr/share/pyventa/"
if sys.platform == 'linux2':
    home = os.path.join(os.path.expanduser('~'), ".pyventa")
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, 'pyventa\0')
    except:
        pass

else:
    sys.stdout = open(os.path.join(
        os.path.expanduser('~'), "pyventa.salida.log"), "w")
    sys.stderr = open(os.path.join(
        os.path.expanduser('~'), "pyventa.error.log"), "w")
    home = os.path.join(os.path.expanduser('~'), "pyventa")

    # home=os.path.join(aqui,'perfil')
# sys.path.append(os.path.join(aqui,'plugins'))
# sys.path.append(os.path.join(aqui,'lib'))
# sys.path.append('ui')
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

sys.path.append(os.path.join(home, 'drivers'))
import tempfile
import socket
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QSize, QTimer
from PyQt4.QtGui import QMenu, QAction, QIcon, QToolButton
from ui.ui_pyventa import Ui_Principal
import MySQLdb
import ConfigParser
from lib.db_conf import configurador
from lib.buscador import Buscador
from lib.config import Configs
from lib.cobro import Cobros
from lib.caja import Cajas
from lib.reporte import Reportes
from lib.cventa import Cventa
from lib.pendientes import Pendientes
from lib.selector import Selector
from lib.utileria import Documento, MyTableModel, AperturaCaja
from lib.dialogos.marca_faltante import Faltante
from lib.nletras import *
import lib.libutil as libutil
from lib.swap import Swaproductos
from lib.librerias.configurador import Configurador
from lib.librerias.conexion import Conexion, dicursor
from lib.librerias.seguridad import Seguridad
from lib.libutil import listaHtml, printa
from lib.factura import Factura
from lib.librerias.conexion import dicursor
#from check import Checador
try:
    import win32print
except:
    pass


class Pyventa(QtGui.QMainWindow, Ui_Principal):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self.home = home
        self.datosModulos = {}
        self.stack.setCurrentIndex(0)
        self.lista2.setSortingEnabled(True)
        self.canasta = None
        self.maquina = socket.gethostname()
        self.version = version
        self.lista2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.actionIngresar, QtCore.SIGNAL(
            "triggered()"), self.insert)
        self.connect(self.actionPreferencias, QtCore.SIGNAL(
            "triggered()"), lambda: self.stackMove(7))
        self.connect(self.codigo, QtCore.SIGNAL("returnPressed()"),
                     lambda: self.adomatic(self.codigo.text()))
        self.connect(self.codigo, QtCore.SIGNAL(
            "textChanged(QString)"), self._buscar)
        self.connect(self.cant, QtCore.SIGNAL("returnPressed()"), self.ingreso)
        self.connect(self.actionQuitar_prod,
                     QtCore.SIGNAL("triggered()"), self.delete)
        self.connect(self.actionAbrir_cajon, QtCore.SIGNAL(
            "triggered()"), self.abrirCajon)
        self.connect(self.actionModo_rapido, QtCore.SIGNAL(
            "toggled (bool)"), self.activarModo)
        self.connect(self.actionGuardarcompra, QtCore.SIGNAL(
            "triggered()"), self.guardarCompra)
        self.connect(self.actionAbrir_compra, QtCore.SIGNAL(
            "triggered()"), self.editarCompra)
        self.connect(self.actionNueva_compra, QtCore.SIGNAL(
            "triggered()"), self.nuevaCompra)
        self.connect(self.actionSwap, QtCore.SIGNAL("triggered()"), self.swap)

        self.connect(self.actionNueva, QtCore.SIGNAL(
            "triggered()"), self.limpiar)
        self.connect(self.tbTrash, QtCore.SIGNAL("clicked()"), self.limpiar)
        self.connect(self.tbFull, QtCore.SIGNAL("clicked()"), self.pantalla)
        self.connect(self.tbOpen, QtCore.SIGNAL("clicked()"), self.editarNota)
        self.connect(self.tbSave, QtCore.SIGNAL("clicked()"), self.guardar)

        self.connect(self.bventa, QtCore.SIGNAL("clicked()"), self.insert)
        self.connect(self.csCliente, QtCore.SIGNAL(
            "clicked()"), self.selCliente)
        self.connect(self.actionImprimir, QtCore.SIGNAL(
            "triggered()"), self.imprimirTicket)
        self.connect(self.actionReimprimir, QtCore.SIGNAL(
            "triggered()"), self.reprint)
        self.connect(self.actionPunto_de_venta,
                     QtCore.SIGNAL("triggered()"), self.ver)
        self.connect(self.actionA_Pyventa, QtCore.SIGNAL(
            "triggered()"), self.about)
        self.connect(self.aAbrir, QtCore.SIGNAL(
            "triggered()"), self.editarNota)
        self.connect(self.actionPresupuesto, QtCore.SIGNAL(
            "triggered()"), self.presupuestar1)
        self.connect(self.actionAutorizar_descuento,
                     QtCore.SIGNAL("triggered()"), self.autDescuento)
        #self.connect(self.clSeleccionar_estilo, QtCore.SIGNAL("clicked()"), self.loadStyle)
        #self.connect(self.actionUpdate, QtCore.SIGNAL("triggered()"), self.actualizar)
        self.connect(self.actionCopiar_nota, QtCore.SIGNAL(
            "triggered()"), self.copiarNota)
        self.connect(self.actionCancelar_nota, QtCore.SIGNAL(
            "triggered()"), self.cancelNota)

        self.connect(self.lista2, QtCore.SIGNAL(
            "activated(const QModelIndex&)"), self.busca2)
        #self.connect(self.tbusk, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.adomatic)
        # self.menubar.setVisible(False)
        self.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.openf)
        self.connect(self.actionGuardar, QtCore.SIGNAL(
            "triggered()"), self.savef)
        self.connect(self.actionFacturar, QtCore.SIGNAL(
            "triggered()"), self.cerrarFactura)
        self.connect(self.actionNueva_sesion, QtCore.SIGNAL(
            "triggered()"), self.iniciarSesion)
        self.connect(self.actionCerrar_sesion, QtCore.SIGNAL(
            "triggered()"), self.cerrarSesion)
        self.connect(self.actionCambiar_usuario, QtCore.SIGNAL(
            "triggered()"), self.iniciarSesion)
        self.connect(self.actionCompleta, QtCore.SIGNAL(
            "triggered()"), self.pantalla)
        self.connect(self.aConfigBd, QtCore.SIGNAL(
            "triggered()"), self.configBd)
        self.lista2.setSelectionMode(1)
        self.curser = None
        self.cursor = None
        self.modulos = {}
        self.sesion = {}
        self.iniVal()
        self.full = False
        self.moli2 = None

        self.cfg = Configurador(self)
        if self.cfg.stat:
            self.conexion = Conexion(self, self.cfg)
            self.caja = self.cfg.get('pyventa', 'caja')
            if self.conexion.stat:
                self.cursor = self.conexion.cursor
                self.curser = self.conexion.curser
                self.iniciarEstilo()
                self.iniciarSesion()
                driver = self.cfg.get('ticket', 'driver')
                self.ticketDriver = __import__("perfil.drivers.{}".format(
                    driver), globals(), locals(), [driver])
        else:
            print "Error al iniciar configuraciones"
        # self.conexion()

        self.iniciarMenus()
        self.iconset = self.cfg.get("pyventa", "resolucion")+"/"
        #self.connect(self.lista2, QtCore.SIGNAL("keyPressEvent ( QKeyEvent * event )"), self.drive)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(
            ":/modulos/images/png/elegant/ventas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28.addPixmap(QtGui.QPixmap(
            ":/modulos/images/png/elegant/ventas.png"), 2, QtGui.QIcon.Off)
        self.bventa.setIcon(icon28)
        # self.bventa.setIconVisibleInMenu(True)
        self.banderas = {'modo': 0, 'edicion': False, 'tipo': 'v'}
        self.current = self
        self.setupWidgets()
        self.hoy = datetime.date.today().isoformat()
        self.lfecha.setText("Fecha: <b>{0}</b>".format(self.hoy))
        self.fecha = str(datetime.date.today().strftime("%d-%m-%Y"))
        self.datos['fecha'] = self.fecha
        self.hlm.addWidget(self.bventa)

        self.modulos["config"] = Configs(self, self.stack.count())
        # self.stack.addWidget(self.modulos["config"])
        self.modulos["buscador"] = Buscador(self, self.stack.count())
        self.stack.addWidget(self.modulos["buscador"])

        self.modulos["cventa"] = Cventa(self, self.stack.count())
        # self.stack.addWidget(self.modulos["cventa"])
        # self.modulos["cobros"]=Cobros(self,self.stack.count())
        # self.stack.addWidget(self.modulos["cobros"])
        self.modulos["cajas"] = Cajas(self, self.stack.count())
        self.stack.addWidget(self.modulos["cajas"])
        self.modulos["reportes"] = Reportes(self, self.stack.count())
        self.stack.addWidget(self.modulos["reportes"])
        self.modulos["pendientes"] = Pendientes(self, self.stack.count())
        self.stack.addWidget(self.modulos["pendientes"])
        self.connect(self.lista2, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint)'), self.ocm2)
        self.tbRegist.setDefaultAction(self.modulos["cventa"].action)
        # self.modulos["config"]=config(self,self.stack.count())
        # self.datosModulos.append(self.modulos["config"].datos)
        # self.stack.addWidget(self.modulos["config"])
        # self.menuModulos.addAction(self.modulos["config"].action)

        # self.modulos["cventa"]=cventa(self,self.stack.count())
        # self.datosModulos.append(self.modulos["cventa"].datos)
        self.connect(self.aGuardar, QtCore.SIGNAL("triggered()"), self.guardar)

        #action=self.menuEdicion.addAction("Registrar compra")
        #self.connect(action, QtCore.SIGNAL("triggered()"),self.nuevaCompra)
        self.setupActions()
        #print self.sesion['usuario']['level']
        self.scan()
        self.iniciarCaja()

    def conexion(self):
        self.conexion = Conexion(self, self.cfg)
        if self.conexion.stat:
            self.cursor = self.conexion.cursor
            self.curser = self.conexion.curser
            self.iniciarSesion()

    def ver(self):
        self.current = self
        self.stack.setCurrentIndex(0)

    def nuevaCompra(self):
        self.limpiar()
        self.banderas['tipo'] = 'c'
        self.logo.setText("Nueva compra")
        self.csCliente.setText("Seleccione Proveedor")
        # nc=nuevaLista(self)
        # nc.exec_()

    def setupWidgets(self):
        self.footer.setVisible(False)
        self.wResumen.setVisible(False)
        self.dsbCambio.setVisible(False)
        self.lblCambio.setVisible(False)

        self.codigo.setFocus()

    def setupActions(self):
        menu = QMenu(self)
        modific = menu.addAction(
            QIcon(":/actions/images/actions/black_18/pecil.png"), "Modificar")
        self.removerProducto = menu.addAction(QIcon(
            ":/actions/images/actions/black_18/cancel.png"), "Quitar de la lista", self.delete)
        self.tabla.addAction(modific)
        self.tabla.addAction(self.removerProducto)
        #self.menuHerramientas.addAction(QIcon(":/modulos/images/png/mini/productos.png"),"Checador de precios",self.checador)

    # def checador(self):
        # check=Checador()
        # check.show()

    def iniVal(self):
        self.datos = {'total': 0, 'subtotal': 0, 'descuento': 0, 'fecha': 0}
        self.cliente = {'id': 1, 'nombre': "Normal mostrador", 'tipo': 0}
        self.basket = []
        self.logo.setText("Nota de venta")
        self.tutmp = False  # Variable de producto temporal

    def limpiar(self):
        #model = tablaModelo(0, 0, self)
        self.iniVal()
        self.verCanasta()
        # self.display()
        self.csCliente.setText("Seleccione cliente")
        self.grant()
        self.csCliente.setText(self.cliente['nombre'])
        self.cursor.execute(
            "select `id` from notas order by `id` desc limit 1;")
        self.nota = self.cursor.fetchone()
        self.nota = str(self.nota[0])
        self.lnota.setText("Ultima Nota: <b>#"+self.nota+"</b>")
        self.codigo.setFocus()


    def iniciarMenus(self):
        self.popLista2 = QtGui.QMenu(self)
        action = self.popLista2.addAction(QtGui.QIcon(
            ":/actions/images/actions/color_18/battery_empty.png"), "Marcar como faltante ", self.marcarFalta)
        action.setIconVisibleInMenu(True)

    def iniciarEstilo(self):
        try:
            kcss = open(os.path.join(os.path.dirname(os.path.realpath(
                __file__)), "perfil", "estilos", self.cfg.get("pyventa", "estilo")), "r")
            estilo = kcss.read()
            self.setStyleSheet(estilo)
            kcss.close()
        except:
            try:
                kcss = open(os.path.join(self.home, "estilos",
                                         self.cfg.get("pyventa", "estilo")), "r")
                estilo = kcss.read()
                self.setStyleSheet(estilo)
                kcss.close()
            except:
                print "No se cargo el estilo " + \
                    self.cfg.get("pyventa", "estilo")

    def configBd(self):
        print "Configurando base de datos"
        ui = configurador(self.cfg)
        dialog = ui.exec_()
        if (dialog == 1):
            self.conexion()

    def iniciarCaja(self):
        if self.aut(2) > 0:

            caja = self.cfg.get("pyventa", "caja")
            # if caja>0:
            #self.cursor.execute("SELECT maquina FROM cajas WHERE estado != {0} and num_caja={1} ;".format(self.hoy,caja))
            # mac=self.cursor.fetchone()
            # if mac!=None: #Si caja esta disponible
            #sql="UPDATE cajas SET estado={0}, maquina='{1}' where num_caja={2};".format(self.hoy,self.maquina,caja)
            # self.cursor.execute(sql)
            # self.caja=caja
            # self.setCaja()
            # else:
            #self.cursor.execute("SELECT maquina='{0}' FROM cajas WHERE  num_caja={1} ;".format(self.maquina,caja))
            # mac=self.cursor.fetchone()
            # if mac!=None and mac>0:
            # self.caja=caja

        #print "caja",self.caja

    def setCaja(self):
        ap = AperturaCaja(self)
        ap.exec_()

    def scan(self):
        # group=QActionGroup(self)
        for mod, clase in self.modulos.iteritems():
            self.datosModulos[clase.datos['nombre']] = clase.datos
            # self.menuModulos.addAction(self.modulos["config"].action)
            self.menuModulos.addAction(clase.action)
            # self.toolbar.addAction(clase.action)
            tb = QToolButton(self)
            tb.setDefaultAction(clase.action)
            tb.setAutoRaise(True)
            tb.setIconSize(QSize(32, 32))
            tb.setToolButtonStyle(3)
            self.hlm.addWidget(tb)
        # self.hlm.addWidget(group)

    def about(self):
        QtGui.QMessageBox.about(self, "Acerca de Pyventa", " <p>Pyventa es un sistema libre para la gestion de recursos  de pequenas y medianas \
empresas.<p/> <p>Version %s<br/>Libreria visual: Qt4<br/>Plataforma: %s <br/> Desarrodador: David Osorio Hernandez\n\nPara mas informacion y actualizaciones: <a href=\"http://pyventa.com\">http://pyventa.com/</a></p>" % (sys.platform, version))

    def pantalla(self):
        if self.full == True:
            self.showMaximized()
            self.full = False
        else:
            self.showFullScreen()
            self.full = True

    def insert(self):
        self.stack.setCurrentIndex(0)
        self.current = self
        self.codigo.selectAll()
        self.codigo.setFocus()
        self.wResumen.setVisible(False)

    def tabular(self, tabla, sql, head):
            # col='`'
            # col+='`,`'.join(head)
            # col+='`'
        tabla.clear()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except MySQLdb.Error, e:
            print e
        else:
            tabla.setColumnCount(len(head))
            tabla.setRowCount(len(result))
            for i, data in enumerate(head):
                item = QtGui.QTableWidgetItem(1)
                item.setText(str(data))
                tabla.setHorizontalHeaderItem(i, item)
            for i, elem in enumerate(result):
                for j, data in enumerate(elem):
                    item = QtGui.QTableWidgetItem(1)
                    item.setText(str(data))
                    tabla.setItem(i, j, item)
            tabla.resizeColumnsToContents()

    def entablar(self, tabla, lista, head):
        # Cumple la misma funcion que tabular, con la diferencia que esta recibe una lista de tuplas
        tabla.clear()
        tabla.setColumnCount(len(head))
        tabla.setRowCount(len(lista))
        for i, data in enumerate(head):
            item = QtGui.QTableWidgetItem(1)
            item.setText(str(data))
            tabla.setHorizontalHeaderItem(i, item)
        for i, elem in enumerate(lista):
            for j, data in enumerate(elem):
                item = QtGui.QTableWidgetItem(1)
                item.setText(str(data))
                tabla.setItem(i, j, item)
        tabla.resizeColumnsToContents()

    # def on_context_menu(self, point):
        #self.popMenu.exec_( self.lista2.mapToGlobal(point) )

    def loadStyle(self):
        openFile = QFileDialog.getOpenFileNames(
            self, "Seleccione el estilo", aqui + "perfil", "Hojas de estilo (*.css)")
        if (openFile != ""):
            kcss = open(openFile[0], "r")
            estilo = kcss.read()
            self.setStyleSheet(estilo)
            kcss.close()

    def aut(self, nivel):
        # recibe una clave (key) y un valor requerido (req) para ver si tiene el nivel necesario
        # if (self.stack.currentIndex()==modulo):
        if nivel <= self.sesion['usuario']['nivel']:
            return self.sesion['usuario']['id_usuario']
        else:
            Acceso = QtGui.QInputDialog.getText(self, self.tr("Filtro de Acceso"), self.tr(
                "Ingrese su clave de autorizacion."), QtGui.QLineEdit.Password)
            key = str(Acceso[0])
            m = md5.new(key)
            self.cursor.execute(
                "select id_usuario,nivel from usuarios where clave='{0}' ".format(m.hexdigest()))
            val = self.cursor.fetchone()
            if val != None:
                if int(val[1]) >= int(nivel):
                    return val[0]
                else:
                    return -1
            else:
                return -1

    def stackMove(self, num):
        if self.aut(self.datosModulos[num]['nivel']) > 0:
            self.stack.setCurrentIndex(num)

    def move(self, nombre):
        if self.aut(self.datosModulos[nombre]['nivel']) > 0:
            self.current = self.modulos[nombre.lower()]
            self.stack.setCurrentIndex(self.datosModulos[nombre]['id'])

    def activarModo(self, val):
        if val:
            self.banderas['modo'] = 1
            #msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Modo de ingreso rapido activado","Ha activado el modo de ingreso rapido con lo que evita ingresar la cantidad de productos manualmente.",QtGui.QMessageBox.Close,self)
            # msgBox.exec_()
            self.lblModo.setText("Ingreso rapido")
            self.lblModo.setToolTip(
                "En \"Ingreso rapido\" no se preguntara la cantidad\nel articulo \"entra\" directo a la canasta de productos. ")
            self.codigo.setStyleSheet('color:#900;')

        else:
            self.banderas['modo'] = 0
            #msgBox=QtGui.QMessageBox(QtGui.QMessageBox.Information,"Modo manual","Se ha desactivado el modo de ingreso rapido.",QtGui.QMessageBox.Close,self)
            # msgBox.exec_()
            self.lblModo.setToolTip(
                "En \"Ingreso manual\" los productos no entran a la canasta hasta que se defina la cantidad,\nesto requiere por lo tanto la participacion del teclado. ")
            self.lblModo.setText("Ingreso manual")
            self.codigo.setStyleSheet('color:#333')

    def adomatic(self, txt):
        """Busca el producto por referencia o codigo(s) y lo pone en modo cantidad"""
        cantidad = False
        codigo = None
        txt = str(txt)
        if (txt != ''):
            if txt[0] == '-':
                if len(txt[1:]) > 0:
                    self.abrirNota(int(txt[1:]))
            elif txt[0] == '+':
                if len(txt[1:]) > 0:
                    self.abrirNota(int(txt[1:]), False)
            else:
                code = str(txt).split('*')
                if len(code) <= 1:
                    code = str(txt).split(' ')
                if ((len(code) > 0) and len(code[0]) > 0):
                    if (code[0][0].isdigit()):
                        codigo = code[0]
                if ((len(code) == 2) and len(code[0]) > 0 and len(code[1]) > 0 and (code[0][0].isdigit())):
                    codigo = code[1]
                    cantidad = code[0]
                if codigo != None:
                    try:
                        np = self.curser.execute(
                            "select ref, descripcion,precio,costo,unidades.nombre as unidad FROM productos,unidades where ref='{0}' or codigo='{0}' and unidades.id=unidad ".format(codigo))
                        if np == 0:
                            self.curser.execute(
                                "SELECT distinct ref, descripcion,precio,costo, unidades.nombre as unidad FROM productos as p, codigos as c, unidades where producto=ref and unidades.id=unidad and c.codigo='{0}';".format(codigo))  # Deprecated
                        #self.curser.execute("SELECT `ref`,`descripcion`,`precio`  from productos as p where FIND_IN_SET('{0}',p.codigo) OR ref={0} limit 1".format(codigo))
                        #print "SELECT `ref`,`descripcion`,`precio`  FROM productos as p, codigos as c where (ref=%s  OR p.codigo=%s OR c.codigo='%s') and producto=ref limit 1"%(codigo,codigo,codigo)
                    except MySQLdb.Error, e:
                        if e.args[0] in (2006, 2013):
                            self.conexion()
                        else:
                            raise(e)
                    else:
                        rec = self.curser.fetchone()

                        if rec != None:
                            rec = dicursor(self.curser, rec)
                            if len(code) == 1:  # Cuando solo exista  REFERENCIA
                                self.tutmp = [int(rec['ref']), 0, str(rec['descripcion']), float(
                                    rec['precio']), 0, 0, 0, float(rec['costo']), rec['unidad']]
                                if self.banderas['modo'] == 0:  # modo normal
                                    self.codigo.setText(
                                        str(rec['descripcion']))
                                    self.dsbPrecio.setValue(
                                        float(rec['precio']))
                                    self.cant.setText("1")
                                    self.cant.setFocus()
                                    self.cant.selectAll()
                                else:
                                    self.tutmp[1] = 1
                                    self.ingreso(self.tutmp)

                            elif cantidad != False:  # Cuando reconozca un asterisco CANTIDAD*REFERENCIA
                                sub = float(cantidad)*float(rec['precio'])
                                tmp = [int(rec['ref']), float(cantidad), str(rec['descripcion']), float(
                                    rec['precio']), sub, 0, 0, float(rec['costo']), rec['unidad']]
                                self.ingreso(tmp)
                            # self.codigo.selectAll()
                            return rec
                        else:
                            self.codigo.setText("Producto no encontrado")
                            self.codigo.selectAll()
                            self.dsbPrecio.setValue(0)

    def ingreso(self, tmp=False):
        # Se encarga de visualizar y agregar los datos de una tupla que contenga un producto su cantidad y precio
        if (tmp == False):
            tmp = self.tutmp
            self.tutmp = False
            tmp[1] = float(self.cant.text())
        if (tmp != None):
            # tmp[1]=float(self.cant.text())
            # self.tabla.setHorizontalHeaderItem(self.tabla.columnCount()+1,QtGui.QTableWidgetItem("Descuento",1))
            k = 0
            if (self.buscar_canasta(tmp) == False):
                tmp[4] = float(tmp[1])*float(tmp[3])
                tmp = self.descontar(tmp)
                # tmp[5]=tmp[4]*(tmp[5]*.01)
                # tmp[4]=tmp[4]-tmp[5]
                self.basket.append(tmp)
                self.verCanasta()

            self.tabla.scrollToBottom()
            self.tabla.resizeColumnsToContents()
            self.tabla.horizontalHeader().setResizeMode(2, 1)
            tmp = None
            self.grant()
            self.cant.setText('1')
            self.codigo.clear()
            self.dsbPrecio.clear()
            self.codigo.setFocus()
            self.codigo.selectAll()

    def descontar(self, producto):
        producto[5] = producto[4]
        self.curser.execute(
            """SELECT `ref`,`precio`, familia, departamento  FROM productos,familias where ref={0} AND familia=familias.id   AND familia=familias.id limit 1""".format(producto[0]))
        rec = self.curser.fetchone()
        if rec != None:
            rec = dicursor(self.curser, rec)
            promo = self.checkPromo(rec, producto[1])
            if promo != False and promo != None:
                self.footer.setVisible(True)
                timer = QTimer.singleShot(5000, self.clearPromo)
                descuento = float(promo['descuento'])
                desc = producto[4]*(descuento*.01)
                self.Promo.setText(
                    "Aplica descuento de :{0}. ".format(promo['nombre']))
                producto[5] = producto[4]-desc
                producto[6] = descuento
        return producto

    def clearPromo(self):
        self.footer.setVisible(False)
        self.Promo.setText("")

    def checkPromo(self, prod, cant):
        self.curser.execute("""SELECT * FROM ofertas as O,promociones as P WHERE conjunto={0} AND 
	  tipo=0 AND O.promocion=P.id AND {hoy} BETWEEN P.inicio AND P.fin AND minimo<={1} AND 
	  maximo>={1} order by P.descuento desc """.format(prod['ref'], cant, hoy=self.hoy))
        oferta = self.curser.fetchone()
        if oferta == None:
            self.curser.execute("""SELECT * FROM ofertas as O,promociones as P WHERE conjunto={0} AND 
	    tipo=1 AND O.promocion=P.id AND {hoy} BETWEEN P.inicio AND P.fin AND minimo<={1} AND 
	    maximo>={1} order by P.descuento desc""".format(prod['familia'], cant, hoy=self.hoy))
            oferta = self.curser.fetchone()
            if oferta == None:
                self.curser.execute("""SELECT * FROM ofertas as O,promociones as P WHERE conjunto={0} AND 
	      tipo=2 AND O.promocion=P.id AND {hoy} BETWEEN P.inicio AND P.fin AND minimo<={1}  AND 
	      maximo>={1} order by P.descuento desc""".format(prod['departamento'], cant, hoy=self.hoy))
                oferta = self.curser.fetchone()
                if oferta == None:
                    return False
                else:
                    oferta = dicursor(self.curser, oferta)
                    return oferta
            else:
                oferta = dicursor(self.curser, oferta)
                return oferta
        else:
            oferta = dicursor(self.curser, oferta)
            return oferta

    def checkAllPromos(self, ref):
        promos = []
        self.curser.execute(
            "SELECT `ref`,`precio`, familia, departamento  FROM productos,familias where ref=%s AND familia=familias.id   AND familia=familias.id limit 1" % ref)
        prod = self.curser.fetchone()
        if prod != None:
            prod = dicursor(self.curser, prod)
            self.cursor.execute("""SELECT nombre,minimo, descuento, {precio}-({precio}*descuento*0.01) FROM ofertas as O,promociones as P
	    WHERE ((tipo=0 and conjunto={ref}) OR (tipo=1 and conjunto={familia}) OR (tipo=2 and conjunto={departamento})) AND 
	    O.promocion=P.id AND date({hoy}) BETWEEN P.inicio AND P.fin  order by P.descuento desc """.format(hoy=self.hoy, **prod))
            oferta = self.cursor.fetchall()
            if oferta != None:
                # oferta=list(oferta)
                promos.extend(oferta)
            return promos

    def buscar(self, txt):
        if(txt != None and self.tutmp == False):
            txt = str(txt)
            if ((len(txt) > 2) and (txt[0].isdigit() == False)):
                li = txt.split(' ')
                fil = []
                for l in li:
                    fil.append(" descripcion like '%{0}%' ".format(l))
                sql = "SELECT `ref`,`descripcion`,`precio` FROM productos where {0} order by vendidas desc  limit 20".format(
                    "and".join(fil))
                head = ['Ref', 'Descripcion del producto', 'Precio']
                self.cursor.execute(sql)
                qry = self.cursor.fetchall()
                self.moli2 = MyTableModel(qry, head, self)
                self.lista2.setModel(self.moli2)
                # self.tabular(self.lista2,sql,head)
                self.lista2.setColumnHidden(0, True)
                self.lista2.resizeColumnsToContents()
                #print self.lista2.columnWidth(1)
                #self.lista2.resize(self.lista2.columnWidth(1)+self.lista2.columnWidth(2), self.lista2.height() )
                self.splitter.moveSplitter(
                    self.lista2.columnWidth(1)+self.lista2.columnWidth(2), 1)

    def busca2(self, modelIndex):
        ref = self.moli2.getCell(modelIndex, 0)
        desc = self.moli2.getCell(modelIndex, 1)
        precio = self.moli2.getCell(modelIndex, 2)
        self.tutmp = [int(ref), 0, desc, float(precio), 0]
        rec = self.adomatic(ref)
        self.checkAllPromos(ref)

    def reprint(self):
        nota = QtGui.QInputDialog.getInteger(self, self.tr(
            "Copiar nota"), self.tr("Ingrese el numero de nota."))
        if nota[1]:
            self.limpiar()
            ide = nota[0]
            self.curser.execute('select * from notas where `id`='+str(nota[0]))
            nota = self.curser.fetchone()
            nota = dicursor(self.curser, nota)
            prods = nota['productos']
            cant = nota['cant']
            prods = prods.split(',')
            cant = cant.split(',')
            for i, prod in enumerate(prods):
                try:
                    self.cursor.execute(
                        "SELECT `descripcion`,`precio` FROM productos where `ref`="+str(prod)+" ;")
                except:
                    print 'Producto no existe'
                else:
                    producto = self.cursor.fetchone()
                    total = float(cant[i])*float(producto[1])
                    tmp = [float(prod), float(cant[i]),
                           producto[0], float(producto[1]), total]
                    self.ingreso(tmp)
            self.imprimirTicket()
            self.limpiar()

    def grant(self):
        # Hace la suma de todos los productos es un Gran Total
        # Devuelve una tupla del tipo [subtotal, descuento. total]
        suma = 0
        total = 0
        nart = 0
        for prod in self.basket:
            suma += float(prod[4])
            total += float(prod[5])
            nart += float(prod[1])
        # desc=(suma*self.desc)/100
        desc = round(suma-total, 1)
        total = round(total, 1)
        sub = round(suma, 1)
        self.ltotal.setText("GT: ${:,.2f}".format(total))
        self.resumen.setText("<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Subtotal:</span><span style=\" font-size:11pt;\"> 	</span><span style=\" font-size:11pt; font-weight:600; \">$ "+str(sub)+"</span></p>\
<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><span style=\" font-style:italic;\">Descuento:	</span><span style=\" \">$ "+str(desc)+"</span></p>")
        self.datos['subtotal'] = sub
        self.datos['descuento'] = desc
        self.datos['total'] = total
        self.datos['narticulos'] = nart
        return [sub, desc, total]

    def buscar_canasta(self, tupla):
        # Busca un producto dentro de la canasta de compra y regresa verdadero si existe y falso en caso contrario
        ret = False
        if (len(self.basket) > 0):
            for i, prod in enumerate(self.basket):
                if (prod[0] == tupla[0]):
                    prod[1] += tupla[1]
                    prod[4] = prod[1]*prod[3]
                    # prod[5]=prod[4]*(tupla[5]*.01)
                    # prod[4]=prod[4]-prod[5]
                    prod = self.descontar(prod)
                    self.verCanasta()
                    ret = True
        return ret

    # def nuevaCompra(self):
        # if self.aut(2)>0:
        # self.banderas['tipo']='c'
        # self.modulos["cventa"].guardarCompra()
        # self.limpiar()

    def guardar(self):
        if self.banderas['tipo'] == 'v':
            self.modulos["cventa"].inicia(False)
            self.limpiar()

        elif self.banderas['tipo'] == 'c':
            self.guardarCompra()

    def guardarCompra(self):
        if self.aut(2) > 0:
            self.banderas['tipo'] = 'c'
            #print self.cliente['id']
            if self.cliente['id'] < 2:
                #QtGui.QMessageBox(QtGui.QMessageBox.Warning,"Seleccione un proveedor","Busque y seleccione el proveedor de la compra .",QtGui.QMessageBox.Ok,self)
                if self.selCliente() > 0:
                    self.guardarCompra()
            else:
                self.modulos["cventa"].guardarCompra()

    def editarNota(self):
        if self.aut(2) > 0:
            ref = QtGui.QInputDialog.getText(self, self.tr("Editar nota"), self.tr(
                "Numero de venta:"), QtGui.QLineEdit.Normal)
            if ref[1]:
                self.abrirNota(ref[0])

    def editarCompra(self):
        if self.aut(2) > 0:
            ref = QtGui.QInputDialog.getText(self, self.tr("Editar compra"), self.tr(
                "Numero de compra: "), QtGui.QLineEdit.Normal)
            if ref[1]:
                self.abrirCompra(ref[0])

    def copiarNota(self):
        nota = QtGui.QInputDialog.getInteger(self, self.tr(
            "Copiar nota"), self.tr("Ingrese el numero de nota."))
        if nota[1]:
            self.limpiar()
            ide = nota[0]

            for i, prod in enumerate(prods):
                try:
                    print prod
                    self.cursor.execute(
                        "SELECT `descripcion`,`precio` FROM productos where `ref`="+str(prod)+" ;")
                except:
                    print 'Producto no existe'
                else:
                    producto = self.cursor.fetchone()
                    total = float(cant[i])*float(producto[1])
                    tmp = [int(prod), float(cant[i]), producto[0],
                           float(producto[1]), total]
                    self.ingreso(tmp)

    def abrirNota(self, ide, edicion=True):
        nota = None
        cliente = []
        msgBox = QtGui.QMessageBox(self)
        try:
            sql = "select cliente, nombre, rfc, C.tipo  from notas as N, clientes as C where  N.`id`=%s  AND C.id=N.cliente ;" % ide
            #print sql
            self.curser.execute(sql)
            cliente = self.curser.fetchone()
        except MySQLdb.Error, e:
            msgBox.setText("No se pudo abrir la nota.")
            msgBox.setInformativeText(str(e))
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            ret = msgBox.exec_()
        else:
            if cliente != None:
                cliente = dicursor(self.curser, cliente)
                if edicion:
                    self.limpiar()
                    self.banderas['edicion'] = str(ide)
                else:
                    self.banderas['edicion'] = False
                self.banderas['tipo'] = 'v'
                self.cliente['id'] = cliente['cliente']
                self.cliente['tipo'] = cliente['tipo']
                self.cliente['nombre'] = cliente['nombre']
                self.csCliente.setText(self.cliente['nombre'])
                self.nota = str(ide)
                self.curser.execute(
                    "SELECT ref,`descripcion`,precio,cantidad, V.total as total, unidades.nombre as unidad FROM notas as N, unidades, vendidos as V, productos as P where V.venta=N.id AND P.ref=V.producto AND unidades.id=unidad and N.id=%s ;" % ide)
                notas = self.curser.fetchall()
                if notas != None:
                    notas = dicursor(self.curser, notas)
                    for nota in notas:
                        total = float(nota['cantidad'])*float(nota['precio'])
                        tmp = [nota['ref'], float(nota['cantidad']), str(nota['descripcion']), float(
                            nota['precio']), total, nota['total'], [], [], nota['unidad']]
                        self.ingreso(tmp)
                    self.logo.setText("Edicion de venta")
                    return True
            else:
                msgBox.setText("No se puede abrir la nota.")
                msgBox.setInformativeText(
                    "Problema con la informacion del cliente.")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                ret = msgBox.exec_()
                return False

    def abrirCompra(self, ide, edicion=True):
        # Abrir Compra
        nota = None
        msgBox = QtGui.QMessageBox(self)
        try:
            restrict = " "
            if edicion:
                restrict = " AND DATE(fecha)='{0}' ;".format(self.hoy)
            sql = "SELECT id,proveedor FROM compras WHERE id=%s %s" % (
                ide, restrict)
            #print sql
            self.cursor.execute(sql)
            compra = self.cursor.fetchone()
        except MySQLdb.Error, e:
            msgBox.setText("Error en la base de datos.")
            msgBox.setInformativeText(str(e))
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        else:
            if compra == None:
                msgBox.setText("Error.")
                msgBox.setInformativeText(
                    "No se puede editar notas de dias anteriores.")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.exec_()
            else:
                if edicion:
                    self.limpiar()
                    self.banderas['edicion'] = str(ide)
                else:
                    self.banderas['edicion'] = False
                self.banderas['tipo'] = 'c'
                sql = "SELECT ref,`descripcion`,precio,cantidad, CC.total as total,P.costo as costo  FROM compras as C, comprados as CC, productos as P where CC.compra=C.id AND ref=CC.producto AND  C.id=%s ;" % ide
                #print sql
                self.curser.execute(sql)
                notas = self.curser.fetchall()
                self.cliente['id'] = int(compra[1])
                self.csCliente.setText("%s" % self.cliente['id'])
                if notas != None:
                    notas = dicursor(self.curser, notas)
                    for nota in notas:
                        total = float(nota['cantidad'])*float(nota['precio'])
                        tmp = [nota['ref'], float(nota['cantidad']), str(nota['descripcion']), float(
                            nota['precio']), total, nota['total'], 0, nota['costo']]
                        self.ingreso(tmp)
                    self.logo.setText("Edicion de compra")
                    return True

    def eliminarCompra(self, compra=-1):
        dlg = False
        if self.aut(2) > 0:
            if compra == -1:
                dlg = QtGui.QInputDialog.getInteger(self, self.tr(
                    "Cancelar Compra"), self.tr("Ingrese el numero de compra."))
                compra = dlg[0]
            if (dlg != False and dlg[1]) or (dlg == False and compra > 0):
                return self.modulos['cventa'].eliminarCompra(compra)

    def cancelNota(self):
            # msgBox=QMessageBox()
            #msgBox.setText("Se cancelara la nota <b>"+str(self.nota)+"</b> ")
            #msgBox.setInformativeText("Desea eliminar permanentemente la nota?")
            #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # ret=msgBox.exec_()
        if self.aut(2) > 0:
            nota = QtGui.QInputDialog.getInteger(self, self.tr(
                "Cancelar nota"), self.tr("Ingrese el numero de nota."))
            if nota[1]:
                try:
                    self.cursor.execute(
                        """UPDATE existencia as e, vendidos as v SET stock_logico=stock_logico+cantidad WHERE e.producto=v.producto and venta=%s;""" % nota[0])
                    self.cursor.execute(
                        "DELETE FROM vendidos WHERE venta=%s " % nota[0])
                    self.cursor.execute(
                        "DELETE FROM notas where `id`="+str(nota[0]))
                except MySQLdb.Error, e:
                    print e
                else:
                    self.cursor.execute("COMMIT")

    def seleccionarFilas(self, tabla, modelo):  # regresa las filas seleccionadas
        refs = []
        lista = tabla.selectedIndexes()
        lastrow = -1
        for li in lista:
            if (li.row() != lastrow):
                lastrow = li.row()
                refs.append(str(modelo.getFila(li)))
        return refs

    def delete(self):
        if len(self.basket) > 0:
            ref = self.canasta.getCell(self.tabla.selectedIndexes()[0], 0)
            print ref
            for item in self.basket:
                if int(ref) == int(item[0]):
                    self.basket.remove(item)
            self.verCanasta()
            self.grant()

            # lista=self.tabla.selectedIndexes()
            # for index in lista:
            # if self.canasta.removeRow(index.row()):
            # self.basket=self.canasta.getVector()
            # self.grant()

    def abrirCajon(self):
        if self.aut(2) > 0:
            ticket = "<cajon>"
            if sys.platform == 'linux2':
                f = tempfile.NamedTemporaryFile(delete=False)
            else:
                f = open(os.path.normpath(
                    os.path.join(self.home, "tmp.txt")), "w+")
            tags = self.ticketDriver.etiquetas
            for key, item in tags.iteritems():
                ticket = ticket.replace(key, item)
            f.write(ticket)
            f.close()
            self.imprimir(f, self.cfg.get('ticket', 'impresora'))
            os.unlink(f.name)

    def imprimir(self, archivo, impresora):
        if self.cfg.get('ticket', 'formato') == "ps":
            self.imprimirPs(archivo, impresora)
        else:
            if sys.platform == 'linux2':
                try:
                    os.system("lp  %s -d \"%s\" " % (archivo.name, impresora))
                    #os.system("echo  %s "%(archivo.name))
                except:
                    print 'No fue posible imprimir'
            else:
                f = open(archivo.name, "r+")
                ticket = f.read()
                f.close()
                defprt = win32print.GetDefaultPrinter()
                prt = win32print.OpenPrinter(defprt)
                win32print.StartDocPrinter(prt, 1, ("Ticket", None, None))
                win32print.WritePrinter(prt, ticket)  # CRLF+FF
                win32print.EndDocPrinter(prt)
                win32print.ClosePrinter(prt)

    def imprimirPs(self, archivo, impresora):
        f = open(archivo.name, "r+")
        ticket = f.read()
        f.close()
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setPaperSize(QtGui.QPrinter.A7)
        # printer.setOutputFormat(2)
        # printer.setOutputFileName("/tmp/ticket.ps")
        printer.setFullPage(True)
        printer.setOrientation(0)
        printer.setPrinterName(impresora)
        printer.setPageMargins(0, 0, 0, 0, 0)
        tedit = QtGui.QTextEdit(QtCore.QString(ticket))
        tedit.print_(printer)

    def imprimirTicket(self, extraTags={}):

        # try:
        f = open(os.path.join(home, 'ticket.xml'), 'r+')
        ticline = f.readlines()  # Lee el archivo en lineas y lo guarda en un arreglo
        # ticline=ticket.split('\n')
        f.close()
        try:
            tags = self.ticketDriver.etiquetas  # carga las etiquetas del driver esc/pos
        except:
            tags = {}
        prd = ''
        prods = ''
        # |Para el caso de manejar la edicion individual de los datos de los productos
        dataf = ['', '']
        for i, linea in enumerate(ticline):
            #print linea
            if linea.find("<importe/>") >= 0 or linea.find("<idesc/>") >= 0:
                # En la linea donde encuentre el importe lo toma como la segunda linea
                dataf[1] = linea
                ticline.remove(linea)
            if linea.find("<producto/>") >= 0:
                # En la linea donde encuentre la etiqueta producto lo toma como la primera linea
                dataf[0] = linea
                ticline[i] = "<producto/>"
        ticket = ''.join(ticline)
        # Aqui es donde el ticket se convierte en una sola cadena
#['Ref','Ctd','Descripcion del producto','Precio','Importe','C/Dcto']
        for prod in self.basket:  # por cada articulos de la canasta va llenando de acuerdo al formato de dataf
            if prod[1] > 0:
                microtags = {'<cantidad/>': str(libutil.cifra(prod[1])), '<producto/>': str(prod[2]), '<precio/>': str(libutil.cifra(prod[3])), "<importe/>": str(
                    libutil.cifra(prod[4])), "<ref/>": str(prod[0]), "<idesc/>": str(libutil.cifra(prod[5])), "<pdesc/>": str(libutil.cifra(prod[5]/prod[1]))}
                disc = prod[5]-prod[4]
                if disc != 0:
                    microtags['<descontado/>'] = str(libutil.cifra(disc))
                # "lineas" guarda de manera temporal una copia de los formatos esta sera modificada con los datos
                lineas = [dataf[0], dataf[1]]
                for key, item in microtags.iteritems():  # Se reemplazan las etiquetas por los datos de cada producto
                    lineas[0] = lineas[0].replace(key, item)
                    lineas[1] = lineas[1].replace(key, item)
                prods += ''.join(lineas)
                prd += "#%s | %s\n %s\t*\t $%s \t\t= \t$%s\n" % (
                    str(prod[0]), str(prod[2]), str(prod[1]), str(prod[3]), str(prod[4]))
        #print prods
        tags['<cantidad/>'] = ''
        tags['<precio/>'] = ''
        tags['<importe/>'] = ''
        tags['<idesc/>'] = ''
        tags['<pdesc/>'] = ''
        tags['<ref/>'] = ''
        tags['<numero-productos/>'] = str(len(self.basket))
        tags['<productos/>'] = prd
        tags['<producto/>'] = prods
        tags['<subtotal/>'] = str(libutil.cifra(self.grant()[0]))
        tags['<impuestos/>'] = ''  # self.cfg.get('empresa','impuestos')+"%"
        tags['<descuento/>'] = str(libutil.cifra(self.grant()[1]))
        tags['<total/>'] = str(libutil.cifra(self.grant()[2]))
        tags['<fecha/>'] = str(self.fecha)
        tags['<nota/>'] = str(self.nota)
        tags['<tletra>'] = str(nletras(self.grant()[2]))
        tags['<usuario/>'] = self.sesion['usuario']['nombre']

        for key in self.modulos['config'].modulos['empresa']:
            try:
                tags['<'+key+'/>'] = self.cfg.get('empresa', key)
            except:
                pass
        for key, item in extraTags.iteritems():
            ticket = ticket.replace(key, item)
        for key, item in tags.iteritems():
            ticket = ticket.replace(key, item)
        for key, item in tags.iteritems():
            ticket = ticket.replace(key, item)
        if sys.platform == 'linux2':
            f = tempfile.NamedTemporaryFile(delete=False)
        else:
            f = open(os.path.normpath(os.path.join(self.home, "tmp.txt")), "w+")
        #print ticket
        f.write(ticket)
        f.close()
        #print ticket
        self.imprimir(f, self.cfg.get('ticket', 'impresora'))
        os.unlink(f.name)

    def autDescuento(self):
        if self.aut(2) > 0:
            dsc = QtGui.QInputDialog.getDouble(self, self.tr("Autorizar descuento"), self.tr(
                "Escriba el porcentaje de descuento que se aplicara"))
            dsc = dsc[0]
            if dsc > 50:
                msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, "El porcentaje de descuento es muy alto.<br> Desea continuar? ",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, self, Qt.WindowStaysOnTopHint)
                ret = msgBox.exec_()
                if ret != QtGui.QMessageBox.Yes:
                    return

            ls = []
            for prod in self.basket:
                prod[5] = float(prod[4])-(float(prod[4])*(dsc*0.01))
                ls.append(prod)
            self.basket = ls
            self.verCanasta()
            self.Promo.setText("Descuento aplicado.")
            self.grant()

    def openf(self):
        openFile = QFileDialog.getOpenFileNames(
            self, "Selecciona un archivo de nota", home, "Notas (*.pv)")
        if (openFile != ""):
            print openFile[0]
            out = open(openFile[0], "r")
            l = []
            for item in out:
                l.append(item)
            items = l[3].split(',')
            for prod in items:
                p = prod.split(":")
                try:
                    self.cursor.execute(
                        "SELECT `ref`,`descripcion`,`precio` FROM productos WHERE `ref`="+p[0])
                    rec = self.cursor.fetchone()
                except:
                    print "No existe el producto"
                else:
                    tmp = [rec[0], p[1], rec[1], rec[2],
                           (float(p[1])*float(rec[2]))]
                    self.ingreso(tmp)
            out.close()

    def savef(self):
        # Guarda en un archivo la nota, pero no la asienta en la base de dtos
        File = QtGui.QFileDialog()
        saveFile = File.getSaveFileName(
            self, "Guardar nota", os.path.expanduser("~"), "Notas (*.pv)")
        if (saveFile != ""):
            print "Guardando..."
            out = open(saveFile+".pv", "w")
            out.write(str(self.cliente['id'])+'\n')
            out.write(str(self.fecha)+'\n')
            # out.write(str(self.tipo)+'\n')
            for aux in self.basket:
                print aux[0]
                out.write(str(aux[0])+':'+str(aux[1])+',')
            out.write('\n'+str(self.grant()[2]))
            out.close()

    def presupuestar1(self):
        print "Creando presupuesto.."
        campos = {'titulo': 'Presupuesto', 'fecha': self.fecha}
        for key in self.modulos['config'].modulos['empresa']:
            try:
                campos["{%s}" % key] = self.cfg.get('empresa', key)
            except:
                pass
        gt = self.grant()
        campos['{descripciones}'] = ''
        campos['{cantidades}'] = ''
        campos['{precios}'] = ''
        campos['{importes}'] = ''
        campos['{unidades}'] = ''
        nl = "<br/>"
        filas = ""
        for item in self.basket:
            filas += """
	  <table:table-row table:style-name="tabla.3">
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" >
      <text:p text:style-name="P43">{0} {2}</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" >
      <text:p text:style-name="P44">{1}</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" >
      <text:p text:style-name="P44">{8}</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" >
      <text:p text:style-name="P44">{3}</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.E3" office:value-type="string" >
      <text:p text:style-name="P44">{4}</text:p>
     </table:table-cell>
    </table:table-row>\n
    """.format(*item)

        campos['{total}'] = str(gt[2])
        campos['{fecha}'] = str(self.fecha)
        campos['{cliente}'] = self.cliente['nombre']
        new = "/tmp/presupuesto.fodt"
        doc = open("perfil/formas/presupuesto.fodt", "r")
        tmp = open(new, "w")
        body = doc.read()
        tabla = """<table:table-row table:style-name="tabla.3">
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" table:protected="true">
      <text:p text:style-name="P43">Descripcion del producto</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" table:protected="true">
      <text:p text:style-name="P44">000,000.00 </text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" table:protected="true">
      <text:p text:style-name="P44">PIEZA</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.A3" office:value-type="string" table:protected="true">
      <text:p text:style-name="P44">$000,000.00</text:p>
     </table:table-cell>
     <table:table-cell table:style-name="tabla.E3" office:value-type="string" table:protected="true">
      <text:p text:style-name="P44">$000,000.00</text:p>
     </table:table-cell>
    </table:table-row>"""
        body = body.replace(tabla, filas)
        for key, item in campos.iteritems():
            body = body.replace(key, item)
        tmp.write(body)
        doc.close()
        tmp.close()
        if sys.platform == 'linux2':
            os.system("gnome-open '%s' " % new)
        else:
            os.startfile(new)

    def presupuestar(self):
        print "Creando presupuesto.."
        campos = {'titulo': 'Presupuesto', 'fecha': self.fecha}
        for key in self.modulos['config'].modulos['empresa']:
            try:
                campos[key] = self.cfg.get('empresa', key)
            except:
                pass
        #print campos['%logo%']
        campos['%ref%'] = ''
        campos['%prods%'] = ''
        campos['%cantidad%'] = ''
        campos['%precio%'] = ''
        campos['%importe%'] = ''
        campos['%desc%'] = ''
        for item in self.basket:
            campos['%ref%'] += "%s <br>" % item[0]
            campos['%prods%'] += "%s <br>" % item[2]
            campos['%cantidad%'] += "%s <br>" % item[1]
            campos['%precio%'] += "%s <br>" % item[3]
            campos['%importe%'] += "%s <br>" % item[4]
            campos['%desc%'] += "%s <br>" % item[5]
        gt = self.grant()
        campos['sub'] = str(gt[0])
        campos['descuento'] = str(gt[1])
        campos['total'] = str(gt[2])
        campos['nletra'] = str(nletras(gt[2]))

        html = listaHtml(self.basket, titulo="Lista de productos", cabezas='Ref,Cantd,Descripcion del Producto,Precio,Importe,Subtotal', fondo='#000',
                         css="table, tr, td, th{border:0px;border:0px solid #000}, table, tr{width:100%;align:center; margin:auto;} hr{border:1px solid #bbb} ", anchos=[10, 10, 45, 10, 10, 15])
        campos['%tabla%'] = html
        head = """<table border="0" width="100%" cellspacing="5px" cellpadding="5px">
		<tr valign='top'>
			<td width="50%"><img src="{logo}" align="left" valign="top" style="float:left;margin-right:20px;display:inline" />
			    <span style=" font-size:large; font-weight:800; 
			    color:#222;">{nombre}</span><br/>
			    <span>{slogan}</span></td>
		  <td width="25%" style="font-size:80%"></td>
		  <td width=25%>
		  <span style=" font-size:xx-large; font-weight:800; color:#294e5e;">Presupuesto</span><br/>
		  <span style=" font-size:normal; font-weight:600; color:#294e5e;">Fecha: {fecha}</span></td></tr></table>	""".format(**campos)
        foot = """<hr/><table border="0" width="100%" cellspacing="5px" cellpadding="5px">
			<tr><td rowspan="3" width="70%" valign="middle">{nletra}</td>
			    <td style="font-size:large; font-weight:600;">Subtotal:</td>
			    <td style="font-size:large; font-weight:600;" align="right">{sub}</td>
			</tr><tr>
			  <td style="font-size:large; font-weight:600;">Descuento:</td>
			  <td style="font-size:large; font-weight:600;" align="right">{descuento}</td>
			</tr><tr>
			  <td style="font-size:large; font-weight:600;">Total:</td>
			  <td style="font-size:large; font-weight:600;"align="right">{total}</td>
			</tr>
			</table>
			<hr align="center"/>
			<p style="font-size:10px; color:#999;text-align:center" align="center">{nombre}, {slogan}<br/>{direccion} {ciudad}, C.P {cp}<br>{email} Tel: {telefono}<br/>{pagina}</p>
			""".format(**campos)
        printa(head+html+foot, "Presupuesto", self)
        #print head+html+foot
        # doc=Documento(self,os.path.join("perfil","formas","presupuesto.html"),campos)
        # doc.guardarPDF()

    def cerrarFactura(self):
        self.banderas['tipo'] = 'f'
        self.modulos["cventa"].ver()
        ##F=Factura(self, 14)
        # F.imprimir()
        # self.modulos["cventa"].facturar()
        # if (self.modulos["cventa"].checkCliente()):
        # self.facturar(self.modulos["cventa"].allocate(1,0))
        # self.limpiar()

    def facturar(self, id):
        F = Factura(self, id)
        F.imprimir()

    def ticketPrev(self):
        self.cvticket.setHtml(self.ceticket.toPlainText())

    def selCliente(self):
        tipo = 0
        titulo = "Cliente"
        if self.banderas['tipo'] == 'c':
            tipo = 1
            titulo = "Proveedor"
            print "Seleccionando proveedor"
        app = Selector(self, titulo, 'clientes', 'id,nombre,rfc', 'Id,Nombre ,RFC',
                       "(`nombre` like '%{0}%' or `rfc` like '{0}%') order by nombre desc ")
        done = app.exec_()
        if done == 1:
            cliente = app.retorno[0]
            self.cliente = {'id': str(cliente[0]), 'nombre': str(
                cliente[1]), 'rfc': str(cliente[2])}
            self.csCliente.setText(self.cliente['nombre'])
            self.csCliente.setToolTip(self.cliente['nombre'])
            return app.retorno[0][0]
        else:
            return -1
        # self.lista2.horizontalHeader().setResizeMode(0,1)

    def cerrarSesion(self):
        self.sesion['usuario'] = {
            'nombre': 'Mostrador', 'nivel': 0, 'id_usuario': 1, 'usuario': 'Mostrador'}

    def iniciarSesion(self):
        self.cerrarSesion()
        dlg = Seguridad(self)
        acceso = dlg.exec_()
        if acceso > -1:
            self.sesion['usuario'] = dlg.usuario
            self.cursor = dlg.cursor
            self.curser = dlg.curser

    # def queryTable(self):
        #print self.dbm.open()

        # model=QtSql.QSqlQueryModel(self)
        #model.setQuery("select descripcion, costo from productos limit 10,10;")
        # self.lista2.setModel(model)
        # return QtSql.QSqlQueryModel(self)
    def verCanasta(self):
        # if len(self.basket)<=0:
        head = ['Ref', 'Ctd', 'Descripcion del producto',
                'Precio', 'Importe', 'c/Dcto']
        if self.canasta == None:
            # hacemos un recorte para mostrar solo 6 columnas
            tmp = [l[:6] for l in self.basket]
            self.canasta = MyTableModel(tmp, head, self)
            self.tabla.setModel(self.canasta)
            font = QtGui.QFont("Monospace", 12)
            self.tabla.setFont(font)
        else:
            self.canasta.setVector([l[:6] for l in self.basket])
        self.tabla.resizeColumnsToContents()

    def entabla(self, tabla, header, query, modelo=None):
        sql = str(query)
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
        except:
            print "Problema al ejecutar el query"
        else:
            if lista != None:
                if modelo == None:
                    modelo = MyTableModel(lista, header, self)
                    tabla.setModel(modelo)
                else:
                    modelo.setVector(lista)
                # tabla.resizeColumnsToContents()
        return modelo

    def marcarFalta(self):
        refs = libutil.seleccionar(self.lista2, self.moli2, 0)
        lis = Faltante(self, refs, self.sesion['usuario']['id_usuario'])
        lis.exec_()

    def swap(self):
        if self.aut(2) > 0:
            aw = Swaproductos(self)
            aw.exec_()

    def ocm2(self, point):
        self.popLista2.exec_(self.lista2.mapToGlobal(point))

    def _buscar(self, texto):
        try:
            self.current.buscar(str(texto))
        except:
            pass

    def closeEvent(self, event):
        self.conexion.commit()
        self.conexion.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.processEvents()
    QtCore.QLocale.setDefault(QtCore.QLocale(111, 139))
    aw = Pyventa()
    aw.show()
    app.exec_()

    #app = QtGui.QApplication(sys.argv)
    # Create and display the splash screen
    #splash_pix = QtGui.QPixmap('/usr/share/pyventa/images/splash.png')
    #splash = QSplashScreen(splash_pix, Qt.SplashScreen)
    # splash.setMask(splash_pix.mask())
    # splash.show()
    #splash.showMessage("Cargando modulos...",1,Qt.white)
    # app.processEvents()
    # Simulate something that takes time
    # time.sleep(2)
    #aw = Pyventa()
    # aw.show()
    # splash.finish(aw)
    # app.exec_()

    #app = QtGui.QApplication(sys.argv)
    # app.processEvents()
    #aw = ingreso()
    # aw.show()

    # sys.exit(app.exec_())
