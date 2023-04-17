from pathlib import Path
import h5py
import numpy as np


def compress_data(numpy_outputs_folder_name: str | Path,
                  output_file_name: str | Path,
                  time_file_name: str = "_time.npy"):
    """
    Function that takes the numpy results folder and returns the h5 compressed file

    :param time_file_name:
    :param numpy_outputs_folder_name:
    :param output_file_name:
    :return:
    """
    full_data = []
    numpy_outputs_folder = Path(numpy_outputs_folder_name)
    result_files = list(numpy_outputs_folder.glob("[!_]*.npy"))
    files_len = len(result_files)

    time_file_name = Path.joinpath(numpy_outputs_folder, time_file_name)
    t = np.load(str(time_file_name))
    for index, result_file in enumerate(result_files):

        if index % 100 == 0:
            print(str(index) + "/" + str(files_len))
        data = np.load(str(result_file))
        full_data.append(data[::100, :])

    with h5py.File(output_file_name, 'w') as hf:
        hf.create_dataset('time', data=t)

        hf.create_dataset('data', data=full_data)

    print("en voila!")


if __name__ == "__main__":
    numpy_results_folder = r"H:/datasets/1fg_NumpyResults"
    output_file = "H:/datasets/datos_fallas.h5"

    compress_data(
        numpy_outputs_folder_name=numpy_results_folder,
        output_file_name=output_file
    )
