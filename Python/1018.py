value = int(input())

bills = [100, 50, 20, 10, 5, 2, 1]
iterator = 0

print(value)

for i in range(len(bills)):
    iterator = value // bills[i]
    value %= bills[i]
    print('{} nota(s) de R$ {},00'.format(iterator, bills[i]))
    