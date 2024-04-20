import os # se delara solo una vez
os.system("cls") # limpiar pantalla

# for básico, repite x cantidad de veces
for i in range(10):
    print(f"ciclo : {i}")

for i in range(15,20): # for desde un inicio (5) hasta un final (10)
    print(f"ciclo : {i}")

for i in range(32,40,2): # el tercer parametro es de cuanto en cuanto aumenta (i) en cada ciclo
    print(f"ciclo : {i}")