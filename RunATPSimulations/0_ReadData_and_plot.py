# from bokeh.io import curdoc
# from bokeh.plotting import figure, output_file, show
from utils import readPL4
import matplotlib.pyplot as plt
from pathlib import Path

plt.style.use('dark_background')

cwd = Path.cwd()
DATA_FOLDER = cwd.parents[1] / "datasets" / "ATP_Results" / "testing_data"
test_file = DATA_FOLDER.rglob("*.pl4")
df, data, SimulationData = readPL4(next(test_file))
t, data = data[:, 0], data[:, 1:]

df_REG1 = df[df['FROM'].str.contains("REG1")]

fig, axs = plt.subplots(2)
##
axs[0].plot(t, data[:, df_REG1[df_REG1.TYPE == "V-node"].index])
axs[0].set_ylabel('Voltaje [V]')
##
axs[1].plot(t, data[:, df_REG1[df_REG1.TYPE == "I-bran"].index])
axs[1].set_ylabel('Corriente [A]')

plt.show()
x = 1

# for index in [0, -1]:
#     df, data, SimulationData = readPL4(simulations[index])
#     t, data = data[:, 0], data[:, 1:]
#
#     df_REG1 = df[df['FROM'].str.contains("REG1")]
#
#     fig, axs = plt.subplots(2)
#     ##
#     axs[0].plot(t, data[:, df_REG1[df_REG1.TYPE == "V-node"].index])
#     axs[0].set_ylabel('Voltaje [V]')
#     ##
#     axs[1].plot(t, data[:, df_REG1[df_REG1.TYPE == "I-bran"].index])
#     axs[1].set_ylabel('Corriente [A]')
#
#     plt.show()
