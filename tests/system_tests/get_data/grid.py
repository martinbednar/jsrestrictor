from subprocess import Popen
import time

from configuration import Config


def start_server():
    start_server_command = ['java', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'hub']
    server = Popen(start_server_command)
    time.sleep(6)
    return server


def start_nodes():
    start_node_command = ['java', '-Dwebdriver.gecko.driver=../../common_files/webbrowser_drivers/geckodriver.exe', '-Dwebdriver.chrome.driver=../../common_files/webbrowser_drivers/chromedriver.exe', '-jar', 'selenium-server-standalone-3.141.59.jar', '-role', 'node', '-hub', 'https://localhost:4444/grid/register/']
    nodes = []
    for node_number in range(Config.number_of_grid_nodes):
        nodes.append(Popen(start_node_command))
        time.sleep(7)
    return nodes


def end_nodes(nodes):
    for node in nodes:
        node.kill()

def end_server(server):
    server.kill()
