def primoOuNao(n):
    if n>0 :
        cont = 0
        for i in range(1, n+1):
            if n%i==0:
                cont += 1
        if cont==2:
            return True
        else:
            return False

def qtdPrimos(n):
    cont = 0
    listaPrimos = []
    for i in range(0, n+1):
        result = primoOuNao(i)
        if result==True:
            cont += 1
            listaPrimos.append(i)
    return listaPrimos

'''código'''

Y = int(input("Os ultimos dois ultimos digitos do RA: "))
soma = 0
Y = Y*2 + 5
lista = qtdPrimos(Y)
for i in range(0, len(lista)):
    soma += lista[i]

print(f"O numero é primo? {primoOuNao(Y)}")
print(f"A lista de valores primos ate o valor {Y} é: {lista}")
print(f"A soma dos valores da lista é {soma}")




