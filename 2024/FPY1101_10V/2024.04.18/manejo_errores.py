import os # se delara solo una vez
os.system("cls") # limpiar pantalla

try: # inicialia la captura de errores
    numero = int(input("Ingresa un número > ")) 
    print(f"El número es: {numero}")
except: # esto se ejecuta cuando ocurre un error
    print("Se requiere el ingreso un número")