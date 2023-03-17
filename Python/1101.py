while True:
    data = input().split()
    m, n = int(data[0]), int(data[1])

    if(m <= 0 or n <= 0):
        break

    if m > n:
        m, n = n, m

    soma = 0
    string = ''
    for i in range(m, n+1):
        string = string + str(i) + ' '
        soma += i
    print(string +'Sum=%d' %soma)