t = int(input())
n = []
aux = 0
for i in range(1000):
    n.append(aux)
    if(aux == t-1):
        aux = 0
    else:
        aux += 1
for i in range(1000):
    print("N[{}] = {}".format(i, n[i]))
