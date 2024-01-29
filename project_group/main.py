from pathlib import Path
from overheads import over_heads
from cash_on_hand import coh 
from profits_loss import pnl

# Specify the folder where your CSV files are located
csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")

# Specify the file names
overheads_file_name = "OVERHEADS FINAL.csv"
coh_file_name = "Final COH .csv"
pnl_file_name = "P&F Final.csv"

# Create the full paths including the folder and file names
overheads_fp = csv_folder / overheads_file_name
coh_fp = csv_folder / coh_file_name
pnl_fp = csv_folder / pnl_file_name

# Run the functions on the specified files
result_overheads = over_heads(overheads_fp)
result_coh = coh(coh_fp)
result_pnl = pnl(pnl_fp)

# Create the summary report
summary_report = f"{result_overheads}\n{result_coh}{result_pnl}"

# Specify the output file path for the summary report
output_file_path = csv_folder / "Summary_report.txt"

# Write the summary report to a text file
output_file_path.write_text(summary_report)

# Print the summary report
print(summary_report)

