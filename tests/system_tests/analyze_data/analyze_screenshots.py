import io_funcs as io
from os import listdir
import cv2
import numpy as np



def main():
    io.delete_file_if_exists("../data/screenshots/screenshots_comparsion.html")

    sites = listdir("../data/screenshots")
    sites.sort(key=lambda x: int(x.split('_')[0]))
    for site in sites:
        screen_without_jsr = cv2.imread("../data/screenshots/" + site + "/without_jsr.png")
        screen_with_jsr = cv2.imread("../data/screenshots/" + site + "/with_jsr.png")
        differences = cv2.subtract(screen_with_jsr, screen_without_jsr)
        cv2.imwrite("../data/screenshots/" + site + "/differences.png", differences)
        differences_gray = cv2.cvtColor(differences, cv2.COLOR_BGR2GRAY)
        print(np.mean(differences_gray))

if __name__ == "__main__":
    main()
