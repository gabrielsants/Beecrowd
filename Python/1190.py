matriz=[]
linha = input()

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

soma = 0
cont = 0
col = 11
for i in range(1,11):
    for j in range(col,12):
        soma += matriz[i][j]
        cont += 1
    if(i < 5):
        col -= 1
    if(i > 5):
        col += 1

med = soma / cont

if linha == "S":
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(med))