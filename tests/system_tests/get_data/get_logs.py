import time
import json
import numpy as np
from threading import Thread

import io_funcs as io
import grid
import driver
from configuration import Config


class Site_logs:
    site = ''
    logs = []

    def __init__(self, site, logs):
        self.site = site
        self.logs = logs

    def to_json(self):
        return '{"site": "' + self.site + '", "logs": ' + json.dumps(self.logs) + '}'


def init_output_files():
        io.create_folder_structure("../data/logs")
        io.delete_file_if_exists("../data/logs/logs_without_jsr.json")
        io.delete_file_if_exists("../data/logs/logs_with_jsr.json")
        io.append_file("../data/logs/logs_without_jsr.json","[")
        io.append_file("../data/logs/logs_with_jsr.json","[")


def finish_output_files():
        io.append_file("../data/logs/logs_without_jsr.json","]")
        io.append_file("../data/logs/logs_with_jsr.json","]")


def get_page_logs(my_driver, top_site):
    try:
        print("Getting page started.")
        my_driver.get('http://www.' + top_site)
        print("Getting page finished.")
        time.sleep(5)
    except e:
        print("An exception occurred while loading page: " + top_site)
        print(e)
        logs = Site_logs(top_site, 'ERROR_WHILE_LOADING_PAGE')
    else:
        print("Getting logs started.")
        logs = Site_logs(top_site, my_driver.get_log('browser'))
        print("Getting logs finished.")
    return logs


def get_logs_thread(top_sites):
    my_driver = driver.create_driver(with_jsr=False)
    for top_site in top_sites:
        logs = get_page_logs(my_driver, top_site)
        f = open('../data/logs/logs_without_jsr.json', 'a', newline='')
        f.write(logs.to_json() + ',')
        f.close()
    my_driver.close()

    my_driver = driver.create_driver(with_jsr=True)
    for top_site in top_sites:
        logs = get_page_logs(my_driver, top_site)
        f = open('../data/logs/logs_with_jsr.json', 'a', newline='')
        f.write(logs.to_json() + ',')
        f.close()
    my_driver.close()


def run_getting_logs_threads():
    top_sites = io.read_n_top_rows_csv(n=Config.number_of_sites_for_testing)
    browser_jobs = np.array_split(top_sites, Config.number_of_browser_instances)
    testing_threads = []
    for browser_job in browser_jobs:
        new_thread = Thread(target=get_logs_thread, args=(browser_job,))
        testing_threads.append(new_thread)
        new_thread.start()
        time.sleep(2)

    for thread in testing_threads:
        thread.join()


def main():
    server = grid.start_server()
    nodes = grid.start_nodes()

    try:
        init_output_files()
        run_getting_logs_threads()
        finish_output_files()
    finally:
        grid.end_nodes(nodes)
        grid.end_server(server)


if __name__ == "__main__":
    main()
