# crear un listado para registrar los datos de una
# persona: nombre, apellido, edad, peso y estatura
import os
os.system("cls")

persona = []

nombre = input("Ingrese su nombre >> ")
apellido = input("Apellido >> ")
edad = int(input("Edad >> "))
peso = float(input("Peso >> "))
estatura = float(input("Estatura >> "))

persona.append(nombre)
persona.append(apellido)
persona.append(edad)
persona.append(peso)
persona.append(estatura)

print(persona)
print(persona[:2])
print(persona[-2:])