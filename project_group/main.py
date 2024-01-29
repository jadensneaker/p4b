#import functions from different modules
from pathlib import Path
from overheads import over_heads
from cash_on_hand import coh 
from profits_loss import pnl

#The raw string (r"...") 
#is used to handle backslashes without interpreting them as escape characters.

csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

#These lines define the names of three CSV files: 
#"OVERHEADS FINAL.csv", "Final COH .csv", and "P&F Final.csv".

overheads_file_name = "OVERHEADS FINAL.csv"
coh_file_name = "Final COH .csv"
pnl_file_name = "P&F Final.csv"

#create path by joining folder and file names

overheads_fp = csv_folder / overheads_file_name
coh_fp = csv_folder / coh_file_name
pnl_fp = csv_folder / pnl_file_name

#store results from path in variable

result_overheads = over_heads(overheads_fp)
result_coh = coh(coh_fp)
result_pnl = pnl(pnl_fp)

#format all the results in a singular string and separate it using a line "\n"

summary_report = f"{result_overheads}\n{result_coh}{result_pnl}"

#create path for where summary report will be located


output_file_path = csv_folder / "Summary_report.txt"

#writes summary report in a text file


output_file_path.write_text(summary_report)


print(summary_report)

