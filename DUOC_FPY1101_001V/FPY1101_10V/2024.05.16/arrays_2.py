import os
os.system("cls")

nombre = "Alan Brito Delgado"

# recorre el texto letra por letra
for letra in nombre:
    print(letra)

# recorre el texto letra por letra y además podemos saber la posición
for i, letra in enumerate(nombre):
    print(f"{i} {letra}")

# Escriba su nombre completo una variable y muestre la
# cantidad de vocales y consonantes que tiene

            # 0     1       2   3     4
persona = ["Alan","Brito", 19, 1.8, False]
for i, info in enumerate(persona):
    print(f"{i} {info}")