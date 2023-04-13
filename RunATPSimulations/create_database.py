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
OUTPUT_FOLDER_2 = Path(r"H:/datasets/NumpyResults")
resistances = np.linspace(10, 1000, 100)
# TODO: Use multiprocessing (or multithreading) library to parallelize this process
for resistance in resistances:
    resistance = np.round(resistance, 2)
    atp_new_file = OUTPUT_FOLDER / ("3fg_r_" + str(resistance) + ".atp")
    flag_key_R = "$FLAG_F_R$"
    flag_value_R = f"{resistance:010.2f}"

    flags = {flag_key_R: flag_value_R}

    create_atp_file(atp_template_file, flags, atp_new_file)
    pl4_results = run_atp_simulation(atp_new_file)
    pl4_to_npy(pl4_results, OUTPUT_FOLDER_2)
