from pathlib import Path
import csv

#function

def pnl(file_path):
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  

#These lines initialize empty lists days and values which will be used to store data from the CSV file.
        days = []
        values = []
#replace $ and , so that code can read the numbes on its own
        for row in reader:
            days.append(int(row[0]))
            values.append(float(row[4].replace('$', '').replace(',', '')))

#These lines check whether the values are strictly increasing (increasing) or 
#strictly decreasing (decreasing) across all days.

    increasing = all(values[i] > values[i-1] for i in range(1, len(values)))
    decreasing = all(values[i] < values[i-1] for i in range(1, len(values)))
#If the values are strictly increasing, it calculates the highest increment, 
#the day it occurred, and constructs a result string accordingly.

    if increasing:
        highest_increment = max(values[i] - values[i-1] for i in range(1, len(values)))
        highest_increment_day = days[values.index(max(values)) - 1] + 1
        result = (f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n"
                  f"[HIGHEST NET PROFIT SURPLUS]. The highest increment is {highest_increment} "
                  f"and it occurs between day {highest_increment_day-1} and day {highest_increment_day}.")
#If the values are strictly decreasing, it calculates the highest deficit, the day it occurred, 
#and constructs a result string accordingly.
    elif decreasing:
        highest_deficit = min(values[i] - values[i-1] for i in range(1, len(values)))
        highest_deficit_day = days[values.index(min(values)) - 1] + 1
        result = (f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n"
                  f"[HIGHEST NET PROFIT DEFICIT]. The highest deficit is {highest_deficit} "
                  f"and it occurs between day {highest_deficit_day-1} and day {highest_deficit_day}.")
    else:

     deficits = [(days[i], values[i] - values[i-1]) for i in range(1, len(values)) if values[i] < values[i-1]]  
    if deficits:  
            result = ""  
            for deficit in deficits:  
                result += f"[NET PROFIT DEFICIT]Day: {deficit[0]}. AMOUNT: {deficit[1]}\n"  
     #for top 3 deficits (scenario 3) sort highest to lowest, find top 3 highest         
            top_deficits = sorted(deficits, key=lambda x: x[1], reverse=False)[:3]  
            #sorting of values from largest to smallest   
            for i, deficit in enumerate(top_deficits):  
                if i == 0:  
                    result += f"[HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"  
                elif i == 1:  
                    result += f"[2ND HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"  
                elif i == 2:  
                    result += f"[3RD HIGHEST NET PROFIT DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"  
    else:  
            result = "There are no deficits."  

    return result


  
#These lines define the path to the CSV file by joining the folder path   
#(csv_folder) and the file name (csv_file_name) using the / operator,   
#which is overloaded by the Path class.  
  
  
csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")  
  
csv_file_name = "P&F FINAL.csv"  
  
file_path = csv_folder / csv_file_name  
  
#This line calls the pnl function with the specified file path   
#and stores the result in the variable result.  
  
  
  
result = pnl(file_path)