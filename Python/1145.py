x, y = map(int, input().split())

num = 1
while num <= y:
    for i in range(x):
        if num <= y:
            print(num, end=' ')
            num += 1
    print()