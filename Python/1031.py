def remaining(n, k):
    r = 0
    for i in range(1, n):
        r = (r + k) % i
    return r

while True:
    n = int(input())
    if n == 0:
        break
    y = 1
    while True:
        if remaining(n, y) != 11:
            y += 1
        else:
            break
    print(y)