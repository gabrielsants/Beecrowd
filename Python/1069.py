def is_diamond(c):
    return c == '<' or c == '>'

n = int(input())

for i in range(n):
    seq = input().strip()

    stack = []

    count = 0

    for c in seq:
        if c == '<':
            stack.append(c)
        elif c == '>' and len(stack) > 0 and stack[-1] == '<':
            stack.pop()
            count += 1
    print(count)