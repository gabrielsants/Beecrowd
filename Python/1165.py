import math

n = int(input())

for i in range(n):
    x = int(input())
    eh_primo = True
    if x <= 1:
        eh_primo = False
    else:
        for j in range(2, int(math.sqrt(x))+1):
            if x % j == 0:
                eh_primo = False
                break
    if eh_primo:
        print("{} eh primo".format(x))
    else:
        print("{} nao eh primo".format(x))
