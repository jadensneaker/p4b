# 1 
# For each of the following expressions, fill in the blank
# (indicated by __) with an appropriate Boolean comparator so that 
# the expression evaluates to True: 

#print(4 > 2)

#print(5 < 10)

#print("python" != "C++")

#print(50 != "50")


# 2
# Add parentheses where necessary so that each of the following 
# expressions evaluates to True:

#print(not False == True)

#print("True and False" == "True and False")

#(not True == ("A" == "B"))


# 3 
# Write a conditional statement to evaluate if the school variable contains `business and accountancy`. 
# If the evaluation is true, print `business and accountancy`, else print `invalid entry`.

school = "business and accountancy"

if school == "business and accountancy":
  print("business and accountancy")
else:
    print("invalid entry")

# 4 
# Write a conditional statement to evaluate the price of an apple and orange. 
# If the price of apple is greater than orange, print "apple price is higher than orange". 
# If the price of apple is greater than orange, print "apple price is lower than orange". 
# Otherwise, print "apple and orange prices are equal" 

# Test your conditions by assigning different values to 2 variables, example:
apple_price = 0.74
orange_price = 0.74

if apple_price > orange_price:
   print ("apple price is higher than orange")
elif apple_price == orange_price:
   print ("apple and orange prices are equal")
else:
   print("apple price is lower than orange")

# 5
# Write a conditional statement to evaluate the following conditions of a variable `height`:
# If height is greater or equal to 175, print "tall"
# If height is greater or equal to 165 and less than 175, print "average"
# If height is less than 165, print "short"
# Test the condition with 160, 170 and 180 to evaluate the conditional statements, example:

#height = 190

#if height >= 175:
   #print("tall")
#elif height >= 165 and height < 175:
   #print("average")
#else:
   #print("short")
   

# 6 
# Write a conditional statement to evaluate the following conditions: 
    # gender == "female" and hair_length == "long", print "tie up your hair"
    # gender == "female" and hair_length == "short", print "style your hair"
    # gender == "male" and hair_length == "long", print "cut your hair"
    # gender == "male" and hair_length == "short", print "comb your hair"

# Test the conditions to evaluate the conditional statement, example:
gender = "male" 
hair_length = "short"

if gender == "female" and hair_length == "long":
   print("tie up your hair")
elif gender == "female" and hair_length =="short":
   print("style your hair")
elif gender == "male" and hair_length == "long":
   print("cut your hair")
else:
   print("comb your hair")

# 7
# Write a `for loop` to iterate over range(21) to evaluate each value of the range function
# with the following conditions:

    ## value == 1, print (f"{value} is first value")
    ## value == 10 , print (f"{value} is middle value")
    ## value == 20, print (f"{value} is last value")

# When the program is executed, it should display the output:
    ## 1 is first value
    ## 10 is middle value
    ## 20 is last value

for num in range(21):
   if num == 1:
      print(f"{num} is first value")
   elif num ==10:
      print(f"{num} is middle value")
   elif num==20:
      print(f"{num} is last value")
      

# 8 
# Create a for loop to iterate over enumerate(range(80, 150)).
# In each loop, print the index (coming from enumerate() function) and value (coming from range() function) 
# Break the iteration when the index reach number 20.


for count, num in enumerate(range(80,159)):
   print(count, num)
   if count == 20:
    break
   

# 9 
# Create a function `height_func()` to convert height in metres to feet.
# The function will ask for a user to input the height.
# You can use: user_input = float(input("Enter your height in metres : ")) to ask user to input height.
# If the input is string data type, the program should print: "Your input is invalid, please try again".
# If a user input is float or integer data type, the program will convert input height to feet 
# and print: "Your height of ___ in metre is ____ in feet." 
# Note that 1 metre = 3.28084 feet.
# The function will loop endlessly, prompting the user to input height until the correct data type is entered.
# The function does not take in any parameters.
# Here is how the program will look like when executed:

    ## Enter your height in metres: two  (user input height as "two")
    ## Your input is invalid, please try again
    ## Enter your height in metres: TWO  (user input height as "TWO")
    ## Your input is invalid, please try again
    ## Enter your height in metres: 2 (user input height as 2)
    ## Your height of 2.0 in metre is 6.56168 in feet.

def height_func():

    while True:

        user_input = input("Enter your height in metres: ")

        if user_input.isdigit() == False:
            print("Your input is invalid, please try again")
        
        else:
            feet = float(user_input) * 3.28084
            return f"Your height of {user_input} in metre is {feet} in feet."
            
print(height_func())





    

# 10
# Create a function to prompt a user to enter temperature in degrees celsius.
# Users are allowed to enter only number data type. If a user enters strings or characters,
# the function will return a message "Invalid entry, please enter the temperature in numbers again",
# it will keep prompting for temperature until a number is entered.
# The functions will return the followings when a temperature is correctly input.

# Temperature (degrees celsius)     # Weather Category #
# ------------------------------    --------------------
#   < 0                                 FROZEN
#   0 to less or equal 10               COLD
#   10 to less or equal 20              COOL
#   20 to less or equal 30              WARM
#   > 30                                HOT

def weather_function():

    while True:

        temp =input("Enter temperature in degrees celsius: ")
        
        if temp.isdigit() == False:
            print("Invalid entry, please enter the temperature in numbers again")
        
        else:

            temp = float(temp)
          
            if temp > 30:
                weather_category = "HOT"
            elif temp >= 20:
                weather_category = "WARM"
            elif temp >= 10:
                weather_category = "COOL"
            elif temp >= 0:
                weather_category = "COLD"
            else:
                weather_category = "FROZEN"

            return weather_category

print(weather_function())