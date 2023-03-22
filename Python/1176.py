t = int(input())

for i in range(t):
    n = int(input())
    fib = [0, 1]
    
    for j in range(2, n+1):
        fib.append(fib[j-1] + fib[j-2])
    print("Fib({}) = {}".format(n, fib[n]))
