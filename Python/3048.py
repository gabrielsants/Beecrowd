n = int(input())
seq = [int(input()) for _ in range(n)]

last = 0
count = 0
for i in range(n):
    if seq[i] != last:
        last = seq[i]
        count += 1

print(count)
