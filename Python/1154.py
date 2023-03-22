entradas = 0
idades = 0
while True:
    idade = int(input())
    if(idade < 0):
        break
    else:
        idades += idade
        entradas += 1
print('%.2f' %(idades/entradas))