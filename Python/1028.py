def mdc(a,b):
    return a if not b else mdc(b, a % b)

data = int(input())

for i in range(data):
    a,b = input().split(' ')
    a, b = int(a), int(b)
    print(mdc(a,b))
