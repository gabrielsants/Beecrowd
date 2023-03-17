N = -1
alcool = 0
gasolina = 0
diesel = 0

while True:
    N = int(input())
    if(N in(1,2,3,4)):
        if(N == 4):
            break
        elif(N == 1):
            alcool += 1
        elif(N == 2):
            gasolina += 1
        elif(N == 3):
            diesel += 1
        
print('MUITO OBRIGADO')
print('Alcool: %d' %alcool)
print('Gasolina: %d' %gasolina)
print('Diesel: %d' %diesel)