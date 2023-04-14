from pathlib import Path
import h5py
import numpy as np

NP_OUTPUT_FOLDER = Path(r"H:/datasets/NumpyResults")
full_data = []
t = np.load(r"H:/datasets/NumpyResults/_time.npy")

files = list(NP_OUTPUT_FOLDER.glob("[!_]*.npy"))
files_len = len(files)

for index, file in enumerate(files):

    if index % 100 == 0:
        print(str(index) + "/" + str(files_len))

    full_data.append(np.load(file))

with h5py.File('H:/datasets/datos_fallas.h5', 'w') as hf:
    hf.create_dataset('time', data=t)

    hf.create_dataset('data', data=full_data)

print("en voila!")
