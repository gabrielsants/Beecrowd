n = int(input())
pares = []
impares = []

for i in range(n):
    value = int(input())
    if(value % 2 == 0):
        pares.append(value)
    else:
        impares.append(value)
pares.sort()
impares.sort(reverse=True)

for par in pares:
    print(par)
for impar in impares:
    print(impar)