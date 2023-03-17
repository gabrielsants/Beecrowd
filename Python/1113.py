while True:
    data = input().split()
    x, y = int(data[0]), int(data[1])
    
    if(x == y):
        break
    
    if(x > y):
        print('Decrescente')
    else:
        print('Crescente')