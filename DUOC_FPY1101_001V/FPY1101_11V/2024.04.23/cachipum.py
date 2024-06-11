import os
import time
import random
os.system("cls")

juegos = int(input("Indique la cantidad de juegos > "))


for i in range(juegos):
    menu = True
    while menu:
        print("=== CACHIPUM ===")
        print("1. piedra")
        print("2. papel")
        print("3. tijera")
        opcion = 0
        try:
            opcion = int(input("ingresa una de las opciones > "))
        except:
            print("La opción debe ser numérica ")

        if opcion < 1 or opcion > 3:
            print("La opción es inválida, intente nuevamente")
            time.sleep(2)
            os.system("cls")
        else:
            menu = False

            eleccion = ""
            eleccion_enemigo = ""

            if opcion == 1:
                eleccion = "PIEDRA"
            elif opcion == 2:
                eleccion = "PAPEL"
            elif opcion == 3:
                eleccion = "TIJERAS"
            else:
                eleccion = "ERROR"

            # la opcion del enemigo 
            op_enemigo = random.randint(1,3)

            if op_enemigo == 1:
                eleccion_enemigo = "PIEDRA"
            elif op_enemigo == 2:
                eleccion_enemigo = "PAPEL"
            elif op_enemigo == 3:
                eleccion_enemigo = "TIJERAS"
            else:
                eleccion_enemigo = "ERROR"

            os.system("cls")
            if opcion == 1 and op_enemigo == 3 or opcion == 2 and op_enemigo == 1 or opcion == 3 and op_enemigo == 2:
                print("==== GANASTE ====")
            elif opcion == 3 and op_enemigo == 1 or opcion == 1 and op_enemigo == 2 or opcion == 2 and op_enemigo == 3:
                print("===== PERDIMOS =====")
            elif opcion == op_enemigo:
                print("===== EMPATE ======")

            print(f"{eleccion} VS {eleccion_enemigo}")
            print("====================")

    seguir_jugando = int(input("desea seguir jugando 1:SI 2:NO"))
    if seguir_jugando == 1:
        juegos = juegos-1
    
