def tax(salary):
    if(0 < salary <= 2000):
        return("Isento")
    elif(2000 < salary <= 3000):
        tax = (salary - 2000)
        tax8 = (tax * 8) / 100
        return(f"R$ %.2f" %tax8)
    elif(3000 < salary <= 4500):
        tax = (salary - 2000)
        tax1 = tax - 1000
        tax8 = (1000 * 8) / 100
        tax18 = (tax1 * 18) / 100
        return(f"R$ %.2f" %(tax8+tax18))
    else:
        tax = (salary - 2000)
        tax1 = tax - 1000
        tax8 = (1000 * 8) / 100
        tax2 = tax1 - 1500
        tax18 = (1500 * 18) / 100
        tax28 = (tax2 * 28) / 100
        return(f"R$ %.2f" %(tax28+tax8+tax18))
    
print(tax(float(input())))