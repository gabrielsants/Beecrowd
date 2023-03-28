n = int(input())
max_nota = -1
index_max_nota = -1

for i in range(n):
    matricula, nota = map(float, input().split())
    if nota > max_nota:
        max_nota = nota
        index_max_nota = int(matricula)
        
if max_nota >= 8:
    print(index_max_nota)
else:
    print("Minimum note not reached")
