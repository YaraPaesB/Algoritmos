salarioMin = float(input("Digite o valor do salário mínimo: "))
wattsConsumidos = float(input("Digite a quantidade de quilowatts consumida pela residência: "))

valorWatt = salarioMin / 8
total = valorWatt * wattsConsumidos
desconto = total * 0.85

print(f"O valor de cada quilowatt em reais é R$ {valorWatt}")
print(f"O valor a ser pago pela residência em reais é R$ {total}")
print(f"O valor a ser pago com desconto de 15% em reais é R$ {desconto}")
