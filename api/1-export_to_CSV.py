#!/usr/bin/python3
"""
Extend your Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    if response_user.status_code != 200 or response_todos.status_code != 200:
        print("Error: Unable to fetch data from API")
        exit(1)

    user_data = response_user.json()
    todos_data = response_todos.json()

    user_id = user_data["id"]
    username = user_data["username"]
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed_status = str(task["completed"])
            task_title = task["title"]
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

    print(f"Data exported to {csv_filename}")
