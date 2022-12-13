#!/usr/bin/python3
"""serialization json"""
import json
from sys import argv
from requests import get


def json_export():
    """export json"""

    base_url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]

    employee = get('{}/users/{}'.format(base_url, user_id))
    username = employee.json().get('username')

    tasks = get('{}/todos?userId={}'.format(base_url, user_id))
    task_list = tasks.json()

    json_dict = {user_id: [{"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username}
                           for task in task_list]}

    with open('{}.json'.format(user_id), 'w') as fp:
        json.dump(json_dict, fp)


if __name__ == "__main__":
    json_export()
