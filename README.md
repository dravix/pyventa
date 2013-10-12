Pyventa
=======

### Software para punto de venta.
Pyventa ofrece una serie de servicios administrativos para pequenas y medianas empresas.
Entre estos servicios esta el administrar el catalogo de productos, inventarios, cartera
de clientes, manejo de reportes de ventas, graficas de ventas, registro de entradas y 
salidas, impresion de tickets, manejo de conexiones remotas, cuentas de usuarios, 
maquetacion de cotizaciones usando fodt, manejo de precios especiales tales como ofertas.

### Instalacion de pyventa
Pyventa se distribuye atravez de [http://pyventa.com] y del repositorio oficial de launchpad
ppa:dravix/pyventa 

### Modo de empleo usando el codigo fuente
Considering that you are at the project root path
1. Set the default configuration 
      cp -r perfil/ ~/.pyventa
*  Edit the ~/.pyventa/config.cfg to use a test db
Check that the last line of the first module is like:
      motor=sqlite3
Then you can run one of the folowing scripts:
pyventa.py padmin.py y check.py



