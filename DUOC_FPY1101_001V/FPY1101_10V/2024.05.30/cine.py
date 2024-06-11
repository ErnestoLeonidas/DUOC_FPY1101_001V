import os
os.system("cls")

def menu_principal():
    os.system("cls")
    print("=== MENU CINE ===")
    print("1. Comprar Entrada")
    print("2. Cancelar Entrada")
    print("3. Visualizar Sala")
    print("4. Listar Ventas")

def elegir_menu(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una de las opciones disponibles >> "))
        except:
            pass
        
        if opcion < 1 or opcion > max_opcion:
            input("Opción fuera de rango, presione enter para continuar ")
        else:
            return opcion

sala = [
    ['A1','A2','A3','A4'],
    ['B1','B2','B3','B4'],
    ['C1','C2','C3','C4']
]

todos_los_asientos = []
asientos_ocupados = []
registro_clientes = []

def dibujar_sala_cine():
    dibujo = "\n== SALA 10 ==\n"

    print(registro_clientes)

    for fila in sala:
        for asiento in fila:
            todos_los_asientos.append(asiento) # acá guardamos cada asiento en el array de todos_los_asientos
            
            if asiento in asientos_ocupados:
                dibujo += f"| {color_rojo(asiento)} "
            else:
                dibujo += f"| {color_verde(asiento)} "
        dibujo += f"|\n"

    print(f"asientos ocupados : {asientos_ocupados}")

    print(dibujo)
    print("\n")


def comprar_entrada():
    asiento = input("Seleccione una de los asientos disponibles >> ")

    if asiento in todos_los_asientos and asiento not in asientos_ocupados:
        print(" asiento disponible ")
        asientos_ocupados.append(asiento)
        registrar(asiento)
    else:
        print(" asiento NO disponible ")

def registrar(entrada):
    nombre = input("Ingrese su nombre >> ")
    apellido = input("Ingrese su apellido >> ")
    edad = input("Ingrese su edad >> ")

    registro_clientes.append( [entrada, nombre, apellido, edad] )

def color_amarillo(texto):
    return f"\033[2;33m{texto}\033[0;m"

def color_rojo(texto):
    return f"\033[2;31m{texto}\033[0;m"

def color_verde(texto):
    return f"\033[2;32m{texto}\033[0;m"

def color_gris(texto):
    return f"\033[2;30m{texto}\033[0;m"

    # print(f"\033[2;30mcolor\033[0;m")   #30 gris
    # print(f"\033[2;31mcolor\033[0;m")   #31 rojo
    # print(f"\033[2;32mcolor\033[0;m")   #32 verde
    # print(f"\033[2;33mcolor\033[0;m")   #33 amarillo
    # print(f"\033[2;34mcolor\033[0;m")   #34 azul
    # print(f"\033[2;35mcolor\033[0;m")   #35 magenta
    # print(f"\033[2;36mcolor\033[0;m")   #36 celeste

def listar_ventar():
    ventas = "\n===== VENTAS =======\n"
    ventas +="| Asiento | Nombre \t| Apellido \t| Edad |\n"

    for cliente in registro_clientes:
        for info in cliente:
            ventas += f"| {info} \t"
        ventas += "\n"
    
    print(ventas)

salir = False
while not salir:
    menu_principal()

    opcion = elegir_menu(4)
    if opcion == 1:
        print("== COMPRAR ENTRADAS ==")
        dibujar_sala_cine()
        comprar_entrada()
    elif opcion == 2:
        print("== CANCELAR ENTRADAS ==")
    elif opcion == 3:
        print("== VISUALIZAR SALA ==")
        dibujar_sala_cine()
    elif opcion == 4:
        print("== LISTAR VENTAS ==")
        listar_ventar()
    
    input("presione enter para continuar")