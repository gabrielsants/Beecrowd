x = float(input())
n = []
def getDivision(x):
    return x / 2
for i in range(100):
    if(i == 0):
        n.append(x)
    else:
        n.append(getDivision(n[i-1]))

for i in range(100):
    print("N[{}] = {:.4f}".format(i, n[i]))
