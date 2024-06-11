import os
os.system("cls")

numeros = [10,2,8,4,5,6,7,3,9,1]
numeros.append(11) # agrega un elemento al final del listado
numeros.sort() # ordena el listado de menor a mayor
numeros.sort(reverse=True) # ordena el listado de mayor a menor
numeros.pop() # borra el ultimo elemento del listado
numeros.remove(8) # borra el dato indicado dentro del remove()
# numeros.remove(13) # si el dato indicado no se encuentra dara error
print(numeros)
numeros.pop(2) # borra el elemento del listado segun su indice
print(numeros)
numeros.clear() # borra todos los elemento del listado
print(numeros)
