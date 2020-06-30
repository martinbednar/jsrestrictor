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


def get_page_logs_thread(my_driver, top_site, q):
    try:
        my_driver.execute_script("console.clear()")
        print("Getting page " + top_site + " started.")
        my_driver.get('http://www.' + top_site)
        print("Getting page " + top_site + " finished.")
        print("Sleeping page " + top_site + " started.")
        time.sleep(5)
        print("Sleeping page " + top_site + " finished.")
    except:
        print("An exception occurred while loading page: " + top_site)
        logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    else:
        try:
            print("Getting log " + top_site + " started.")
            logs = my_driver.get_log('browser')
            print(logs)
            print("Getting log " + top_site + " finished.")
        except:
            print("An exception occurred while getting page logs: " + top_site)
            logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    q.put(logs)
    return


def get_logs_thread(thread_mark, top_sites):
    driver_without_jsr = driver.create_driver(with_jsr=False)
    driver_with_jsr = driver.create_driver(with_jsr=True)

    queue_without_jsr = multiprocessing.Queue()
    queue_with_jsr = multiprocessing.Queue()

    i = 1
    for top_site in top_sites:
        print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site)

        #Clear queues
        while not queue_without_jsr.empty():
            queue_without_jsr.get()
        while not queue_with_jsr.empty():
            queue_with_jsr.get()

        logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"

        get_logs_without_jsr_thread = multiprocessing.Process(target=get_page_logs_thread, args=(driver_without_jsr, top_site, queue_without_jsr))
        get_logs_without_jsr_thread.start()

        get_logs_with_jsr_thread = multiprocessing.Process(target=get_page_logs_thread, args=(driver_with_jsr, top_site, queue_with_jsr))
        get_logs_with_jsr_thread.start()

        print("Waiting to join.")
        get_logs_without_jsr_thread.join(30)
        print("Joined 1.")
        get_logs_with_jsr_thread.join(30)
        print("Joined 2.")


        if get_logs_without_jsr_thread.is_alive():
            print("running... let's kill it...")
            # Terminate
            get_logs_without_jsr_thread.terminate()
            print("terminated")
            get_logs_without_jsr_thread.join()
            print("joined after terminated")
            logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        else:
            if not queue_without_jsr.empty():
                logs_without_jsr = queue_without_jsr.get()
            else:
                logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"

        if get_logs_with_jsr_thread.is_alive():
            print("running... let's kill it... with jsr")
            # Terminate
            get_logs_with_jsr_thread.terminate()
            get_logs_with_jsr_thread.join()
            logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        else:
            if not queue_with_jsr.empty():
                logs_with_jsr = queue_with_jsr.get()
            else:
                logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"


        print("terminating finished")
        if logs_without_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE":
            print("before driver close")
            #os.system("taskkill /f /im chromedriver.exe")
            #driver_without_jsr.service.process.kill()
            #driver_with_jsr.service.process.kill()
            driver_without_jsr = driver.create_driver(with_jsr=False)
            print("after driver close")
        if logs_with_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE":
            print("before driver close")
            #os.system("taskkill /f /im chromedriver.exe")
            #driver_without_jsr.service.process.kill()
            #driver_with_jsr.service.process.kill()
            driver_with_jsr = driver.create_driver(with_jsr=True)
            print("after driver close")

        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": logs_with_jsr")
        page_logs = Site_logs(top_site, logs_without_jsr, logs_with_jsr)
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": page_logs")
        io.append_file("../data/logs/logs.json",page_logs.to_json() + ',')
        #print("Thread " + thread_mark + ": Page " + str(i) + " of " + str(len(top_sites)) + ": " + top_site + ": append_file")
        i += 1
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
        os.system("taskkill /f /im chromedriver.exe")
        os.system("taskkill /f /im chrome.exe")
        grid.end_nodes(nodes)
        grid.end_server(server)


if __name__ == "__main__":
    main()
