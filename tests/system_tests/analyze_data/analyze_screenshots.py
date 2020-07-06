import io_funcs as io
from os import listdir
import cv2
import numpy as np


def html_header():
    return "<html>" \
           "<head><title>Screenshots comparsion</title>" \
           "<style>" \
           "body {background-color: white;} " \
           "img {width: 100%;} " \
           "td {width: 50%;  border: 1px solid black; padding: 5px;}" \
           "table {width: 100%; text-align: center; border-collapse: collapse;}" \
           ".differences-table {width: 50%; margin-left: 25%; margin-right: 25%;}" \
           "</style>" \
           "</head>" \
           "<body><h1>Screenshots comparsion</h1>"


def html_footer():
    return "<br><br></body></html>"


def build_site_screenshots_comparsion(site, average_color_of_differences):
    output = "<br><h2>" + site + "</h2><table><tr><th>Without JSR</th><th>With JSR</th></tr>"
    output += '<tr><td><img src="' + site + '/without_jsr.png"></td><td><img src="' + site + '/with_jsr.png"></td></tr></table>'
    output += '<table class="differences-table"><tr><th>Differences</th></tr><tr><td><img src="' + site + '/differences.png"></td></tr></table>'
    return output


def main():
    io.delete_file_if_exists("../data/screenshots/screenshots_comparsion.html")

    output = html_header()

    sites = listdir("../data/screenshots")
    sites.sort(key=lambda x: int(x.split('_')[0]))
    j = 1
    sites_number = len(sites)
    for site in sites:
        print("Site " + str(j) + " of " + str(sites_number) + ": " + site)
        screen_without_jsr = cv2.imread("../data/screenshots/" + site + "/without_jsr.png")
        screen_with_jsr = cv2.imread("../data/screenshots/" + site + "/with_jsr.png")
        differences = cv2.subtract(screen_with_jsr, screen_without_jsr)
        cv2.imwrite("../data/screenshots/" + site + "/differences.png", differences)
        differences_gray = cv2.cvtColor(differences, cv2.COLOR_BGR2GRAY)
        output += build_site_screenshots_comparsion(site, np.mean(differences_gray))
        j += 1

    output += html_footer()
    io.write_file("../data/screenshots/screenshots_comparsion.html", output)

if __name__ == "__main__":
    main()
