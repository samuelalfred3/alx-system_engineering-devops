#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""
import json
import requests
from sys import argv


def export_all_tasks():
    """Export all tasks for all employees in JSON format."""
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Get users and convert to dictionary
    users = requests.get(url_users).json()
    users_dict = {user['id']: user['username'] for user in users}

    all_tasks = {}
    for user_id, username in users_dict.items():
        # Get tasks for each user
        tasks = requests.get(url_todos, params={'userId': user_id}).json()
        # Create a list of tasks for each user
        user_tasks = [{"username": username, "task": task['title'],
                       "completed": task['completed']} for task in tasks]
        # Store user tasks in the dictionary
        all_tasks[str(user_id)] = user_tasks

    # Export all tasks to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks()

