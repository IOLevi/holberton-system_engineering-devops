#!/usr/bin/python3
import json
import requests

if __name__ == '__main__':

    allemp = requests.get("https://jsonplaceholder.typicode.com/users").json()
    emp_dict = {}

    for emp in allemp:
        employee_username = emp.get('username', None)
        employee_id = emp.get('id', None)

        r = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)).json()
        task_list = []

        for task in r:
            a = {
                'username': employee_username, 'task': task.get(
                    'title', None), 'completed': task.get(
                    'completed', None)}
            task_list.append(a)
        emp_dict[employee_id] = task_list

    j = json.dumps(emp_dict)

    with open("todo_all_employees.json".format(employee_id), 'w', encoding='utf-8') as a:
        a.write(j)
