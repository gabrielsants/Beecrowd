def getDestination(dd):
    if(dd == 61):
        return 'Brasilia'
    elif(dd == 71):
        return 'Salvador'
    elif(dd == 11):
        return 'Sao Paulo'
    elif(dd == 21):
        return 'Rio de Janeiro'
    elif(dd == 32):
        return 'Juiz de Fora'
    elif(dd == 19):
        return 'Campinas'
    elif(dd == 27):
        return 'Vitoria'
    elif(dd == 31):
        return 'Belo Horizonte'
    else:
        return 'DDD nao cadastrado'
    
    
print(getDestination(int(input())))
