import os
import time
os.system("cls")

cant_pantalon_corto = 0
cant_pantalon_largo = 0
cant_pantalon_jean = 0

menu_general = True
while menu_general:
    print("=== FALAFERIA ===")
    print("1. Pantalones")
    print("2. Camisas")
    print("3. Zapatos")
    print("4. Otros")
    print("5. Imprimir Boleta")
    print("6. Salir")
    opcion_general = 0
    try:
        opcion_general = int(input("Ingrese una de las opciones > "))
    except:
        print("La opción debe ser númerica")
    
    if opcion_general < 1 or opcion_general > 6:
        print("La opción no esta disponible, seleccione nuevamente")
        time.sleep(2)
        os.system("cls")
    else:
        os.system("cls")
        if opcion_general == 1:
            menu_pantalones = True
            while menu_pantalones:
                print("==== PANTALONES ====")
                print("1. Corto \t $ 9000")
                print("2. Largo \t $ 12000")
                print("3. Jeans \t $ 15000")
                print("4. Volver al menú anterior")
                opcion_pantalones = 0
                try:
                    opcion_pantalones = int(input("Ingrese una de las opciones > "))
                except:
                    print("La opción debe ser númerica")
                
                if opcion_pantalones < 1 or opcion_pantalones > 4:
                    print("La opción no esta disponible, seleccione nuevamente")
                    time.sleep(2)
                    os.system("cls")
                else:

                    if opcion_pantalones == 1:
                        cant_pantalon_corto += int(input("Ingresa la cantidad de pantalones cortos que desas > "))
                    elif opcion_pantalones == 2:
                        cant_pantalon_largo += int(input("Ingresa la cantidad de pantalones largos que desas > "))
                    elif opcion_pantalones == 3:
                        cant_pantalon_jean += int(input("Ingresa la cantidad de Jeans que deseas > "))
                    elif opcion_pantalones == 4:
                        menu_pantalones = False
                os.system("cls")

        elif opcion_general == 2:
            print("==== Camisas ====")
            print("1. De Vestir \t $ 9500")
            print("2. Guayabera \t $ 10000")
            print("3. Roja \t $ 12000")
        
        elif opcion_general == 5:
            print("================== BOLETA ==================")
            print("CANT \t| NOMBRE \t\t| COSTO \t| TOTAL")
            print(f"{cant_pantalon_corto} \t| Pantalon Corto \t| $ 9000 \t| ${cant_pantalon_corto*9000}")
            print(f"{cant_pantalon_largo} \t| Pantalon Largo \t| $12000 \t| ${cant_pantalon_largo*12000}")
            print(f"{cant_pantalon_jean} \t| Jeans \t\t| $15000 \t| ${cant_pantalon_jean*15000}")
            print("============================================")
            total = cant_pantalon_corto*9000 + cant_pantalon_largo*12000 + cant_pantalon_jean*15000
            print(f"TOTAL: {total}")
            print("=========== GRACIAS POR LA COMPRA =========")

            menu_general = False

    # menu_general = False