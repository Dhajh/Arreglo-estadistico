# Arreglo-Estadístico
  ### Cálculo estádistico de un arreglo
  #### Programa para la obtencion de promedio y de la desviación estandar de un arreglo (#,#,#)
  ###### Facultad de Ingeniería Civil, Carretera Coquimatlán Kilómetro 9, Coquimatlán 28,400, Coquimatlán, Coli-ma, Sebastián George Heredia, sgeorge@ucol.mx - Programa Educativo Ingeniero Topógrafo Geomáti-co (PE-ITG) 
  
  **Resumen**
  
  Se determinará la desviación estándar por nivel, columna y renglón de un arreglo, siguiendo todos los pasos para la obtención de la desviación están-dar de cada uno de los factores, determinadas por el promedio o media.
Palabras clave: Estadística. Arreglo. Google Cola-boratory. Nivel, columna y renglón. Bucle
  
  
  **Abstract**
  
  The standard deviation will be determined by level, column, and line of an arrangement, following all the steps to obtain the standard deviation of each of the factors, determined by the average or mean.
Keywords:   
Statistics. Arrangement. Google Colaboratory. Level, column and line. Loop  

  
  
  **1. 	Introducción**
  Cálculos estadísticos: Puede personalizar las estadísticas predeterminadas para que se mues-tren en un informe de clasificación.
Se pueden añadir cálculos estadísticos prede-terminados adicionales para informes de clasifi-cación basados para mostrarse cuando ejecuta el informe, incluidos la media, la mediana, la desviación estándar y otros cálculos matemáti-cos evaluados entre sus datos en función de los informes específicos que necesite.

  
  1.1. 	Media o promedio
  La media es un promedio aritmético de los valo-res de filas en un conjunto de datos, calculado mediante la suma dividida por el recuento (su-ma/recuento). La media se ve influida por los datos alejados, a diferencia de la mediana, que generalmente se utiliza para distribuciones ses-gadas. Sera el principal paso para el objetivo de nuestro dicho programa.
  
  1.2. 	Desviación Estándar
  La desviación estándar muestra cuánta variación existe con respecto a la media esperada. Una desviación estándar baja muestra puntos de datos cercanos a la media. Una desviación es-tándar alta muestra que los puntos de datos se reparten entre un gran rango de valores.
  
  
  1.3. 	Programas para utilizar
  Se utilizará un enlace asociada de Google, lla-mado Google Colaboratory, la herramienta de Google en la nube para ejecutar código Python.
  
  1.4. 	Google Colaboratory
  La principal ventaja que ofrece esta herramienta es que libera a nuestra máquina de tener que llevar a cabo un trabajo demasiado costoso tanto en tiempo como en potencia o incluso nos permite realizar ese trabajo si nuestra máquina no cuenta con recursos suficientemente poten-tes. Y todo de forma gratuita.
«Google Colaboratory es un entorno gratuito de Jupyter Notebook que no requiere configuración y que se ejecuta completamente en la nube».

  1.5. 	Python
  Lenguaje de programación interpretado, basado en una estructura que busca una sintaxis de un código legible. También es un lenguaje multipa-radigma, ya que soporta orientación a objetos, programación imperativa y programación fun-cional.


  **2. 	Desarrollo Experimental**
  
  Se busca que el programa obtenga la división estándar de un arreglo de hasta 100x100x100 datos al azar, el código va realizando cada una de las operaciones por columna, renglón y ni-vel, para eso se crean variables de almacena-miento y después se crean bucles for para cada renglón, nivel y columna, dando como resultado un array de acuerdo con el random de datos de hasta 100 datos.

  2.1. 	Código generado
  
     #Calcular la desviación estándar por nivel, columna y renglón de un cubo con valores al azar
     from numpy import *
     import numpy as np
     #Crear el arreglo de 3 niveles, 3 renglones, 3 columnas
     random.seed (0);
     a= random.rand(3,3,3)
     a

     a.shape

     #Crear las variables de almacenamiento para los promedios por niveles, renglones y columnas
     prom_niv = zeros(a.shape[0])
     prom_reng = zeros(a.shape[1])
     prom_column = zeros(a.shape[2])

     #Se crea un bucle para obtener el promedio por cada nivel

     for k in range(a.shape[0]):
         #Crear la variable sum, para guardar los resultados de la suma por nivel
         sum=0
         #Iterar por cada renglón
         for i in range(a.shape[1]):
              #Iterar por columna
             for j in range(a.shape[2]):
            
                 #Comenzar la suma
                 sum = sum + a [k,i,j]
            
                 #Teniendo las sumas, se puede comenzar a calcular el promedio por nivel
                 prom_niv[k]= sum / (a.shape[1]*a.shape[2])

     prom_niv

     #Se crea bucle para calcular el promedio por rengón

     for i in range(a.shape[1]):
         #Crear la variable suma que guarde las sumas por renglón
         sum= 0
         #Iterar por columna
         for j in range(a.shape[2]):
             #Iterar por nivel
             for k in range(a.shape[0]):
            
                 #Iniciar la suma
                 sum = sum + a[k,i,j]
            
                 #Teniendo las sumas, pasamos a obtener el promedio por renglón
                 prom_reng[i]= sum / (a.shape[2]*a.shape[0])
     prom_reng

     #Se crea un bucle para el promedio por columnas

     for j in range(a.shape[2]):
         #Crear variable suma
         sum= 0
         #Iterar por nivel
         for k in range(a.shape[0]):
             #Iterar por renglón
             for i in range(a.shape[1]):
            
                 #Iniciar suma
                 sum = sum + a[k,i,j]
                 #Calcular promedio
                 prom_column[j]= sum / (a.shape[0]*a.shape[1])
     prom_column 
     
     #Se crean las nuevas variables que almacenarán la desviación estandar por i,j,k
     desv_niv= zeros(a.shape[0])
     desv_ren= zeros(a.shape[1])
     desv_col= zeros(a.shape[2])
     
     #Crear bucle para obtener la desviación estándar por nivel
     #Iterar por nivel
     for k in range(a.shape[0]):
    
         #Crear variable de suma
         sum = 0
         #Iterar por los elementos del renglón
         for i in range (a.shape[1]):
             #Iterar por los elementos de la columna
             for j in range(a.shape[2]):
            
                 #Realizar la suma      
                 sum= sum + a[k,i,j]-prom_niv[k]**2
        
             #calcular desviación por renglones
        
         desv_niv[k] = sqrt(sum) / (a.shape[1]*a.shape[2])
     'La desviacion estandar por nivel es:',  desv_niv

     #Crear un bucle para calcular la desviación estándar por renglón
     #Iterar por renglón
     for i in range(a.shape[1]):
         #Crear variable de suma
         sum = 0
         #Iterar por columna
         for j in range(a.shape[2]):
             #Iterar por nivel
             for k in range(a.shape[0]):
            
                 #Hacer la suma
                 sum= sum + a[k,i,j]-prom_reng[i]**2
            
                 #Calculo de desviación
                 desv_ren[i]= sqrt (sum) / (a.shape[0]*a.shape[2])

     'La desviacion estandar por renglon es:',desv_ren


     #Crear bucle para calcular la desviación estandar por columna
     #Iterar por columna
     for j in range(a.shape[2]):
         #Crear variable de suma
         sum= 0
         #Iterar por nivel
         for k in range(a.shape[0]):
             #Iterar por renglon
             for i in range(a.shape[1]):
            
                 #Hacer la suma
                 sum = sum + a[k,i,j]-prom_column**2
                 #Calcular la desviación
                 desv_col= sqrt (sum)/(a.shape[0]*a.shape[1])

     'La desviacion estandar por columnas es:',desv_col
     
     
   **3. 	Manejo de datos**
  
  A continuación, se proporcionarán los datos de los aspectos en los que fue probado el pro-grama.
  
   3.1. 	Tipos de datos manejados
  Los datos que utilice para mi programa son datos estadísticos el cual se hacen operaciones y ciclos, almacenándolos en variables y gene-rando un array como resultado.

  3.2. 	Sistema Operativo
  Puede utilizarse desde un medio con internet, buscando “Google Colab”, accediendo con una cuenta de Google totalmente gratis, y en siste-ma Windows.
  
  3.3. Equipo de prueba
  El equipo en el cual fue probado el programa es una computadora portátil de la marca Hp con las siguientes características:
     
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura1.jpg)

                                          Figura 1. Especificaciones del dispositivo

   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura2.jpg)

                                          Figura 2. Especificaciones del dWindows

     
   **4. 	Resultados**
   
   Se utilizara un ejemplo de arrary de (3,3,3), pero en el programa se pueden generar datos de hasta (100,100,100)
   
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura3.jpg)
                   
                                           Figura 3. Creación del arreglo
   
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura4.jpg)

                                           Figura 4. Creacion de variables de almacenamiento

   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura5.jpg)

                                           Figura 5. Creacion del bucle promedio por nivel

   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura6.jpg)

                                           Figura 6. Creacion del bucle promedio por renglon
 
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura6.jpg)
 
                                           Figura 7. Creacion del bucle promedio por columna

   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura8.jpg)
 
                                           Figura 8.  Creacion de nuevas variables de almacenamiento
                                           
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura9.jpg)
 
                                           Figura 9.  Creacion de bucle desviacion estandar por nivel
                                           
   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura10.jpg)
 
                                           Figura 10.  Creacion de bucle desviacion estandar por renglon

   ![PalabrasdelTextoAlternativo](https://github.com/Sebastian-george09/Arreglo-estadistico/blob/master/IMAGENES/Figura11.jpg)
 
                                           Figura 11.  Creacion de bucle desviacion estandar por columna


**5. Conclusiones**

El lenguaje de programación Python puede ser utilizado para trabajar con la estadística y cálcu-los matemáticos, ya que facilita la realización de diversas tareas en ellos. Un ejemplo es el pro-grama anterior presentado el cual puede ser utilizado en procesos específicos estadísticos, INEGI (Instituto Nacional de Estadística y Geo-grafía) es una empresa encargada de datos estadísticos de información en México, este programa facilita al usuario hacer un cálculo estadístico de un array, ya sea con datos al azar o establecidos.

**6. Bibliografía**

Oscar, de la Fuente (2019). Google Colab: Python y Machine Learning en la nube. Adictosaltrabajo.
https://www.adictosaltrabajo.com/2019/06/04/google-colab-python-y-machine-learning-en-la-nube/

Anonimo (2019). Adobe. Resumen de los informes. Guia de herramientas de Analytics.
https://claudiovz.github.io/scipy-lecture-notes-ES/intro/numpy/array_object.html

Alejandro, Lamadrid y Antonio, Jimenez, España, (2014-2020). Tipos de datos en arrays Numpy (dtype).
https://python-para-impacientes.blogspot.com/2019/10/tipos-de-datos-en-arrays-numpy-dtype.html 

