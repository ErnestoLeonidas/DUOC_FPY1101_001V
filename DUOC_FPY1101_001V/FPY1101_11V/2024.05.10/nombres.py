import os
os.system("cls")

nombres = []

for i in range(3):
    nombre = input("ingrese un nombre >> ")
    nombres.append(nombre)

# ordena de menor a mayor alfabeticamente o numericamente
nombres.sort()

# nombres.sort(reverse=True)
print(nombres)

# orderar texto según la cantidad de caracteres
# por defecto de menor a mayor
nombres.sort(key=len)
# Ordenar de mayor a menor
nombres.sort(key=len, reverse=True)

print(nombres[2])