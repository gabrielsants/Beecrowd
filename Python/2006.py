t = int(input())
correct = 0
vector = list(map(int, input().split()))
for i in range(5):
    if(vector[i] == t):
        correct += 1
print(correct)
