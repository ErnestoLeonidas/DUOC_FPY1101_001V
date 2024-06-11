import os
os.system("cls")

animales = ["Perro", "Gato", "Hamster"]

# animales.sort() # ordenar de menor a mayor
# animales.sort(reverse=True) # ordenar de mayor a menor
# animales.sort(key=len)  # Ordena por la cantidad de letras de menor a mayor
# animales.sort(key=len, reverse=True) # Ordena por la cantidad de letras de mayor a menor
# print(animales) # ojo que no pueden ordenar a la misma vez que se hace el print porque mostraria None

# animales.pop(0)
# animales[:-1]

for i, animal in enumerate(animales):
    print(i)