print("=== BEBIDAS ===")
print("1. COCA-COLA")
print("2. PEPSI")
print("3. FANTA")
opcion = int(input("Ingrese una de las opciones > "))

if opcion < 1 or opcion > 3:
    print("opción no válida")

if opcion >= 1 and opcion <= 3:
    if opcion == 1:
        print("Eligió la coca cola")
    elif opcion == 2:
        print("Eligió PEPSI")
    elif opcion == 3:
        print("Eligió la FANTA")
    else:
        print("opción no válida en el ELSE")

