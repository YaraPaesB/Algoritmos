preco = float(input("Insira o preço do produto: "))
codOrigem = input("Insira o codigo de origem: ")
taxa = 0.0

if codOrigem == "1":
    print("Seu produto vem do Sul.")
    taxa = preco * (11/100)
elif codOrigem == "2":
    print("Seu produto vem do Norte.")
    taxa = preco * (13/100)
elif codOrigem == "3":
    print("Seu produto vem do Nordeste.")
    taxa = preco * (9/100)
elif codOrigem == "4":
    print("Seu produto vem do Centro-Oeste.")
    taxa = preco * (12/100)
elif codOrigem == "5":
    print("Seu produto vem do Sudeste.")
    taxa = preco * (18/100)

precoFinal = preco + taxa
print(f"A taxa de imposto do seu produto é de {taxa}, e p preço final é de {precoFinal}")



