operacao = input()
matriz = []
soma = 0
quantidade = 0

for i in range(12):
    linha = []
    for j in range(12):
        elemento = float(input())
        linha.append(elemento)
        if j > i:
            soma += elemento
            quantidade += 1

    matriz.append(linha)

if operacao == 'S':
    resultado = soma
elif operacao == 'M':
    resultado = soma / quantidade

print('{:.1f}'.format(resultado))