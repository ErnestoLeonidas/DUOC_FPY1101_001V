import os
os.system("cls")

personal = []

def menu_general():
    os.system("cls")
    print("== PESONAL ==")
    print("1. Registrar")
    print("2. Listar")
    print("3. Salir")

def elegir_opcion(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opción no válida, presione enter para continuar >> ")
        else:
            return opcion

def registrar_persona():
    os.system("cls")
    print("== REGISTRAR ==")

    nombre = input("Ingrese su nombre >> ")
    apellido = input("Ingrese su apellido >> ")
    edad = input("Ingrese su edad >> ")

    personal.append({
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad
    })
    
    input("Usuario registrado, presione enter para continuar >> ")

def listar_personal():
    os.system("cls")
    print("== LISTAR PERSONAL ==")

    print("| NOMBRE | APELLIDO | EDAD |")
    for persona in personal:
        print(f"| {persona['nombre']} | {persona['apellido']} | {persona['edad']}")
    
    input()

def iniciar_programa():
    while True:
        menu_general()
        opcion = elegir_opcion(3)
        if opcion == 1:
            registrar_persona()
        elif opcion == 2:
            listar_personal()
        elif opcion == 3:
            return

iniciar_programa()