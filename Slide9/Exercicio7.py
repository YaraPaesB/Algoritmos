def primoOuNao(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

numerosPrimos = []
numeroAtual = 101

while len(numerosPrimos) < 10:
    if primoOuNao(numeroAtual):
        numerosPrimos.append(numeroAtual)
    numeroAtual += 1

print(numerosPrimos)