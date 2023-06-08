num = input("Digite 9 caracteres numericos: ")

decimal = num[7:10]
centena = num[4:7]
milhar = num[1:4]
milhao = num[0]

pontuado = milhao + "." + milhar + "." + centena + "," + decimal

print(pontuado)
