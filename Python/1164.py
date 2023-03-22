n = int(input())

for i in range(n):
    x = int(input())
    soma = 0
    for j in range(1, x):
        if(x % j == 0):
            soma += j
    if(soma == x):
        print("%d eh perfeito" %x)
    else:
        print("%d nao eh perfeito" %x)
