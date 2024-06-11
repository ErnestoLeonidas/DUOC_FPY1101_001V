import os
os.system("cls")

tablero = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

elecciones_X = []
elecciones_O = []

jugador = "X"

def menu_general():
    os.system("cls")
    t = ""
    print("=== GATO ===")
    for fila in tablero:
        for num in fila:
            if num in elecciones_X:
                t += f"| {color_amarillo('X')} "
            elif num in elecciones_O:
                t += f"| {color_amarillo('O')} "
            else:
                t += f"| {color_gris(num)} "
        t += "|\n"
    print(t)    
    
def eleccion(jugador):
    opcion = int(input(f"Jugador {jugador} selecciona >> "))
    
    if opcion in elecciones_X or opcion in elecciones_O:
        input("Opción ocupada, intente nuevamente ")
    else:
        elecciones_X.append(opcion) if jugador == "X" else elecciones_O.append(opcion)
        
def ganador():
    jugadas_ganadoras = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # filas
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columnas
        (1, 5, 9), (3, 5, 7)              # diagonales
    ]

    for combo in jugadas_ganadoras:
        if all(pos in elecciones_X for pos in combo):
            return "X"
        if all(pos in elecciones_O for pos in combo):
            return "O"
    return False

def color_amarillo(texto):
    return f"\033[1;33m{texto}\033[0;m"

def color_gris(texto):
    return f"\033[2;30m{texto}\033[0;m"

existe_ganador = False
while existe_ganador == False:
    menu_general()

    eleccion(jugador)
    if ganador() in ("X","O"):
        menu_general()
        print(f"¡Jugador {jugador} ha ganado!")
        existe_ganador = True
    else:
        jugador = 'O' if jugador == 'X' else 'X'
