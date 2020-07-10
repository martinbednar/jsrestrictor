from os import system, remove, path
from shutil import rmtree
import csv
import numpy as np
from pathlib import Path
import glob

from configuration import Config


def read_n_top_rows_csv(n):
    with open(Config.sites_to_test_csv_path, 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))
    return data[0:n, 1]


def delete_files_if_exist(dir, files_regex):
    for file_path in Path(dir).glob(files_regex):
        if path.isdir(file_path):
            rmtree(file_path)
        elif path.isfile(file_path) or path.islink(file_path):
            remove(file_path)


def create_folder_structure(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def append_file(path, text):
    f = open(path, 'a', newline='')
    f.write(text)
    f.close()


def init_output_files():
    create_folder_structure("../data/logs")
    create_folder_structure("../data/screenshots")
    delete_files_if_exist("../data/logs", "*")
    delete_files_if_exist("../data/screenshots", "*")


def finish_output_files():
    logs_parts = list(Path("../data/logs").glob("logs_part_*.json"))

    f = open("../data/logs/logs.json", 'a', newline='')
    f.write("[")
    for path in logs_parts[:-1]:
        g = open(path, 'r', newline='')
        f.write(g.read())
        g.close()
        remove(path)
    with logs_parts[-1] as path:
        g = open(path, 'r', newline='')
        f.write(g.read()[:-1])
        g.close()
        remove(path)
    f.write("]")
    f.close()


def terminate_zombie_processes():
    system("taskkill /f /im chromedriver* 1>nul 2>&1")
    system("taskkill /f /im chrome* 1>nul 2>&1")
