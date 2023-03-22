a = []
for i in range(100):
    x = float(input())
    a.append(x)
for i in range(100):
    if(a[i] <= 10):
        print("A[{}] = {:.1f}".format(i, a[i]))
