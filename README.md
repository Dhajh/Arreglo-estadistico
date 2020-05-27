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
     
     
     
