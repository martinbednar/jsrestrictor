from subprocess import Popen
import time
import csv
import numpy as np


def read_n_top_sites_csv(n):
    with open('tranco.csv', 'r') as csvTopSites:
        data = np.array(list(csv.reader(csvTopSites)))

    return data[0:n, 1]



start_server = ['java', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'hub']
start_node1 = ['java', '-Dwebdriver.gecko.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\geckodriver.exe', '-Dwebdriver.chrome.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\chromedriver.exe', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'node', '-hub', 'https://localhost:4444/grid/register/']
start_node2 = ['java', '-Dwebdriver.gecko.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\geckodriver.exe', '-Dwebdriver.chrome.driver=D:\\Development\\jsrestrictor\\tests\\common_files\\webbrowser_drivers\\chromedriver.exe', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'node', '-hub', 'https://localhost:4444/grid/register/']

server = Popen(start_server)
print(server)

time.sleep( 5 )

node1 = Popen(start_node1)
print(node1)
time.sleep( 7 )
node2 = Popen(start_node2)
print(node2)

time.sleep( 7 )

####################################
try:
    processes = []

    for top_site in read_n_top_sites_csv(n=3):
        run_test = ['python', 'test.py', top_site]
        processes.append(Popen(run_test, shell=True))
        time.sleep(5)

    i = 0
    for process in processes:
        processes[i].wait()
        i+=1

###################################

finally:
    time.sleep( 10 )

    node1.kill()
    node2.kill()

    time.sleep( 2 )

    server.kill()
