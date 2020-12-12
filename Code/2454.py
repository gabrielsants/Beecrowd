def decide():
    p, r = map(int, input().split())

    if p == 0:
        print('C')
    elif p == 1 and r == 1:
        print('A')
    elif p == 1 and r == 0:
        print('B')

if __name__ == "__main__":
    decide()