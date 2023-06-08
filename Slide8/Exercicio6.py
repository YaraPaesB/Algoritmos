frase = input("Digite a frase: ").lower()
print(frase)
fraseLimpa = frase.replace(" ", "")
print(fraseLimpa)
fraseInvertida = fraseLimpa[::-1]
print(fraseInvertida)
if fraseLimpa == fraseInvertida:
    print("A frase é palindroma.")
else:
    print("A frase não é palindroma.")