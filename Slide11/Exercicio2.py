dicionario = {}
for i in range(10):
    sobrenome = input(f"Digite o sobrenome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    dicionario[sobrenome] = idade

pessoa_mais_velha = max(dicionario, key=dicionario.get)



print("Sobrenome da pessoa mais velha:", pessoa_mais_velha)