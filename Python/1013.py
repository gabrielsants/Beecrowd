import math

data = input().split(" ")
a, b, c = data
a = int(a)
b = int(b)
c = int(c)

greaterAB = (a + b + abs(a - b)) / 2
greater = (greaterAB + c + abs(greaterAB - c)) / 2

print("%d eh o maior" %greater)
