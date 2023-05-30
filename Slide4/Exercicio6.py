salario = float(input("Salario do funcionario: "))
aumento = float(input("Percentual de aumento(%): "))

novoSal = salario + (salario * aumento/100)

print(f"O salario do funcionario apos sofrer {aumento}% de aumento é de {novoSal}")