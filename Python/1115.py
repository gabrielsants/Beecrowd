while True:
    data = input().split()
    x, y = int(data[0]), int(data[1])
    
    if(x == 0 or y == 0):
        break
    elif x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("quarto")