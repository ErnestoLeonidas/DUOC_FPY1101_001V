import os
os.system("cls")

todos_los_pedidos = []

def menu_general():
    os.system("cls")
    print("== GAS EXPLOSIVE ==")
    print("1. Registrar Pedido")
    print("2. Listar Todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

def elegir_opcion(max_option):
    while True:
        opcion = 0
        try:
            opcion = int(input("Ingresa una de las opciones disponibles >> "))
        except:
            pass

        if opcion < 1 or opcion > max_option:
            input("opción no disponible, intente nuevamente")
        else:
            return opcion

def registrar_pedido():
    os.system("cls")
    print("=== REGISTRAR PEDIDO ===")

    nombre = input("Ingrese su Nombre: ")
    apellido = input("Ingrese su Apellido: ")
    comuna = input("Ingrese su comuna: ")
    cilindros = seleccionar_cilindros()

    todos_los_pedidos.append( [nombre, apellido, comuna, cilindros] )

    input(todos_los_pedidos)

def seleccionar_cilindros():
    cant_5kg = 0
    cant_15kg = 0
    cant_45kg = 0
 
    while True:
        os.system("cls")
        print("Seleccione el gas que desea comprar: ")
        print("1. Cilindro 5kg")
        print("2. Cilindro 15kg")
        print("3. Cilindro 45kg")

        opcion = elegir_opcion(3)

        if opcion == 1:
            try:
                cant_5kg += int(input("Ingrese la cantidad de cilindros de 5kg que desea comprar >> "))
            except:
                input("la cantidad debe ser numerica, presione enter para continuar >> ")
        elif opcion == 2:
            try:
                cant_15kg += int(input("Ingrese la cantidad de cilindros de 15kg que desea comprar >> "))
            except:
                input("la cantidad debe ser numerica, presione enter para continuar >> ")
        elif opcion == 3:
            try:
                cant_45kg += int(input("Ingrese la cantidad de cilindros de 45kg que desea comprar >> "))
            except:
                input("la cantidad debe ser numerica, presione enter para continuar >> ")
        
        print("Desea seguir comprando | 1: SI 2: NO | >> ")
        salir = elegir_opcion(2)

        if salir == 2:
            return {
                "5kg": cant_5kg,
                "15kg": cant_15kg,
                "45kg": cant_45kg
            }





def iniciar_programa():
    menu = True
    while menu:
        menu_general()
        opcion = elegir_opcion(4)
        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            print("2. Listar Todos los pedidos")
        elif opcion == 3:
            print("3. Imprimir hoja de ruta")
        elif opcion == 4:
            print("4. Salir del programa")
            menu = False


iniciar_programa()