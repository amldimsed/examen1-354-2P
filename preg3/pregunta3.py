# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:02:53 2023

@author: Andres
"""

import pandas as pd
import numpy as np

archivo='D:\INF-354\segunda_parte\Tagged-Data-Final.csv'
tabla=pd.read_csv(archivo)

def inputar_media(tabla, num_columna):
    
    
    lista = tabla.iloc[:,num_columna]
    print("lista completa")
    print(lista)
    
    #hallamos la media con numpy
    auxiliar=lista
    # Filtramos los valores NaN elementos que no son nan
    auxiliar = auxiliar[(~np.isnan(auxiliar))]
    
    # Calcular la media de los valores restantes
    media = np.mean(auxiliar)
    print("La Media --> ",media) 
    
    #reemplazamos por la media
    listaCambio=np.where(np.isnan(lista),media,lista)
    print("*******************CAMBIO****************")
    print(listaCambio)

inputar_media(tabla, 12)