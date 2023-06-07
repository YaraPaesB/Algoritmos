import math

num = int(input("Digite um numero: "))
quad = 0
cub = 0
raiz = 0
if num==0:
    print("Digite um valor maior que 0")
else:
    quad = num ** 2
    cub = num ** 3
    raiz = math.sqrt(num)

print(f"Ao quadrado, o numero é {quad}, ao cubo é {cub} e a raiz quadrada é {raiz}.")