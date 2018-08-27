#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    tasksr = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
    r = tasksr.json()  # list of dictionaries
    someiterable = []
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_username = response.json().get('username', None)

    someiterable = []
    for task in r:
        a = []
        a.append("{}".format(employee_id))
        a.append("{}".format(employee_username))
        a.append("{}".format(task.get('completed', None)))
        a.append("{}".format(task.get('title', None)))
        someiterable.append(a)

    with open("{}.csv".format(employee_id), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(someiterable)
