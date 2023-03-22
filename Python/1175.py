n = []

for i in range(20):
    x = int(input())
    n.append(x)
    
for i in range(10):
    temp = n[i]
    n[i] = n[19-i]
    n[19-i] = temp
    
for i in range(20):
    print("N[{}] = {}".format(i, n[i]))
