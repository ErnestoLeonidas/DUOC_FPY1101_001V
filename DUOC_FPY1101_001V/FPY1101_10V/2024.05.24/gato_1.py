import os
os.system("cls")

tablero = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

jugador = "X"
opciones_X = []
opciones_O = []

def mostrar_tablero():
    os.system("cls")
    print("== GATO ==")
    t = ""
    for fila in tablero:
        for num in fila:
            if num in opciones_X:
                t += f"| X "
            elif num in opciones_O:
                t += f"| O "
            else:
                t += f"| {num} "
        t += "|\n"

    print(t)

def opcion_elegida():
    opcion = int(input(f"Jugador {jugador} selecciona >> "))

    if opcion < 1 or opcion > 9:
        return False
    elif opcion in opciones_X or opcion in opciones_O:
        input("Opción no disponible, presione enter para continuar >> ")
        return False
    else:
        if jugador == "X":
            opciones_X.append(opcion)
        else:
            opciones_O.append(opcion)
        return True

def hay_ganador():
    jugadas_ganadoras = [
        (1,2,3),(4,5,6),(7,8,9),     # filas
        (1,4,7),(2,5,8),(3,6,9),    # columnas
        (1,5,9),(3,5,7)             # diagonal
    ]

    for jugadas in jugadas_ganadoras:
        if all(pos in opciones_X for pos in jugadas):
            input("Gano el X")
        if all(pos in opciones_O for pos in jugadas):
            input("Gano el O")

ganador = False
while ganador == False:
    mostrar_tablero()
    print("opciones X = ", opciones_X)
    print("opciones O = ", opciones_O)

    hay_ganador()
    if opcion_elegida():
        jugador = "O" if jugador == "X" else "X"
    else:
        input("opcion elegida devolvio False, hubo un error")




