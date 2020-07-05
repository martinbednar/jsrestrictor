import json
import os

import levenshtein_distance as levenshtein
import cosine_similarity as cosine


def was_log_added(log, logs_without_jsr):
    for log_without_jsr in logs_without_jsr:
        if log_without_jsr['level'] == log['level']:
            if log_without_jsr['source'] == log['source']:
                if log_without_jsr['message'] == log['message']:
                    return False
    return True


def main():
    if os.path.exists("../data/logs/logs_comparsion.html"):
        os.remove("../data/logs/logs_comparsion.html")

    with open("../data/logs/logs.json", 'r', newline='') as f:
        data = json.loads(f.read())


    output = "<html>" \
             "<head><title>Logs comparsion</title>" \
             "<style>" \
             "table {width: 100%; border-collapse: collapse; table-layout: fixed;}" \
             "th, td {width: 50%; border: 1px solid black; word-wrap: break-word; padding: 5px;}" \
             ".colored-results-table-visible td {width: 33%; border: none; padding: 0px; height: 15px;}" \
             ".colored-results-table-visible .added-plain {background-color: Red;}" \
             ".colored-results-table-visible .added-levenshtein {background-color: Blue;}" \
             ".colored-results-table-visible .added-cosine {background-color: Green;}" \
             ".colored-results-table {display: none;}" \
             ".colored-results-table-visible {display: table;}" \
             "</style>" \
             "</head>" \
             "<body><h1>Logs comparsion</h1>"

    for site in data:
        print(site['site'])
        output += "</br><h2>" + site['site'] + '</h2><table><tr><th>Without JSR</th><th>With JSR</th></tr>'
        i = 0
        while i < max(len(site['logs_without_jsr']), len(site['logs_with_jsr'])):
            output += "<tr><td>"
            if i < len(site['logs_without_jsr']):
                output += "Level: " + site['logs_without_jsr'][i]['level'] + "<br>"
                output += "Source: " + site['logs_without_jsr'][i]['source'] + "<br>"
                output += "Message: " + site['logs_without_jsr'][i]['message']
            output += "</td><td><table"
            output_tmp = "><tr>"
            colored_results_table_visible = False
            if i < len(site['logs_with_jsr']):
                output_tmp += "<td"
                if was_log_added(site['logs_with_jsr'][i], site['logs_without_jsr']):
                    output_tmp += ' class="added-plain"'
                    colored_results_table_visible = True
                output_tmp += "></td><td"
                if levenshtein.was_log_added(site['logs_with_jsr'][i], site['logs_without_jsr']):
                    output_tmp += ' class="added-levenshtein"'
                    colored_results_table_visible = True
                output_tmp += "></td><td"
                if cosine.was_log_added(site['logs_with_jsr'][i], site['logs_without_jsr']):
                    output_tmp += ' class="added-cosine"'
                    colored_results_table_visible = True
                output_tmp += "></td>"
            if colored_results_table_visible:
                output += ' class="colored-results-table-visible"'
            else:
                output += ' class="colored-results-table"'
            output += output_tmp + '</tr></table></br>'
            if i < len(site['logs_with_jsr']):
                output += "Level: " + site['logs_with_jsr'][i]['level'] + "<br>"
                output += "Source: " + site['logs_with_jsr'][i]['source'] + "<br>"
                output += "Message: " + site['logs_with_jsr'][i]['message']
            output += "</td></tr>"
            i += 1
        output += "</table>"

    output += "</br></br></body>"

    with open("../data/logs/logs_comparsion.html", 'a', newline='') as f:
        f.write(output)


if __name__ == "__main__":
    main()
