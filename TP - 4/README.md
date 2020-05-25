Link :
https://github.com/AJVelezRueda/Bioinfo_UNQ/blob/master/Trabajos_Practicos/TP_N_4_En_qu%C3%A9_se_parece_una_vaca_y_una_gallina.pdf


| **Secuencia**      | **Nombre taxonómico**        | **Nombre comun** |
|:--------------:|:------------------------:|:-------------:|  
| NP_061820.1    | Homo sapiens             | Humano |
| NP_001072946.1 | Gallus gallus            | Gallo |
| NP_001065289.1 | Pan troglodytes			| Chimpancé |
| NP_001157486.1 | Equus caballus			| Caballo | 
| NP_001183974.1 | Canis lupus familiaris	| Perro |
| AEP27192.1   	 | Gorilla gorilla			| Gorila |
| XP_024245566.1 | Oncorhynchus tshawytscha	| Salmón real |
| NP_001086101.1 | Xenopus laevis			| Rana |
| NP_477164.1	 | Drosophila melanogaster	| Mosca de la fruta |


### Secuencias FASTA del cytochrome c para distintas especies:

| **Nombre**         | **Secuencia**                |
|:--------------:|:------------------------:|
| >NP_061820.1 cytochrome c [**Homo sapiens**]| MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE|
| >NP_001072946.1 cytochrome c [**Gallus gallus**] | MGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGITWGEDTLMEYLENPKKYIPGTKMIFAGIKKKSERVDLIAYLKDATSK|
| >NP_001065289.1 cytochrome c [**Pan troglodytes**] | MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE |
| >NP_001157486.1 cytochrome c [**Equus caballus**] | MGDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGFSYTDANKNKGITWKEETLMEYLENPKKYIPGTKMIFAGIKKKTEREDLIAYLKKATNE |
| >NP_001183974.1 cytochrome c [**Canis lupus familiaris**] | MGDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGFSYTDANKNKGITWGEETLMEYLENPKKYIPGTKMIFAGIKKTGERADLIAYLKKATKE |
| >AEP27192.1 cytochrome c [**Gorilla gorilla**] | MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE |
| >XP_024245566.1 cytochrome c [**Oncorhynchus tshawytscha**] | MGDIEKGKKAFVQKCAQCHTVENGGKHKVGPNLWGLFGRKTGQAEGFSYTDANKAKGIVWDTDTLMTYLENPKKYIPGTKMIFAGIKKKGERADLIAYLKSATS |
| >NP_001086101.1 cytochrome c, testis-specific [**Xenopus laevis**] | MGDVEKGKKVFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGIVWDEDTLMVYLENPKKYIPGTKMIFAGIKKKGERQDLIAYLKQSTSS |
| >NP_477164.1 cytochrome c distal, isoform A [**Drosophila melanogaster**] | MGSGDAENGKKIFVQKCAQCHTYEVGGKHKVGPNLGGVVGRKCGTAAGYKYTDANIKKGVTWTEGNLDEYLKDPKKYIPGTKMVFAGLKKAEERADLIAFLKSNK |

Los cuales se pueden apreciar en la carpeta [FASTA](https://github.com/pache0015/Bioinformatica-UNQ/tree/master/TP%20-%204/FASTA)

### ¿Cuán sencillo será alinear dos o más secuencias a mano? ¿Cuánto influirán el número de secuancias a alinear, su longitud, y la similitud entre ellas?

-- Alinear dos secuencias sería relativamente sencillo ya que son secuencias de aminoácidos cortas que tienen, en promedio, un largo de 100 caracteres, los cuales presentan similitudes apreciables. Pero, llegado el caso de querer alinear a mano más de dos secuencias, se tornaría muy complejo, considerando las distintas longitudes o al menos, muy poco eficiente.

### Son parecidos los citocromos c del gumano y el gallo?

-- Todo depende de que denominemos como parecido o determinar en que factores denominamos como determinantes para diferencia entre 2 secuencias del mismo, citocromo para dos especies distintas. Encontrar una respuesta determinista no ha sido una tarea sencilla y a partir de lo visto en clase se puede afirmar que ha existido una gran brecha entre los conocimientos y volúmenes de datos adquiridos durante años de investigación, y la eficiencia con la que estos pueden ser analizados. Sin embargo en la actualidad con la ayuda de sosticados algoritmos y el desarrollo del campo de la biología computacional (y de la informática en general) se ha logrado acortar la diferencia mencionada.
Con respecto al citocromos c del humano y el del gallo, presentan la misma longitud (de 105 caracteres/aminoácidos). Además de un gran nivel de coincidencias, caracter a caracter, como se puede observar en la captura del resultado de alineamiento de múltiples secuencias de Clustal Omega, que como se vio en clase es una herramienta de alineamiento para n más secuencias. (con n >= 2 )

![Gallo vs humanos - por poco ponemos huevos, bro](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%204/img/gallovshumano.jpg)

### ¿Qué teorías subyacen a este análisis?



-- Existen varias teorías que subyacen a este análisis. En función del número de secuencias que se comparan podemos distinguir: 

**• Alineamiento de dos secuencias:** Se comparan dos secuencias utilizando diversos métodos como, por ejemplo, la matriz de puntos (dot-plot), algoritmos de programación dinámica (Needleman-Wunsch o Smith-Waterman)para determinar regiones similares entre dos secuencias de nucleótidos o proteínas. o algoritmos heurísticos (FASTA, BLAST)

**• Alineamiento múltiple de secuencias:** Se comparan más de dos secuencias. Para ello se pueden utilizar diversos programas basados en algoritmos heurísticos como, por ejemplo, CLUSTALW.


### ¿Cómo nos ayuda la evolución a explicar sus similitudes y diferencias?

-- Se podría decir que dos secuencias similares pueden presentar pequeñas diferencias porque una de ellas sufrió una evolución que provocó un cambio en uno de sus aminoácido.
Según la investigación de Stanley L. Miller y Joan Oró se nos indican que la vida probablemente comenzó hace unos 3.800 millones de años. Lo cual implica que en la Tierra primitiva se sintetizaron las primeras moléculas orgánicas, muy posiblemente en el  que fueron organizándose progresivamente para formar otras más largas y complejas, que derivó en moléculas mucho más avanzadas. A partir de estas se originaron sistemas que combinaban características fundamentales: un compartimento (delimitado por una membrana - citoplasmática), un metabolismo básico (que permitía intercambiar materia y energía con el entorno) y una molécula con información genética (probablemente el ARN, que luego daría lugar a las proteínas y al ADN). Se consideran que esas células primitivas fueron los primeros seres vivos, pues ya tenían capacidad para automantenerse y autorreproducirse. A partir de ellas, la evolución por selección natural dio lugar a una especie unicelular más compleja, que fue el antepasado del que deriva toda la biodiversidad actual. Entendiendo que desde un punto de vista biológico, la evolución se va dando a través de mutaciones que perduran en el tiempo, para una especie dada. En este punto, el término evolución y mutación está fuertemente relacionados (siempre considerando la condición necesaria y suficiente de que esta perdure en la descendencia). Y si bien no se sabe exactamente cómo empezó la vida, este conocimiento nos invita a reflexionar sobre el papel que tuvo la evolución y como esta determinó cambios en las secuencias, lo cual conlleva a que se presenten similitudes y diferencias entre estas.

### Podemos elegir verlo en colores (Show Color) ¿Qué indican los colores?

-- Los colores se utilizan para indicar propiedades de los aminoácidos para ayudar en la caracterización de conservación o en una sustitución aminoacídica dada. Cuando se introducen múltiples secuencias la última fila de cada columna suele representar la secuencia consenso determinada por el alineamiento. Independientemente, también suele representarse la secuencia consenso en un formato gráfico.

### ¿Qué indican el guión (-), los dos  puntos (:) y el asterisco (*)?

-- Un alineamiento de secuencias es una forma de representar y comparar dos o más secuencias o cadenas de ADN, ARN o Proteínas y sirve para resaltar similitudes y diferencias,  que bien podrían indicar relaciones funcionales o evolutivas y mutaciones entre los genes o proteínas consultados. Las secuencias alineadas se escriben con las letras (representando aminoácidos o nucleótidos) en filas de una  matriz. 
En tal acción, hay situaciones que las que es necesario insertar espacios para que las zonas con idéntica o similar estructura se alineen. El guión (**-**) indica un **GAP**, es decir un corrimiento de una secuencia para hacer coincidir con otra. (Cabe destacar que un **GAP** puede corresponder tanto a una deleción como a una inserción. Debido a la existencia de gaps y sustituciones alinear dos secuencia no es una acción trivial.) El objetivo del alineamiento es conseguir alinear las posiciones homólogas.
Por otro lado, también tenemos el “carácter” especial de dos puntos (**:**) que indica si existe una conservación fuerte. Por ejemplo, si tomamos un nuevo elemento es bastante equivalente, si su puntuación es > 0.5 en una matriz 250 **PAM** (**PAM** es una mutación aceptada. Es decir, mutaciones en una proteína que NO afectan a su función biológica, y puede pasar a la siguiente generación. Dos secuencias están a una unidad **PAM** si una se transforma en la otra por mutaciones aceptadas.) Resumiendo, los (**:**) indican posiciones en las que se han realizado sustituciones conservativas.
Finalmente, el **(*)** indica una coincidencia. Es decir, que en dicha posición los residuos son 100% idénticos.

### A simple viste, ¿se conserva la secuencia del citocromo c en los organismos?

-- No, ya que que cada secuencia FASTA varía al hacer el alineamiento. 

### ¿Creeríamos que todos los organismos se asemejan por igual al resto, o se pueden identificar grupos de mayor similitud? Si es así, ¿tienen sentido?

-- No, cada organismo se vincula más con algunos organismos que con otros. Esto se puede ver en el árbol filogenético. (Cabe agregar que un árbol filogenético es un esquema con forma arbórea que muestra las relaciones evolutivas entre varias especies u otras entidades que se cree que tienen una ascendencia común, el cual se determina gracias a la información proveniente de fósiles y de la comparación anatómica, fisiológica y molecular de los organismos actuales.)

### ¿Qué evidencias nos aportaría este análisis, a la luz de la evolución?

-- Podríamos decir que a partir del árbol filogenético podemos ver cómo se agrupan los distintos organismos según sus similitudes. Si tomamos por ejemplo, el humano está en el mismo árbol que el chimpancé y este árbol viene está en otro compartido con el gorila. Entonces, esto nos indicaría que, el chimpancé y el humano tienen la misma procedencia. Esta rama, a su vez, compartiría el origen con el gorila. Por lo tanto podríamos explicar cómo se dio la evolución de ciertos organismos a partir de sus similitudes en la secuencia de su **ADN**.
