def parOuNao(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Digite um numero: "))
res = parOuNao(n)
if res == True:
    print(f"O valor {n} é par.")
else:
    print(f"O valor {n} não é par.")