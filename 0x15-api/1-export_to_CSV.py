#!/usr/bin/python3
"""
Python script that exports data retrieved from a REST API to CSV format.
"""

import csv
import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Function to get employee TODO list progress
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        return None

    employee_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    employee_info_response = requests.get(employee_info_url)
    employee_info = employee_info_response.json()
    username = employee_info.get('username', 'Unknown')

    return username, [[todo['userId'], username, todo['completed'], todo['title']] for todo in todos]


def export_to_csv(employee_id, data):
    """
    Function to export data to CSV format
    """
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(data)


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

    username, todos = employee_data
    export_to_csv(employee_id, todos)
    print("Data exported to {}.csv".format(employee_id))


if __name__ == "__main__":
    main()

