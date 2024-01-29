#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "conditionals"
#name = Jaden Quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042
#class_number = Tc08

#------------------------ Part 1 : if, elif, else ------------------------#
# Write a function: tax_rebate() to determine tax rebate from income level
#-------------------------------------------------------------------------#

# The function will prompt a user to declare his/her yearly income
# and determine the amount of one-time off tax rebate he/she should receive.
# Note that the function does not require any parameters. It will return the
# amount of tax rebate based on the following tax rules:

# Yearly Income in $ 	                # Tax Rebate in $
# ------------------                      -------------
# 0 to less than 40000 	                      2000
# 40000 to less than 100000	                  1000
# 100000 to less than 150000 	              500
# equal or greater than 150000 	             not eligible

# Executing the function based om different income levels will display and return output
# like the followings:

#### Example 1 ####
# Declare your yearly income : 10000
# Your tax rebate is : $2000

#### Example 2 ####
# Declare your yearly income : 80000
# Your tax rebate is : $1000

#### Example 3 ####
# Declare your yearly income : 110000
# Your tax rebate is : $500

#### Example 4 ####
# Declare your yearly income : 150000
# You are not eligible for tax rebate

#### Example 5 ####
# Declare your yearly income : 200000
# You are not eligible for tax rebate

#Delete the word pass, then add your code for the workshop
#Add necessary doc-string to explain your function
#Add necessary comment to explain your code
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


#---------------------------------- Part 2  ---------------------------------#
# Improve the tax_rebate() function from Part 1 to make the program
# less susceptible to crashing.
#----------------------------------------------------------------------------#

# It should prevent the program from crashing if the user entered "string"
# data type when declaring his/her income.

# The function should loop maximum 3 times to ask the user to declare the income until
# he/she use "number" data type. 

# You can assume user only enter integer data type for this exercise.
# You can use the isdigit() function to check if a user enters an integer or not

# Here is an example of how the program will behave:

    # Declare your yearly income: ten thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: one thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: 10000
    # Your tax rebate is : $2000

# Here is a second example of how the program will behave 
# when a user enters non-integer 3 times consecutively:

    # Declare your yearly income: ten thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: one thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: two thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # You have reached maximum number of attempts. Bye bye!

# Tips:
# Design the function with `while loop` in mind to make the program 
# loop at most 3 times until the user input enter an integer.

#Delete the word pass, then add your code for the workshop
#Add necessary doc-string to explain your function
#Add necessary comment to explain your code
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
    
    
#The code to test your function
#Do not change or delete
print(tax_rebate_2())