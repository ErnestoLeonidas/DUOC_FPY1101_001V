import os
os.system("cls")

list_notas = []
print(f"listado notas inicial {list_notas}")

for i in range(4):
    nota = float(input(f"Ingresa una nota número {i+1} >> "))
    list_notas.append(nota)
    # list_notas.append(float(input(f"Ingresa una nota número {i+1} >> ")))

list_notas.sort()
print(f"listado notas final {list_notas}")