def tax_rebate_2():
    """
    - Function will return rebate based on income level
    """
    
    
    count = 0
    while count < 3:
            income = input("Declare your yearly income: ")

            if income.isdigit() == False:
                print("invalid input, only numbers are allowed") 
                count += 1
                print("You have reached maximum number of attempts. Bye bye!")
            else:
                income = float(income)

                if income < 40000:
                    print("Your tax rebate is: 2000")
                    break
                elif income > 40000 and income < 100000:
                    print("Your text refund is: 1000")
                    break
                elif income > 100000 and income < 150000:
                    print("Your tax refund is: 500")
                    break
                else:
                    print("You are not eligible for tax rebate")
                    break
    


print(tax_rebate_2())