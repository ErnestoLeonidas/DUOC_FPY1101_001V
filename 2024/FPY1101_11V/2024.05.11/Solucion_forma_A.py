import os
import time
os.system("clear")


cant_pullmay = 0
cant_cancato = 0
cant_cazuela_cordero = 0
cant_curanto = 0
cant_asado_cordero = 0

total_productos = 0
nombre_descuento = ""
descuento = 0
subtotal = 0
total = 0

anular = 0

menu_general = True
while menu_general:
    os.system("clear")
    print("========== EL CHILOTE =========")
    print("1. PULLMAY \t\t$11.000")
    print("2. CANCATO \t\t$10.000")
    print("3. CAZUELA CORDERO \t$ 9.500")
    print("4. CURANTO \t\t$12.000")
    print("5. ASADO DE CORDERO \t$15.000")
    print("6. ANULAR PEDIDO")
    print("7. PAGAR PEDIDO")
    opcion_general = 0
    try:
        opcion_general = int(input("Ingrese una de las opciones disponibles >> "))
    except:
        print("La opción debe ser numérica")
    
    if opcion_general < 1 or opcion_general > 7:
        print("Opción ingresada está fuera de rango")
        print("Intente nuevamente")
        time.sleep(2)
        os.system("clear")
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
                cant_cazuela_cordero += int(input("Ingrese la cantidad de CAZUELAS DE CORDERO que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 4:
            try:
                cant_curanto += int(input("Ingrese la cantidad de CURANTOS que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general ==  5:
            try:
                cant_asado_cordero += int(input("Ingrese la cantidad de ASADOS DE CORDERO que desea >> "))
            except:
                print("La opción debe ser numérica")
        elif opcion_general == 6:
            try:
                anular = int(input("¿Realmente desea anular el pedido? \n1: SI \n2: NO \n>> "))
            except:
                print("La opción debe ser numérica")
            if anular == 1:
                os.system("clear")
                print("PEDIDO ANULADO")
                menu_general = False
        elif opcion_general == 7:
            total_productos = cant_pullmay + cant_cancato + cant_cazuela_cordero + cant_curanto + cant_asado_cordero
            if total_productos == 0:
                print("SIn comprar no puede pagar")
                time.sleep(2)
                os.system("clear")
            else:
                
                menu_descuento = True
                while menu_descuento:
                    os.system("clear")
                    print("===== DESCUENTOS DISPONIBLES =====")
                    print("1. CLIENTE FRECUENTE \t\t15%")
                    print("2. FUNCIONARIO SALUD \t\t10%")
                    print("3. FUNCIONARIO MUNICIPAL \t7%")
                    print("4. NO POSEE DESCUENTO \t\t0%")
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
                            nombre_descuento = "NO POSEE DESCUENTO "
                            descuento = 0
                        else:
                            print("Opción no disponible")
                        
                        os.system("clear")
                        print("============== EL CHILOTE ==============")
                        print("----------------------------------------")
                        print(f"TOTAL PRODUCTOS \t\t\t{total_productos}")
                        print("----------------------------------------")
                        if cant_pullmay > 0:
                            print(f"{cant_pullmay} PULLMAY \t\t${cant_pullmay*11000}")
                        if cant_cancato > 0:
                            print(f"{cant_cancato} CANCATO \t\t${cant_cancato*10000}")
                        if cant_asado_cordero > 0:
                            print(f"{cant_cazuela_cordero} CAZUELA CORDERO \t\t${cant_cazuela_cordero*9500}")
                        if cant_curanto > 0:
                            print(f"{cant_curanto} CURANTO \t\t${cant_curanto*12000}")
                        if cant_asado_cordero > 0:
                            print(f"{cant_asado_cordero} ASADO CORDERO \t\t${cant_asado_cordero*15000}")
                        print("----------------------------------------")
                        subtotal = cant_pullmay*11000 + cant_cancato*10000 + cant_cazuela_cordero*9500 + cant_curanto*12000 + cant_asado_cordero*15000
                        print(f"SUBTOTAL \t\t${subtotal}")
                        print("DESCUENTO")
                        print(f"{descuento}% {nombre_descuento} \t${int(subtotal*descuento/100)}")
                        print("----------------------------------------")
                        total = subtotal-subtotal*descuento/100
                        print(f"TOTAL \t\t\t${total}")
                        print("----------------------------------------")
                        print("¡GRACIAS POR SU COMPRA! :D")
                        
                        menu_descuento = False
                        menu_general = False
                        