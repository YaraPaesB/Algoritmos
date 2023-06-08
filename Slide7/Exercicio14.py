fatorial = 1
while True:
    n= int(input("Digite o valor a ser calculado: "))
    if n >=0:
        break
    print("Valor inválido, o valor tem que ser maior do que 0!")

    if (n == 0) or (n == 1):
        fatorial = 1

    else:

        for i in range(1, n+1):
            fatorial *= i

print(f"O valor de {n}! é igual a {fatorial}")