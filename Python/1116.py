n = int(input())
for i in range(n):
    data = input().split()
    x, y = int(data[0]), int(data[1])
    
    if(y == 0):
        print("divisao impossivel")
    else:
        resultado = x / y
        print("{:.1f}".format(resultado))