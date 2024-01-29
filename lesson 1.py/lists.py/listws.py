#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "Data Structure"
#name = jaden Quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042
#class_number = Tc08

#--------------------- 1. List ---------------------#

# A sneaker shop recorded product sales information in a sneakerSales_list.
# The information is a nested list `sales_data`. The elements in each sub-list contain:
## 1. The name of the sneaker
## 2. The unit cost of the sneaker
## 3. The unit selling price of the sneakder
## 4. The quantity sold

#sneakersSales_list = [['Adidas Superstar', 80, 159, 100], 
 #                     ['Chuck 70', 65, 115, 50], 
  #                    ['Air Max 90', 100, 152.50,75], 
   #                   ['Gel-Lyte III', 70, 114.59, 62], 
    #                  ['Classic Leather', 72.99, 114.99,39]
     #                 ]


#def total_summary(option):
 #   total = 0

 #   if option == 'revenue':
 #       for item in sneakersSales_list:
  #          total += item[2] * item[3]
    
 #   elif option == 'profit':
  #      for item in sneakersSales_list:
  #         total += (item[2] - item[1]) * item[3]
    
 #   else:
 #       return "invalid entry"
    
 #   return total
#
#print(total_summary('revenue'))




# 1.
# Write a function `total_summary` with a single parameter `option`.
# When "revenue" is supplied to the option parameter, 
# `total_summary` will return the total revenue of all sneakers sold.
# When "profit" is supplied to the option parameter, 
# `total_summary` will return the total profit made from all sneakers sold.
# It will return `invalid entry` for any other values supplied to the option parameter.
# The total revenue the sum of : unit selling price x quantity sold
# The total profit is the sum of : (unit selling price - unit cost) x quantity sold

#Delete the word pass, then add your code for the workshop
#Add necessary doc-string to explain your function
#Add necessary comment to explain your code


# Examples of what the functions will display and return when executed:

# revenue=total_summary_list("revenue")
# print(revenue)
## Total revenue is: 44676.69

# profit=total_summary_list("profit")
# print(profit)
## Total profit is: 18740.08

# result=total_summary_list("discount")
# print(result)
## invalid entry

#--------------------- 2. Dictionary ---------------------#
# The same information is now structured as a dictionary. 
# Write a similar function that will calculate total revenue and profit.
sneakersSales_dict = {'Adidas Superstar': {"Cost": 80, 
                              "Selling Price": 159,
                              "Quantity": 100
                            },
                 "Chuck 70": {"Cost": 65, 
                              "Selling Price": 115,
                              "Quantity": 50
                            },
                 "Air Max 90":  {"Cost": 100, 
                              "Selling Price": 152.50, 
                              "Quantity": 75
                            },
                 "Gel-Lyte III": {"Cost": 70,  
                              "Selling Price": 114.59,  
                              "Quantity": 62
                            },
                 "Classic Leather": {"Cost": 72.99,  
                              "Selling Price": 114.99, 
                              "Quantity": 39
                            },
                }


#Delete the word pass, then add your code for the workshop
#Add necessary doc-string to explain your function
#Add necessary comment to explain your code
def total_summary_dict(option):
  
    total = 0
    
    if option == "revenue":
        for sneaker in sneakersSales_dict.values():
            total += sneaker["Quantity"] * sneaker["Selling Price"]

        return f"Total revenue {total}"
    elif option == "profit":
        for sneaker in sneakersSales_dict.values():
            total += sneaker["Quantity"] * (sneaker["Selling Price"] - sneaker["cost"])
        return f"Total profit {total}"
    else:
        return "invalid entry"
    
    return total

print(total_summary_dict("revenue"))
