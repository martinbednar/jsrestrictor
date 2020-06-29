import os
import csv
import numpy as np
from pathlib import Path


def read_n_top_rows_csv(n):
    with open('tranco.csv', 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))
    return data[0:n, 1]


def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

def create_folder_structure(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def append_file(path,text):
    f = open(path, 'a', newline='')
    f.write(text)
    f.close()
