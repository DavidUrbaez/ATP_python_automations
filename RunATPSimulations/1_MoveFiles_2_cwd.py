# from bokeh.io import curdoc
# from bokeh.plotting import figure, output_file, show
from utils import readPL4
import matplotlib.pyplot as plt
from pathlib import Path
import h5py
import shutil

plt.style.use('dark_background')

WORK_DIR = Path(r"C:\Users\USUARIO\Documents\ATPdata\work")
cwd = Path.cwd()

DATA_PATH = cwd / 'data' / '110kV_Monofasica'

DATA_PATH.mkdir(exist_ok=True, parents=True)

simulations = list(WORK_DIR.rglob('*.pl4'))

for index, simulation in enumerate(simulations):
    print(str(simulation))
    sim_folder = DATA_PATH / str(index)
    sim_folder.mkdir(exist_ok=True, parents=True)
    atp_file_name = simulation.name.replace(".pl4", ".atp")
    atp_file = simulation.parent / atp_file_name

    shutil.move(simulation, sim_folder / simulation.name)
    shutil.move(atp_file, sim_folder / atp_file.name)
