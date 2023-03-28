def linha():
    for i in range(39):
        print('-',end='')
    print()

def column(control):
    i = 0
    while i < 39:
        if (i == 0 or i == 38):
            print('|', end='')
        elif (i == 9 and control == 0):
            print('Roberto', end='')
            i += len('Roberto') - 1
        elif (i == 9 and control == 2):
            print('5786', end='')
            i += len('5786') - 1
        elif (i == 9 and control == 4):
            print('UNIFEI', end='')
            i += len('UNIFEI') - 1
        else:
            print(' ', end='')
        i += 1
    print('')

linha()
for i in range(5):
    column(i)
linha()