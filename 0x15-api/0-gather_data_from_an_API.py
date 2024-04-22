#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Function to get employee TODO list progress
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        return None

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    employee_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    employee_info_response = requests.get(employee_info_url)
    employee_info = employee_info_response.json()
    employee_name = employee_info.get('name', 'Unknown')

    return employee_name, completed_tasks, total_tasks, [todo['title'] for todo in todos if todo['completed']]


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data = get_employee_todo_progress(employee_id)

    if employee_data is None:
        print("Employee with ID {} not found.".format(employee_id))
        sys.exit(1)

    employee_name, completed_tasks, total_tasks, completed_titles = employee_data

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for title in completed_titles:
        print("\t", title)


if __name__ == "__main__":
    main()

