Link :
https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo

link 2:
https://classroom.google.com/u/0/w/NTQ5MzQ3MDU2NzNa/t/all


👉 **PARA PENSAR: ¿Qué tipo de información se puede extraer de la comparación de secuencias? ¿Cómo esperás que se vea en una comparación? 🤔**

 -- El tipo de información que se puede extraer de la comparación de secuencias es aquella que permite:

- Determinar (y cuantificar) el grado de similitud que hay entre ellas
- Determinar si existe algún tipo de relación entre ellas (por ejemplo, si son homólogas) o si el parecido es simplemente fruto de la casualidad
- Detectar la presencia de motivos estructurales y/o funcionales conservados
- Construir árboles filogenéticos que reflejen sus relaciones evolutivas
En definitiva: Comparando secuencias se puede extraer similitudes existentees entre las cadenas dadas, determinar si las mismas son homólogas o no, si se pueden ver partes estructurales de las secuencias o determinar la relación entre ellas y en base a tales datos armar un árbol filogenético 

La forma más habitual de comparar secuencias consiste en hacer un alineamiento.Esto consiste en escribirlas una encima de la otra de modo que el número de símbolos que coinciden en una misma posición sea máximo. Si es necesario, se pueden introducir huecos en cualquiera de las secuencias. Los huecos (gaps) introducidos en las secuencias también se denominan indels (insertion/deletion) ya que se pueden considerar, indistintamente, como la inserción de un residuo en una de las secuencias o como la desaparición (o deleción) de un residuo en otra. La comparación adopta esta forma de matriz, donde se intenta coincidir el Elemento **A**ij de una secuencia con el elemento **B**ij de la otra, tal como se puede apreciar en la siguiente imagen:

![comparacion - matriz](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/tabla5bio1.png)

En una comparación se espera verlas alineadas. Buscando asi la mayor cantidad de coincidencias, para poder obtener resultados mas precisos en la comparación.

👉 **PARA PENSAR: ¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas? 🤔**

-- Es mejor evaluar las relaciones evolutivas lejanas comparando proteinas porque la base funcional de la proteína tienda a mantenerse a traves del tiempo y lo que se modifica son partes *no* fundamentales para su funcionamiento. Cabe destacar que la comparación de proteínas permite indicar genes en común, heredados de antepasados en común, dado dos (o más) muestras de especies distintas. De esto se desprende que el grado de similitud en las secuencias de aminoácidos indica el grado de la relación filogenética entre dichas especies. Un ejemplo claro es la comparación que se tuvo que hacer en el [TP nro. 4](https://github.com/pache0015/Bioinformatica-UNQ/tree/master/TP%20-%204), cuando comparábamos la muestra de **Citocroma C** proveniente de Humanos y Gallos, la cual es una proteína transportadora de electrones, común en todos los organismos aeróbicos, en una gran variedad de especies. Es mejor evaluar relaciones evolutivas lejanas comparando proteínas, dado que permite establecer hipótesis acerca de las relaciones evolutivas, entre un grupo de organismos, de forma más completa.
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
-- No existe una existe una única forma de alinear ambas seucencias. No tienen la misma cantidad de caracteres con lo cual se pueden hacer dos alineaciones posibles minimamente, por ejemplo agregados, deleciones o GAP. Con algunas alineaciones hay mayor coincidencia con menor insercion de GAPs, agregados o deleciones. Dos posibles alineamientos son los siguientes:

a)
![ali1](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali1.png)


b)
![ali2](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali2.png)


👇 **RETO II: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamitno que intentes.***
-- Se realizaron los alineamientos de ANA con ANANA como se puede apreciar en la siguiente imagen:

![ali2-1](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali2-1.png)

y se notó que por cada GAP que aparece en el alineamiento se pierden puntos de identidad. Si se agregan las letras faltantes a la palabra para que matcheen correctamente, la identidad da 1. Con lo cual cada discrepancia o cada letra faltante (reemplazada por GAP para la alineación) hacen que este disminuzca. 


👇 **RETO III: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamitno que intentes y un botón para cambiar la penalidad que se le otorga a dicho para el cálculo de identidad.**

![ali3-1](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali3-1.png)

La penalidad hace que al poner GAPS se descuente un porcentaje de la identidad, este (no)valor es mayor a que si tuviera otra “letra” que no matcheara EJ:

![ali3-2](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali3-2.png)

La palabra “ANAF” tiene un "score" mayor con respecto a “ANA” ya que se tuvo que ingresar menos cantidad de GAPs. A menor penalidad, menor es el porcentaje que se descuenta del valor de identidad cuando se debe ingresar GAPS.


👉 **PARA PENSAR: Entonces, pensando en un alineamiento de ácidos nucleicos ¿Cuáles te parece que son las implicancias de abrir un gap en el alineamiento? ¿Qué implicaría la inserción o deleción de una región de más de un residuo?**

-- Debido a la naturaleza ternaria del código genético comprendido como una sucesión de codones; la inserción o deleción de un número de nucleótidos de una región de más de un residuo podría implicar que este no sea divisible por tres, lo que puede cambiar el marco de lectura del propio gen, provocando una traducción completamente diferente al de la original. Cuanto antes aparezca la inserción o deleción en el gen, mayor es la alteración que sufre la proteína.


👇 **RETO IV: En la siguiente tabla probá distintos alineamientos para las secuencias nucleotídicas. Podrás ver las traducciones para cada secuencia.**

![ali4-1](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali4-1.png)

En este caso, lo que se puede apreciar es que en la alineación efectuada, no basta con dos nucleótidos para definir el aminoácido. Por más que se hayan alineado lo más posible no alcanza para determinarlo.

![ali4-2](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/ali4-2.png)

En este caso se puede apreciar que a la cadena hubo que modificarla mucho mas que en las ocasiones anteriores, corriendo a la derecha casi toda la cadena. Aún así no alcanza para determinar dos aminoácidos; y en el caso de la tercer cadena, no estando alineado, no se corresponde con el final de la segunda.


👉 **PARA PENSAR: ¿Dá lo mismo si el gap que introducís cae en la primera, segunda o tercer posición del codón? ¿Cómo ponderarías las observaciones de este ejercicio para evaluar el parecido entre dos secuencias?**

![meme - STOP](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%205/img/meme.jpg)

-- La traducción del codón dependen del posicionamiento de las bases para determinar el aminoácido resultante. Un desplazamiento del marco de lectura puede, por lo general, conducir a que la lectura de los codones en la secuencia posterior a este termine en la codificación de aminoácidos distintos. El desplazamiento de marco también puede provocar la aparición, o desaparición, de un codón de terminación o **STOP** (UAA, UGA, o UAG) en una posición diferente de la secuencia original. El polipéptido creado resulta entonces anormalmente corto o demasiado largo, y en la mayor parte de los casos esto lo afectaría negativamente, haciendo que pierda su funcionalidad. 


👉 **PARA PENSAR: ¿En qué casos serán de utilidad uno u otro tipo de alineamientos? ¿Qué limitaciones tendrá cada uno?**
El alineamiento global es más util cuando se comparan secuencias de tamaño y composición similar. Pero de ser muy secuancias muy distintas no dará el mejor resultado. Mientras que el local, siver más para comparar regiones específicas de las secuencias por si tienen tamaños muy distintos.


👉 **PARA PENSAR: Ingresá al servidor del NCBI y mirá los distintos programas derivados del BLAST que se ofrecen ¿Para qué sirve cada uno?¿En qué casos usarías cada uno?**
    -- Nucleotide BLAST --> a partir del fasta de una secuencia de nucleotidos busca porcentualmente  en la bd especificada las secuencias similares.
    -- Blastx --> Sintetiza una proteina a partir de la secuencia de nucleotidos
    -- tblastn --> A partir de una proteina devuelve la posinle secuencia de nucleotidos que lo forman
    -- Protein BLAST --> a partir del fasta de una proteina busca porcentualmente  en la bd especificada las secuencias similares.

👇 **RETO VII: calculá el E-value y % identidad utilizando el programa Blast de la siguiente secuencia input usando 20000 hits, un e-value de 100 y tomando aquellos hits con un mínimo de 70% cobertura. Observe y discuta el comportamiento de : E-value vs. % id, Score vs % id, Score vs E-value**

Secuencia: VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTV
TTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG

Estos valores están relacionados. Cuando varia uno varian también los otros dos. El e-value es nuestro valor de referencia para saber que tan certero es esa proteina en esa cadena, cuando menor sea el valor mas confianza nos transmite. Corriendo en blast la proteina que tiene el menor e-value también tiene el mayor score y porcentaje de identidad, es decir que era la misma proteína. De igual forma, hay varias secuencias que disminuye el e-value pero el porcentaje de identidad sigue siendo 100%, viendo esto entre el score para desempatar y así podemos ver cual es la proteina que comparada con toda esta base de datos es la mas cercana o directamente es la misma

👇 **RETO VIII: Realizá nuevas búsquedas usando la mitad de la secuencia problema y para un cuarto de la secuencia original. Compará los gráficos obtenidos.¿Qué conclusiones puede sacas?**

Al usar la mitad de la secuencia, cambiaron los valores. No solo el e-value mas confiable es mayor que el valor con la cadena original, sino que el valor maximo también es mucho menor, Estos cambios también se reflejan con el resultado ya que también cambio la proteína con un coverage del 100%, antes era "prion protein precursor [Homo sapiens]" ahora con la secuencia por la mitad es "Chain A, Major prion protein". Todos estos valores se ven también y mas agraviados cuando menor sea la longitud de la cadeana, con un cuarto de la misma el e-value paso de ser un valor negativo a ser 85 el max valu de casi 300 puntos a 23 pero la identidad como en los casos anteriores es 100% y da como resultado "biotin--[acetyl-CoA-carboxylase] ligase [Halorubrum saccharovorum]". Algo también para resltar que llama mucho la atención es que los primeros dos resultados eran proteinas que se encontraban en el humano y esta última es una bacteria, es decir que dependiendo de la longitud de la cadena no solo altera los valores de evalu, maxscore sino de que estamos buscando y en que organismo aparece.

👇**RETO X: Realizá una nueva corrida del BLASTp, utilizando la misma secuencia , pero ahora contra la base de datos PDB. ¿Se obtienen los mismo resultados? ¿Qué tipo de resultados(hits) se recuperan? ¿Cuándo nos podría ser útil este modo de corrida?**

Luego de realizar la comparación de la secuencia contra PDB, me da otro resultado, no podría ser que es totalmente diferente pero si que no es el mismo "UDP N-ACETYLGLUCOSAMINE O-ACYLTRANSFERASE" vs "UDP N-ACETYLGLUCOSAMINE O-ACYLTRANSFERASE" en la primera hay siete posibles organismo que poseen esta proteina mientras que en la segunda solo dos, pero esos dos son dos de los siete de la primer cadena. Viendo esto puedo asumir que en las bases de datos tienen cargados ambas cadenas pero con diferentes mutaciónes o datos de la mismas, ya que en ambas queries me dieron 100% de identidad, es decir que esa cadena era la misma que me estaba dando pero el resultado no es el mismo. Posiblemente esto sirva para ver las diferencias que una cadena puede representar en los diferentes organismos.