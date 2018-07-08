#!/bin/sh
BASE=$(pwd)
cd $BASE;
BUILDER="$BASE/../builder"
VERSION=$(zenity --width 200 --entry --title "Debianizando Pyventa" --text "Indica la version que sera publicada:" );
ov=$(cat $BUILDER/debian/changelog |awk -F '[()]' '{print $2}')
if [ "$(echo $ov" <= "$VERSION|bc)" -eq 1 ]; then 
	
	(
	echo "5" ;cp $BASE/*.py $BUILDER;cp $BASE/*.desktop $BUILDER;cp pyventa $BUILDER;cp padmin $BUILDER;cp pvcheck $BUILDER;cp images/pyventa.png $BUILDER;cp images/padmin.png $BUILDER; #cp $BASE/{pyventa.py,padmin.py,check.py,Checador.desktop,padmin.desktop,Pyventa.desktop,padmin,pyventa,pvcheck} $BUILDER; 
	echo "# Copiando las aplicaciones" ; sleep 1	
	echo "15" ; rsync -av --delete lib modulos ui perfil $BUILDER/;
	echo "# Copiando los archivos" ; sleep 1
	echo "20" ; rm -r -f $BUILDER/lib/*.py~ $BUILDER/lib/*.pyc $BUILDER/lib/*/*.py~ $BUILDER/lib/*/*.pyc $BUILDER/modulos/*.py~ $BUILDER/modulos/*.pyc $BUILDER/modulos/*/*.py~ $BUILDER/modulos/*/*.pyc  $BUILDER/ui/*.pyc $BUILDER/ui/*/*.pyc ;
	echo "# Cambiando al directorio $BUILDER" ; sleep 1
	echo "25" ; cd $BUILDER;
	echo "# Estableciendo version" ; sleep 1
	echo "30" ; sed -i 's/pyventa (.*)/pyventa ('$VERSION')/g' $BUILDER/debian/changelog;
	echo "# Compilando" ; sleep 1
	echo "75" ; dpkg-buildpackage -rfakeroot -us -uc
	echo "# Construccion completa" ; sleep 1
	echo "100" ; 
	) |
	zenity --progress \
	  title="Construyendo paquete deb" \
	  text="Recopilando informacion para la debianizacion..." \
	  percentage=0

	if [ "$?" = -1 ] ; then
		zenity --error \
		text="Construccion cancelada."
	fi

fi


