n = int(input())
x = 0
y = 0
for i in range(n):
    data = input().split()
    x = int(data[0])
    y = int(data[1])
    
    if x > y:
        x, y = y, x
    
    soma = 0
    for i in range(x+1, y):
        if i % 2 != 0:
            soma += i
    print(soma)