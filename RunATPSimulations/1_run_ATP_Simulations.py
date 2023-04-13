import matplotlib.pyplot as plt
from pathlib import Path
import os

plt.style.use('dark_background')

TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
OUTPUT_FOLDER = Path(r"data\TEST")
template_file = TEMPLATES_FOLDER_PATH / "system_110kv_single_phase.atp"

with open(template_file, "r") as atp_template_file:
    data = atp_template_file.read()

output_file = OUTPUT_FOLDER / "test2.atp"
fault_R_flag = "$FLAG_F_R$"

R = 110
f_R = f"{R:010.2f}"
with open(output_file, 'w') as f:
    line = data.replace(fault_R_flag, f_R)
    f.write(line)


os.system(r"run_ATP.bat " + str(output_file.resolve()))
# print(data)
