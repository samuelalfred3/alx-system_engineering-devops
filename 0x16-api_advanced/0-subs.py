#!/usr/bin/python3
"""
0-subs module
This module contains the function `number_of_subscribers` which returns the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Define the URL for the Reddit API query
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/yourusername)'}

    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and contains the necessary data
    if response.status_code == 200:
        # Extract the data from the JSON response
        data = response.json()
        return data['data']['subscribers']
    else:
        # Return 0 if the subreddit is invalid or if an error occurred
        return 0

