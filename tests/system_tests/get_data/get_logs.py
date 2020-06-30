import time
import json
import numpy as np
from threading import Thread
import multiprocessing
import os

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


def get_page_logs_thread(my_driver, site, logs_ready, ret_logs):
    logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    try:
        my_driver.get('http://www.' + site)
        time.sleep(5)
    except:
        print("An exception occurred while loading page: " + top_site)
        logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    else:
        try:
            logs = my_driver.get_log('browser')
        except:
            print("An exception occurred while getting page logs: " + top_site)
            logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    finally:
        print("before send logs")
        logs_ready.value = 1
        ret_logs.send(logs)
        print("after_send_logs")


def get_logs_thread(thread_mark, top_sites):
    driver_without_jsr = driver.create_driver(with_jsr=False)
    driver_with_jsr = driver.create_driver(with_jsr=True)

    receive_logs_without_jsr_pipe, send_logs_without_jsr_pipe = multiprocessing.Pipe(False)
    receive_logs_with_jsr_pipe, send_logs_with_jsr_pipe = multiprocessing.Pipe(False)

    send_logs_without_jsr_pipe_ready = multiprocessing.Value('i', 0)
    send_logs_with_jsr_pipe_ready = multiprocessing.Value('i', 0)

    i = 1
    for top_site in top_sites:
        print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site)

        logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"

        send_logs_without_jsr_pipe_ready.value = 0
        send_logs_with_jsr_pipe_ready.value = 0

        get_logs_without_jsr_thread = multiprocessing.Process(target=get_page_logs_thread, args=(driver_without_jsr, top_site, send_logs_without_jsr_pipe_ready, send_logs_without_jsr_pipe))
        get_logs_without_jsr_thread.start()

        get_logs_with_jsr_thread = multiprocessing.Process(target=get_page_logs_thread, args=(driver_with_jsr, top_site, send_logs_with_jsr_pipe_ready, send_logs_with_jsr_pipe))
        get_logs_with_jsr_thread.start()

        for j in range(12):
            time.sleep(5)

            if send_logs_without_jsr_pipe_ready.value == 1 and send_logs_with_jsr_pipe_ready.value == 1:
                print("breaked")
                break

        if send_logs_without_jsr_pipe_ready.value == 1:
            logs_without_jsr = receive_logs_without_jsr_pipe.recv()
            get_logs_without_jsr_thread.join(10)
            if get_logs_without_jsr_thread.is_alive():
                get_logs_without_jsr_thread.terminate()
                get_logs_without_jsr_thread.join()
                logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        else:
            logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
            if get_logs_without_jsr_thread.is_alive():
                get_logs_without_jsr_thread.terminate()
                get_logs_without_jsr_thread.join()

        if send_logs_with_jsr_pipe_ready.value == 1:
            logs_with_jsr = receive_logs_with_jsr_pipe.recv()
            get_logs_with_jsr_thread.join(10)
            if get_logs_with_jsr_thread.is_alive():
                get_logs_with_jsr_thread.terminate()
                get_logs_with_jsr_thread.join()
                logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        else:
            logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
            if get_logs_with_jsr_thread.is_alive():
                get_logs_with_jsr_thread.terminate()
                get_logs_with_jsr_thread.join()


        if logs_without_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE" or logs_without_jsr == "":
            driver_without_jsr = driver.create_driver(with_jsr=False)

        if logs_with_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE" or logs_without_jsr == "":
            driver_with_jsr = driver.create_driver(with_jsr=True)

        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": logs_with_jsr")
        page_logs = Site_logs(top_site, logs_without_jsr, logs_with_jsr)
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": page_logs")
        io.append_file("../data/logs/logs.json",page_logs.to_json() + ',')
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": append_file")
        i += 1
    receive_logs_without_jsr_pipe.close()
    send_logs_without_jsr_pipe.close()
    receive_logs_with_jsr_pipe.close()
    send_logs_with_jsr_pipe.close()

    driver_without_jsr.quit()
    driver_with_jsr.quit()


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
        time.sleep(5)
        os.system("taskkill /f /im chromedriver.exe")
        os.system("taskkill /f /im chrome.exe")
        grid.end_nodes(nodes)
        grid.end_server(server)


if __name__ == "__main__":
    main()
