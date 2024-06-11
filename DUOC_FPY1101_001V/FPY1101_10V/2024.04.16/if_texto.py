# limpiar pantalla
import os
os.system("cls")

user = input("Ingrese su usuario > ")
clave = input("Ingrese su contraseña > ")

if user == "alan" and clave == "brito":
    print("usted es alan brito")
else:
    print("No se quien eres, chao")


# edad = int(input("Ingresa tu edad > "))
edad = input("Ingresa tu edad > ")

# if edad == 19:
if edad == "19":
    print("Es la edad de Alan Brito")
else:
    print("No es la edad indicada, clave bloqueada")