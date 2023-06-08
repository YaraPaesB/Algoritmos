def calImc(peso, altura):
    return peso / (altura**2)

maiorImc = 0
menorImc = 0
totAltura = 0
totPeso = 0

for i in range(0, 20):
    peso = float(input("Insira o peso: "))
    altura = float(input("Insira a altura: "))

    imc = calImc(peso, altura)

    totPeso += peso
    totAltura += altura

    if imc > maiorImc:
        maiorImc = imc
    elif imc < menorImc:
        menorImc = imc

mediaPeso = totPeso / 20
mediaAltura = totAltura / 20

print(f"O peso medio é de {mediaPeso}, e a altura media é de {mediaAltura}.")
print(f"O maior imc é de {maiorImc} e o menor imc é de {menorImc}")
