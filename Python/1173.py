n = []
x = int(input())
def getDouble(x):
    return x * 2

for i in range(10):
    if(i == 0):
        n.append(x)
    else:
        n.append(getDouble(n[i-1]))

for i in range(10):
    print("N[{}] = {}".format(i, n[i]))
  