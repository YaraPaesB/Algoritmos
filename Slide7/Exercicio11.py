tot = 0
while True:
    m = int(input("Digite um numero: "))
    n = int(input("Digite outro numero: "))
    if m <= n:
        print("O primeiro valor precisa ser maior.")
    else:
        for i in range(n, m+1):
            tot += i
    print(f"Soma de todos os numeros inteiros entre os valores {tot}")

