#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    tasksr = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(employee_id))
    r = tasksr.json()  # list of dictionaries
    number_of_tasks = len(r)
    tasks_completed = 0
    for task in r:
        if task.get('completed', None):
            tasks_completed += 1

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_name = response.json().get('name', None)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name,
                 tasks_completed, number_of_tasks))

    for task in r:
        if task.get('completed', None):
            print("\t {}".format(task.get('title', None)))
