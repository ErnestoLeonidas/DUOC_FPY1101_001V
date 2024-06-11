edad = int(input("Ingrese su edad > "))

if edad == 0 and edad < 1 :
    print("Nació")
elif edad < 18:
    print("Joven")
elif edad >= 18:
    print("Adulto Joven")
else:
    print("Edad no válida")