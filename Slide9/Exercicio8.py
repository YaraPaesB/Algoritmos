def ordenaVetor(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

A = []
B = []
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    A.append(numero)

B = A.copy()

ordenaVetor(B)

print("Vetor A:", A)
print("Vetor B:", B)