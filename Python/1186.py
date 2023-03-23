op = input()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0

for i in range(12):
    for j in range(12):
        if j > 11 - i:
            soma += matriz[i][j]

if op == 'S':
    print('{:.1f}'.format(soma))
elif op == 'M':
    media = soma / 66
    print('{:.1f}'.format(media))
