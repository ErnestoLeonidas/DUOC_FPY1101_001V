import os
os.system("cls")

nombres = []

for i in range(3):
    nom = input(f"{i+1}. Ingresa un nombre >> ")
    nombres.append(nom)

print(nombres)

nombres.sort()
print(nombres)

nombres.sort(key=len)
print(nombres)

nombres.sort(key=len, reverse=True)
print(nombres)

print(nombres[0])
