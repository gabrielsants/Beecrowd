y = 0
media = 0
for x in range(1,7):
    a = float(input())
    if a > 0:
        y = y + 1
        media += a
print('{} valores positivos'.format(y))
print('%.1f'%(media/y))