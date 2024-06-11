import os
import time
os.system("cls")

menu = True
while menu:
    print("=== TIENDA ===")
    print("1. lapices $500")
    print("2. Goma borrar $300")
    print("3. Sacapuntas $200")
    opcion = 0

    while opcion < 1 or opcion > 3:
        try:
            opcion = int(input("Ingrese una de las opciones > "))
        except:
            print("la opción debe ser numérica")

        if opcion < 1 or opcion > 3:
            print("la opción no es valida, intente nuevamente")
            time.sleep(2)
            os.system("cls")
    
    menu = False

valor_producto = 0
nombre_producto = ""

if opcion == 1:
    valor_producto = 500
    nombre_producto = "lapices"
elif opcion == 2:
    valor_producto = 300
    nombre_producto = "Goma borrar"
elif opcion == 3:
    valor_producto = 200
    nombre_producto = "Sacapuntas"
else:
    nombre_producto = "No definido"

print("===== BOLETA =====")
print(f"Producto: {nombre_producto}")
print(f"Valor: {valor_producto}")
print("==================")