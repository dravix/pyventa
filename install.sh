#!/bin/bash


install_glob(){
echo "***********************************\n"
echo "* Instalacion generica de Pyventa.*\n"
echo "***********************************\n"
echo "Instalacion canonica"
if [[ $EUID -ne 0 ]]; then
   echo "Necesitas ser root para continuar" 
   exit 1
fi
WORKDIR=${1:-/usr/share/pyventa}
#Making directories
mkdir -p $WORKDIR &&
#remove all unused files
#find . -name ".py[a-z]" -print0 | xargs -0 rm -rf
cp -r {lib,ui,images,perfil,modulos,*.py,app.metadata} $WORKDIR &&
cp ./{pyventa,padmin} /usr/bin/ &&
chmod +x /usr/bin/{pyventa,padmin} &&
cp ./*.desktop /usr/share/applications/ 

}

install_local(){
echo "Instalacion local"
HP=$(readlink -f ~/pyventa)
WORKDIR=$(readlink -f ${1:-~/pyventa})
echo "WORKDIR: "$WORKDIR 
#Making directories
mkdir -p $WORKDIR && mkdir -p ~/bin
#remove all unused files
#find . -name ".py[a-z]" -print0 | xargs -0 rm -rf
cp -r {lib,ui,images,perfil,modulos} $WORKDIR &&
cp {pyventa.py,padmin.py,check.py,app.metadata} $WORKDIR &&
cp {pyventa,padmin} ~/bin/ &&
chmod +x ~/bin/{pyventa,padmin} &&
sed -i "s~/usr/share/pyventa/~$WORKDIR/~g" ~/bin/{pyventa,padmin}
cp *.desktop ~/.local/share/applications/ 
 }

configuration(){
	echo "Configurando..."
	cp -R -u -p perfil ~/.pyventa 	
}

install_deps(){
echo "Intentando instalar dependencias..."
if [ -f /etc/redhat-release ]; then
  sudo dnf install python2.7 python-mysqldb libqtcore4 python-qt4 python-cups
fi

if [ -f /etc/lsb-release ]; then
  sudo apt-get update &&
  sudo apt-get install python2.7 python-mysqldb libqtcore4 python-qt4
fi
}


while [ $# -gt 0 ]; do
  case "$1" in
    --dep*)
      install_deps
      ;;
    --all*)
      install_deps
      install_glob $2
      configuration
      ;;
    --local*)
      install_local $2
      configuration
      ;;   
    --glob*)
      install_glob $2
      configuration
      ;; 
    *)
      exit 1
  esac
  shift
done
