altura = float(input("Qual sua altura: "))
sexo = input("Seu sexo (homem ou mulher): ")

if sexo == "homem":
    pesoIdeal = (72.7 * altura) - 58
elif sexo == "mulher":
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Valor inválido.")

print(f"Seu peso ideal é de {pesoIdeal}")