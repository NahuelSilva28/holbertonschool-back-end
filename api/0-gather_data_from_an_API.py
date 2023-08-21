#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    # Define the API endpoint and employee ID
    api_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])

    # Request user data
    user_response = requests.get("{}/users/{}".format(api_url, employee_id))
    user_data = user_response.json()

    # Request tasks data
    tasks_response = requests.get("{}/todos?userId={}".format(api_url, employee_id))
    tasks_data = tasks_response.json()

    # Calculate task statistics
    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Print employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], num_completed_tasks, total_tasks))

    # Print the titles of completed tasks
    for task in completed_tasks:
        print("\t", task["title"])
