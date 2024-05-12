import os
import time
os.system("clear")

# acumuladores
cant_pullmay = 0
cant_cancato = 0
cant_cazuela_cordero = 0
cant_curanto = 0
cant_asado_cordero = 0

# boleta
total_productos = 0
nombre_descuento = ""
descuento = 0
subtotal = 0
total = 0

anular = 0

menu_general = True
while menu_general:
    os.system("clear")
    print("===== EL CHILOTE =====")
    print("1. PULLMAY \t\t$11.000")
    print("2. CANCATO \t\t$10.000")
    print("3. CAZUELA CORDERO \t$9.500")
    print("4. CURANTO \t\t$12.000")
    print("5. ASADO CORDERO \t$15.000")
    print("6. ANULAR PEDIDO")
    print("7. PAGAR")
    
    opcion_general = 0 
    
    try:
        opcion_general = int(input("Ingrese una de las opciones disponibles >> "))
    except:
        print("La opción debe ser numérica")
        
    if opcion_general < 1 or opcion_general > 7:
        print("Opción fuera de rango")
        time.sleep(2)
        os.system("clear")
        # os.system("cls")
    else:
    
        if opcion_general == 1:
            try:
                cant_pullmay += int(input("Ingrese la cantidad de PULLMAYS que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 2:
            try:
                cant_cancato += int(input("Ingrese la cantidad de CANCATOS que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 3:
            try:
                cant_asado_cordero += int(input("Ingrese la cantidad de CAZUELAS DE CORDERO que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 4:
            try:
                cant_curanto += int(input("Ingrese la cantidad de CURANTOS que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 5:
            try:
                cant_asado_cordero += int(input("Ingrese la cantidad de ASADOS DE CORDERO que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 6:
            try:
                anular = int(input("¿Realmente desea anular el pedido? \n1: SI \n2: NO"))
            except:
                print("La opción debe ser numérica")
            if anular == 1:
                print("PEDIDO ANULADO")
                menu_general = False
        elif opcion_general == 7:
            total_productos = cant_pullmay + cant_cancato+ cant_asado_cordero + cant_curanto + cant_asado_cordero
            if total_productos == 0:
                print("No puede pagar sin comprar")
                time.sleep(2)
                os.system("clear")
            else:
                
                menu_descuento = True
                while menu_descuento:
                    print("=== DESCUENTOS DISPONIBLES ===")
                    print("1. CLIENTE FRECUENTE 15%")
                    print("2. FUNCIONARIO SALUD 10%")
                    print("3. FUNCIONARIO MUNICIPAL 7%")
                    print("4. NO POSEE DESCUENTO 0%")
                    opcion_descuento = 0
                    try:
                        opcion_descuento = int(input("Ingrese una de las opciones disponibles >> "))
                    except:
                        print("La opción debe ser numérica")
                    
                    if opcion_descuento < 1 or opcion_descuento > 4:
                        print("Opción fuera de rango")
                        time.sleep(2)
                        os.system("clear")
                        # os.system("cls")
                    else:
                        if opcion_descuento == 1:
                            nombre_descuento = "CLIENTE FRECUENTE"
                            descuento = 15
                        elif opcion_descuento == 2:
                            nombre_descuento = "FUNCIONARIO SALUD"
                            descuento = 10
                        elif opcion_descuento == 3:
                            nombre_descuento = "FUNCIONARIO MUNICIPAL"
                            descuento = 7
                        elif opcion_descuento == 4:
                            nombre_descuento = "NO POSEE DESCUENTO"
                            descuento = 0
                        else:
                            print("Opción no disponible")
                        
                        os.system("clear")
                        print("============== EL CHILOTE ==============")
                        print("----------------------------------------")
                        print(f"TOTAL PRODUCTOS {total_productos}")
                        print("----------------------------------------")
                        if cant_pullmay > 0:
                            print(f"PULLMAY \t\t${cant_pullmay*11000}")
                        if cant_cancato > 0:
                            print(f"PULLMAY \t\t${cant_cancato*10000}")
                        if cant_asado_cordero > 0:
                            print(f"PULLMAY \t\t${cant_asado_cordero*9500}")
                        if cant_curanto > 0:
                            print(f"PULLMAY \t\t${cant_curanto*12000}")
                        if cant_asado_cordero > 0:
                            print(f"PULLMAY \t\t${cant_asado_cordero*15000}")
                        print("----------------------------------------")
                        subtotal = cant_pullmay*11000 + cant_cancato*10000 + cant_asado_cordero*9500 + cant_curanto*12000 + cant_asado_cordero*15000
                        print(f"SUBTOTAL \t\t${subtotal}")
                        print("DESCUENTO")
                        print(f"{descuento}% {nombre_descuento} \t${subtotal*descuento/100}")
                        print("----------------------------------------")
                        total = subtotal-descuento
                        print(f"TOTAL \t\t\t ${total}")
                        print("----------------------------------------")
                        print("¡GRACIAS POR SU COMPRA! :D")
                        
                        menu_descuento = False
                        menu_general = False
                
        else:
            print("Opción no disponible")
            
        