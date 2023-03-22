n = int(input())
if(n != 0):
    fatorial = 1
else:
    fatorial = 0
for i in range(2,n+1):
    fatorial *= i
print(fatorial)
