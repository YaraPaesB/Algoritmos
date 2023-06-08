num = int(input("Digite um numero: "))
e = 0

for i in range(0, num+1):
    e += 2**i
    print(e, end=" ")
