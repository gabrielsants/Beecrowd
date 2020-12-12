'''
    @Author : Gabriel Santos;
'''

def _exec():

    while True:

        try:
            entry = input()
    
            values = []

            if len(entry) == 0:
                exit()

            value = 0
            
            for i, j in zip(entry, range(len(entry))):
                values.append(ord(i))
                value += (ord(i) - 64)

            _len = len(values)
            
            if _len > 1:
                if values[0] == 65:
                    value += 25
                elif values[0] == 66:
                    value += 50
                elif values[0] == 67:
                    value += 75
                elif values[0] == 68:
                    value += 100
                elif values[0] == 69:
                    value += 125
                elif values[0] == 70:
                    value += 150
                elif values[0] == 71:
                    value += 175
                elif values[0] == 72:
                    value += 200
                elif values[0] == 73:
                    value += 225
                elif values[0] == 74:
                    value += 250
                elif values[0] == 75:
                    value += 275
                elif values[0] == 76:
                    value += 300
                elif values[0] == 77:
                    value += 225
                elif values[0] == 78:
                    value += 350
                elif values[0] == 79:
                    value += 375
                elif values[0] == 80:
                    value += 400
                elif values[0] == 81:
                    value += 425
                elif values[0] == 82:
                    value += 550
                elif values[0] == 83:
                    value += 575
                elif values[0] == 84:
                    value += 600
                elif values[0] == 85:
                    value += 625
                elif values[0] == 86:
                    value += 650
                elif values[0] == 87:
                    value += 675
                elif values[0] == 88:
                    value += 700                    
                elif values[0] == 89:
                    value += 725
                elif values[0] == 90:
                    value += 750
            # A - XFD
            if _len > 3:
                print('Essa coluna nao existe Tobias!')
            elif len(values) == 3:
                if values[0] > 88:
                    print('Essa coluna nao existe Tobias!')
                elif values[0] > 88 and values[1] > 70 and values[2] > 68:
                    print('Essa coluna nao existe Tobias!')
                else:
                    print(value)
            else:
                print(value)
        except EOFError:
            exit()


if __name__ == "__main__":
    _exec()