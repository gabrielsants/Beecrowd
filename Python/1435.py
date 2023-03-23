while True:
    m = int(input())
    mlen = m
    sm = 1
    aux = 1
    matriz = []

    if m == 0:
        print()
        break

    for i in range(m):
        linha = []
        for j in range(m):
            linha.append(sm)
        matriz.append(linha)

    while m - 2 > 0:
        for i in range(aux, m - 1):
            for j in range(aux, m - 1):
                matriz[i][j] = sm + 1
        sm += 1
        aux += 1
        m -= 1
    for i in matriz:
        for pos, j in enumerate(i):
            if pos == 0:
                print('{:3}'.format(j), end='')
            else:
                print('{:4}'.format(j), end='')
        print('')