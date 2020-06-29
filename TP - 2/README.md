# Bioinformatica-UNQ

## Tp 2 - 

#### Integrantes Tp2: ####

*Facundo Pacheco

*Horacio Valenzuela

### ¿Qué información nos provee esta página?
 
 Es una base de datos que nuclea información de la estructura de las proteínas que han sido cristalizadas.
 
### ¿Cómo se determinó la estructura de esta proteina?

 La estructura de una proteína se determina en la actualidad por diferentes métodos en los cuales se obtienen una serie de datos que el científico utiliza para crear el modelo atómico final. Entre ellos citaremos:
  + La cristalografía de rayos-X: genera un modelo de difracción de rayos X
  + La espectroscopía de resonancia magnética nuclear (NMR): aporta información sobre la conformación local y distancia entre átomos próximos entre sí
  + La microscopía electrónica: ofrece una imagen de la forma completa de la molécula.

### Representa esa imagen a la realidad del sistema biológico?

No. Esto se debe a que las proteínas están en movimiento constantemente y puede tomar otras formas.

### Este es el error asociado al experimento: Mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo. ¿Cuál es la utilidad y los condicionamientos de usar un modelo científixo que sabemos inexacto?

 Entendiendo a resolución como la capacidad que se tiene para determinar o distinguir lo que hay entre dos puntos cercanos. A más cercanía mejor apreciación. Los medios actuales hacen que por el momento se utilice este medio, dado una limitación tecnológica, pero de todas formas sigue siendo de gran utilidad ya que aporta una representación para poder tener una idea de la forma de la proteína. 
 
### En la pantalla principal vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas?

 Son las formas de representaición de la estructura secundaria de cada aminoácido. Pueden ser Alpha Hélice, Beta Plegada o Loop.

### ¿Qué diferencias y similitudes notamos respecto de la representación inicial?

 Que este tipo de estructura representa la proteina en función del espacio. Es decir, Esto es una representación gráfica de la proteína en el espacio, en cambio la inicial no. Las similitudes son que ambas representan a la misma proteína, su representación no cambia.

 
### En el menú de la izquierda hay opciones de distintos tipos de representación y formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?

 Para entender y estudiar las dintintas formas que tiene la proteína. Esto irá en función de lo que querramos estudiar. Si estamos viendo la proteína solo a nivel estructural la imágen principal servirá. Pero si queremos ver cómo se puede acoplar esta proteina con otras o incluso con alguna droga, esta vista estructural no será suficiente.

### ¿Qué información esperaría encontrar como resultado un experimento destinado a determinar la estructura terciaria de una molécula biológica?
Esperaría obtener las coordenadas para poder armar la estructura de la molécula.

### Podemos explorar el contenido del archivo que acabamos de descargar si lo observamos con un editor de texto. Haciendo clic con el botón derecho del mouse sobre el archivo descargado, usemos la opción Abrir con y seleccionemos el Bloc de Notas u otro editor de texto. ¿En qué consiste un archivo PDB?

Un archivo .PDB consiste  la información y las coordenadas de los atomos de una proteína. 

### Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección?

La sección ATOM brinda la información de cada átomo que compone la molécula, como podria ser, por ejemplo, las coordenadas para poder graficarla.

### ¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional:¿de qué tipo de dato se trata esta información?

Si, cada línea de ATOM tiene el átomo y además el aminoácido del cual forma parte. Se representa como una cadena de 3 caracteres que referencian a los aminoácidos los cuales son compuestos por varias líneas de átomos. Por Ejemplo, MET, GLN, ILE. Entonces, desde el punto de vista computacional, esta información se resepresenta mediante cadenas de caracteres como tipo de dato.

### ¿Considera que el formato PDB es útil para presentar los resultados del experimento?
El formato PDB es útil ya que esta armado precisamente para ser exportado a otras aplicaciones que lo puedan consumir.

### Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento?
Los beneficios son la facilidad para poder migrar la información de un sistema a otro solo pasando un "único" archivo. Las limitaciones inherentes que se presentan es justamente es la estructura del archivo, y que no se puede salir de esa estructura para que sea útil. Además de su dificultad para poder ser interpretado por una persona (dado que no es cómodo de leer).

### Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?
Ya que al parecer hay una convención para guardar los archivos con este formato en particular, se tiende a pensar que si.

### Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso a punto Rosalind.
