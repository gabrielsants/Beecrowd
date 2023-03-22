x = []
for i in range(10):
    z = int(input())
    if(z <= 0):
        z = 1
    x.append(z)
    
for i in range(10):
    print("X[{}] = {}".format(i, x[i]))
    