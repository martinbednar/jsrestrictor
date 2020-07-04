import os
import csv
import numpy as np
from pathlib import Path
from os import system


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


def init_output_files():
        create_folder_structure("../data/logs")
        delete_file_if_exists("../data/logs/logs.json")
        append_file("../data/logs/logs.json","[")


def finish_output_files():
        append_file("../data/logs/logs.json","]")


def terminate_zombie_processes():
    system("taskkill /f /im chromedriver.exe")
    system("taskkill /f /im chrome.exe")
