C = int(input())
op = input().upper()

M = []
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    M.append(row)

start_row = 0
start_col = C
end_row = 11
end_col = C

total = 0
count = 0
for i in range(12):
    for j in range(12):
        if i >= start_row and i <= end_row and j >= start_col and j <= end_col:
            total += M[i][j]
            count += 1

if op == 'S':
    result = total
else:
    result = total / count

print('{:.1f}'.format(result))