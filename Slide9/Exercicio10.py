matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

MaiorElemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > MaiorElemento:
            MaiorElemento = elemento

matrizRes = []
for linha in matriz:
    linhaRes = []
    for elemento in linha:
        linhaRes.append(elemento * MaiorElemento)
    matrizRes.append(linhaRes)

print("Matriz resultante:")
for linha in matrizRes:
    print(linha)