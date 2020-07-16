from time import sleep
from numpy import array_split
from multiprocessing import Process, Value, Pipe

from configuration import Config
from website import Logs
import io_funcs as io
import grid
import driver
from web_browser_type import BrowserType
from test_type import TestType


def confirm_alerts_if_open(my_driver, with_jsr, time):
    if with_jsr and Config.jsr_level == 3:
        i=0
        while i<time:
            try:
                sleep(0.1)
                my_driver.switch_to.alert.accept()
            except:
                pass
            finally:
                i += 1


def receive_logs(send_logs_pipe_ready, receive_logs_pipe, get_logs_thread):
    if send_logs_pipe_ready.value == 1:
        logs = receive_logs_pipe.recv()
        get_logs_thread.join(10)
        if get_logs_thread.is_alive():
            get_logs_thread.terminate()
            get_logs_thread.join()
            logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    else:
        logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        if get_logs_thread.is_alive():
            get_logs_thread.terminate()
            get_logs_thread.join()
    return logs


def get_page_data_thread(my_driver, with_jsr, site, site_number, logs_ready, ret_logs):
    logs = []
    confirm_alerts_if_open(my_driver, with_jsr, 10)
    try:
        my_driver.get('http://www.' + site)
        confirm_alerts_if_open(my_driver, with_jsr, 100)
    except:
        print("An exception occurred while loading page: " + site)
        logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
    else:
        if TestType.LOGS in Config.perform_tests:
            try:
                confirm_alerts_if_open(my_driver, with_jsr, 10)
                logs = my_driver.get_log('browser')
            except:
                print("An exception occurred while getting page logs: " + site)
                logs = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        if TestType.SCREENSHOTS in Config.perform_tests:
            try:
                jsr = "without"
                if with_jsr:
                    jsr = "with"
                io.create_folder_structure("../data/screenshots/" + str(site_number) + "_" + site)
                confirm_alerts_if_open(my_driver, with_jsr, 10)
                my_driver.save_screenshot("../data/screenshots/" + str(site_number) + "_" + site + "/" + jsr + "_jsr" + ".png")
            except:
                print("An exception occurred while getting page screenshot: " + site)
    finally:
        logs_ready.value = 1
        ret_logs.send(logs)


def testing_controller_thread(thread_mark, browser_type, top_sites, sites_offset):
    driver_without_jsr = driver.create_driver(browser_type, with_jsr=False, jsr_level=None)
    driver_with_jsr = driver.create_driver(browser_type, with_jsr=True, jsr_level=Config.jsr_level)

    receive_logs_without_jsr_pipe, send_logs_without_jsr_pipe = Pipe(False)
    receive_logs_with_jsr_pipe, send_logs_with_jsr_pipe = Pipe(False)

    send_logs_without_jsr_pipe_ready = Value('i', 0)
    send_logs_with_jsr_pipe_ready = Value('i', 0)

    site_number = 1
    top_sites_number = len(top_sites)
    for top_site in top_sites:
        print("Thread " + thread_mark + ": " + str(browser_type) + ": Page " + str(site_number) + " of " + str(top_sites_number) + ": " + top_site)

        logs_without_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"
        logs_with_jsr = "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE"

        send_logs_without_jsr_pipe_ready.value = 0
        send_logs_with_jsr_pipe_ready.value = 0

        get_logs_without_jsr_thread = Process(target=get_page_data_thread, args=(driver_without_jsr, False, top_site, sites_offset + site_number, send_logs_without_jsr_pipe_ready, send_logs_without_jsr_pipe))
        get_logs_without_jsr_thread.start()

        get_logs_with_jsr_thread = Process(target=get_page_data_thread, args=(driver_with_jsr, True, top_site, sites_offset + site_number, send_logs_with_jsr_pipe_ready, send_logs_with_jsr_pipe))
        get_logs_with_jsr_thread.start()

        for _ in range(int(Config.get_page_data_timeout/Config.wait_between_checks_if_page_data_loaded)):
            sleep(Config.wait_between_checks_if_page_data_loaded)
            if send_logs_without_jsr_pipe_ready.value == 1 and send_logs_with_jsr_pipe_ready.value == 1:
                break

        logs_without_jsr = receive_logs(send_logs_without_jsr_pipe_ready, receive_logs_without_jsr_pipe, get_logs_without_jsr_thread)
        logs_with_jsr = receive_logs(send_logs_with_jsr_pipe_ready, receive_logs_with_jsr_pipe, get_logs_with_jsr_thread)

        if logs_without_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE" or logs_without_jsr == "":
            driver_without_jsr = driver.create_driver(browser_type, with_jsr=False, jsr_level=None)

        if logs_with_jsr == "ERROR_WHILE_LOADING_THIS_OR_PREVIOUS_PAGE" or logs_without_jsr == "":
            driver_with_jsr = driver.create_driver(browser_type, with_jsr=True, jsr_level=Config.jsr_level)

        page_logs = Logs(top_site, logs_without_jsr, logs_with_jsr)
        io.append_file("../data/logs/logs_part_" + thread_mark + ".json", page_logs.to_json() + ',')
        site_number += 1

    receive_logs_without_jsr_pipe.close()
    send_logs_without_jsr_pipe.close()
    receive_logs_with_jsr_pipe.close()
    send_logs_with_jsr_pipe.close()

    driver_without_jsr.quit()
    driver_with_jsr.quit()


def run_browsers_thread(thread_mark, browser_job, sites_offset):
    browser_threads = []
    for browser_type in Config.tested_browsers:
        new_thread = Process(target=testing_controller_thread, args=(thread_mark, browser_type, browser_job, sites_offset))
        browser_threads.append(new_thread)
        new_thread.start()

    for thread in browser_threads:
        thread.join()


def run_getting_logs_threads():
    if not Config.perform_tests:
        print("'perform_tests' property in Configuration is empty. No test to perform.")
    else:
        top_sites = io.read_n_top_rows_csv(n=Config.number_of_sites_for_testing)
        browser_jobs = array_split(top_sites, Config.number_of_concurrent_sites_testing)
        testing_threads = []
        thread_mark = 'A'
        sites_offset = 0
        for browser_job in browser_jobs:
            new_thread = Process(target=run_browsers_thread, args=(thread_mark, browser_job, sites_offset))
            testing_threads.append(new_thread)
            new_thread.start()
            thread_mark = chr(ord(thread_mark) + 1)
            sites_offset += len(browser_job)

        for thread in testing_threads:
            thread.join()


def main():
    if Config.grid_server_ip_address == 'localhost':
        server = grid.start_server()
    nodes = grid.start_nodes()

    if Config.grid_server_ip_address == 'localhost':
        try:
            io.init_output_files()
            run_getting_logs_threads()
            io.finish_output_files()
        finally:
            sleep(3)
            io.terminate_zombie_processes()
            grid.end_nodes(nodes, manually=False)
            grid.end_server(server)
    else:
        grid().end_nodes(nodes, manually=True)


if __name__ == "__main__":
    main()
