tupla = ()
tupla2 = ()

for i in range(10):
        x = int(input(f"Digite o {i+1}º: "))
        tupla += (x,)

tupla2 = tuple(reversed(tupla))
print(tupla2)
