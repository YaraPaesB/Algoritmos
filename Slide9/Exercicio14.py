matriz = []
for i in range(10):
    linha = []
    for j in range(20):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

soma_linhas = []
for linha in matriz:
    soma = sum(linha)
    soma_linhas.append(soma)

matriz_resultante = []
for i in range(10):
    linha_resultante = []
    for j in range(20):
        elemento_resultante = matriz[i][j] * soma_linhas[i]
        linha_resultante.append(elemento_resultante)
    matriz_resultante.append(linha_resultante)

print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)