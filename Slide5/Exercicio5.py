anoNasc = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite em qual ano estamos:"))

idade = anoAtual - anoNasc

if idade >= 18:
    print("Você já pode votar e tirar sua CNH.")
elif idade >= 16:
    print("Você já pode votar.")
else:
    print("Você ainda não pode votar nem tirar sua CNH.")