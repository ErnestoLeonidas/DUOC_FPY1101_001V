import os # libreria de comandos para limpiar pantalla
import time # libreria para esperar x segundos
os.system("cls") # limpia la pantalla

for i in range(10):
    print(f"Repitiendo x veces {i}")

for i in range(5,10):
    print(f"El pimer parametro indica el número de inicio")
    print(f"El segundo parámetro indica la cantidad de veces")
    print(f"La i indica el número incremental y va en el {i}")

for i in range(2,10,2):
    print(f"El pimer parametro indica el número de inicio")
    print(f"El segundo parámetro indica la cantidad de veces")
    print(f"El tercer parámetro indica de cuanto en cuanto")
    print(f"La i indica el número incremental y va en el {i}")
