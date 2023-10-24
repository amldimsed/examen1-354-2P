# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:05:28 2023

@author: Andres
"""

import pandas as pd
#import numpy as np
#from sklearn.impute import SimpleImputer
from sklearn.preprocessing import KBinsDiscretizer
 
archivo='D:\INF-354\segunda_parte\Tagged-Data-Final.csv'
tabla=pd.read_csv(archivo)

def eliminar_columna(tabla):
    
    
    #lista = tabla.iloc[:,num_columna]
    print("lista completa")
   
    print(tabla)
    
    lista = tabla.drop(['Gameplay Focus','Series','Story Focus'], axis=1)
    
    #print(lista)
    
    return lista

def inputar_media(tab):
    
    
    #lista = tab.iloc[:,num_columna]
    print("lista completa")
    print(tab)
    
    """
    #algoritmo visto en clases
    imputador = SimpleImputer(missing_values=np.nan, strategy='mean')
    
    # Aplicar la imputación a mis datos
    #evaluar = imputador.fit_transform(tab)
    evaluador = imputador.fit_transform(tab.iloc[:, [12]])
        
    # Creamos un nuevo DataFrame con los datos imputados
    datos_nuevo = pd.DataFrame(tab, columns=tab.columns)
    
    #print(datos_nuevos)
    
    """
    datos_nuevos = pd.DataFrame(tab)
    print("Se reemplaza los datos faltantes por la media")
    datos_nuevos['User_Count'].fillna(datos_nuevos['User_Count'].mean(), inplace=True)
    print(datos_nuevos)
    print(datos_nuevos['User_Count'])
    
    return datos_nuevos
 
def discretizar(tab):
    #Solo con datos puros de formato flotante no caracter, String   
    #datos imputados
    discreto=tab
    #En clase
    prepro=KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
    rangos=prepro.fit_transform(discreto)
    #Nuevo DataFrame con los datos discretos
    datos_discretizados = pd.DataFrame(rangos, columns=tab.columns)
    
    print("Datos discretizados:")
    print(datos_discretizados.head)

lista2 = eliminar_columna(tabla)
#print(lista2)

dat_imputados = inputar_media(lista2)


#discretizar(dat_imputados)



