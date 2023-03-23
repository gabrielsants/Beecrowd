operacao = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))
if operacao == 'S':
    soma = 0
    cont = 11
    
    for i in range(11,0,-1):
        for j in range(0,cont):
            soma += matriz[i][j]
        cont -= 1
    print('{:.1f}'.format(soma))
else:
    soma = 0
    cont = 11
    cont2 = 0
    for i in range(11,0,-1):
        for j in range(0, cont):
            soma += matriz[i][j]
            cont2 += 1
        cont -= 1
    media = soma / cont2
    print('{:.1f}'.format(media))
