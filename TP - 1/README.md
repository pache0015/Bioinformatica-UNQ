# Bioinformatica-UNQ

## Tp 1 - Introducción a la Bioinformática

#### RETO I: ¿Podrías buscar un ejemplo de macromoléculas que almacenen información sobre la ‘identidad’ de un organismo dado?  

    ##### Un ejemplo de esto son los acidos nucleicos (el *ácido desoxirribonucleico* - o ADN - y el *ácido ribonucleico* - o  ARN-). 

![Meme - Daenerys - ADN/ARN](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/img/ADN%7CARN.jpg)
 
      
        
#### RETO II: Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

Siendo simplistas, se podria expresarla informacion contenida en la estructura primaria de las poteinas usando cualquier estructura que sea iterable; amerita mencionar la simpleza de un String o cadenas de caracteres. Teniendo en cuenta que para este trabajo se eligío el lenguaje de programación ___Haskell___, una posible forma de modelar dicha estructura primaria sería con los datas especificados en el archivo: [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-1.hs).
  
    
      
        
          
#### RETO III: ¿ En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?
La informacion de la estructura terciaria proteica  se podría expresar de varias maneras distintas, dependiendo el nivel de dificultad que se quiera imprimir en la calidad delcódigo. Una forma simple de verlo es como una listas de listas. Por cada aminoácido tener una lista con donde en principio esté el string establecido anteriormente como estructura primaria y otra lista con las coordenadas para saber dónde graficarlo en función del espacio (o bien cualquier estructura que permita aglomerar una serie de estructuras o datos relacionados, como puede ser una ___n-tupla___ o similar). Otra forma de pensarlo, quizas un poco mas compleja, es atraves de una estructura arbolea, como puede ser un grafo, donde se podria incluir mucha más informacion estructural. Para ganar un conocimiento profundo al respecto, en el [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-1.hs) se podra encontrar una propuesta utilizando nuevamente ___Haskell___ y un par de funciones pertinentes.
  
    
      
        
          
          
#### RETO IV: Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. ¿Cuáles fueron sus contribuciones en este campo? ¿Qué nos cuenta su historia acerca del mundo de la ciencia?
 Sus contribucioines en este campo fueron basicamente la clave para poder entender la estructura del ADN mediante las fotos que pudo tomar con los rayos x.
En cuanto a su historia en el mundo de la cienca puede resaltarse lo machista de la época y el poco lugar que se le daba a las mujeres en los ámbitos científicos por muy buenas que fueran. Ya que por más descubrimiento que hagan, como es el caso de Rosalind no le daba el prestigio o importancia que merecían. 
  
![Meme - Rosalind](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/img/rosalinda.jpg)
      
        
        
#### RETO V: Proponé en pseudocódigo un programa que prediga la estructura secundaria que adoptará cada residuo de la secuencia proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).
Ver una posible solución en el [TP-1.hs](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/tp-1.hs).
___Nota___: Para predecir la estructura secundaria que adoptará cada residuo de la secuencia proteica dada, a traves de una serie de datos que se obtienen de analizar la secuencia y la estructura de amplios conjuntos de proteínas con estructura conocida y se establece una correlación entre las características estructurales y la secuencia para determinar cuál es la
probabilidad de que un determinado residuo adopte un tipo de estructura secundaria u otro. Este calculo devengará en un porcentaje que determina la probabilidad de que se adopte o bien una hélice, una hoja beta plegada o un loop. Como puede verse en la siguiente tabla:

![tabla - Estructura secundaria](https://github.com/pache0015/Bioinformatica-UNQ/blob/master/TP%20-%201/img/tabla.jpg)

Esto podria pensarse como: (asumiendo que la lógica de las probabilidades esta abstraida en la función problabilidad_ __estructura__)

~~~~
analisis{
    Por cada ___residuo___ en ___secuencia_proteica___ {
        Si probabilidad_helix(___residuo___){
            retorna H (informacion_de(___residuo___)) + residuos en secuencia
        } 
        Sino{
            Si (){
                retorna B (informacion_de(___residuo___))  + residuos en secuencia
            }
            Sino{
                retorna L (informacion_de(___residuo___)) + residuos en secuencia
            }
    }
}
~~~~

Por simplicidad, en el modelo propuesto, la forma de resolver dicha situacion fue priorizando, tomando dichos valores deforma deterministica, sin recurrir en las probabilidades. Se intenta priorizar la idea fundamental por sobre la implementación, como motivación para el acercamiento a un tema nuevo.   
 
    
- PREGUNTAS DISPARADORAS: ¿Qué inputs tendría tu programa? ¿De qué modo se te ocurre configurar el output?
 (What)
    
     
#### RETO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de corroborar tu respuesta realizando un diagrama de un posible método computacional para dicho fin.
  
(Revisar)
Lo que hace distintos a dos individuos de la misma especie es la informacion de su ___ADN___.
    
    
- PREGUNTAS DISPARADORAS: ¿Qué información deberías tener? ¿De qué modo deberías expresar dicha información para el análisis?
(What) 
La información que se deberia tener a priori es una muestra genetica de ambos individuos.
