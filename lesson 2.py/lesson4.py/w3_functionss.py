#####  Store your, name, email, student_id and class_number as STRINGS #####
exercise = "functions"
name = "Jaden Quak"
np_email = "s10225042@connect.np.edu.sg"
student_id = "S10225042"
class_number = "TC08"

#-------------------------------- Q1 ------------------------------------#
# Return on investment (ROI) is an approximate measure of profitability of an investment .
# It is calculated by subtracting the initial cost of the investment from its final value, 
# then dividing result by the initial cost of the investment, 
# and finally, multiplying it by 100.
# Write a program that allow users to calculate initial cost, final value and ROI
#------------------------------------------------------------------------#

# The program should include 3 functions:

    #### ROI_function() ####
    # ROI = (finalValue-initialCost)/initialCost*100

    #### finalValue_function() ####
    # finalValue = initialCost + initialCost*(ROI/100)

    #### initCost_function() ####
    # initialCost = finalValue/(1+(ROI/100))

# The functions will round float to 2 decimal places.

# When the 3 functions are executed, they should display and return:

    ##### Example of ROI_function() #####
    ## Enter initial cost: 10.0
    ## Enter final value: 12.0
    ## Based on the initial cost and final value, the calculated ROI = 20.0
    
    ##### Example of finalValue_function() #####
    ## Enter initial cost: 10.0
    ## Enter expected ROI: 30.0
    ## Based on the initial cost and ROI, the calculated final value = 13.0

    ##### Example 
    # of initialCost_function() #####
    ## Enter final value: 12.0
    ## Enter expected ROI: 20.0
    ## Based on the final value and ROI, initialCost = 10.0

#Write your code below and try out other numbers to make sure your program works correctly

# For each funtion, delete the word 'pass', 
# then write your code for the function

 

def ROI_function(initialCost, finalValue):
    """
    - Function calculates ROI based on initial cost and final value
    """
    
    ROI =  (finalValue-initialCost)/initialCost*100
    return (f"Based on the initial cost and final value, the calculated ROI= {ROI}") 


initialC=float(input('Please enter initial cost: '))
finalV=float(input('Please enter final value: '))
ROI_result=ROI_function(initialCost=initialC, finalValue=finalV)
print(ROI_result)

   
def finalValue_function(initialCost, ROI):
    """
    - Function calculates final value based on inital cost and expected ROI
    """
    finalValue = initialCost + initialCost*(ROI/100)
    return (f"Based on the initial cost and ROI, the calculated final value= {finalValue}")
initialC=float(input('Please enter initial value: '))
ROI=float(input('Please enter ROI: '))
finalValue_result=finalValue_function(initialCost=initialC, ROI=ROI)
print(finalValue_result)



def initialCost_function(finalValue, ROI):
    """
    - Function calculates inital cost based on final value and expected ROI
    """
    initialCost = finalValue/(1+(ROI/100))
    return (f"Based on the final value and ROI, initial cost= {initialCost}")
finalV= float(input('Please enter final value: '))
ROI=  float(input('Please enter ROI: '))

InitialCost_result=initialCost_function(finalValue=finalV, ROI=ROI)
print(InitialCost_result)

    


# The code for testing ROI_function is almost completed
# You just need to complete the missing part by filling in the balnk
# Other than that, no need to change any other part


#write your code to test finalValue_function and initialCost_function below
#test finalValue_function


#test initialCost_function

