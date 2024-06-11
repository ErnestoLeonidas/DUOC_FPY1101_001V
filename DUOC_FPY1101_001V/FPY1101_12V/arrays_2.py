import os
os.system("cls")

        #   0          1        2     3    4    5
persona = ["Alan", "Brito", "Doctor", 30, 1.8, False]

print(persona[2]) # obtenemos el dato en la posicion 2
print(persona[:2]) # mostrar los primeros 2 elementos del array
print(persona[2:]) # borra los primero 2 elementos del array
print(persona[-2]) # trae solamente el penúltimo elemento del array
print(persona[:-2]) # borra los últimos 2 elementos del array
print(persona[-2:]) # trae solamente los últimos 2 elementos
print(persona[::2]) # salta de a 2 elementos
print(persona[::-1]) # invierte el orden de los elementos de un array