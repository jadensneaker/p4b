print('Part 1')
def tax_rebate():
    """
    - function will return rebate based on income level
    """
    income = float(input("Declare your yearly income: "))

    if income < 40000:
        print("Your tax rebate is: 2000")
    elif income > 40000 and income < 100000:
        print("Your text refund is: 1000")
    elif income > 100000 and income < 150000:
        print("Your tax refund is: 500")
    else:
        print("You are not eligible for tax rebate")


#The code to test your function
#Do not change or delete
print(tax_rebate())