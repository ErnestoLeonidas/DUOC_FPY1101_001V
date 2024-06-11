# limpiar pantalla
import os
os.system("cls")

# etapa 1
print("Bienvenido al mundo de la programación")
nom = input("Para comenzar ingresa tu nombre > ")

# para comentar rapido:  ctl+k+c
# descomentar rápido: ctl+k+u
# etapa 2
print(f"Bienvenido {nom}")

# etapa 3
# para elevar un numero se usa doble * 
# ej: 3**3 3 elevado a 3
x = int(input("Ingrese un número > "))
resultado = (x**2+3*x+1)/4
print(f"El resultado es {resultado}")
