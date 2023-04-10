import h5py
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

print("Saving Data -> h5 file ")
cwd = Path.cwd()

with h5py.File(cwd / "Data.h5", 'w') as hf_out:
    for falla in ["Monofasica", "Bifasica"]:
        for TFALLA in ["0.00416", "0.00833", "0.01249", "0.01666"]:
            with h5py.File(cwd / falla / 'data' / 'h5_files' / ('datos_fallas_T_' + TFALLA + '.h5'), 'r') as hf:
                # hf.keys()

                data = np.array(hf.get('Datos_Falla_' + falla + '_T_' + TFALLA))
                Rfalla = np.array(hf.get('Rfalla'))
                t = np.array(hf.get('time'))
            # Down Sampling
            data = data[:, ::100, :]
            # Save Data
            hf_out.create_dataset('data_' + falla[:3] + '_T_' + TFALLA, data=data)
            hf_out.create_dataset('Rfalla_' + falla[:3] + '_T_' + TFALLA, data=Rfalla)
            print("SAVED DATA FOR: " + falla + " - " + TFALLA)
    # Down Sampling
    t = t[::100]
    hf_out.create_dataset('time', data=t)

# plt.plot(Bifasica[50, 15000:30000, 3:])
# plt.show()
#
