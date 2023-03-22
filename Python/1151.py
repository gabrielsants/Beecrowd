n = int(input())

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

fib_str = ' '.join(map(str, fib))

print(fib_str)