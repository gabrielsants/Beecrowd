numeros = []
pares = 0

for i in range(5):
    numeros.append(int(input()))

for num in numeros:
    if num % 2 == 0:
        pares += 1

print('%d valores pares' %pares)