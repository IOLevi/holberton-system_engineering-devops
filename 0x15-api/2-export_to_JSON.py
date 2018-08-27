#!/usr/bin/python3
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    tasksr = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
    r = tasksr.json()  # list of dictionaries
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_username = response.json().get('username', None)

    emp_dict = {}
    task_list = []

    for task in r:
        a = {
            'task': task.get(
                'title', None), 'completed': task.get(
                'completed', None), 'username': employee_username}
        task_list.append(a)
    emp_dict[employee_id] = task_list

    j = json.dumps(emp_dict)

    with open("{}.json".format(employee_id), 'w', encoding='utf-8') as a:
        a.write(j)
