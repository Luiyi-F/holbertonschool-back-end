#!/usr/bin/python3
"""serialization json"""
import json
from requests import get


def dld():
    """export json"""

    base_url = "https://jsonplaceholder.typicode.com"
    employee = get('{}/users'.format(base_url))
    user_list = employee.json()
    task_list = []

    for user in user_list:
        tasks = get('{}/todos?userId={}'.format(base_url, user.get("id")))
        task_list += tasks.json()

    json_dict = {user.get("id"): [{"task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": user.get('username')}
                                  for task in task_list
                                  if user.get('id') == task.get("userId")]
                 for user in user_list}

    with open('todo_all_employees.json', 'w') as fp:
        json.dump(json_dict, fp)


if __name__ == "__main__":
    dld()
