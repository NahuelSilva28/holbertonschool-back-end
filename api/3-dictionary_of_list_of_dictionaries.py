#!/usr/bin/python3
"""Export all employee tasks to JSON"""

import json
import requests

if __name__ == "__main__":
    # API URL
    URL = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{URL}/users")
    users_data = users_response.json()

    all_tasks = {}

    # Fetch tasks for all users
    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        tasks_response = requests.get(f"{URL}/todos", params={"userId": user_id})
        tasks_data = tasks_response.json()

        tasks_list = []
        for task in tasks_data:
            task_info = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            tasks_list.append(task_info)

        all_tasks[user_id] = tasks_list

    # Write data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)
