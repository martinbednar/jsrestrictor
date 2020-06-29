import json
from jsoncomment import JsonComment

with open("../data/logs/logs_without_jsr.json", "r") as logs_file:
    parser = JsonComment(json)
    data = parser.load(logs_file)

print(data[0]['site'])
