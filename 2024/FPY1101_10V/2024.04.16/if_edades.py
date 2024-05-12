# limpiar pantalla
import os
os.system("cls")

edad = int(input("Ingrese una edad > "))

if edad >= 0 and edad < 18:  # si Entonces
    print("Es menor de edad")

elif edad >= 18:            # de otro modo
    print("Es adulto mayor")
else:                       # siNo
    print("No ha nacido, esta en proceso")

# and
# or