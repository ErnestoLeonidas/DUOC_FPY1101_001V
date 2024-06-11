import os
os.system("cls")

# persona = ["alan", "brito"]
persona = {
    "nombre": "Alan",
    "apellido": "Brito",
    "edad": 30,
    "peso": 75.5,
    "estatura": 1.75,
    "sexo": "M"
}

print(persona)

print(persona["nombre"]) # visualizar el dato de un diccionario según su clave (key)
print(persona["edad"])

persona["edad"] = 18 # modificar un registro del diccionario

print(persona["edad"])

persona["ocupacion"] = "Estudiante" # creamos y agregamos elementos al diccionario

print(persona["ocupacion"])
print(persona)

for dato in persona:
    print(dato)