def calc_hotdogs():
    h, p = map(int, input().split())

    hotdogs = h / p

    print('{0:.2f}'.format(hotdogs))

if __name__ == "__main__":
    calc_hotdogs()