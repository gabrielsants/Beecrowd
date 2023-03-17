n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        quadrado = i ** 2
        print("{}^2 = {:.0f}".format(i, quadrado))