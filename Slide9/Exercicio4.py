def reverseWord(palavra):
    palavraRev = palavra[::-1]
    return palavraRev

vetor = []
reversedVetor = []
for i in range(20):
    x = (input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
for i in range(20):
    palavraRev = reverseWord(vetor[i])
    reversedVetor.append(palavraRev)

print(reversedVetor)
