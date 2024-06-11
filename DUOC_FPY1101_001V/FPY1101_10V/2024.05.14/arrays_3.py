import os
os.system("cls")

listado_trabajadores = []
print("listado inicial: ", listado_trabajadores)

for i in range(3):
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Registra tu edad: ")
    trabajador = [nombre,apellido,edad]
    # append permite agregar informacion a un array
    listado_trabajadores.append(trabajador)

print("listado final: ", listado_trabajadores)