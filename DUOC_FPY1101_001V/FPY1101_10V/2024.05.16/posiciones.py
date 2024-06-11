import os
os.system("cls")

nombre = "Alan Brito"
nombre.upper()      # Texto a mayúsculas
nombre.lower()      # Texto a minúsculas
print(nombre[3])    # Tercera letra de la cadena o array
print(nombre[-2])   # Penúltima letra de la cadena o array
print(nombre[:3])   # Primeras 3 letras o elementos de un array
print(nombre[3:])   # Elimina las primeras 3 letras o elementos de un array
print(nombre[:-3])  # Elimina las últimas 3 letras o elementos de un array
print(nombre[-3:])  # Últimas 3 letras o elementos de un array
print(nombre[::3])  # Obtiene las letras cada 3 o elementos de un array
print(nombre[::-1]) # Obtiene las letras o elementos de un array en orden inverso 
print(len(nombre))  # Obtiene la cantidad de elementos de un array
print(nombre[2:4])  # Obtiene los elementos desde una posición hasta otra de la cadena

# Crea una clave con 
# Los 2 primeros dígitos del primer nombre en mayúsculas
# Los 3 últimos caracteres del apellido parteno en minúscula
# La cantidad de caracteres totales del apellido materno