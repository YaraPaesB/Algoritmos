num1 = int(input("Digite um numero: "))
num2 = int(input("Outro numero: "))

print("----------------------------------------")
print("Escolha uma opção:")
print("1 - Média entre os dois números")
print("2 - Diferença do maior pelo menor")
print("3 - Produto entre os dois numeros")
print("4 - Divisão do primeiro pelo segundo")
print("----------------------------------------")

opcao = input("Digite o numero referente a sua ecolha: ")

if opcao == "1":
    result = (num1 + num2)/2
    print(f"O resultado da sua operação é {result}")
elif opcao == "2":
    if num1 > num2:
        result = num1 - num2
        print(f"O resultado da sua operação é {result}")
    elif num1 == num2:
        print("Os dois numeros são iguais")
    else:
        result = num2 - num1
        print(f"O resultado da sua operação é {result}")
elif opcao == "3":
    result = num1 * num2
    print(f"O resultado da sua operação é {result}")
elif opcao == "4":
    result = num1 / num2
    print(f"O resultado da sua operação é {result}")
else:
    print("Valor invalido. Rode novamente.")

