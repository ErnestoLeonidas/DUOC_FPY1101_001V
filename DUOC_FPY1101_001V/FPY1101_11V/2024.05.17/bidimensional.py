import os
os.system("cls")

doctores = [
    ["Pedro","Pascal","Urgencias"],
    ["Maria","Dolores","Enfermería"],
    ["Alan","Brito","Auxiliar"]
]

print(doctores[2][1])

for doctor in doctores:
    print(doctor[0])

for doctor in doctores:
    for info in doctor:
        print(info)