import os
os.system("cls")

edad = int(input("Ingrese su edad > "))

if edad > 0 and edad < 5:
    print("Niño/Niña")
elif edad >= 5 and edad < 18:
    print("Joven")
elif edad >= 18 and edad < 65:
    print("Adulto")
elif edad >= 65:
    print("Adulto Mayor")
else:
    print("Aún no nace, se esta creando")


print("Se terminó el código")
