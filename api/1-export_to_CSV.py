#!/usr/bin/python3
"""Export data to CSV format"""


import csv
import requests
from sys import argv


def get_api():

    """Retrieve data from an API"""

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    # Fetch user information from API
    user_info = requests.get(base_url + 'users/{}'.format(user_id)).json()

    # Fetch tasks associated with the user ID
    user_tasks = requests.get(base_url + 'todos', params={'userId': user_id}
                              ).json()

    with open('{}.csv'.format(user_id), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            user_id = user_id
            username = user_info.get('username')
            task_completed = task.get('completed')
            task_title = task.get('title')

            task_record = [user_id, username, task_completed, task_title]
            writer.writerow(task_record)


if __name__ == '__main__':
    get_api()
