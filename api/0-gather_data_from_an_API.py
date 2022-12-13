#!/usr/bin/python3
"""Return the infor for employee
whose ID is passed in the script"""
from requests import get
from sys import argv


def api_todo():
    """Data struct"""
    employee_id = int(argv[1])
    employee_name = ""
    number_of_task = 0
    number_of_done_task = 0
    titles_of_task = []

    api_users = get("https://jsonplaceholder.typicode.com/users").json()
    for user in api_users:
        if user["id"] == employee_id:
            employee_name = user["name"]
            break

    api_tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    for task in api_tasks:
        if task["id"] == employee_id:
            if task["complete"]:
                titles_of_task.append(task["title"])
                number_of_done_task += 1
            number_of_task += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_task, number_of_task))

    for title in titles_of_task:
        print("\t {}".format(title))


if __name__ == "__main__":
    api_todo()
