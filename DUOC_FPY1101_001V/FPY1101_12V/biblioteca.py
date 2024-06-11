import os
os.system("cls")

biblioteca = [
    ["S1","S2","S3","S4"],
    ["C1","C2","C3","C4","C5","C6"],
    ["P1","P2","P3"]
]

elementos_disponibles = []
salas_reservada = []
compus_reservados = []
puestos_reservados = []

def menu_principal():
    os.system("cls")
    print("== RESERVAS ==")
    print("1. Reservar Salas")
    print("2. Reservar Computadores")
    print("3. Reservar Puestos")
    print("4. Cancelar Reserva")
    print("5. Listar Reserva")
    print("6. Salir")

def elegir_opcion(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingresa una de las opciones >> "))
        except:
            pass

        if opcion < 1 or opcion > max_opcion:
            input("Opción fuera de rango, intente nuevamente")
        else:
            return opcion

def dibujar_biblioteca():
    print("S: Salas")
    print("C: Computadores")
    print("P: Puestos")
    print("\n")

    print(f"salas_reservada: {salas_reservada}")
    print("\n")

    b = ""
    for elemento in biblioteca:
        for i in elemento:
            # recorremos elemento por elemento

            # asignamos todos los elementos al listado 
            # de elementos disponibles uno por uno
            elementos_disponibles.append(i)

            b += f"| {i} "
        b += "|\n"

    print(b)

def reservar_sala():
    dibujar_biblioteca()

    opcion = input("Ingresa una de las salas disponibles >> ")

    # necesitamos validar que la sala exista :  opcion in elementos_disponibles
    # y tambien que este disponible:            and opcion not in salas_reservada
    if opcion in elementos_disponibles and opcion not in salas_reservada:
        print("EXISTE Y ESTA DISPONIBLE ")
        salas_reservada.append(opcion)
    else:
        print("NO EXISTE O ESTA OCUPADA")


salir = False
while not salir:
    menu_principal()
    opcion = elegir_opcion(6)

    if opcion == 1:
        print("\n== RESERVAR SALA ==")
        reservar_sala()
    elif opcion == 2:
        print("\n== RESERVAR COMPUTADORES ==")
    elif opcion == 3:
        print("\n== RESERVAR PUESTOS ==")
    elif opcion == 4:
        print("\n== CANCELAR RESERVAS ==")
    elif opcion == 5:
        print("\n== LISTAR RESERVAS ==")
    elif opcion == 6:
        print("\n== SALIR ==")
        salir = True
    
    input()



