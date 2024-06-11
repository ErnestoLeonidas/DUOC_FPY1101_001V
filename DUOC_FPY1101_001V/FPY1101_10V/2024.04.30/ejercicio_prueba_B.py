import os
import time
os.system("cls")

cantidad_tradicional = 0
cantidad_peperoni = 0
cantidad_all_carnes = 0
subtotal = 0
descuento = 0
total_pagar = 0

menu_pizza = True
while menu_pizza:
    os.system("cls")
    print("=== PIZZADUOC ===")
    print("1. Tradicional \t$12.000")
    print("2. Peperoni  \t$14.000")
    print("3. All Carnes \t$17.000")
    print("4. Pagar")
    print("5. Cancelar pedido")

    opcion = 0

    try:
        opcion = int(input("Ingresa una de las opciones > "))
    except:
        print("la opción no es valida")

    if opcion < 1 or opcion > 5:
        print("Opción fuera de rango, intente nuevamente")
        time.sleep(2)
        os.system("cls")
    else:

        if opcion == 1:
            try:
                cantidad_tradicional += int(input("Ingrese la cantidad de pizzas tradicionales que desea > "))
            except:
                print("Cantidad debe ser numerica")
        elif opcion == 2:
            try:
                cantidad_peperoni += int(input("Ingrese la cantidad de pizzas peperoni que desea > "))
            except:
                print("Cantidad debe ser numerica")
        elif opcion == 3:
            try:
                cantidad_all_carnes += int(input("Ingrese la cantidad de pizzas All Carnes que desea > "))
            except:
                print("Cantidad debe ser numerica")
        elif opcion == 4:
            # solicitar descuento
            os.system("cls")
            menu_descuento = True
            while menu_descuento:
                print("=== DESCUENTOS ===")
                print("1. Estuante Diurno \t\t 12%")
                print("2. Estudiante Vespertino \t 10%")
                print("3. Administrativos \t\t 0%")
                opcion_descuento = 0

                try:
                    opcion_descuento = int(input("ingrese una de las opciones disponibles > "))
                except:
                    print("la opción no es valida")

                if opcion_descuento < 1 or opcion_descuento > 3:
                    print("Opción fuera de rango, intente nuevamente")
                    time.sleep(2)
                    os.system("cls")
                else:
                    if opcion_descuento == 1:
                        descuento = 12 # porque es el 12%
                    elif opcion_descuento == 2:
                        descuento = 10
                    elif opcion_descuento == 3:
                        descuento = 0
                    else:
                        descuento = 0
                    
                    menu_descuento = False
            
            # boleta
            os.system("cls")
            print("=== PIZZAS DUOC ===")
            print("----------------------------")
            if cantidad_tradicional > 0:
                print(f"{cantidad_tradicional} pizza tradicional \t ${cantidad_tradicional*12000}")
            if cantidad_peperoni > 0:
                print(f"{cantidad_peperoni} pizza peperoni \t ${cantidad_peperoni*14000}")
            if cantidad_all_carnes > 0:
                print(f"{cantidad_all_carnes} pizza all carnes  \t ${cantidad_all_carnes*17000}")
            print("----------------------------")
            
            subtotal = cantidad_tradicional*12000 + cantidad_peperoni*14000 + cantidad_all_carnes*17000

            if subtotal > 0:
                print(f"Subtotal \t\t {subtotal}")
                print(f"Descuento {descuento}% \t\t ${subtotal*descuento/100}")

                total_pagar = subtotal-subtotal*descuento/100

                print("----------------------------")
                print(f"Total a pagar \t\t ${total_pagar}")
                print("\nGracias por su compra!")
                menu_pizza = False
            else:
                print("No hay productos para facturar")
                time.sleep(2)
                os.system("cls")

        elif opcion == 5:
            print("Pedido cancelado")
            time.sleep(2)
            os.system("cls")
            menu_pizza = False
        else:
            print("opción no valida")