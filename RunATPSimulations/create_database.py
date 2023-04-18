import numpy as np

from utils import readPL4
from pathlib import Path
import h5py
import os
from run_ATP_simulation import run_atp_simulation, pl4_to_npy, create_atp_file


def create_database(atp_template_file, output_folder_numpy):
    # create output folders
    OUTPUT_FOLDER.mkdir(exist_ok=True, parents=True)
    output_folder_numpy.mkdir(exist_ok=True, parents=True)

    fault_resistances = np.linspace(100, 1000, 10)
    fault_times = np.linspace(0.02, 0.08, 6 * 10 + 1)

    # TODO: Use multiprocessing (or multithreading) library to parallelize this process

    for fault_resistance in fault_resistances:
        for fault_time in fault_times:
            atp_new_file = OUTPUT_FOLDER / (
                    "1Afg_r_" + f"{fault_resistance:08.2f}" + "_t_" + f"{fault_time:05.5f}" + ".atp")

            flag_key_T = "$FLAG_F_R$"
            flag_value_T = f"{fault_resistance:010.2f}"

            flags = {
                "$FLAG_F_R$": f"{fault_resistance:010.2f}",
                "$FLAG_F_T$": f"{fault_time:010.5f}",
            }

            create_atp_file(atp_template_file, flags, atp_new_file)
            pl4_results = run_atp_simulation(atp_new_file)
            pl4_to_npy(pl4_results, output_folder_numpy)

    # Store time
    t, _ = pl4_to_npy(pl4_results, output_folder_numpy, return_data=True)

    np.save(output_folder_numpy / "_time.npy", t)


if __name__ == "__main__":
    # Define template file
    TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
    atp_template_file_name = TEMPLATES_FOLDER_PATH / "System_110kV_ThreePhase_Ground.atp"

    # define output folder/file
    OUTPUT_FOLDER = Path(r"H:/datasets/Simulations")
    NUMPY_OUTPUT_FOLDER = Path(r"H:/datasets/NumpyResults")

    create_database(atp_template_file_name, NUMPY_OUTPUT_FOLDER)
