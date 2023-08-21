#!/usr/bin/python3
"""Import necessary modules"""

import requests
import sys

if __name__ == "__main__":
    # Check if employee ID is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Missing employee ID")
        sys.exit(1)

    # API URL and employee ID
    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    # Get employee's tasks with expanded user data
    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos", params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    # Extract employee name, total tasks count, and completed tasks
    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0

    # Count completed tasks
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1

    # Print employee's task progress
    print(f"First line formatting: {'OK' if len(sys.argv) == 2 else 'Incorrect'}")
