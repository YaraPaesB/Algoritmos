vetor = []
vetor2 = []
intercalado = []
for i in range(10):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
for i in range(10):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor2.append(x)

for i in range(10):
    intercalado.append(vetor[i])
    intercalado.append(vetor2[i])

print(intercalado)