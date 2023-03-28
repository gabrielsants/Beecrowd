def linha():
    for i in range(39):
        print('-',end='')
    print()

def column():
    for i in range(39):
        if(i == 0 or i == 38):
            print('|',end='')
        else:
            print(' ',end='')
    print()

linha()
for i in range(5):
    column()
linha()