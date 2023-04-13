from pathlib import Path
import os

import numpy as np

from utils import readPL4


def create_atp_file(template_file, flags, output_file):
    """
    Function that copies and pastes a template ATP file, then it replaces Flag values in the new
    ATP file.
    :param template_file:
    :param output_file:
    :return:
    """
    # Read ATP template file - Note: atp files could be interpreted as txt files
    # hence the variable "data" is going to be a large string variable.
    with open(template_file, "r") as atp_template_file:
        data = atp_template_file.read()

    # Since the variable "data" is a string, it is possible to replace the flags
    # with the corresponding values according to the "flags" dictionary
    for flag, value in flags.items():
        assert len(flag) == len(value), "Check the len of the flag and the values, they must be equal"
        data = data.replace(flag, value)

    # Finally save the "data" variable in the output file
    with open(output_file, 'w') as atp_output_file:
        atp_output_file.write(data)


def run_atp_simulation(atp_file):
    """
    Function that calls the .bat file with the script to run the ATP file using tpbig.exe
    :param atp_file:
    :return:
    """
    os.system(r"run_ATP.bat " + str(atp_file.resolve()))
    pl4_results = Path(str(output_file.resolve()).replace("atp", "pl4"))
    return pl4_results


def pl4_to_npy(pl4_results):
    df, data, simulation_data = readPL4(pl4_results)
    t, data = data[:, 0], data[:, 1:]

    df_REG1 = df[df['FROM'].str.contains("REG1")]
    output_array = data[:, df_REG1.index]
    np.save(str(output_file.resolve()).replace(".atp", '.npy'), output_array)
    # np.savetxt(str(output_file.resolve()).replace(".atp", '.csv'), output_array, delimiter=",")


# Define template file
TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
template_file = TEMPLATES_FOLDER_PATH / "System_110kV_ThreePhase_Ground.atp"

# define output folder/file
OUTPUT_FOLDER = Path(r"H:\test_dataset")
output_file = OUTPUT_FOLDER / "test0.atp"

R = 110
flag_key_R = "$FLAG_F_R$"
flag_value_R = f"{R:010.2f}"

flags = {flag_key_R: flag_value_R}

if __name__ == '__main__':
    create_atp_file(template_file, flags, output_file)
    pl4_results = run_atp_simulation(output_file)
    pl4_to_npy(pl4_results)
