import os
os.system("cls")

# agregar a un listado sus 4 notas del semestre que espera tener
# luego imprimir ese listado
notas = []

for i in range(4):
    try:
        nota = float(input("Ingrese su nota>> "))   
    except:
        print("La nota debe ser numerica ")
    
    notas.append(nota)

notas.sort(key=len)

print(notas)