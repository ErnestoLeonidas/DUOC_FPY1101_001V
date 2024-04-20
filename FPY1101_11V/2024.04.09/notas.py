import os # libreria de comandos para limpiar pantalla
import time # libreria para esperar x segundos
os.system("cls") # limpia la pantalla


print("calculadora de promedios")

cantidad = int(input("Ingresa la cantidad de notas > "))

notas_acumulada = 0

for i in range(cantidad):
    nota = int(input(f"ingresa la nota número {i+1} > "))
    notas_acumulada = notas_acumulada + nota

print(f"el promedio de las notas es: {notas_acumulada/cantidad}")