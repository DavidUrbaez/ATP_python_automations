import h5py
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

plt.style.use('dark_background')

falla = "Monofasica"
TFALLA = "0.01666"

with h5py.File('Data.h5', 'r') as hf:
    for key in hf.keys():
        print(key)

    t = np.array(hf.get('time'))
    data = np.array(hf.get('data_' + falla[:3] + '_T_' + TFALLA))
    Rfalla = np.array(hf.get('Rfalla_' + falla[:3] + '_T_' + TFALLA))
#######################################################################################
## Se grafica la solucion
plt.plot(data[50, :, 3:])
plt.show()

# plt.plot(Bifasica[50, 15000:30000, 3:])
# plt.show()
#
