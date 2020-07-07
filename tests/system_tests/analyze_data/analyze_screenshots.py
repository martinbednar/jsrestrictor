import io_funcs as io
from os import listdir
import cv2
import numpy as np


def html_header():
    return "<html>" \
           "<head><title>Screenshots comparison</title>" \
           "<style>" \
           "body {background-color: white;} " \
           "img {width: 100%;} " \
           "td {width: 50%;  border: 1px solid black; padding: 5px;} " \
           "table {width: 100%; text-align: center; border-collapse: collapse;} " \
           ".differences-table {width: 50%; margin-left: 25%; margin-right: 25%;} " \
           ".treshold-cointainer {width: 100%; text-align: center;} " \
           ".slider {width: 85%; display: block; margin: auto;} " \
           "h2 {width: 50%; float: left;} " \
           "h3 {width: 50%; text-align: right; float: right; margin-top: 5px;} " \
           ".site-container {display: initial;} " \
           ".site-container-hidden {display: none;} " \
           "</style>" \
           "</head>" \
           '<body><h1>Screenshots comparison</h1>' \
           '<div class="treshold-cointainer"><input type="range" min="0" max="255" value="0" class="slider" id="threshold">' \
           '<p>The treshold for the mean value of pixels in the Differences image (Screenshots below treshold will not be shown on this page.): <span id="treshold_value"></span></p></div>'


def html_footer():
    return "<br><br>" \
           "<script>" \
           "function hideIfUnderTreshold(item) {" \
           'var slider = document.getElementById("threshold");' \
           'if (parseFloat(item.getAttribute("mean_pixel_value_of_diff")) < slider.value) {' \
           'item.classList.remove("site-container"); item.classList.add("site-container-hidden");}' \
           "}" \
           "function showIfNotUnderTreshold(item) {" \
           'var slider = document.getElementById("threshold");' \
           'if (!(parseFloat(item.getAttribute("mean_pixel_value_of_diff")) < slider.value)) {' \
           'item.classList.remove("site-container-hidden"); item.classList.add("site-container");}' \
           "}" \
           'var slider = document.getElementById("threshold");' \
           'var slider_value = document.getElementById("treshold_value");' \
           'slider_value.innerHTML = slider.value;' \
           'slider.oninput = function() {' \
           'slider_value.innerHTML = this.value;' \
           'var visibleSites = Array.from(document.getElementsByClassName("site-container"));' \
           'visibleSites.forEach(hideIfUnderTreshold);' \
           'var hiddenSites = Array.from(document.getElementsByClassName("site-container-hidden"));' \
           'hiddenSites.forEach(showIfNotUnderTreshold);' \
           '}' \
           "</script>" \
           "</body></html>"


def build_site_screenshots_comparison(site, site_name, site_number, average_color_of_differences):
    output = '<div class="site-container" mean_pixel_value_of_diff="' + str(average_color_of_differences) + '"><br><h2>' + str(site_number) +\
             ") "  + site_name + '</h2><h3>Mean pixel value in Differences image: ' + str(average_color_of_differences) + '</h3><table><tr><th>Without JSR</th><th>With JSR</th></tr>'
    output += '<tr><td><img src="' + site + '/without_jsr.png"></td><td><img src="' + site + '/with_jsr.png"></td></tr></table>'
    output += '<table class="differences-table"><tr><th>Differences</th></tr><tr><td><img src="' + site + '/differences.png"></td></tr></table></div>'
    return output


def main():
    io.delete_file_if_exists("../data/screenshots/screenshots_comparison.html")

    output = html_header()

    sites = listdir("../data/screenshots")
    sites.sort(key=lambda x: int(x.split('_')[0]))
    j = 1
    sites_number = len(sites)
    for site in sites:
        site_name = site.split('_', 1)[1]
        print("Site " + str(j) + " of " + str(sites_number) + ": " + site_name)
        screen_without_jsr = cv2.imread("../data/screenshots/" + site + "/without_jsr.png")
        screen_with_jsr = cv2.imread("../data/screenshots/" + site + "/with_jsr.png")
        differences = cv2.subtract(screen_with_jsr, screen_without_jsr)
        cv2.imwrite("../data/screenshots/" + site + "/differences.png", differences)
        differences_gray = cv2.cvtColor(differences, cv2.COLOR_BGR2GRAY)
        output += build_site_screenshots_comparison(site, site_name, j, round(np.mean(differences_gray), 3))
        j += 1

    output += html_footer()
    io.write_file("../data/screenshots/screenshots_comparison.html", output)

if __name__ == "__main__":
    main()
