import os # se delara solo una vez
import time # libreria para esperar x tiempo
os.system("cls") # limpiar pantalla

menu = True

while menu:
    print("== Restorant ==")
    print("1. porotos con riendas \t $5.000")
    print("2. cancato \t\t $8.000")
    print("3. fideos boloñesa \t $5.500")
    print("4. pollo arverjado \t $6.000")

    try:
        opcion = int(input("Ingresa una de las opciónes > "))
    except:
        opcion = 0

    if opcion < 1 or opcion > 4:
        print("La opción no esta disponible, intente nuevamente")
        time.sleep(1.5) # esperar x segundo
        os.system("cls") # limpiar pantalla
    else:
        menu = False

print("Salió del while")