def linha():
    for i in range(39):
        print('-',end='')
    print()

def column(control):
    i = 0
    while i < 39:
        if (i == 0 or i == 38):
            print('|', end='')
        elif (i == 1 and control == 0):
            print('x = 35', end='')
            i += len('x = 35') - 1
        elif (i == 16 and control == 2):
            print('x = 35', end='')
            i += len('x = 35') - 1
        elif (i == 32 and control == 4):
            print('x = 35', end='')
            i += len('x = 35') - 1
        else:
            print(' ', end='')
        i += 1
    print('')

linha()
for i in range(5):
    column(i)
linha()