# limpiar pantalla
import os
os.system("cls")

# el salto de linea se usa \n

print("Este texto es tan largo que \n necesita ocupar 2 lineas y para ello uso el \ n")


nombre = input("Ingrese su nombre > ")
rut = input("Ingrese su rut > ")
correo = input("Ingrese su correo > ")
telefono = int(input("Ingrese su telefono > "))


# para tabular usamos alt+92 \t
print(f"NOMBRE: \t{nombre}")
print(f"RUT: \t\t{rut}")
print(f"CORREO: \t{correo}")
print(f"TELEFONO: \t{telefono}")

print(f"NOMBRE: \t{nombre} \n RUT: \t\t{rut} \n CORREO: \t{correo} \n TELEFONO: \t{telefono} ")