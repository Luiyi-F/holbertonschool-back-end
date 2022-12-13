#!/usr/bin/python3
"""CSV EXPORT"""

import csv
from sys import argv
from requests import get


def csv_export():
    """csv export"""

    url_base = "https://jsonplaceholder.typicode.com/"
    user = "{}user/{}".format(url_base, argv[1])
    res = get(user)
    json_user = res.json()
    username = json_user.get("username")

    todos = "{}todos?userI={}".format(url_base, argv[1])
    res = get(todos)
    json_task = res.json()
    done_task = []

    for todo in json_task:
        done_task.append(
            [argv[1], username, todo.get("completed"), todo.get("title")])

    csv_file = argv[1] + ".csv"
    with open(csv_file, mode="w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in done_task:
            writer.writerow(task)


if __name__ == "__main__":
    csv_export()
