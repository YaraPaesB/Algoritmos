alturaCm = float(input("Digite a altura do degrau em centímetros: "))
alturaFinal = float(input("Digite a altura que deseja alcançar em metros: "))

alturaM = alturaCm / 100
qtdDegraus = int(alturaFinal / alturaM)

print(f"Número de degraus a subir: {qtdDegraus}")