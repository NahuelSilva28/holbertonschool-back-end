#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit()

    employee_id = sys.argv[1]
    api_base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user information
    user_response = requests.get(f"{api_base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Fetch tasks for the user
    tasks_response = requests.get(f"{api_base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Count completed tasks and collect their titles
    completed_tasks = [task for task in tasks_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    completed_task_titles = [task["title"] for task in completed_tasks]

    # Print employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], num_completed_tasks, len(tasks_data)))

    # Print the titles of completed tasks
    for title in completed_task_titles:
        print("\t{}".format(title))
