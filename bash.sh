###
pyuic4 qt/ui_pyventa.ui -o ui/ui_pyventa.py
pyuic4 qt/ui_admin.ui -o ui/ui_admin.py
#modulos
pyuic4 qt/modulos/ui_ventas.ui -o ui/ui_ventas.py
pyuic4 qt/modulos/ui_reportes.ui -o ui/ui_reportes.py
pyuic4 qt/modulos/ui_config.ui -o ui/ui_config.py
pyuic4 qt/modulos/ui_caja.ui -o ui/ui_caja.py

#Dialogos
pyuic4 qt/dialogos/ui_agregar_deposito.ui -o ui/ui_agregar_deposito.py
pyuic4 qt/dialogos/ui_agregar_gasto.ui -o ui/ui_agregar_gasto.py
pyuic4 qt/dialogos/ui_cobrador.ui -o ui/ui_cobrador.py
