x = int(input("Digite o primeiro valor"))
y = int(input("Digite o segundo valor"))
z = int(input("Digite o terceiro valor"))

if x < (y+z) and y < (x+z) and z < (x+y):
    if x == y and y == z:
        print("Os valores formam um triangulo equilátero.")
    elif (x == y != z) or (y == z != x) or (x == z != y):
        print("Os valores formam um triangulo isósceles")
    elif x != y != z:
        print("Os valores formam um triangulo escaleno")
else:
    print("Os valores não formam um triangulo.")