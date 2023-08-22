#!/usr/bin/python3
"""Export to JSON"""

import json
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

    # Get employee's tasks with expanded user data
    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos", params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    # Extract employee username
    EMPLOYEE_USERNAME = data[0]["user"]["username"]

    # Prepare data in JSON format
    tasks_json = {}
    tasks_json[EMPLOYEE_ID] = []

    for task in data:
        task_json = {
            "task": task["title"],
            "completed": task["completed"],
            "username": EMPLOYEE_USERNAME
        }
        tasks_json[EMPLOYEE_ID].append(task_json)

    # Write data to JSON file
    with open(f"{EMPLOYEE_ID}.json", "w") as json_file:
        json.dump(tasks_json, json_file, indent=4)

    print(f"Data exported to {EMPLOYEE_ID}.json")
