vetor = []
maiorVal = 0
maiorValPos = 0
for i in range(10):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)

for i in range(len(vetor)):
    if vetor[i] > maiorVal:
        maiorVal = vetor[i]
        maiorValPos = i

print(f"O maior valor digitado é o {maiorVal}, que esta na posição {maiorValPos}")