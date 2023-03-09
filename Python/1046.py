hi, hf = map(int, input().split())

if hi < hf:
    duracao = hf - hi
else:
    duracao = 24 - hi + hf
print("O JOGO DUROU %d HORA(S)" %duracao)