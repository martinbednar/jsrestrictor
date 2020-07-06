import os
import json


def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)


def get_json_file_content(path):
    data = []
    try:
        f = open(path, 'r', newline='')
        data = json.loads(f.read())
        f.close()
    except:
        print("File " + path + " not exists or it is not accessible for reading. If you are trying analyze logs, you have to generate them first.")
    finally:
        return data


def write_file(path, content):
    with open(path, 'w', newline='') as f:
        f.write(content)


def html_header():
    return "<html>" \
           "<head><title>Logs comparsion</title>" \
           "<style>" \
           "body {background-color: white} " \
           "table {width: 100%; border-collapse: collapse; table-layout: fixed;} " \
           ".added-log {background-color: LightPink} " \
           "th, td {width: 50%; border: 1px solid black; word-wrap: break-word; padding: 5px;} " \
           ".colored-results-table-visible td {width: 33%; border: none; padding: 5px; color: white; text-align: center;} " \
           ".colored-results-table-visible .method {background-color: red;} " \
           ".colored-results-table {display: none;} " \
           ".colored-results-table-visible {display: table; margin-bottom: 5px} " \
           "</style>" \
           "</head>" \
           "<body><h1>Logs comparsion</h1>"


def html_footer():
    return "<br><br></body></html>"
