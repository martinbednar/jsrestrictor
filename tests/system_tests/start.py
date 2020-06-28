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
for node_number in range(0,Config.number_of_grid_nodes-1):
    nodes.append(Popen(start_node_command))
    time.sleep( 7 )

####################################
if os.path.exists("logs_without_jsr.csv"):
    os.remove("logs_without_jsr.csv")

try:
    testing_threads = []
    for top_site in read_n_top_sites_csv(n=Config.number_of_sites_for_testing):
        new_thread = Thread(target=start_test, args=(top_site,))
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
