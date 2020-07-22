# Introducción a la Bioinformática - TRABAJO PRÁCTICO FINAL
 
_El presente software representa una manera amigable para con el usuario de servir de asistencia al proceso del análisis bioinformático y/o herramienta educativa para la enseñanza de la Biología. Su función principal es la de aportar una interfaz sencilla, minimalista e intuitiva que permita  la visualización para estudios filogenéticos y filodinámicos de secuencias (puntualmente de secuencias proteicas). Este permite cargar un archivo .fasta, alinearlas de ser necesario, armar el árbol filiogenetico y marcar las geocoordenadas de donde se tomaron las mencionadas secuencias en un mapa interactivo. El objetivo del presente trabajo práctico es integrar los conceptos biológicos y bioinformáticos desarrollados durante la materia, transversalmente a los conocimientos, prácticas y habilidades propias de la informática y la programación adquiridas en otras materias de la carrera._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local. Empecemos por clonar el [repositorio](https://github.com/pache0015/Bioinformatica-UNQ). y dirigirnos a la carpeta *TP FINAL*._ 
Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Las *cosas* necesitas para instalar el software:_

- Python 3.x.y
- Pip3
- Geopy >= 2.0.0 
- Folium >= 0.11.0
- Biopython >= 1.77
- Cefpython3 >= 66.0
- Tkinter >= 8.6
- Anaconda >= 4.8.3
- [IQTree](https://www.iqtree.org/)
- [Crustal](http://www.clustal.org/omega/)


_Las instalamos localmente de la siguiente forma:

```
#Dependiendo la versión
sudo apt-get install python-pip3

!conda install -c etetoolkit ete3
!export PATH=~/anaconda_ete/bin:$PATH
!conda install -c bioconda iqtree
!conda install -c anaconda pillow
!apt-get install -y clustalo

#Mapa - librerias
!pip install geopy
!pip install folium
!pip install cefpython3
!pip install biopython

#Ventanas
!apt-get install -y python-tk

```

_Dentro de la carpeta **TP FINAL**, al correr la primer celda se instalan_ 

**Ojo**: _Si bien los pre-requisitos estan pensandos y documentados para servir en plataformas UNIX, si se instalaran tales librerias en Windows o en Mac OS, el programa es multiplataforma._


### Instalación 🔧

_Mas allá de lainstalación de los pre-requisitos, el proyecto no necesita de ninguna instalación previa. El mismo corre en el entorno de Jupyer Notebook. Para lo cual corremos el entorno_

```
source ~/anaconda3/bin/activate base
jupyter notebook
```

_Una vez dentro de */home/tu usuario/la carpeta donde clonaste el repositorio/ * , corre las 3 celdas y *voila*!_

## Despliegue 📦

_El archivo a cargar debe tener la extension .fasta exclusivamente. Para garantizar el correcto funcionamiento las secuencias proteicas deben tener el siguiente formato_

```
Numero | Ubicacion
Secuencia
```
_Por ejemplo, una secuencia correcta seria:_

```
>XP_024245566.1 | Buenos Aires
--MGDIEKGKKAFVQKCAQCHTVENGGKHKVGPNLWGLFGRKTGQAEGFSYTDANKAKGIVWDTDTLMTYLENPKKYIPGTKMIFAGIKKKGERADLIAYLKSATS-
```
Cualquier otro formato se considera **inválido**
Demás esta decir que la ubicacíon tiene que ser válida.


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [Python](https://www.python.org/) - Para el back-end (Utilizamos la version **3.6.8**).
- [Geopy](https://pypi.org/project/geopy/) - Para obtener los puntos desde la ubicación de la secuencia.
- [Folium](https://pypi.org/project/folium/) - Para renderizar el mapa.
- [Biopython](https://pypi.org/project/biopython/) - Para parsear la secuencia.
- [Cefpython3](https://pypi.org/project/cefpython3/) - Para realizar el navegador minimizado donde se renderiza el mapa.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Para el front-end.
- [Anaconda](https://www.anaconda.com/) - Para aprovechar el entorno.
- [IQTree](https://www.iqtree.org/) - Para realizar el árbol filigenetico.
- [Crustal](http://www.clustal.org/omega/) - Para alinear las secuencias


## Autores ✒️

_Integrantes del equipo:_

* [**Gonzalo Guasch**](https://github.com/GonzaloGuasch)
* [**Facundo Pacheco**](https://github.com/pache0015)
* [**Mariano Pais**](https://github.com/PaisMariano)
* [**Horacio Valenzuel**](https://github.com/UnderABloodySky)


## Licencia 📄

Este proyecto está bajo la Licencia GPLv3 - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓. edit: Aunque no vivimos de gracias (?) 
* Pedir por privado el CBU



---
⌨️ powered by NombrePendiente ❤️ 😊
