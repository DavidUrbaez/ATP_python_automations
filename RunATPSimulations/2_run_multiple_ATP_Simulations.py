# from bokeh.io import curdoc
# from bokeh.plotting import figure, output_file, show
from utils import readPL4
import matplotlib.pyplot as plt
from pathlib import Path
import h5py
import os

TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
OUTPUT_FOLDER = Path(r"H:/datasets")
template_file = TEMPLATES_FOLDER_PATH / "System_110kV_ThreePhase_Ground.atp"

with open(template_file, "r") as atp_template_file:
    data = atp_template_file.read()

fault_R_flag = "$FLAG_F_R$"
full_data = []
atp_files = []
for R in [100, 150, 200, 250]:
    output_file = OUTPUT_FOLDER / "Simulations" / ("3fg_r_" + str(R) + ".atp")
    atp_files.append(output_file)

    f_R = f"{R:010.2f}"
    with open(output_file, 'w') as f:
        line = data.replace(fault_R_flag, f_R)
        f.write(line)

    os.system(r"run_ATP.bat " + str(output_file.resolve()))

for atp_file in atp_files:
    pl4_results = Path(str(atp_file.resolve()).replace("atp", "pl4"))
    df, data, simulation_data = readPL4(pl4_results)
    t, data = data[:, 0], data[:, 1:]

    df_REG1 = df[df['FROM'].str.contains("REG1")]
    full_data.append(data[:, df_REG1.index])

############
# Save data
hf = h5py.File(OUTPUT_FOLDER / 'datos_fallas.h5', 'w')
hf.create_dataset('time', data=t)
hf.create_dataset('Datos_Falla_Monofasica', data=full_data)
