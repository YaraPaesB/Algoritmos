base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))

if base <= 0 or altura <= 0:
    print("Valores invalidos, os valores precisam ser maiores de 0")
else:
    area = (base * altura) / 2
    print(f"A area do triangulo equivale a {area}.")
    
