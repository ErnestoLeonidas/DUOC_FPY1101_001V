import os
import time
os.system("cls")

menu = True
while menu:
    print("=== RESTAURANTE ===")
    print("1. Fideos \t\t $ 5000")
    print("2. Porotos \t\t $ 6000")
    print("3. Arroz con pio pio \t $ 5500")
    print("4. Hamburguesa \t\t $ 4000")
    opcion = 0
    
    try:
        opcion = int(input("Ingrese una de las opciones > "))
    except:
        print("La opción debe ser un número")

    if opcion < 1 or opcion > 4:
        print("La opción no es válida, intente nuevamente")
        time.sleep(1.5)
        os.system("cls")
    else:
        menu = False

valor_producto = 0
nombre_producto = ""

if opcion == 1:
    nombre_producto = "Fideos"
    valor_producto = 5000
elif opcion == 2:
    nombre_producto = "Porotos"
    valor_producto = 6000
elif opcion == 3:
    nombre_producto = "Arroz con pollo"
    valor_producto = 5500
elif opcion == 4:
    nombre_producto = "Hamburguesa"
    valor_producto = 4000
else:
    nombre_producto = "No definido"
    valor_producto = 0

pago = 0

while pago < valor_producto:
    try:
        pago += int(input("Ingrese su dinero a pagar > "))
    except:
        print("Debe ser un valor numérico")

    if pago < valor_producto:
        print(f"aún le falta : ${valor_producto-pago}")


os.system("cls")
print("==== BOLETA ====")
print(f"Producto: \t {nombre_producto}")
print(f"Valor: \t\t ${valor_producto}")
print(f"Monto Pagado: \t ${pago}")
print(f"Vuelto: \t ${pago-valor_producto}")
print("=== GRACIAS x COMPRAR ===")
