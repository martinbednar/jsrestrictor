from subprocess import Popen
from time import sleep

from configuration import Config


def start_server():
    start_server_command = ['java', '-jar', Config.selenium_server_jar_path, '-role', 'hub']
    server = Popen(start_server_command)
    sleep(6)
    return server


def start_nodes():
    start_node_command = ['java', '-Dwebdriver.chrome.driver=' + Config.chrome_driver_path, '-jar', Config.selenium_server_jar_path, '-role', 'node', '-hub', 'https://' + Config.grid_server_ip_address + ':4444/grid/register/']
    nodes = []
    if Config.number_of_grid_nodes_on_this_device == 0:
        input("When all testing nodes will be running, press Enter to start JSR system testing.")
    else:
        for node_number in range(Config.number_of_grid_nodes_on_this_device):
            nodes.append(Popen(start_node_command))
            sleep(7)
    return nodes


def end_nodes(nodes, manually):
    if manually:
        input("After testing, press Enter to end the nodes.")
    for node in nodes:
        node.kill()

def end_server(server):
    server.kill()
