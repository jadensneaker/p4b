# 1. Create a dictionary named `fruits_order` with the following key/value pairs
# "apple" : 200, "orange": 150, "papaya": 50, "pineapple" : 45.

fruits_order = {
    "apple" : "200",
    "orange" : "150",
    "papaya" : "50",
    "pineapple" : "45"

}

# 2. Insert a new key/pair "durian": 300 to `fruits_order`. 

fruits_order["durian"] = "300"

# 3. Access the value of "papaya" using [] and .get() method.

print(fruits_order["papaya"])
print(fruits_order.get("papaya"))

# 4. Write a if statement to check if "durian" exists as a key of the dictionary
# and set the value to 100 if it exists.

if "durian" in fruits_order.keys():
    fruits_order["durian"] = 100




# 5. Write a `for loop` to display the key/value pairs using f-strings to print.
# It should display the followings:
    # apple order: 200
    # orange order: 150
    # papaya order: 50
    # pineapple order: 45
    # durian order: 100

for fruit, order in fruits_order.items():
    print(f"{fruit} order: {order}")

# 6. Write a `for loop` with a if statement to check for value less than 100 among
# the key/value pairs. If the value is less than 100, print the key using f-string.
# It should display the followings:
    # urgent order: papaya
    # urgent order: pineapple

for fruit in fruits_order:
    if fruits_order[fruit] < 100:
        print(f"urgent order: {fruit}")


# 7. Create an empty list named `total_quantity` and write a `for loop` to append
# the values of `fruits_order` to `total_quantity`, using dictionary's .values() method.
# Sum the values in `total_quantity` using sum() and print. The sum should be 545.

total_quantity = []


for order in fruits_order.values():
    total_quantity.append(order)


total_sum = sum(total_quantity)
print(f"The total quantity is: {total_sum}")

# 8.
# `business_data` variable contains financial data of the revenue and cost for 3 types of furnitures.
#  The data is a nested list with the following elements in each sub-list:
## 1. Furniture type
## 2. Revenue
## 3. Cost of Goods

business_data = [['Armchair', 120000, 85000], ['Dining Table', 180000, 100000], ['Bed', 230000, 140000]]

# Write a function with 1 parameter, example: total_function(option).
# Depending on the parameter, the function will return the total revenue or total cost of the 3 furnitures
# If 'revenue' is supplied to the parameter, the function will return total revenue.
# If 'cost' is supplied to the parameter, the function will return total cost.
# If the options are neither 'revenue' nor 'cost', the function will return "Invalid Option"

def total_function(option):
    total=0

    if option == 'revenue':
        for item in business_data:
            total += item[1]

    elif option == 'cost':
        for item in business_data:
            total += item[2]

    else:
        return "invalid option"
    
    return total

print(total_function("revenue"))

# 9.
# A tuition center keeps track of monthly new sign up of subjects it offered and signup fee per student.
# A sample of 3 months of data is given below in the variable tuition data.
#  The data is a nested list with the following elements in each sub-list:
## 1. Subject
## 2. Month 
## 3. Number of new sign ups
## 4. Signup fee per student

tuition_data = [['math', 1, 100, 320], ['Econ', 1, 110, 300], ['English', 1, 80, 280],
                ['math', 2, 150, 330], ['Econ', 2, 130, 300], ['English', 2, 90, 280],
                ['math', 3, 200, 350], ['Econ', 3, 170, 320], ['English', 3, 120, 300]]

# Write a code automatically calculate the total number of new signups and the signup fees collected by subjects.
# Your code should be generic to handle data of more than 3 months 
# It should display the follow output:
    # Summary of new signups by subjects
    # Math: 450 151500
    # Econ: 410 126400
    # English: 290 83600

tuition_summary = {}

# Iterate through the tuition data and update the dictionary
for signupRecord in tuition_data:
    if signupRecord not in tuition_summary:
        tuition_summary[signupRecord[0]] = [0,0]
    tuition_summary[signupRecord[0][0]] += signupRecord
    tuition_summary[signupRecord[0][1]] += signupRecord[2] * signupRecord[3]

print(tuition_summary)

print('Summary of new signups by subject')
for subject in tuition_summary:
    print(f"{subject} : {tuition_summary[subject][0]}, {tuition_summary}[subject][1]")
    
    