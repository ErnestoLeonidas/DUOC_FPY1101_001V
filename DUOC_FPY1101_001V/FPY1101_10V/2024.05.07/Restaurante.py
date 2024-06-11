import os
import time
os.system("cls")

# acumuladores
cant_camaron = 0
cant_mongoliana = 0
cant_pollo = 0
cant_carne = 0
cant_parrillada = 0

cant_productos = 0
subtotal = 0
nombre_descuento = ""
descuento = 0
total = 0

menu_general = True
while menu_general:
    os.system("cls")
    print("=== SHIN WHE WENSHA ===")
    print("1. Camarón Mandarín \t$11.000")
    print("2. Carne Mongoliana \t$10.000")
    print("3. Chapsui Pollo \t$ 9.500")
    print("4. Chapsui Carne \t$12.000")
    print("5. Parrillada China \t$15.000")
    print("6. Anular pedido")
    print("7. Pagar")
    opcion_general = 0

    try:
        opcion_general = int(input("Ingrese una de las opciones disponibles >> "))
    except:
        print("La opción debe ser numérica")
    
    if opcion_general < 1 or opcion_general > 7:
        print("Opción fuera de rango")
        time.sleep(2)
        os.system("cls")
    else:
        if opcion_general == 1:
            try:
                cant_camaron += int(input("ingrese la cantidad de Camarón Mandarín que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 2:
            try:
                cant_mongoliana += int(input("ingrese la cantidad de Carne Mongoliana que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 3:
            try:
                cant_pollo += int(input("ingrese la cantidad de Chapsui Pollo que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 4:
            try:
                cant_carne += int(input("ingrese la cantidad de Chapsui Carne que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 5:
            try:
                cant_parrillada += int(input("ingrese la cantidad de Parrillada China que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 6:
            try:
                anular = int(input("¿Realmente desea anular el pedido?, 1:SI 2:NO >> "))
            except:
                print("La opción debe ser numérica")
            
            if anular == 1:
                os.system("cls")
                print("PEDIDO ANULADO")
                menu_general = False

        elif opcion_general == 7:
            cant_productos = cant_camaron + cant_mongoliana + cant_carne + cant_pollo + cant_parrillada
            if cant_productos == 0:
                os.system("cls")
                print("Sin comprar no puede pagar.")
                time.sleep(2)
            else:
                menu_descuento = True
                while menu_descuento:
                    print("=== DESCUENTOS DISPONIBLES ===")
                    print("1. Cliente Frecuente \t15%")
                    print("2. Tarjeta Vecino \t10%")
                    print("3. Carnet tercera edad \t7%")
                    print("4. No posee descuento \t0%")
                    opcion_descuento = 0

                    try:
                        opcion_descuento = int(input("Ingrese una de las opciones disponibles >> "))
                    except:
                        print("La opción debe ser numérica")
                    
                    if opcion_descuento < 1 or opcion_descuento > 4:
                        print("Opción fuera de rango")
                        time.sleep(2)
                        os.system("cls")
                    else:
                        if opcion_descuento == 1:
                            nombre_descuento = "CLIENTE FRECUENTE"
                            descuento = 15
                        elif opcion_descuento == 2:
                            nombre_descuento = "TARJETA VECINO"
                            descuento = 10
                        elif opcion_descuento == 3:
                            nombre_descuento = "TERCERA EDAD"
                            descuento = 7
                        elif opcion_descuento == 4:
                            nombre_descuento = "SIN DESCUENTO"
                            descuento = 0
                        else:
                            print("opción no válida")

                        os.system("cls")
                        print("=== BOLETA ===")
                        print("---------------------------------")
                        if cant_camaron >0:
                            print(f"{cant_camaron} CAMARON MANDARIN \t${cant_camaron*11000}")
                        if cant_mongoliana > 0:
                            print(f"{cant_mongoliana} CARNE MONGOLIANA \t${cant_mongoliana*10000}")
                        if cant_pollo > 0:
                            print(f"{cant_pollo} CHAPSUI POLLO \t${cant_pollo*9500}")
                        if cant_carne > 0:
                            print(f"{cant_carne} CHAPSUI CARNE \t${cant_carne*12000}")
                        if cant_parrillada > 0:
                            print(f"{cant_parrillada} PARRILLADA CHINA\t${cant_parrillada*15000}")
                        print("---------------------------------")
                        subtotal = cant_camaron*11000+cant_mongoliana*10000+cant_pollo*9500+cant_carne*12000+cant_parrillada*15000
                        print(f"SUBTOTAL \t\t${subtotal}")
                        print("DESCUENTO:")
                        print(f"{descuento}% {nombre_descuento} \t${int(subtotal*descuento/100)}")
                        print("---------------------------------")
                        total = subtotal - descuento
                        print(f"TOTAL \t\t\t${total}")
                        print("---------------------------------")
                        input()
        else:
            print("opción no está disponible")