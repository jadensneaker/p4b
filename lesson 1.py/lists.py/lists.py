# Create a list named `apparel` with two elements, "shoes" and "shirt".

list_apparel = ["shoes", "shirt"]

# Append the string "tie" to apparel using .append().

list_apparel.append("tie")

# Add the strings "sunnies" and "pants" to apparel using .extend().

new_apparel = ["sunnies", "pants"]

list_apparel.extend(new_apparel)

# Print the first two items in the apparel list using print() and slice notation.

print(list_apparel[0:2])

# Print the last item in apparel using print() and index notation.

print(list_apparel[-1])

### Exercise 2 ###
# Create a single string: "running, cycling, swimming" 
# Split the single using .split() method and assign to a variable: sports_list

sports_list = "running, cycling, swimming"

sports = sports_list.split(",")

print(len(sports))

# Verify that sports has three items using len().

# Create a new list called sports_length using a list comprehension 
# that contains the length of each string in sports_list.