#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    # Check if user ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    # Fetch user data
    user_id = sys.argv[1]
    user_response = requests.get
    ('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch user's tasks
    tasks_response = requests.get
    ('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    tasks_data = tasks_response.json()

    # Write tasks data to CSV file
    with open('{}.csv'.format(user_id), 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow
        (["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks_data:
            csv_writer.writerow
            ([user_id, username, str(task['completed']), task['title']])

    print("Data exported to {}.csv".format(user_id))
