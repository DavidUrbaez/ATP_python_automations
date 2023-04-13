import numpy as np

from utils import readPL4
from pathlib import Path
import h5py
import os
from run_ATP_simulation import run_atp_simulation, pl4_to_npy, create_atp_file

# Define template file
TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
atp_template_file = TEMPLATES_FOLDER_PATH / "System_110kV_ThreePhase_Ground.atp"

# define output folder/file
OUTPUT_FOLDER = Path(r"H:/datasets/Simulations")
NP_OUTPUT_FOLDER = Path(r"H:/datasets/NumpyResults")

fault_resistances = np.linspace(100, 1000, 10)
fault_times = np.linspace(0.02, 0.08, 6 * 10 + 1)

# TODO: Use multiprocessing (or multithreading) library to parallelize this process

for fault_resistance in fault_resistances:
    for fault_time in fault_times:

        atp_new_file = OUTPUT_FOLDER / ("3fg_r_" + f"{fault_resistance:08.2f}" + "_t_" + f"{fault_time:05.5f}" + ".atp")

        flag_key_T = "$FLAG_F_R$"
        flag_value_T = f"{fault_resistance:010.2f}"

        flags = {
            "$FLAG_F_R$": f"{fault_resistance:010.2f}",
            "$FLAG_F_T$": f"{fault_time:010.5f}",
        }

        create_atp_file(atp_template_file, flags, atp_new_file)
        pl4_results = run_atp_simulation(atp_new_file)
        pl4_to_npy(pl4_results, NP_OUTPUT_FOLDER)
