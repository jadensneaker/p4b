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