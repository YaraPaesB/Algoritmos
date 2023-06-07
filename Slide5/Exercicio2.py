nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 3.0:
    print("Reprovado")
elif media < 6.0:
    print("Exame")
    notaExame = 10 - media
    print(f"A nota necessária no exame é {notaExame}")
else:
    print("Aprovado")