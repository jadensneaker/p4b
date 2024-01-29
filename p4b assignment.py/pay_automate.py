from pathlib import Path

import csv

#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "Individual Assignment"
#name = Jaden Quak
#np_email = s10225042@connect.np.edu.sg
#student_id = S10225042C
#class_number = TC08

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file path to csv file.
fp = Path.cwd()/"deliveryRecords.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    deliveryRecords=[] 

    # append delivery record into the deliveryRecords list
    for row in reader:
        #get the driver id, sales, distance, and event type for each record
        #and append to the deliveryRecords list
        deliveryRecords.append([row[0], float(row[1].replace('$', '')), float(row[2]), row[3]])  

print(deliveryRecords)

#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the earing per delivery job, total earning, total sales
# 2. Calculate the sales to earning ratio
        
#earning per delivery job = Basic fare per delivery + mileage rate + event rate 

# Part 2: Calculate earning per delivery job, total earning, total sales, and sales to earnings ratio efficiently.
earning_per_delivery = []

total_earning = 0.0  
total_sales = 0.0    

driver_totals = {}

for record in deliveryRecords:
    driver_id = record[0]

    distance_rate = (
        0.1 * min(5, record[2]) + 0.2 * min(7, max(record[2] - 5, 0)) +
        0.3 * min(10, max(record[2] - 12, 0)) + 0.4 * max(record[2] - 22, 0)
    )
    event_rate = {'Regular': 0, 
                  'Express': 1, 
                  'Premium': 2, 
                  'Mart': 3}[record[3]]

    earnings = 2.5 + distance_rate + event_rate
    earning_per_delivery.append(earnings)
    total_earning += earnings
    total_sales += record[1]

    
    if driver_id not in driver_totals:
        driver_totals[driver_id] = {'sales': 0.0, 'earning': 0.0}
    driver_totals[driver_id]['sales'] += record[1]
    driver_totals[driver_id]['earning'] += earnings


sorted_drivers = sorted(driver_totals.keys())

# Part 3: Write the calculated result into a simple text file (.txt).
#with open('paymentSummary.txt', 'w') as file:
    #file.write("Power Leopard Payment Summary\n")
    #file.write("==============================\n")
    #file.write("Driver ID, Total Sales, Total Earning, Sales to Earnings Ratio\n")

    #for driver_id in sorted_drivers:
        #totals = driver_totals[driver_id]
        #sales_to_earnings_ratio = totals['sales'] / totals['earning'] if totals['earning'] != 0 else 0
        #file.write(f"{driver_id},{totals['sales']:.2f},{totals['earning']:.2f},{sales_to_earnings_ratio:.2f}\n")

#print('Check paymentSummary.txt ')