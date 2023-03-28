while True:
    try:
        n, q = map(int, input().split())
    except:
        break
        
    notas = []
    for i in range(n):
        nota = int(input())
        notas.append(nota)
        
    notas_ordenadas = sorted(notas, reverse=True)
    
    for i in range(q):
        posicao = int(input())
        print(notas_ordenadas[posicao-1])
