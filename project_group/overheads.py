from pathlib import Path
import csv

def over_heads(file_path):
    # read the csv file.
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  

        
        overheadsfinal = []

        
        for i, column in enumerate(reader):
            
            overheadsfinal.append([i, column[0], float(column[1])])

    
    largest_value = max(record[2] for record in overheadsfinal)
    max_location = next(i for i, record in enumerate(overheadsfinal) if record[2] == largest_value)

    #find largest value and corresponding header, print it out

    
    result = f"[HIGHEST OVERHEAD] {overheadsfinal[max_location][1]}:{largest_value}% "

    

    return result


csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

csv_file_name = "OVERHEADS FINAL.csv"

file_path = csv_folder / csv_file_name

result = over_heads(file_path)

