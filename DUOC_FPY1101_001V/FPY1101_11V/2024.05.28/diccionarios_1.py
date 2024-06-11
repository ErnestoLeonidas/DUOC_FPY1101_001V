import os
os.system("cls")

# personas = ["alan", "brito", 18]

persona = {
    "nombre": "alan",
    "apellido": "Brito",
    "edad": 18,
    "peso": 75.5,
    "estatura": 1.8,
    "telefonos": [555555,66666,88888],
    "soltero": True
} 

print(persona)
print(persona["apellido"])
print(persona["telefonos"])
print(persona["soltero"])

persona["edad"] = 20
print(persona["edad"])

persona["trabajo"] = "Jornalero"

for key in persona:
    print(f"clave: {key} - valor: {persona[key]}")



