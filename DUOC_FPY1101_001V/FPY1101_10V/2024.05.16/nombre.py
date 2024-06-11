# Escriba su nombre completo una variable y muestre la
# cantidad de vocales y consonantes que tiene
import os
os.system("cls")

nombre = "aiaoaiaoiaoaiaoi".lower()
vocales = 0
consonantes = 0

todas_vocales = ["a","e","i","o","u"]

for letra in nombre:
    if letra in "aeiou":
        vocales += 1
    elif letra == " ":
        pass
    else:
        consonantes += 1

print(f"VOCALES: {vocales}")
print(f"CONSONANTES: {consonantes}")