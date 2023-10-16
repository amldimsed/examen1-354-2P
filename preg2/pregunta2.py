# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:21:09 2023

@author: Andres
"""

import pandas as pd
import numpy as np

archivo='D:\INF-354\segunda_parte\Tagged-Data-Final.csv'
tabla=pd.read_csv(archivo)
#print(tabla.head)

def Moda_Media_Cuartil_percentiol(tabla, num_columna):
    
    lista = tabla.iloc[:,num_columna]
    #print(lista)
    # Calcular la media
    media = np.mean(lista)
    
    # Calcular la moda realizado con pandas
    moda = lista.mode()
    
    # Calcular los cuartiles (25%, 50%, 75%)
    cuartil_25 = lista.quantile(0.25)
    cuartil_50 = lista.quantile(0.50)
    cuartil_75 = lista.quantile(0.75)

    # Calcular percentiles (por ejemplo, el percentil 90)
    percentil_60 = np.percentile(lista, 60)
    percentil_90 = np.percentile(lista, 90)
    percentil_99 = np.percentile(lista, 99)
   
    print("Media",media,"\n",
          "moda",moda,"\n",
          "cuartil 25",cuartil_25,"\n",
          "cuartil 50",cuartil_50,"\n",
          "cuartil 75",cuartil_75,"\n",
          "percentil 60", percentil_60,"\n",
          "percentil 90", percentil_90,"\n",
          "percentil 99", percentil_99,"\n",
          )

print("Ventas de Na")    
Moda_Media_Cuartil_percentiol(tabla,4)
print("********************************")

print("Ventas de Eu")
Moda_Media_Cuartil_percentiol(tabla,5)
print("********************************")

print("Ventas de Jp")
Moda_Media_Cuartil_percentiol(tabla,6)
print("********************************")

print("Ventas de Otros")
Moda_Media_Cuartil_percentiol(tabla,7)
print("********************************")

print("Ventas de Global")
Moda_Media_Cuartil_percentiol(tabla,8)
print("********************************")

print("Criticas de Aceptacion")
Moda_Media_Cuartil_percentiol(tabla,9)
