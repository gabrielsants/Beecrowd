n = int(input())
while(n > 0):
    s = int(input())
    vector = []
    
    for i in range(s):
        if(i % 2 == 0):
            vector.append(1)
        else:
            vector.append(-1)
    print(sum(vector))
    n -= 1
