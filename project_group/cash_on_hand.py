from pathlib import Path
import csv

#put as function

def coh(fp):
    
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  

        days = []
        values = []
#replace $ and , so that code can read the numbes on its own
        for row in reader:
            days.append(row[0])
            value = float(row[1].replace('$', '').replace(',', ''))
            values.append(value)

    increasing = True
    decreasing = True

    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            decreasing = False
        if values[i] >= values[i-1]:
            increasing = False
#if the value is higher than the day before across all values
    if increasing:
        highest_increment = max(values[i] - values[i-1] for i in range(1, len(values)))
        highest_increment_day = days[values.index(max(values)) - 1] + 1
        result = f"[CASH SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n [HIGHEST NET PROFIT SURPLUS]. The highest increment is {highest_increment} and it occurs between day {highest_increment_day-1} and day {highest_increment_day}."
 # if the value is lower than the day before across all values
    elif decreasing:
        highest_deficit = min(values[i] - values[i-1] for i in range(1, len(values)))
        highest_deficit_day = days[values.index(min(values)) - 1] + 1
        result = f"[CASH DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY \n [HIGHEST NET PROFIT DEFICIT]. The highest deficit is {highest_deficit} and it occurs between day {highest_deficit_day-1} and day {highest_deficit_day}."
    else:
        
        deficits = [(days[i], values[i] - values[i-1]) for i in range(1, len(values)) if values[i] < values[i-1]]
        if deficits:
            result = ""
            for deficit in deficits:
                result += f"[CASH DEFICIT]Day: {deficit[0]}. AMOUNT: {deficit[1]}\n"
         #sorting of values   
            top_deficits = sorted(deficits, key=lambda x: x[1], reverse=False)[:3]
#for top 3 deficits (scenario 3) sort highest to lowest, find top 3 highest
            for i, deficit in enumerate(top_deficits):
                if i == 0:
                    result += f"[HIGHEST CASH DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
                elif i == 1:
                    result += f"[2ND HIGHEST CASH DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
                elif i == 2:
                    result += f"[3RD HIGHEST CASH DEFICIT] Day:{deficit[0]}. AMOUNT: {deficit[1]}\n"
        else:
            result = "There are no deficits."

    

    return result


csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

csv_file_name = "Final COH .csv"

fp = csv_folder / csv_file_name

result = coh(fp)


