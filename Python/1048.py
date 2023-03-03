def salary(ammount):
    new_salaray = 0.00
    percentage_adjustment = 0.00
    in_percentage = 0.00

    if ammount > 0 and ammount <= 400:
        in_percentage = 15
        percentage_adjustment = float(ammount * 0.15)
        new_salaray = float(ammount + percentage_adjustment)

    if ammount >= 400.01 and ammount <= 800:
        in_percentage = 12
        percentage_adjustment = float(ammount * 0.12)
        new_salaray = float(ammount + percentage_adjustment)

    if ammount >= 800.01 and ammount <= 1200:
        in_percentage = 10
        percentage_adjustment = float(ammount * 0.10)
        new_salaray = float(ammount + percentage_adjustment)

    if ammount >= 1200.01 and ammount <= 2000:
        in_percentage = 7
        percentage_adjustment = float(ammount * 0.07)
        new_salaray = float(ammount + percentage_adjustment)

    if ammount > 2000:
        in_percentage = 4
        percentage_adjustment = float(ammount * 0.04)
        new_salaray = float(ammount + percentage_adjustment)
    
    print('Novo salario:', '{0:.2f}'.format(new_salaray))
    print('Reajuste ganho:', '{0:.2f}'.format(percentage_adjustment))
    print('Em percentual:', (in_percentage),'%')



if __name__ == "__main__":
    salary(float(input()))