#Calcular la desviación estándar por nivel, columna y renglón de un cubo con valores al azar
from numpy import *
import numpy as np
#Crear el arreglo de 3 niveles, 3 renglones, 3 columnas
random.seed (0);
a= random.rand(3,3,3)
print (a)

print (a.shape)

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

print (prom_niv)

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
print (prom_reng)

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
print (prom_column )

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
        
    print (desv_niv[k]=sqrt(sum) / (a.shape[1]*a.shape[2]))
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
            print (desv_ren[i]= sqrt (sum) / (a.shape[0]*a.shape[2]))

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
            print (desv_col= sqrt (sum)/(a.shape[0]*a.shape[1]))

'La desviacion estandar por columnas es:',desv_col
