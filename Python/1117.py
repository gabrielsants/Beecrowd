n1 = 0
while True:
    n1 = float(input())
    if(n1 < 0 or n1 >10):
        print('nota invalida')
    else:
        break
n2 = 0
while True:
    n2 = float(input())
    if(n2 < 0 or n2 > 10):
        print('nota invalida')
    else:
        break

media = (n1 + n2) / 2
print('media = %0.2f' %media)