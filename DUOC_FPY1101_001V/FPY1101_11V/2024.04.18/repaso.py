import os # libreria de comandos para limpiar pantalla
import time # libreria para esperar x segundos
os.system("cls") # limpia la pantalla

menu = True
while menu:
    print("=== BEBIDAS ===")
    print("1. COCACOLA \t $ 900")
    print("2. PEPSI \t $ 800")
    print("3. INKACOLA \t $ 700")
    opcion = int(input("Ingresa una de las opciones disponibles > "))

    if opcion < 1 or opcion > 3:
        print("opción no válida, intente nuevamente")
        time.sleep(1) # esperar x segundos
        os.system("cls") # limpia la pantalla
    else:
        menu = False

if opcion == 1:
    print("Eligió COCACOLA")
elif opcion == 2:
    print("Eligió PEPSI")
elif opcion == 3:
    print("Eligió INKACOLA")
else:
    print("opción no válida")
