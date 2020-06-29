import os
import csv
import numpy as np


def read_n_top_rows_csv(n):
    with open('tranco.csv', 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))
    return data[0:n, 1]


def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
