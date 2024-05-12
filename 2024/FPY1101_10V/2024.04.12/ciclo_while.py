import os # se delara solo una vez
os.system("cls") # limpiar pantalla

# while simple
while True:
    print("Ciclo sin fin")
    break # para la ejecución del while

ciclo = True
while ciclo:
    print("Ciclo sin fin")
    ciclo = False

numero = 1
while numero < 10:
    numero = numero + 1 
    print(f"número : {numero}")