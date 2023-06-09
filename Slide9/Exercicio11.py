matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

somaDiagonal = 0
for i in range(4):
    somaDiagonal += matriz[i][i]

print(f"A soma dos elementos da diagonal principal é {somaDiagonal}")