vert = input()
tipo = input()
classe = input()

if(vert[0] == 'v'):
    if(tipo[0] == 'a'):
        if(classe[0] == 'c'):
            print("aguia")
        else:
            print("pomba")
    else:
        if(classe[0] == 'o'):
            print("homem")
        else:
            print("vaca")
else:
    if(tipo[0] == 'i'):
        if(classe[2] == 'm'):
            print("pulga")
        else:
            print("lagarta")
    else:
        if(classe[0] == 'h'):
            print("sanguessuga")
        else:
            print("minhoca")