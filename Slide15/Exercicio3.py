RA = input("Seu RA: ")

lista = list(RA)
soma = 0
mult = 1
for i in range(len(lista)):
    soma += int(lista[i])

for i in range(len(lista)):
    mult = (mult * int(lista[i]))

print(f"A lista é {lista}")
print(f"A soma dos valores da lista é: {soma}")
print(f"A multiplicação dos valores da lista é: {mult}")