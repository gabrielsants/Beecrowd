def verificar_parentheses(expressao):
    pilha = []
    for c in expressao:
        if c == '(':
            pilha.append(c)
        elif c == ')':
            if not pilha or pilha[-1] != '(':
                return "incorrect"
            pilha.pop()
    return "correct" if not pilha else "incorrect"

while True:
    try:
        data = input().split()
        for expressao in data:
            resultado = verificar_parentheses(expressao)
            print(resultado)
    except(EOFError):
        break