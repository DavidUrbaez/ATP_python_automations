import sys

# setting path
sys.path.append('../RunATPSimulations')


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pywt
from utils import readPL4

plt.style.use('dark_background')

cwd = Path.cwd()
DATA_FOLDER = cwd.parents[1] / "datasets" / "ATP_Results" / "testing_data"
test_file = DATA_FOLDER.rglob("*.pl4")
df, data, SimulationData = readPL4(next(test_file))
t, data = data[:, 0], data[:, 1:]

x = 1
scales = range(1, 128)
waveletname = 'morl'
train_size = 5000
test_size = 500

signal = np.array(data[:, 2])
coeff, freq = pywt.cwt(signal, scales, waveletname, 1)
coeff_ = coeff[:, :127]
