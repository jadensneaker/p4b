#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "numbers"
#name = Jaden Quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042C
#class_number = TC08

#-------------------------------- Q1 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.    
# The program will check if the sum between these 2 numbers is an integer. 
#----------------------------------------------------------------------------#

# The program should display message like the following when executed.

    #------ First execution ------#
    # Enter first number : 3.5
    # Enter second number : 1.5
    # 3.5 + 1.5 = 5.0
    # Is the sum of 3.5 and 1.5 an integer? True

    #------ Second execution ------#
    # Enter first number : 3.5
    # Enter second number : 2.3
    # 3.5 + 2.3 = 5.8
    # Is the sum of 3.5 and 2.3 an integer? False

# In the first execution, the input values are  3.5 and 1.5
# In the second execution, the input values are 3.5 and 2.3
# The program will sum the 2 numbers and return True when the sum is an integer or False when sum is a float.

# Assign `num1` as a variable for the first number, `num2` as a variable for the second number
# Assign `sum_num` as the variable to store the arithmatic operation between `num1` and `num2`  

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1_float = float(num1)
num2_float = float(num2)

sum_num = num1_float + num2_float 

print(sum_num)

print(f"Is the sum of {num1_float} and {num2_float} an integer? {sum_num.is_integer()}")



#-------------------------------- Q2 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.  
# The program will use the first number as dividend and second number as a divisor.
# The output should return the remainder of the division. 
#----------------------------------------------------------------------------#

# The program should display the following messages :

    # Enter a dividend: 30
    # Enter a divisor: 3
    # The remainder is 0.0

# In the execution above, the input values are  30  and 3. The program will return the remainder of 30 divided 3.

# Assign `num3` for the dividend and `num4` for the divisor.
# Assign 'modulus` to store the results of the operation.

num3 = input("Enter a dividend: ")
num4 = input("Enter a divisor: ")

num3_float = float(num3)
num4_float = float(num4)

print(f"The remainder is {num3_float % num4_float}")