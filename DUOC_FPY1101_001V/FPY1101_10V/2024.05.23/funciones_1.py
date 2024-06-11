import os
os.system("cls")

def menu_calculadora():
    menu = True
    while menu:
        os.system("cls")
        print("== CALCULADORA ==")
        print("1. Suma")
        print("2. Resta")
        opcion = 0
        try:
            opcion = int(input("Ingresa una de las opciones >> "))
        except:
            print("la opción debe ser numérica, intente nuevamente")
        if opcion < 1 or opcion > 2:
            input("Opción fuera de rango, presione enter para continuar")
        else:
            return opcion

# input(f"la opcion elegida es : {menu_calculadora()}")
# input(f"la OTRA opcion elegida es : {menu_calculadora()}")

def sumar(num1, num2):
    return num1 + num2

def acciones(var_elegida):
    if var_elegida == 1:
        os.system("cls")
        print("== OPCION SUMAR ==")
        numero_1 = int(input("Ingresa el primer número >> "))
        numero_2 = int(input("Ingresa el segundo número >> "))

        input(f"la suma de los 2 numeros es {sumar(numero_1, numero_2)}")
        
    elif var_elegida == 2:
        input("OPCION RESTA")
    
acciones(menu_calculadora())
        
