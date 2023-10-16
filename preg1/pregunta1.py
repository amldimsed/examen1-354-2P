# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
with open('D:\INF-354\segunda_parte\Tagged-Data-Final.csv', newline='') as dataset:
    reader = csv.reader(dataset)
    tabla = list(reader)
dataset.close()

def Cuartiles(tabla, num_columna, Q123_cuartil):
    tamanio = len(tabla)
    lista = list()
    for i in range(1, tamanio):
        lista.append(float(tabla[i][num_columna]))  # agregamos cada elemento
    #print("Tabla No Ordenada - ")
    #print(lista)
    lista.sort()  # Ordenando
    # print("Tabla Ordenada - ")
    # print(lista)
    if tamanio % 2 == 1:  # verificar si la tamanio de la lista es Impar o Par
        # print("Es Impar", tamanio)
        posicionA = int(Q123_cuartil * (tamanio + 1) / 4)
        # print("Posición:", posicionA)
        print("Primer Cuartil:", lista[int(posicionA) - 1])
    else:
        # print("Es par")
        posicionB = (Q123_cuartil * tamanio) / 4
        # print("Posición")
        print("Primer Cuartil Par", lista[int(posicionB) - 1])
    pass

def Percentil(tabla, num1, num2):
    tamanio = len(tabla)
    lista = list()
    for i in range(1, tamanio):
        lista.append(float(tabla[i][num1]))  # agregamos cada elemento
    #print("Tabla No Ordenada - ")
    #print(lista)
    lista.sort() # Ordenando
    #print("Tabla Ordenada - ")
    #print(lista)
    i = (num2 / 100) * tamanio
    #print("indice", i)
    #mod = i % 10
    #print("mod", mod)
    if isinstance(i, int):
        #print("no es entero, se va a la siguiente posición")
        pos1 = int(i) + 1
        #print("Poscion ->", pos1)
        print("Percentil",num2,"->", lista[pos1])
    else:
        #print("es entero")
        #print(tamanio)
        posa = int(i)
        posb = posa + 1
        #print("Poscición", (posa + posb) / 2)
        print("Percentil",num2,"->", (lista[posa - 1] + lista[posb - 1]) / 2,"tamanio",tamanio)
    pass

def Media(tabla, num_columna):          #Funcion para la calcular la MEDIA
    suma = 0
    tamanio = len(tabla)
    for i in range(1, tamanio):
        suma += float(tabla[i][num_columna])
    valor = suma / tamanio 
    
    return valor

def Moda (tabla, num_columna):
    cont = 0
    mayor = 0
    tamanio = len(tabla)
    for i in range(1, tamanio):
        cont = 0
        for j in range(1, tamanio):
            if(float(tabla[i][num_columna]) == float(tabla[j][num_columna])):
                cont = cont + 1
        if (cont > mayor):
            mayor = cont
            mod = float(tabla[i][num_columna])
    print("Moda -> ",mod) 

def Moda2 (tabla, num_columna):
    
    tamanio = len(tabla)
    valores = list()
    for i in range(1, tamanio):
        valores.append(float(tabla[i][num_columna]))  # agregamos cada elemento
        
    # Calculamos la moda
    frecuencia_valores = {}
    max_frecuencia = 0
    moda = 0
    
    for valor in valores:
        if valor in frecuencia_valores:
            #print(valor, "----------- ", frecuencia_valores[valor])
            frecuencia_valores[valor] += 1
            
        else:
            frecuencia_valores[valor] = 1
    
        if frecuencia_valores[valor] > max_frecuencia:
            moda = valor
            max_frecuencia = frecuencia_valores[valor]  
    return moda
 
import matplotlib.pyplot as plt

def graficas_media_moda(tabla, num_columna, media, moda,nombre):
    tamanio = len(tabla)
    lista = list()
    for i in range(1, tamanio):
        lista.append(float(tabla[i][num_columna]))  # agregamos cada elemento
    #print(lista)

    # Crear el histograma
    plt.hist(lista, color='#F2AB6D', rwidth=0.85)
    # Crear la linea donde se encuentra la moda y la media
    plt.axvline(x=moda, color='red', linestyle='dashed', linewidth=2, label=f'Moda ({moda:.2f})')
    plt.axvline(x=media, color='green', linestyle='dashed', linewidth=2, label=f'Media ({media:.2f})')
    plt.title('Histograma de '+nombre)
    #plt.xlabel('datos de la columna')
    #plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()    
    pass

print("SIN LIBRERIAS El calculo del 1er cuartil de datos, el percentil 90, 95 por columna; explique qué significa en cada caso mediante Python sin uso de librerías")
print("-----------------------CUARTILES-----------------------------------")
print("**********PRIMER CUARTIL 25%***********")
print("Ventas de Na")
Cuartiles(tabla, 4, 1)

print("Ventas de Eu")
Cuartiles(tabla, 5, 1)

print("Ventas de Jp")
Cuartiles(tabla, 6, 1)

print("Ventas de Otros")
Cuartiles(tabla, 7, 1)

print("Ventas de Global")
Cuartiles(tabla, 8, 1)

print("Criticas de Aceptacion")
Cuartiles(tabla, 9, 1)

print("----------------------------------------------------------")
print("**********SEGUNDO CUARTIL 50%***********")
print("Ventas de Na")
Cuartiles(tabla, 4, 2)

print("Ventas de Eu")
Cuartiles(tabla, 5, 2)

print("Ventas de Jp")
Cuartiles(tabla, 6, 2)

print("Ventas de Otros")
Cuartiles(tabla, 7, 2)

print("Ventas de Global")
Cuartiles(tabla, 8, 2)

print("Criticas de Aceptacion")
Cuartiles(tabla, 9, 2)

print("----------------------------------------------------------")
print("**********TERCER CUARTIL 75%***********")
print("Ventas de Na")
Cuartiles(tabla, 4, 3)

print("Ventas de Eu")
Cuartiles(tabla, 5, 3)

print("Ventas de Jp")
Cuartiles(tabla, 6, 3)

print("Ventas de Otros")
Cuartiles(tabla, 7, 3)

print("Ventas de Global")
Cuartiles(tabla, 8, 3)

print("Criticas de Aceptacion")
Cuartiles(tabla, 9, 3)

print("-----------------------PERCENTILES-----------------------------------")
print("**********PERCENTIL 90% - 95%***********")
print("Ventas de Na")
Percentil(tabla, 4 ,90)
Percentil(tabla, 4 ,95)

print("Ventas de Eu")
Percentil(tabla, 5 ,90)
Percentil(tabla, 5 ,95)

print("Ventas de Jp")
Percentil(tabla, 6 ,90)
Percentil(tabla, 6 ,95)

print("Ventas de Otros")
Percentil(tabla, 7 ,90)
Percentil(tabla, 7 ,95)

print("Ventas de Global")
Percentil(tabla, 8 ,90)
Percentil(tabla, 8 ,95)

print("Criticas de Aceptacion")
Percentil(tabla, 9 ,90)
Percentil(tabla, 9 ,95)

print("-----------------------MEDIA-----------------------------------")
print("Ventas de Na")
print("Media", Media(tabla, 4))

print("Ventas de Eu")
print("Media", Media(tabla, 5))

print("Ventas de Jp")
print("Media", Media(tabla, 6))

print("Ventas de Otros")
print("Media", Media(tabla, 7))

print("Ventas de Global")
print("Media", Media(tabla, 8))

print("Criticas de Aceptacion")
print("Media", Media(tabla, 9))

print("-----------------------MODA-----------------------------------")
print("Ventas de Na")
print("La moda de la primera columna es:", Moda2(tabla, 4))

print("Ventas de Eu")
print("La moda de la primera columna es:", Moda2(tabla, 5))

print("Ventas de Jp")
print("La moda de la primera columna es:", Moda2(tabla, 6))

#print("Ventas de Otros")
#Moda(tabla, 7)

print("Ventas de Otros")
print("La moda de la primera columna es:", Moda2(tabla, 7))

print("Ventas de Global")
print("La moda de la primera columna es:", Moda2(tabla, 8))

print("Criticas de Aceptacion")
print("La moda de la primera columna es:", Moda2(tabla, 9))

print("-----------------------GRAFICA-----------------------------------")
print("Ventas de Na")
graficas_media_moda(tabla, 4, Media(tabla, 4), Moda2(tabla, 4),"Ventas de Na")

print("Ventas de Eu")
graficas_media_moda(tabla, 5, Media(tabla, 5), Moda2(tabla, 5),"Ventas de Eu")

print("Ventas de Jp")
graficas_media_moda(tabla, 6, Media(tabla, 6), Moda2(tabla, 6),"Ventas de Jp")

print("Ventas de Otros")
graficas_media_moda(tabla, 7, Media(tabla, 7), Moda2(tabla, 7),"Ventas de Otros")

print("Ventas de Global")
graficas_media_moda(tabla, 8, Media(tabla, 8), Moda2(tabla, 8),"Ventas Global")

print("Criticas de Aceptacion")
graficas_media_moda(tabla, 9, Media(tabla, 9), Moda2(tabla, 9),"Criticas de Aceptacion")