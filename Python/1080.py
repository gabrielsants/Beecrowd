maior = -1
n = -1
pos = 0
for i in range(1,101):
    n = int(input())
    if(n > maior):
        maior = n
        pos = i
print(maior)
print(pos)