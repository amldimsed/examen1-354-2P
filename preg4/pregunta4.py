# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 01:23:26 2023

@author: Andres
"""

#from numpy import array
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer


archivo='D:\INF-354\segunda_parte\Tagged-Data-Final.csv'
tabla=pd.read_csv(archivo)


def etiquetado_simple(tabla):
    
    #datos = ["ads","ads","3","er"]
    datos = tabla.iloc[:,0]
    #print("lista completa")
    
    #print("lista acortada")
    lista = list(set(datos))
    #print(lista)
    
    #Etiquetado simple LabelEncoder
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(lista)
    print("Datos con etiquetado simple:","\n",integer_encoded)

#Asignacion de 0 o 1 tomando encueta el tamaño de colimnas del dataset
#Existen dos formas onehot encode y Binary encode
def etiquetado_binario(tabla):
    
    #datos = ["ads","ads","3","er"]
    datos = tabla.iloc[:,0]
    #print("lista completa")
    #print(datos)
    
    #Se elimina los datos repetidos
    #print("lista acortada")
    lista = list(set(datos))
    #print(lista)
    
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(lista)
    
    # onehot encode
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print ("OneHot Encoder:","\n", onehot_encoded)
    
    #Binary encode
    lb = LabelBinarizer()
    metodo2 = lb.fit_transform(lista)
    print ("Label Binarizer:","\n",metodo2)
    
etiquetado_binario(tabla) 
print("*****************************************************************")   
etiquetado_simple(tabla)
print("\n")
