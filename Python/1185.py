operacao = input()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

soma = 0
contador = 0

for i in range(12):
    for j in range(12):
        if i + j < 11:
            soma += matriz[i][j]
            contador += 1

if operacao == 'S':
    resultado = soma
else:
    resultado = soma / contador

print('{:.1f}'.format(resultado))
