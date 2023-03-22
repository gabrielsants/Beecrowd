n = int(input())
x = list(map(int, input().split()))

menor = x[0]
posicao = 0

for i in range(1, n):
    if x[i] < menor:
        menor = x[i]
        posicao = i

print("Menor valor:", menor)
print("Posicao:", posicao)