# Inicializando as variáveis
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

n = int(input())

for i in range(n):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    
    total_cobaias += quantia
    if tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

print("Total: {} cobaias".format(total_cobaias))
print("Total de coelhos: {}".format(total_coelhos))
print("Total de ratos: {}".format(total_ratos))
print("Total de sapos: {}".format(total_sapos))
print("Percentual de coelhos: {:.2f} %".format(percentual_coelhos))
print("Percentual de ratos: {:.2f} %".format(percentual_ratos))
print("Percentual de sapos: {:.2f} %".format(percentual_sapos))
