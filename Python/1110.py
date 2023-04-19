n = int(input())

while n != 0:
    cartas = list(range(1, n+1))

    descartadas = []

    while len(cartas) > 1:
        descartadas.append(cartas.pop(0))

        cartas.append(cartas.pop(0))

    print("Discarded cards: " + ", ".join(str(c) for c in descartadas))

    print("Remaining card: %d" %cartas[0])

    n = int(input())