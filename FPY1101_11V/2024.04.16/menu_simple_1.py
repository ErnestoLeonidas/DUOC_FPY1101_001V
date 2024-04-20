import os
os.system("cls")

# menu simple
print("=== BEBIDAS ===")
print("1. CocaCola")
print("2. Pepsi")
print("3. InkaCola")
opcion = int(input("Ingrese una de las opciones > "))

# validamos que este dentro del rango con el OR
if opcion < 1 or opcion > 3:
    print("Opción no disponible, chao")