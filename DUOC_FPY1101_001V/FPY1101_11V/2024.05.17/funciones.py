import os
os.system("cls")

# completar el menu de bebidas-
def menu():
    print("== BEBIDA ==")
    print("1. COCA COLA")
    print("2. PESPI")

def menu2():
    print("== CALCULADORA ==")
    print("1. SUMA")
    print("2. RESTA")
    opcion = int(input("Ingrese una de las opciones >> "))
    calculadora(opcion)

def suma(num_1,num_2):
    return num_1+num_2

def restar(num1, num2):
    result = num1 - num2
    print("El resultado de la resta es", result)

def calculadora(op):
    if op == 1:
        num_1 = int(input("Ingresa el primer número >> "))
        num_2 = int(input("Ingresa el segundo número >> "))
        print(suma(num_1,num_2))
    elif op == 2:
        numero1 = int(input("Ingresa el primer número >> "))
        numero2 = int(input("Ingresa el segundo número >> "))
        restar(numero1, numero2)

menu2()