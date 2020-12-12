def walking_in_time():
    year1, year2, year3 = map(int, input().split())

    if year1 - year2 == 0:
        print('S')
    elif year1 - year3 == 0:
        print('S')
    elif year2 - year3 == 0:
        print('S')
    elif (year1 + year2) - year3 == 0:
        print('S')
    elif (year2 + year3) - year1 == 0:
        print('S')
    elif (year1 + year3) - year2 == 0:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    walking_in_time()