hi, mi, hf, mf = map(int, input().split())

inicio = hi * 60 + mi
fim = hf * 60 + mf

if inicio < fim:
    duracao = fim - inicio
else:
    duracao = 24 * 60 - inicio + fim

horas = duracao // 60
minutos = duracao % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(horas, minutos))