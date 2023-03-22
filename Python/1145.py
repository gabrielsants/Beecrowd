x, y = map(int, input().split())
num = 1
for i in range(1, int(y/x)+1):
    res = ""
    for i in range(x):
        res += str(num)+" "
        num+=1
    print(res[:-1])