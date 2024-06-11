import os
os.system("cls")

pokemones = []

for i in range(5):
    nuevo_pokemon = input("Ingrese un pokemon >> ")
    # para agregar elementos a un array se utiliza .append()
    pokemones.append(nuevo_pokemon)

    print(f"pokemones en el listado: {pokemones}")
