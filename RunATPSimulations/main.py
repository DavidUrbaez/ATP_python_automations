from pathlib import Path
from create_database import create_database
from read_simulations import compress_data
import numpy as np

# ##################################################################################################
#  Define Settings

# define prefix
prefix = "Sim3_1fg_Randt_"
atp_prefix = "1fg_r"

# Define template file
TEMPLATES_FOLDER_PATH = Path(r"ATP_templates")
atp_template_file_name = TEMPLATES_FOLDER_PATH / "System_110kV_SinglePhase_Ground.atp"

# define output folder/file for numpy
OUTPUT_FOLDER = Path(f"H:/datasets/{prefix}Simulations")
NUMPY_OUTPUT_FOLDER = Path(f"H:/datasets/{prefix}NumpyResults")

# run simulations
fault_resistances_values = np.linspace(100, 1000, 10)
fault_times_values = ((0.03 / 4) * np.random.randn(60) + 0.04)
# fault_times_values = np.linspace(0.02, 0.08, 6 * 10 + 1)


# ##################################################################################################
#  Run

create_database(atp_template_file_name, OUTPUT_FOLDER, NUMPY_OUTPUT_FOLDER,
                fault_resistances_values, fault_times_values, prefix_name=atp_prefix)

# Store/Compress results
output_file = f"H:/datasets/{prefix}datos_fallas.h5"

compress_data(
    numpy_outputs_folder_name=NUMPY_OUTPUT_FOLDER,
    output_file_name=output_file
)
