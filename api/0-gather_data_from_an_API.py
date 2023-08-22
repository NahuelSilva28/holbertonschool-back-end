#!/usr/bin/python3
"""Import necessary modules"""

import requests
import sys

if __name__ == "__main__":
    # Check if employee ID is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Missing employee ID as argument")
        sys.exit(1)

    # API URL and employee ID
    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    # Construct URL for employee's tasks with expanded user data
    employee_todos_url = f"{URL}/users/{EMPLOYEE_ID}/todos"
    EMPLOYEE_TODOS = requests.get(employee_todos_url,
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    # Extract employee name, total tasks count, and completed tasks
    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    # Count completed tasks and store their titles
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])

    # Print employee's task progress
    print(f"Employee {EMPLOYEE_NAME} is done with tasks "
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print("\t", title)
