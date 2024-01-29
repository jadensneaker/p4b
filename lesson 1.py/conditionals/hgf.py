#Add necessary comment to explain your code
def tax_rebate_2():
    """ 
    Function will return rebate based on income level 
    """ 
    count = 0 
    while count < 3: 
        income = input("Declare your yearly income: ") 

        if income.isdigit() == False: 
            print("[INVALID INPUT] Only number is accepted, please re-enter again.")  
            count += 1 
        else: 
            income = float(income) 

            if income < 40000: 
                print("Your tax rebate is: 2000") 
                break 
            elif 40000 <= income < 100000: 
                print("Your tax refund is: 1000") 
                break 
            elif 100000 <= income < 150000: 
                print("Your tax refund is: 500") 
                break 
            else: 
                print("You are not eligible for tax rebate") 
                break
    else:
        print("You have reached the maximum number of attempts. Bye-bye!")
        return None
    

print(tax_rebate_2())