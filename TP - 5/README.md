Link :
https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo



👉 **PARA PENSAR: ¿Qué tipo de información se puede extraer de la comparación de secuencias? ¿Cómo esperás que se vea en una comparación? 🤔**

 -- El tipo de información que se puede extraer de la comparación de secuencias es aquella que permite:

- Determinar (y cuantificar) el grado de similitud que hay entre ellas
- Determinar si existe algún tipo de relación entre ellas (por ejemplo, si son homólogas) o si el parecido es simplemente fruto de la casualidad
- Detectar la presencia de motivos estructurales y/o funcionales conservados
- Construir árboles filogenéticos que reflejen sus relaciones evolutivas

La forma más habitual de comparar secuencias consiste en hacer un alineamiento.Esto consiste en escribirlas una encima de la otra de modo que el número de símbolos que coinciden en una misma posición sea máximo. Si es necesario, se pueden introducir huecos en cualquiera de las secuencias. Los huecos (gaps) introducidos en las secuencias también se denominan indels (insertion/deletion) ya que se pueden considerar, indistintamente, como la inserción de un residuo en una de las secuencias o como la desaparición (o deleción) de un residuo en otra. La comparación adopta esta forma de matriz, donde se intenta coincidir el Elemento Aij de una secuencia con el elemento Bij de la otra, tal como se puede apreciar en la siguiente imagen:

![comparacion - matriz](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/tabla5bio1.png)


👉 **PARA PENSAR: ¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas? 🤔**

-- Cabe destacar que la comparación de proteínas permite indicar genes en común, heredados de antepasados en común, dado dos (o más) muestras de especies distintas. De esto se desprende que el grado de similitud en las secuencias de aminoácidos indica el grado de la relación filogenética entre dichas especies. Un ejemplo claro es la comparación que se tuvo que hacer en el [TP nro. 4](https://github.com/pache0015/Bioinformatica-UNQ/tree/master/TP%20-%204), cuando comparábamos la muestra de **Citocroma C** proveniente de Humanos y Gallos, la cual es una proteína transportadora de electrones, común en todos los organismos aeróbicos, en una gran variedad de especies. Es mejor evaluar relaciones evolutivas lejanas comparando proteínas, dado que permite establecer hipótesis acerca de las relaciones evolutivas, entre un grupo de organismos, de forma más completa.
Además, cuando se hacen alineamientos de secuencias de ADN hay que tener en cuenta que:
- Los 4 nucleótidos aparecen con la misma frecuencia en las bases de datos.
- Todos los cambios posibles tienen una probabilidad similar.
- El proceso es lento porque las secuencias son largas.
- Para conseguir resultados significativos los alineamientos tienen que ser más largos.
- Se tiende a buscar la coincidencia exacta de los caracteres.

En cambio, los alineamientos de secuencias de proteínas son más sensibles, ya que: 

- Aportan más información (cada nucleótido aporta 2 bits, mientras que cada aminoácido más de 4) y, por lo tanto, se pueden obtener resultados significativos con alineamientos más cortos.
- Las búsquedas en bases de datos de proteínas son más rápidas (ya que no son tan grandes y carecen de secuencias no codificantes) 
- La probabilidad de sustituir un aminoácido por otro varía mucho, lo que aumenta la eficacia de las búsquedas


👇 **RETO I: Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema. Alineá en la siguiente table de comparaciones las palabras "BANANA" y "MANZANA".**



👇 **RETO II: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamitno que intentes.**



👇 **RETO III: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamitno que intentes y un botón para cambiar la penalidad que se le otorga a dicho para el cálculo de identidad.**



👉 **PARA PENSAR: Entonces, pensando en un alineamiento de ácidos nucleicos ¿Cuáles te parece que son las implicancias de abrir un gap en el alineamiento? ¿Qué implicaría la inserción o deleción de una región de más de un residuo?**

-- Debido a la naturaleza ternaria del código genético comprendido como una sucesión de codones; la inserción o deleción de un número de nucleótidos de una región de más de un residuo podría implicar que este no sea divisible por tres, lo que puede cambiar el marco de lectura del propio gen, provocando una traducción completamente diferente al de la original. Cuanto antes aparezca la inserción o deleción en el gen, mayor es la alteración que sufre la proteína.


👇 **RETO IV: En la siguiente tabla probá distintos alineamientos para las secuencias nucleotídicas. Podrás ver las traducciones para cada secuencia.**



👉 **PARA PENSAR: ¿Dá lo mismo si el gap que introducís cae en la primera, segunda o tercer posición del codón? ¿Cómo ponderarías las observaciones de este ejercicio para evaluar el parecido entre dos secuencias?**

![meme - STOP](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/meme.jpg)

-- La traducción del codón dependen del posicionamiento de las bases para determinar el aminoácido resultante. Un desplazamiento del marco de lectura puede, por lo general, conducir a que la lectura de los codones en la secuencia posterior a este termine en la codificación de aminoácidos distintos. El desplazamiento de marco también puede provocar la aparición, o desaparición, de un codón de terminación o **STOP** (UAA, UGA, o UAG) en una posición diferente de la secuencia original. El polipéptido creado resulta entonces anormalmente corto o demasiado largo, y en la mayor parte de los casos esto lo afectaría negativamente, haciendo que pierda su funcionalidad. 


👉 **PARA PENSAR: ¿En qué casos serán de utilidad uno u otro tipo de alineamientos? ¿Qué limitaciones tendrá cada uno?**
