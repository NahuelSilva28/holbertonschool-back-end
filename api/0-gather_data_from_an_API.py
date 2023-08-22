#!/usr/bin/python3
"""Export to CSV"""

import json
import requests
import sys

if __name__ == '__main__':
    """Export tasks data to CSV"""

    # Fetch user data
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    user_data = user_response.json()
    name = user_data['name']

    # Fetch user's tasks
    tasks_response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1]))
    tasks_data = tasks_response.json()

    # Count tasks and collect titles
    total_tasks = len(tasks_data)
    tasks_done = 0
    lists_of_titles = []
    
    for task in tasks_data:
        if task['userId'] == int(sys.argv[1]):
            if task['completed']:
                tasks_done += 1
                lists_of_titles.append(task['title'])

    # Print task summary
    print("Employee {} is done with tasks ({}/{}):".format(name, tasks_done, total_tasks))
    for title in lists_of_titles:
        print("\t{}".format(title))
