hora = float(input("Digite as horas (HH.MM): "))

horas = int(hora)
minutos = int((hora - horas) * 60)

totalMinutos = horas * 60 + minutos

print(f"A hora digitada vale {totalMinutos} minutos.")