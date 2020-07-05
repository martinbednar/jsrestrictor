import os
import csv
import numpy as np
from pathlib import Path
from os import system
import glob


def read_n_top_rows_csv(n):
    with open('tranco.csv', 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))
    return data[0:n, 1]


def delete_files_if_exist(dir, files_regex):
    for path in Path(dir).glob(files_regex):
        os.remove(path)


def create_folder_structure(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def append_file(path, text):
    f = open(path, 'a', newline='')
    f.write(text)
    f.close()


def init_output_files():
    create_folder_structure("../data/logs")
    delete_files_if_exist("../data/logs", "logs*.json")


def finish_output_files():
    logs_parts = list(Path("../data/logs").glob("logs_part_*.json"))

    f = open("../data/logs/logs.json", 'a', newline='')
    f.write("[")
    for path in logs_parts[:-1]:
        g = open(path, 'r', newline='')
        f.write(g.read())
        g.close()
        os.remove(path)
    with logs_parts[-1] as path:
        g = open(path, 'r', newline='')
        f.write(g.read()[:-1])
        g.close()
        os.remove(path)
    f.write("]")
    f.close()


def terminate_zombie_processes():
    system("taskkill /f /im chromedriver.exe")
    system("taskkill /f /im chrome.exe")
