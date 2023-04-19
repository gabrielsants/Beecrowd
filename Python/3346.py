f1, f2 = map(float,input().split())

total_fluctuation = (1 + f1/100) * (1 + f2/100) - 1
total_fluctuation_percent = total_fluctuation * 100

print('{:.6f}'.format(total_fluctuation_percent))
