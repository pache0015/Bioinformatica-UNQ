# Bioinformatica-UNQ

## Tp 1 - Introducción a la Bioinformática

#### RETO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?
####
####
####
####
(https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/img/ADN%7CARN.jpg)
####
####
####
####



    ##### Un ejemplo de esto son los acidos nucleicos (el ___ácido desoxirribonucleico___ - o ADN - y el ___ácido ribonucleico___ - o  ARN -). 


#### RETO II: Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

Siendo simplistas, se podria expresarla informacion contenida en la estructura primaria de las poteinas usando cualquier estructura que sea iterable; amerita mencionar la simpleza de un String o cadenas de caracteres. Teniendo en cuenta que para este trabajo se eligío el lenguaje de programación ___Haskell___, una posible forma de modelar dicha estructura primaria sería con los datas especificados en el archivo: [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-1.hs).
 
 
#### RETO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?
La informacion de la estructura terciaria proteica  se podría expresar de varias maneras distintas, dependiendo el nivel de dificultad que se quiera imprimir en la calidad delcódigo. Una forma simple de verlo es como una listas de listas. Por cada aminoácido tener una lista con donde en principio esté el string establecido anteriormente como estructura primaria y otra lista con las coordenadas para saber dónde graficarlo en función del espacio (o bien cualquier estructura que permita aglomerar una serie de estructuras o datos relacionados, como puede ser una ___n-tupla___ o similar). Otra forma de pensarlo, quizas un poco mas compleja, es atraves de una estructura arbolea, como puede ser un grafo, donde se podria incluir mucha más informacion estructural. Para ganar un conocimiento profundo al respecto, en el [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-1.hs) se podra encontrar una propuesta utilizando nuevamente ___Haskell___ y un par de funciones pertinentes.


#### RETO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?
 Sus contribucioines en este campo fueron basicamente la clave para poder entender la estructura del ADN mediante las fotos que pudo tomar con los rayos x.
En cuanto a su historia en el mundo de la cienca puede resaltarse lo machista de la época y el poco lugar que se le daba a las mujeres en los ámbitos científicos por muy buenas que fueran. Ya que por más descubrimiento que hagan, como es el caso de Rosalind no le daba el prestigio o importancia que merecían. 


#### RETO V: Proponé en pseudocódigo un programa que prediga la estructura secundaria que adoptará cada residuo de la secuencia proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).
!!! note
        
      Ver una posible solución en el [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-           1.hs)
      ___Nota___: Para predecir la estructura secudaria que adoptara cada residuo de la secuencia proteica dada, se calculo         un porcentaje que determina la probabilidad de que seadopte una hélice o hoja beta legada. Por simplicidad, en el la         forma de resolver  





- PREGUNTAS DISPARADORAS: ¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output?

#### RETO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.
- PREGUNTAS DISPARADORAS: ¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?
