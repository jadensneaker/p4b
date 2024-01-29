from pathlib import Path
import csv

def pnl(file_path):
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  

        days = []
        values = []

        for row in reader:
            days.append(int(row[0]))
            values.append(float(row[4].replace('$', '').replace(',', '')))

    increasing = all(values[i] > values[i-1] for i in range(1, len(values)))
    decreasing = all(values[i] < values[i-1] for i in range(1, len(values)))

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
        
        deficits = [(days[i], values[i] - values[i-1]) for i in range(1, len(values)) if values[i] < values[i-1]]
        if deficits:
            result = ""
            for deficit in deficits:
                result += f"[NET PROFIT DEFICIT]Day: {deficit[0]}. AMOUNT: {deficit[1]}\n"
            
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
    

    return result


csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

csv_file_name = "P&F FINAL.csv"

file_path = csv_folder / csv_file_name

result = pnl(file_path)


