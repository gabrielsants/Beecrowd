n = int(input())

for i in range(n):
    valores = input().split()
    v1 = float(valores[0])
    v2 = float(valores[1])
    v3 = float(valores[2])
    
    media = (v1*2 + v2*3 + v3*5) / 10
    
    print("{:.1f}".format(media))
