import os   # libreria para limpiar pantalla
import time # libreria para esperar
os.system("cls")    # limpiar pantalla

# para el simbolo alt+92 \
menu = True
while menu:
    print("==== BEBIDAS ====")
    print("1. COCA-COLA \t $800")
    print("2. 7UP \t\t $800")
    print("3. INKACOLA \t $700")
    print("4. PEPSI \t $750")

    opcion = 0
    try:
        opcion = int(input("Ingrese una de las opciones disponibles > "))
    except:
        print("La opcion solo puede ser numérica")

    if opcion < 1 or opcion > 4:
        print("La opción no es válida, intente nuevamente")
        time.sleep(2)   # pausa x cantidad de tiempo
        os.system("cls")  # limpiar pantalla
    else:
        menu = False

nombre_producto = ""
valor_producto = 0

if opcion == 1:
    nombre_producto = "COCA COLA"
    valor_producto = 800
elif opcion == 2:
    nombre_producto = "7UP"
    valor_producto = 800
elif opcion == 3:
    nombre_producto = "INKACOLA"
    valor_producto = 700
elif opcion == 4:
    nombre_producto = "PEPSI"
    valor_producto = 750
else:
    nombre_producto = "No definido"

print("===== BOLETA =====")
print(f"Producto: \t{nombre_producto} ")
print(f"Valor: \t\t${valor_producto}")
print("==================")