N = int(input())

for i in range(N):
    X, Y = map(int, input().split())
    soma = 0
    while Y > 0:
        if X % 2 != 0:
            soma += X
            Y -= 1
        X += 1
    print(soma)
