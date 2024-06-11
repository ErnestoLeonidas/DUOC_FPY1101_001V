import os
os.system("cls")

empleados = [
    ["Pedro", "Pascal", "Doctor"],
    ["Alan", "Brito", "Auxiliar"],
    ["Maria","Dolores", "Enfermera"]
]

print(empleados[1][2])

for empleado in empleados:
    print(empleado[2])

for empleado in empleados:
    for info in empleado:
        print(info)