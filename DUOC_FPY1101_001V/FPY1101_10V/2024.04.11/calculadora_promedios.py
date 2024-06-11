import os # se delara solo una vez
os.system("cls") # limpiar pantalla

try:
    cantidad_notas = int(input("ingresa la cantidad de notas > "))
except:
    print("Debe ser un número")

suma_notas = 0

for cualquier_palabra in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota número {cualquier_palabra+1}: "))
    suma_notas = suma_notas + nota

print(f"el promedio es: {suma_notas/cantidad_notas}")
