L = int(input())
op = input().upper()

M = []
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    M.append(row)

start_row = L
start_col = 0
end_row = L
end_col = 11

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
