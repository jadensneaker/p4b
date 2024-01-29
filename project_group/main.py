#modularize by importing functions to main.py
from pathlib import Path
from overheads import over_heads
from cash_on_hand import coh 
from profits_loss import pnl

csv_folder = Path(r"C:\Users\jaden\Documents\p4b\project_group\csv_reports")


overheads_file_name = "OVERHEADS FINAL.csv"
coh_file_name = "Final COH .csv"
pnl_file_name = "P&F Final.csv"

#link csv path

overheads_fp = csv_folder / overheads_file_name
coh_fp = csv_folder / coh_file_name
pnl_fp = csv_folder / pnl_file_name


result_overheads = over_heads(overheads_fp)
result_coh = coh(coh_fp)
result_pnl = pnl(pnl_fp)

#put in txt file

summary_report = f"{result_overheads}\n{result_coh}{result_pnl}"


output_file_path = csv_folder / "Summary_report.txt"


output_file_path.write_text(summary_report)


print(summary_report)

