import h5py
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

cwd = Path.cwd()

hf = h5py.File(cwd / 'datos_fallas.h5', 'r')
# hf.keys()
t = np.array(hf.get('time'))
Monofasica = np.array(hf.get('Datos_Falla_Monofasica'))
Bifasica = np.array(hf.get('Datos_Falla_Bifasica'))

hf.close()

fig, axs = plt.subplots(2)
##
index = 1
axs[0].plot(t, Monofasica[index, :, :3])
axs[0].set_ylabel('Voltaje [V]')
##
axs[1].plot(t, Monofasica[index, :, 3:])
axs[1].set_ylabel('Corriente [A]')

plt.show()
