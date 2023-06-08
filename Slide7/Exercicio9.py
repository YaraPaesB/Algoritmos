b = int(input("Digite um numero: "))
n = int(input("Digite outro numero: "))
e = 0

for i in range(0, n):
    e += b**i
    print(e, end=" ")
