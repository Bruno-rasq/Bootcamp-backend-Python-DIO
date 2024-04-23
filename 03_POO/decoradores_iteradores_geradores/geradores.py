def gerador_pares(maximo):
    for i in range(maximo):
        if i % 2 == 0:
            yield i

for numero in gerador_pares(10):
    print(numero)