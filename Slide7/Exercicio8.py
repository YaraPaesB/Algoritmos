def primoOuNao(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False


n = int(input("Digite um numero: "))

res = primoOuNao(n)

if res == True:
    print("Esse numero é um numero primo.")
else:
    print("Esse numero não é um numero primo")

