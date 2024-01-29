from pathlib import Path
import csv

def over_heads(file_path):
    # read the csv file.
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  

        #This line initializes an empty list called overheadsfinal,
        # which will be used to store the processed data from the CSV file.

        overheadsfinal = []

        #This line starts a loop that iterates over each row (column) in the CSV file, 
        #and the enumerate function is used to get both the index (i) and the content of the row.
        
        for i, column in enumerate(reader):

        #This line appends a new list to overheadsfinal for each row.
            # The new list contains the index (i), the value from the first column (column[0]), 
            #and the floating-point conversion of the value from the second column (float(column[1])).  
              
            overheadsfinal.append([i, column[0], float(column[1])])

    #This line calculates the maximum value in the third column (record[2]) 
    #of each row in overheadsfinal using the max function.
    largest_value = max(record[2] for record in overheadsfinal)

    #This line finds the index (i) of the first row in overheadsfinal where the third column value is equal to 
    #largest_value using the next function and a generator expression.

    max_location = next(i for i, record in enumerate(overheadsfinal) if record[2] == largest_value)

    #find largest value and corresponding header, print it out

    
    result = f"[HIGHEST OVERHEAD] {overheadsfinal[max_location][1]}:{largest_value}% "

    

    return result

#These lines define the path to the CSV file by joining the folder path (csv_folder)
#and the file name (csv_file_name) using the / operator, 
#which is overloaded by the Path class.


csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

csv_file_name = "OVERHEADS FINAL.csv"

file_path = csv_folder / csv_file_name

#This line calls the over_heads function with the 
#specified file path and stores the result in the variable result.

result = over_heads(file_path)

