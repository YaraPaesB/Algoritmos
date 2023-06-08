totIdade = 0
cont = 0
while True:
    idade = int(input("Digite uma idade: "))
    totIdade += idade
    cont += 1
    if idade == 0:
        break
media = totIdade / cont

print(f"O total de pessoas é de {cont} e a idade media é de {media}")