import os
os.system("cls")

list_personas = []
cantidad_personas = int(input("Cuantas personas? >>"))

for i in range(cantidad_personas):
    nombre = input("Ingrese su nombre >> ")
    apellido = input("Apellido >> ")
    edad = int(input("Edad >> "))
    peso = float(input("Peso >> "))
    estatura = float(input("Estatura >> "))

    pesona = [nombre, apellido, edad, peso, estatura]
    list_personas.append(pesona)

print(list_personas)