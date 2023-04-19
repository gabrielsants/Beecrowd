while True:
    n = int(input())
    if n == 0:
        break
    
    a = input().split()
    b = input().split()
    
    stack = []
    result = []
    j = 0
    
    for i in range(n):
        stack.append(a[i])
        result.append('I')
        while stack and stack[-1] == b[j]:
            stack.pop()
            result.append('R')
            j += 1
        
    if stack:
        print("".join(result) + " Impossible")
    else:
        print("".join(result))