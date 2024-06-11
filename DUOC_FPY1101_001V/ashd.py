limite = 20
numero = 2
while numero < limite:
    es_primo = True
    divisor = 2

    while divisor <= numero // 2:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1

    if es_primo:
        print(numero) # ? 
    numero += 1
