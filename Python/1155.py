soma = 0

for i in range(1, 101):
    soma += 1/i

print("{:.2f}".format(soma))

#1156
soma = 0
denominador = 1

for numerador in range(1, 40, 2):
    soma += numerador/denominador
    denominador *= 2

print("{:.2f}".format(soma))