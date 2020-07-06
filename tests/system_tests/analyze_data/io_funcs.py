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