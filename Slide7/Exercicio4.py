print("Digite 0 quando quiser parar.")
tot = 0
cont = 0
while True:
    num = int(input("Digite um numero"))
    if num % 2 == 0:
        tot += num
        cont += 1
    elif num == 0:
        break

media = tot / cont

print(f"A media dos valores pares é de {media}")