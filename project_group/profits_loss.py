#Profit & Loss csv : The program will firstly compute the difference in the net profit column.
# If the net profit is always increasing, 
#find out the day and amount the highest increment occurs. 
#If the net profit is always decreasing, find out the day and amount the highest decrement occurs. 
#If net profit fluctuates, list down all the days and amount when deficit occurs, 
#and find out the top 3 highest deficit amount and the days it happened. 

#steps to do this code below
#1. insert csv
#2. write code to compute difference in net profit column 
#3. write code if profit ALWAYS increasing, find out day and amount the highest increment occur
#4. write code if profit ALWAYS decreasing, find out day and amount the highest deficit occur
#5. write code if profit flunctuates, list all days and amount hen deficit occurs + 
#6. find out top 3 highest deficit amounts and the day it happened

#link excel here

from pathlib import Path
import csv

def pnl(file_path):
    # read the csv file.
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header 

        # Initialize lists for days and values
        days = []
        values = []

        # Read the CSV file and store the days and values
        for row in reader:
            days.append(int(row[0]))
            values.append(float(row[4].replace('$', '').replace(',', '')))

    # Check if the trend is always increasing or decreasing
    increasing = all(values[i] > values[i-1] for i in range(1, len(values)))
    decreasing = all(values[i] < values[i-1] for i in range(1, len(values)))

    # Find the highest increment or deficit
    if increasing:
        highest_increment = max(values[i] - values[i-1] for i in range(1, len(values)))
        highest_increment_day = days[values.index(max(values)) - 1] + 1
        result = (f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n"
                  f"[HIGHEST NET PROFIT SURPLUS]. The highest increment is {highest_increment} "
                  f"and it occurs between day {highest_increment_day-1} and day {highest_increment_day}.")
    elif decreasing:
        highest_deficit = min(values[i] - values[i-1] for i in range(1, len(values)))
        highest_deficit_day = days[values.index(min(values)) - 1] + 1
        result = (f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n"
                  f"[HIGHEST NET PROFIT DEFICIT]. The highest deficit is {highest_deficit} "
                  f"and it occurs between day {highest_deficit_day-1} and day {highest_deficit_day}.")
    else:
        # Find all the days and amount where a deficit occurs
        deficits = [(days[i], values[i] - values[i-1]) for i in range(1, len(values)) if values[i] < values[i-1]]
        if deficits:
            result = ""
            for deficit in deficits:
                result += f"[NET PROFIT DEFICIT]Day: {deficit[0]}. AMOUNT: {deficit[1]}\n"
            # Find the top 3 highest deficits and the day it happened
            top_deficits = sorted(deficits, key=lambda x: x[1], reverse=False)[:3]
            
            for i, deficit in enumerate(top_deficits):
                if i == 0:
                    result += f"[HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
                elif i == 1:
                    result += f"[2ND HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
                elif i == 2:
                    result += f"[3RD HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
        else:
            result = "There are no deficits."

    # Write the result to a text file
    

    return result


csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")
# Specify the name of your CSV file
csv_file_name = "P&F FINAL.csv"
# Create the full path including the folder and file name
file_path = csv_folder / csv_file_name

result = pnl(file_path)


