import os # libreria para limpiar pantalla
import time # libreria para el pausar
os.system("cls")

ciclo = True
while ciclo:
    print("===== BEBIDAS =====")
    print("1. COCA-COLA \t $ 900")
    print("2. PEPSI \t $ 900")
    print("3. INKACOLA \t $ 950")
    print("4. 7UP \t\t $ 950")
    print("5. FANTA \t $ 850")

    opcion = 0
    try:
        opcion = int(input("Ingrese una de las opciones > "))
    except:
        print("no se puede ingresar texto")
    
    if opcion < 1 or opcion > 5:
        print("Opción no válida, intente nuevamente")
        time.sleep(1.5)
        os.system("cls")
    else:
        ciclo = False

valor = 0
producto = ""

if opcion == 1:
    valor = 900
    producto = "COCA-COLA"
elif opcion == 2:
    valor = 900
    producto = "PEPSI"
elif opcion == 3:
    valor = 950
    producto = "INKACOLA"
elif opcion == 4:
    valor = 950
    producto = "7UP"
elif opcion == 5:
    valor = 850
    producto = "FANTA"
else:
    valor = 0
    producto = "NO DEFINIDO"

dinero = 0
while dinero < valor:
    try:
        dinero_ingresado = int(input("Ingrese su dinero > "))
        dinero = dinero + dinero_ingresado

        # o puede usar el +=
        # dinero += int(input("Ingrese su dinero > "))

        if dinero <= valor:
            print(f"Aún falta ingresar ${valor-dinero}")
            
    except:
        print("El valor ingresado debe ser numerico")


os.system("cls")
print("===== BOLETA =====")
print(f"producto : {producto}")
print(f"total : ${valor}")
print(f"dinero: ${dinero}")
print(f"vuelto : ${dinero-valor}")
print("== GRACIAS POR SU COMPRA ==")

