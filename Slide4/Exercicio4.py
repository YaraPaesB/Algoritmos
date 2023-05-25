diaNasc, mesNasc, anoNasc = (input("Insira sua data de nascimento (dd/mm/aaaa): ")).split("/")
diaAtual, mesAtual, anoAtual = (input("Insira a data atual (dd/mm/aaaa): ")).split("/")

anos = 0
meses = 0
dias = 0
semanas = 0

if int(mesNasc) > int(mesAtual):
    anos = (int(anoAtual) - int(anoNasc)) - 1
    meses = ((12 - int(mesNasc)) + int(mesAtual))
else:
    anos = (int(anoAtual) - int(anoNasc))
    meses = ((int(mesAtual)) - int(mesNasc))

if int(diaNasc) > int(diaAtual):
    dias = (30 - int(diaNasc) + int(diaAtual))

else:
    dias = int(diaAtual) - int(diaNasc)

if dias > 7:
    semanas = dias/7
    semanas = round(semanas)

print(f"Idade: {anos} anos, {meses} meses, {semanas} semanas e {dias} dias.")

