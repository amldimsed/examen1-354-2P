# -*- coding->utf-8 -*-
"""
Created on Mon Oct 23 23:21:23 2023

@author->Andres
"""

from kanren import Relation, facts, run, var

# Definir la relación de parentesco
parentera = Relation()
var1 = var()
facts(parentera, 
      #parentesco Padres
      ("Padre->Pedro", "Hijo->Marlon"),
      ("Padre->Pedro", "Hija->Gabriela"),
      ("Padre->Pedro", "Hijo->Jose"),
      
      ("Madre->Maria", "Hijo->Marlon"),
      ("Madre->Maria", "Hija->Gabriela"),
      ("Madre->Maria", "Hijo->Jose"),
      
      #parentesco Abuelos
      ("Abuelo->Gustavo", "Nieto->Marlon"),
      ("Abuelo->Gustavo", "Nieta->Gabriela"),
      ("Abuelo->Gustavo", "Nieto->Jose"),
      
      ("Abuela->Maria", "Nieta->Gabriela"),

      #parentesco Hermanos
      ("Hermano->Marlon", "Hermana->Gabriela"),
      ("Hermano->Marlon", "Hermano->Jose"),
      
      ("Hermana->Gabriela", "Hermano->Jose"),
      ("Hermana->Gabriela", "Hermano->Marlon"),
      
      ("Hermano->Jose", "Hermana->Gabriela"),
      ("Hermano->Jose", "Hermano->Marlon"),

      #parentesco Tios
      ("Tio->Carlos", "Sobrina->Gabriela"),
      ("Tio->Carlos", "Sobrino->Jose"),
      ("Tio->Carlos", "Sobrino->Marlon"),
      
      #parentesco sobrino
      ("Sobrina->Gabriela", "Tio->Carlos"),
      ("Sobrino->Jose"  , "Tio->Carlos"),
      ("Sobrino->Marlon", "Tio->Carlos"),
      
      #parentesco Primos 
      ("Primo->Gustavo", "Prima->Gabriela"),
      ("Primo->Gustavo", "Primo->Jose"),
      ("Primo->Gustavo", "Primo->Marlon"),
      

)

print("Hijo->Marlon")           
print(run(4,var1,parentera(var1,"Hijo->Marlon")))
print("Hija->Gabriela") 
print(run(4,var1,parentera(var1,"Hija->Gabriela")))

print("Hermano->Jose")
print(run(4,var1,parentera(var1,"Hermano->Jose")))

print("Hermana->Gabriela")
print(run(4,var1,parentera(var1,"Hermana->Gabriela")))

print("Tio->Carlos")
print(run(4,var1,parentera(var1,"Tio->Carlos")))

print("Primo->Jose")
print(run(4,var1,parentera(var1,"Primo->Jose")))
