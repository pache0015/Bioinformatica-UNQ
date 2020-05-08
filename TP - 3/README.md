# Bioinformatica-UNQ

## Tp 3 - 

PARA PENSAR: ¿A qué se refiere el texto con la frase “los genes “informacionales”
tienen su origen en el reino archaea, mientras que los genes “operacionales” tienen
su origen en el reino bacteria”?


### RETO I: Enumerá las diferencias que existen entre una célula procariota y eucariota.

  Para empezar, las células procariotas son más antiguas que las eucariotas. Además en las Procariotas el material genético no está separado del citoplasma y los Eucariotas presentan el material genético está organizado en cromosomas rodeados por una membrana que los separa del citoplasma.
  
  | Procariotas   |      Eucariotas      |
|:----------:|:-------------:|
| Más antiguas | Menos antiguas |
| ADN localizado en una región: Nucleoide, no rodeada por una membrana.  |  Núcleo rodeado por una membrana. Material genético fragmentado en cromosomas formados por ADN y proteínas.  |
| Escasas formas multicelulares. Ausencia de desarrollo de tejidos |    Por lo general células grandes, (10-100 µm). Algunos son microbios, la mayoría son organismos grandes.   |
| Ausencia de mitocondrias: las enzimas para la oxidación de moléculas orgánicas están ligadas a las membranas | División celular por mitosis, presenta huso mitótico, o alguna forma de ordenación de microtúbulos. |
| Flagelos simples formados por la proteína flagelina | Los organismos multicelulares muestran desarrollo de tejidos |
| En especies fotosintéticas, las enzimas necesarias están ligadas a las membranas. Exitencia de fotosíntesis aerobia y anaerobia, con productos finales como azufre, sulfato y Oxígeno | Las enzimas están en las mitocondrias |


PARA PENSAR: ¿Cuáles de los pasos descritos anteriormente deberías cambiar si
habláramos de células procariotas? 🤔


### RETO II: Dado el código genético como se muestra en la tabla crea un programa sencillo en algún lenguaje de programación que conozcas que imprima una cadena de ARN codificante para el siguiente péptido (cadena corta de aminoácidos).

**Sec1: ‘ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'**

Para este reto se ha elegido implementar la resolucion del mismo en el lenguaje de Programacion Haskell, dado la eficiencia de los programas funcionales. Ver archivo [TP-3.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%203/tp3.hs).

`transform :: Peptido -> CadenaARN`

Que toma una cadena de String que representa un Peptido y devuelve una cadena de bases de ARN.
Aclaracion: Es importante aclarar que la misma es una aproximacion, dado que en la resolucion del mismo nos dimos cuenta que no hay forma deterministica de hacer la codificacion, dado que al existir varias combinaciones de bases nitrogenadas que se traducen en el mismo  aminoácido, resulta imposible determinar exactamente cual fue la combinacion original que decanto para el mismo. Ver archivo TP3.hs (Falta link)

### RETO III: En muchos de los genes codificados en el ADN existe un motivo recurrente ubicado antes de la secuencia codificante del gen que direcciona la unión de la ARN Polimerasa II, la proteína encargada de copiar el ADN a un ARN mensajero. Ésta secuencia denominada caja TATA (consistente en una secuencia de nucleótidos 'TATAAA') se encuentra presente en lo que se denomina región promotora de diversos genes, en organismos de todos los reinos (Smale and Kadonaga 2003; Lifton et al. 1978).

#### 👉 Crea un programa sencillo en algún lenguaje de programación que conozcas que permita identificar las regiones promotoras de un gen, en una secuencia dada de ADN, considerando que tal región comienza y termina en con la caja TATA.

Nuevamente utilizando Haskell como lenguaje de programacion se ha propuesto para la resolucion de este reto la siguiente funcion:

`buscarTATA :: String -> String`

Que dada una secuencia de ADN, devuelve las regiones promotoras de un gen, entre la caja TATA del principio y del final.
Ver archivo [TP-3.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%203/tp3.hs).

Como bonus track agregamos la siguiente función:

`buscarTATAS :: String -> String`

Que dada una secuencia de ADN, devuelve **TODAS** las regiones promotoras de un gen.


### RETO VI: Existen numerosas herramientas muy fáciles de usar que te permiten crear videojuegos, como por ejemplo Pilas Engine, y no hay mejor modo de aprender que jugando!

#### 👉 Diseñá un juego de mesa o un videojuego (hecho con la herramienta que más te guste) temático sobre expresión génica, con sus reglas y resúmen. Tené en cuenta que lo vas a tener que compartir con la clase. ¡El cielo es límite, a divertirse!

Ver carpeta [TP-3.hs](https://github.com/pache0015/Bioinformatica-UNQ/tree/master/TP%20-%203/Videojuego/AminoGame
)
