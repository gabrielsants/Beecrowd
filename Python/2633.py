import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    carne = []
    for i in range(n):
        line = input().strip().split()
        carne.append((line[0], int(line[1])))
    carne.sort(key=lambda x: x[1])
    print(" ".join([x[0] for x in carne]))
