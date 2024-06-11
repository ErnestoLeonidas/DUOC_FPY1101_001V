import os
os.system("cls")

tablero = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
]

# print(tablero)
todas_las_opciones = []
opciones_X = []
opciones_O = []

juego = True
while juego:
    os.system("cls")
    dibujar_tablero = ""

    for fila in tablero:
        for e in fila:
            todas_las_opciones.append(e)
            if e in opciones_X:
                dibujar_tablero += f"| X "
            elif e in opciones_O:
                dibujar_tablero += f"| O "
            else:
                dibujar_tablero += f"| {e} "
        dibujar_tablero += "|\n"

    print(dibujar_tablero)

    opcion = input("Selecciona una de las opciones >> ").upper()

    if opcion in todas_las_opciones:
        print("la opción está disponible y será usada")
        opciones_X.append(opcion)