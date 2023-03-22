n = int(input())
distancia = 0
for i in range(n):
    t, v = map(int, input().split())
    distancia += t * v
print(distancia)
