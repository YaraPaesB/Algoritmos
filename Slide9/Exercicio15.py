matriz = []
for i in range(8):
    linha = []
    for j in range(8):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

simetrica = True
for i in range(8):
    for j in range(i+1, 8):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("A matriz digitada é simétrica.")
else:
    print("A matriz digitada não é simétrica.")