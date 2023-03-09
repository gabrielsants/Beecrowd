data = float(input())

bills = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('bills:')
for bill in bills:
    amount_bills = int(data / bill)
    print('{} bill(s) de R$ {:.2f}'.format(amount_bills, bill))
    data -= amount_bills * bill

print('coins:')
for coin in coins:
    data = round(data, 2)
    amount_coins = int(data / coin)
    print('{} coin(s) de R$ {:.2f}'.format(amount_coins, coin))
    data -= amount_coins * coin