par = []
impar = []

for i in range(15):
    x = int(input())
    if(x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)
    
    if(len(par) == 5):
        for j in range(5):
            print("par[{}] = {}".format(j, par[j]))
        par = []
    if(len(impar) == 5):
        for j in range(5):
            print("impar[{}] = {}".format(j, impar[j]))
        impar = []
for j in range(len(impar)):
    print("impar[{}] = {}".format(j, impar[j]))
for j in range(len(par)):
    print("par[{}] = {}".format(j, par[j]))  
