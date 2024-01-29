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
        deliveryRecords.append([row[0],row[1],row[2],row[3]])   


def earning_perjob(distance, event_type):
    distancefloat = float(distance)
    basic_fare = 2.5
    mileagerate = 0
    if distancefloat <= 5:
        mileagerate += distancefloat * 0.1
    elif distancefloat <= 12:
        mileagerate += 5 * 0.1 + (distancefloat - 5) * 0.2
    elif distancefloat <= 22:
        mileagerate += 5 * 0.1 + 7 * 0.2 + (distancefloat - 12) * 0.3
    else:
        mileagerate += 5 * 0.1 + 7 * 0.2 + 10 * 0.3 + (distancefloat - 22) * 0.4
    if event_type == "Regular":
        basic_fare += 0
    elif event_type == "Express":
        basic_fare += 1
    elif event_type == "Premium":
        basic_fare += 2
    elif event_type == "Mart":
        basic_fare += 3
    return mileagerate + basic_fare

def calculate_total_earning(deliveryRecords):
    driver_earnings = {}
    for column in deliveryRecords:
        driver = column[0]
        distance = column[2]
        event_type = column[3]
        earning = earning_perjob(distance, event_type)
        if driver in driver_earnings:
            driver_earnings[driver] += earning
        else:
            driver_earnings[driver] = earning
    return driver_earnings

total_earnings = calculate_total_earning(deliveryRecords)
for driver, earning in total_earnings.items():
    print(f'{driver}: {earning}')
  
