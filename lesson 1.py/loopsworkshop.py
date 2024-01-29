#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "loops"
#name = Jaden Quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042C
#class_number = TC08

#-------------------------------- Q1 ------------------------------------#
# Write a function: loan_calculator(amount, interest, month).
# The function will calculate the total loan amount payable,
# and print out the amount at the end of every month
#------------------------------------------------------------------------#

#### Example of how the function works ####

# Given a loan amount of $1000, 10% interest rate and 5 month loan period,
# the function will calculate the interests payment plus the principal loan amount.
# When `print(loan_calculator(1000, 0.10, 5))` is executed, it will print out:

# Month 1 = $1100 ($1000 * 1.1)
# Month 2 = $1210 ($1100 * 1.1)
# Month 3 = $1331 ($1210 * 1.1)
# Month 4 = $1464.1 ($1331 * 1.1)
# Month 5 = $1610.51 ($1464 * 1.1)
# The total amount after 5 months is $1610.51.


# Round off decimals to 2 decimal places.
# BONUS: Can you use f-strings to include a $ symbol with the return value?

#Delete the word pass, then add your code for the workshop
#Add necessary doc-string to explain your function
#Add necessary comment to explain your code
def loan_calculator(amount, interest, lengthOfLoan):
    """
    Describe what the function does and what parameters are required
    """
    for month in range(1, lengthOfLoan+1):
        amount+= amount * (interest)
        print(f"Month {month} = ${round(amount,2)}({amount}*{1+interest})")
    
    print(f"The total amount after {month} months is ${round(amount,2)}")        

    #
    pass

#The following code is to test your function
#Do not change or delete

print(loan_calculator(1000,0.10,5))
print(loan_calculator(5000,0.15,8))