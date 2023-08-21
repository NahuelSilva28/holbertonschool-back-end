#!/usr/bin/python3
"""Checker script for the gather_data_from_an_API.py script"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def main_0(id):
    """Check correct employee name"""

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']

    filename = 'student_output'

    with open(filename, 'r') as f:
        first = f.readline().strip()

    if name in first:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")


def main_1(id):
    """Check correct number of tasks"""

    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    filename = 'student_output'
    with open(filename, 'r') as f:
        first = f.readline().strip()

    if "{}/{}".format(todos_done, todos_count) in first:
        print("To Do Count: OK")
    else:
        print("To Do Count: Incorrect")


def main_2(id):
    """Check correct formatting of the first line"""

    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']
    
    filename = 'student_output'
    with open(filename, 'r') as f:
        first = f.readline().strip()

    output = "Employee {} is done with tasks({}/{}):".format(name, todos_done, todos_count)

    if first == output:
        print("First line formatting: OK")
    else:
        print("First line formatting: Incorrect")


def main_3(id):
    """Check all tasks in output"""

    resp = requests.get(todos_url).json()
    tasks = [task["title"] for task in resp if task["userId"] == id and task["completed"]]

    filename = 'student_output'
    with open(filename, 'r') as f:
        content = f.read()

    for task in tasks:
        if task not in content:
            print(f"Task {tasks.index(task) + 1} not in output")

    if all(task in content for task in tasks):
        print("All tasks in output: OK")
    else:
        print("All tasks in output: Incorrect")


def main_4():
    """Check correct formatting of all tasks"""

    resp = requests.get(todos_url).json()
    tasks = [task["title"] for task in resp if task["completed"]]

    filename = 'student_output'
    with open(filename, 'r') as f:
        content = f.read()

    for task in tasks:
        if "\t{}".format(task) not in content:
            print(f"Task {tasks.index(task) + 1} Formatting: Incorrect")
        else:
            print(f"Task {tasks.index(task) + 1} Formatting: OK")


if __name__ == "__main__":
    student_id = int(sys.argv[1])

    main_0(student_id)
    main_1(student_id)
    main_2(student_id)
    main_3(student_id)
    main_4()
