frase = input("Digite a frase: ")
qtd = 0
for letra in frase:
    if letra.lower() in 'aeiouáéíóúâêôàãô':
        qtd += 1
print(f"A quantidade de vogais é de {qtd}")