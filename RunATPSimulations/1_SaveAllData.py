# from bokeh.io import curdoc
# from bokeh.plotting import figure, output_file, show
from utils import readPL4
import matplotlib.pyplot as plt
from pathlib import Path
import h5py

plt.style.use('dark_background')

cwd = Path.cwd()

DATA_PATH = cwd / 'data' / '110kV_Monofasica'

simulations = list(DATA_PATH.glob('*.pl4'))

full_data = []
for simulation in simulations:
    df, data, SimulationData = readPL4(simulation)
    t, data = data[:, 0], data[:, 1:]

    df_REG1 = df[df['FROM'].str.contains("REG1")]
    full_data.append(data[:, df_REG1.index])

############
# Save data
hf = h5py.File('datos_fallas.h5', 'w')
hf.create_dataset('time', data=t)
hf.create_dataset('Datos_Falla_Monofasica', data=full_data)

############
# Read Again

DATA_PATH = cwd / 'data' / '110kV_Bifasica'

simulations = list(DATA_PATH.glob('*.pl4'))

full_data = []
for simulation in simulations:
    df, data, SimulationData = readPL4(simulation)
    t, data = data[:, 0], data[:, 1:]

    df_REG1 = df[df['FROM'].str.contains("REG1")]
    full_data.append(data[:, df_REG1.index])

############
# Save data Again
hf.create_dataset('Datos_Falla_Bifasica', data=full_data)

hf.close()
