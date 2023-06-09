def calcular_mdc(a, b):
    if a == 0 or b == 0:
        return max(abs(a), abs(b))
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(calcular_mdc(12, 18))