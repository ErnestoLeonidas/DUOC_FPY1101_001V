import os
os.system("cls")

cine = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50],
    [51,52,53,54,55,56,57,58,59,60],
    [61,62,63,64,65,66,67,68,69,70],
    [71,72,73,74,75,76,77,78,79,80],
    [81,82,83,84,85,86,87,88,89,90],
    [91,92,93,94,95,96,97,98,99,100]
]

def menu_general():
    os.system("cls")
    print("=== CINE ====")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def seleccionar_opcion(max_opciones):
    while True:
        opcion = 0
        try:
            opcion = int(input("Seleccione una de las opciones disponibles >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opciones:
            input("La opción fuera de rango, presione enter para continuar >> ")
        else:
            return opcion

def mostrar_cine():


def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)

        if opcion == 1:
            print("1. Comprar entradas")
        elif opcion == 2:
            print("2. Mostrar ubicaciones disponibles")
        elif opcion == 3:
            print("3. Ver listado de asistentes")
        elif opcion == 4:
            print("4. Mostrar ganancias totales")
        elif opcion == 5:
            print("5. Salir")
        input()

iniciar_programa()