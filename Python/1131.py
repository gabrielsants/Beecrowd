grenais = 0
inter = 0
gremio = 0
empate = 0
while True:
    data = input().split()
    x, y = int(data[0]), int(data[1])
    
    if(x > y):
        inter += 1
    elif(y > x):
        gremio += 1
    else:
        empate += 1
    grenais += 1
    
    exit = -1
    while True:
        print('Novo grenal (1-sim 2-nao)')
        exit = int(input())
        if(exit == 1 or exit == 2):
            break
    if(exit == 2):
        break
print('%d grenais' %grenais)
print('Inter:%d' %inter)
print('Gremio:%d' %gremio)
print('Empates:%d' %empate)
if(gremio > inter):
    print('Gremio venceu mais')
elif(inter > gremio):
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')