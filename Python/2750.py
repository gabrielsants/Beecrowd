num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16 = range(16)

print('-' * 39)
print('| decimal   |  octal  |  Hexadecimal  |')
print('-' * 39)

def print_line(num):
    print('|  {:^9}| {:^7} | {:^13} |'.format(num, oct(num)[2:], hex(num)[2:].upper()))

print_line(num1)
print_line(num2)
print_line(num3)
print_line(num4)
print_line(num5)
print_line(num6)
print_line(num7)
print_line(num8)
print_line(num9)
print_line(num10)
print_line(num11)
print_line(num12)
print_line(num13)
print_line(num14)
print_line(num15)
print_line(num16)

print('-' * 39)