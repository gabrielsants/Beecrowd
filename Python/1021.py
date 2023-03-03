data = float(input())

data += 0.001
bills = (100, 50, 20, 10, 5, 2)
coins = (1, 0.5, 0.25, 0.1, 0.05, 0.01)

print("NOTAS:")

for i in range(len(bills)):
    amount_bills = data // bills[i]
    print("%d nota(s) de R$ %0.2f" %(int(amount_bills), bills[i]))
    data %= bills[i]
    print("MOEDAS:")
    for i in range(len(coins)):
        amount_coins = data // coins[i]
        print("%d moeda(s) de R$ %0.2f" %(int(amount_coins), coins[i]))    
        data %= coins[i]