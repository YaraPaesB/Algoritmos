lista1 = []
lista2 = []
conjunto = []

for i in range(5):
    x = int(input("Digite um valor: "))
    lista1.append(x)
for i in range(5):
    x = int(input("Digite um valor: "))
    lista2.append(x)

conjunto = set(lista1 + lista2)

print(conjunto)