while True:
    data = input().split()
    x1 = int(data[0])
    y1 = int(data[1])
    x2 = int(data[2])
    y2 = int(data[3])
    
    if(x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
        break
    elif(x1 == x2 and y1 == y2):
        print("0")
    elif((x2-x1) == -(y2-y1) or -(x2-x1) == -(y2-y1) or -(x2-x1) == (y2-y1) or (x2-x1) == (y2-y1)):
        print("1")
    elif(x1 == x2 or y1 == y2):
        print("1")
    else:
        print("2")