anoNasc = int(input("Em que ano você nasceu? "))
anoAtual = int(input("Em que ano estamos? "))

anos = anoAtual - anoNasc
meses = anos * 12
dias = anos * 365
semanas = meses * 4

print(f"Você tem {anos} anos, ou {meses} meses, ou {dias} dias, ou {semanas} semanas.")