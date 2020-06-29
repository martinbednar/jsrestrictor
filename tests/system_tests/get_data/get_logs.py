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
    logs_without_jsr = []
    logs_with_jsr = []

    def __init__(self, site, logs_without_jsr, logs_with_jsr):
        self.site = site
        self.logs_without_jsr = logs_without_jsr
        self.logs_with_jsr = logs_with_jsr

    def to_json(self):
        return '{"site": "' + self.site + '", "logs_without_jsr": ' + json.dumps(self.logs_without_jsr) + ', "logs_with_jsr": ' + json.dumps(self.logs_with_jsr) + '}'


def init_output_files():
        io.create_folder_structure("../data/logs")
        io.delete_file_if_exists("../data/logs/logs.json")
        io.append_file("../data/logs/logs.json","[")


def finish_output_files():
        io.append_file("../data/logs/logs.json","]")


def get_page_logs(my_driver, top_site):
    try:
        my_driver.get('http://www.' + top_site)
        time.sleep(2)
    except:
        print("An exception occurred while loading page: " + top_site)
        logs = '"ERROR_WHILE_LOADING_PAGE"'
    else:
        logs = my_driver.get_log('browser')
    return logs


def get_logs_thread(thread_mark, top_sites):
    driver_without_jsr = driver.create_driver(with_jsr=False)
    driver_with_jsr = driver.create_driver(with_jsr=True)
    i = 1
    for top_site in top_sites:
        print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site)
        logs_without_jsr = get_page_logs(driver_without_jsr, top_site)
        if logs_without_jsr == '"ERROR_WHILE_LOADING_PAGE"':
            driver_without_jsr.close()
            driver_without_jsr = driver.create_driver(with_jsr=False)
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": logs_without_jsr")
        logs_with_jsr = get_page_logs(driver_with_jsr, top_site)
        if logs_with_jsr == '"ERROR_WHILE_LOADING_PAGE"':
            driver_with_jsr.close()
            driver_with_jsr = driver.create_driver(with_jsr=True)
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": logs_with_jsr")
        page_logs = Site_logs(top_site, logs_without_jsr, logs_without_jsr)
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": page_logs")
        io.append_file("../data/logs/logs.json",page_logs.to_json() + ',')
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": append_file")
        i += 1
    driver_without_jsr.close()
    driver_with_jsr.close()


def run_getting_logs_threads():
    top_sites = io.read_n_top_rows_csv(n=Config.number_of_sites_for_testing)
    browser_jobs = np.array_split(top_sites, Config.number_of_browser_instances)
    testing_threads = []
    thread_mark = 'A'
    for browser_job in browser_jobs:
        new_thread = Thread(target=get_logs_thread, args=(thread_mark,browser_job))
        testing_threads.append(new_thread)
        new_thread.start()
        thread_mark = chr(ord(thread_mark) + 1)

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
