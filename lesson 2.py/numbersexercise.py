#1. Create 1st variable `num_1` and assign with a value of 5 billion using 
# an underscore '_' to separate every 3 zeros.

num_1 = 5_000_000_000

#2. Create 2nd variable `num_2` and assign 100.50 to the variable.

num_2 = 100.50

#3. Create 3rd variable `num_3` and assign "200.50" to the variable

num_3 = "200.50"


#4. Check the data type of `num_1`, `num_2`, `num_3`.
# `num_3` should be string data type.

print(type(num_1))
print(type(num_2))
print(type(num_3))

#5. 
# Add `num_2` and `num_3` with an addition operation. 
# The result should return 301.00.
# Convert the string to a float before addition. 

num3_float = float(num_3)
print(type(num3_float))

print (num_2 + num3_float)

#6. Create 4th variable `num_4` and assign 50 to the variable.

num_4 = 50

#7. What is the value of an integer division of `num_2` by `num_4`?

print(num_2 // num_4)

#8. What is the  remainder of `num_2` by `num_4`?

print(num_2 % num_4)

#9. What is  the value of 4 raised to the power of 5?

print(4**5)

#10. Multiply `num_2` with `num_4` before adding the value to `num_3` in a single 
# arithmetic expression. 

print(num_2 * num_4 + num3_float)

#11. Add `num_2` and `num_4` before multiplying the value by `num_3` in a single 
# arithemtic expression.

print((num_2 + num_4)*num3_float)

#12. Round 2.02454 to 2 decimal places.

print(round(2.02454, 2))

#13. Round 1000.40 to an integer.

print(round(1000.40))

#14. What is the value of 4 raised to the power of 5 using the pow() function?

print(pow(4, 5))


#15.
# Ask a user to input 2 numbers using 2 separate input functions.
# Print the results of addition, substraction, multiplication, division of the 2 numbers

firstnumber = input("Enter first number: ")
secondnumber = input("Enter second number: ") 

firstnumber_float = float(firstnumber)
secondnumber_float = float(secondnumber)



print(f"Addition results: {firstnumber_float + secondnumber_float}")
print(f"Subtraction results: {firstnumber_float - secondnumber_float}")
print(f"Multiplication results: {firstnumber_float * secondnumber_float}")
print(f"Division results: {firstnumber_float / secondnumber_float}")



# Example:
# Enter first number: 5.5
# Enter second number: 1.5
# Addition results: 7.0
# Substraction results: 4.0
# Multiplication results: 8.25
# Division results (first number / second number): 3.6666666666666665

# Note: 
# 5.5 and 1.5 in first and second number can be any number, depending on a user's input.
# The arithmetic results are the output of the program based on the values of first and second number.