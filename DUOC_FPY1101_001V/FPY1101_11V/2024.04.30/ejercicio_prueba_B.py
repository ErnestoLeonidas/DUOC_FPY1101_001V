import os
import time
os.system("cls")

cantidad_tradicional = 0
cantidad_peperoni = 0
cantidad_all_carnes = 0

subtotal = 0
descuento = 0

total_pagar = 0

menu_pizzas = True
while menu_pizzas:
    os.system("cls")
    print("=== PIZZA DUOC ===")
    print("1. Pizza Tradicional \t $12.000")
    print("2. Pizza Peperoni \t $14.000")
    print("3. Pizza All carne \t $17.000")
    print("4. Pagar")
    print("5. Cancelar pedido")
    opcion_pizzas = 0

    try:
        opcion_pizzas = int(input("Ingrese una de las opciones disponibles > "))
    except:
        print("La opción debe ser numerica")
    
    if opcion_pizzas < 1 or opcion_pizzas > 5:
        print("La opcion no esta disponible, intente nuevamente")
        time.sleep(2)
        os.system("cls")
    else:

        if opcion_pizzas == 1:
            try:
                cantidad_tradicional += int(input("Ingrese la cantidad de pizzas tradicionales que deseas > "))
            except:
                print("La opción debe ser numerica")
                time.sleep(2)
                os.system("cls")
        elif opcion_pizzas == 2:
            try:
                cantidad_peperoni += int(input("Ingrese la cantidad de pizzas peperoni que deseas > "))
            except:
                print("La opción debe ser numerica")
                time.sleep(2)
                os.system("cls")
        elif opcion_pizzas == 3:
            try:
                cantidad_all_carnes += int(input("Ingrese la cantidad de pizzas all carnes que deseas > "))
            except:
                print("La opción debe ser numerica")
                time.sleep(2)
                os.system("cls")
        elif opcion_pizzas == 4:

            if cantidad_tradicional == 0 and cantidad_peperoni == 0 and cantidad_all_carnes == 0:
                print("DEBE COMPRAR ANTES DE PAGAR")
                time.sleep(2)
                os.system("cls")
            else:
                menu_descuento = True
                while menu_descuento:
                    os.system("cls")
                    print("=== DESCUENTOS ===")
                    print("1. Estudiante Diurno \t\t 12%")
                    print("2. Estudiante Vespertino \t 10%")
                    print("3. Administrativo \t\t 0%")
                    opcion_descuento = 0
                    try:
                        opcion_descuento = int(input("Ingrese una de las opciones disponibles > "))
                    except:
                        print("La opción debe ser numerica")
                    
                    if opcion_descuento < 1 or opcion_descuento > 3:
                        print("La opcion no esta disponible, intente nuevamente")
                        time.sleep(2)
                        os.system("cls")
                    else:
                        if opcion_descuento == 1:
                            descuento = 12
                        elif opcion_descuento == 2:
                            descuento = 10
                        elif opcion_descuento == 3:
                            descuento = 0
                        else:
                            print("opción no válida")
                        
                        menu_descuento = False
                
                #boleta
                os.system("cls")
                print("==== PIZZAS DUOC ====")
                print("----------------------------------")
                if cantidad_tradicional > 0:
                    print(f"{cantidad_tradicional} Pizza Tradicional \t${cantidad_tradicional*12000}")
                if cantidad_peperoni > 0:
                    print(f"{cantidad_peperoni} Pizza Peperoni \t${cantidad_peperoni*14000}")
                if cantidad_all_carnes > 0:
                    print(f"{cantidad_all_carnes} Pizza All Carnes \t${cantidad_all_carnes*17000}")
                print("----------------------------------")

                subtotal = cantidad_tradicional*12000 + cantidad_peperoni*14000 + cantidad_all_carnes*17000

                print(f"Subtotal \t\t${subtotal}")
                print(f"Descuento {descuento}% \t\t${subtotal*descuento/100}")
                print("----------------------------------")
                
                total_pagar = subtotal - subtotal*descuento/100

                print(f"Total a Pagar \t\t${total_pagar}")
                print("----------------------------------")
                print("GRACIAS POR SU COMPRA!")

                menu_pizzas = False

        elif opcion_pizzas == 5:
            print("=== PEDIDO CANCELADO ===")
            time.sleep(2)
            os.system("cls")
            menu_pizzas = False
        else:
            print("opción fuera de rango")