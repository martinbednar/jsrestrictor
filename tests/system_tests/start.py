from subprocess import Popen
from threading import Thread
import time
import csv
import numpy as np
import os

from configuration import Config
from testing_control import start_test


def read_n_top_sites_csv(n):
    with open('tranco.csv', 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))
    return data[0:n, 1]


start_server_command = ['java', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'hub']
start_node_command = ['java', '-Dwebdriver.gecko.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\geckodriver.exe', '-Dwebdriver.chrome.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\chromedriver.exe', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'node', '-hub', 'https://localhost:4444/grid/register/']

server = Popen(start_server_command)
time.sleep( 5 )

nodes = []
for node_number in range(Config.number_of_grid_nodes):
    nodes.append(Popen(start_node_command))
    time.sleep( 7 )

####################################
if os.path.exists("logs_without_jsr.json"):
    os.remove("logs_without_jsr.json")
f = open('logs_without_jsr.json', 'a', newline='')
f.write('[')
f.close()

try:
    top_sites = read_n_top_sites_csv(n=Config.number_of_sites_for_testing)
    
    browser_jobs = np.array_split(top_sites, Config.number_of_one_browser_instances)
    testing_threads = []
    for browser_job in browser_jobs:
        new_thread = Thread(target=start_test, args=(browser_job,))
        testing_threads.append(new_thread)
        new_thread.start()
        time.sleep(2)

    for thread in testing_threads:
        thread.join()

###################################

finally:
    for node in nodes:
        node.kill()

    server.kill()

f = open('logs_without_jsr.json', 'a', newline='')
f.write(']')
f.close()