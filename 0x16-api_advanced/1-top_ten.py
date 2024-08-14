#!/usr/bin/python3
"""
1-top_ten module
This module contains the function `top_ten` which prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Define the URL for the Reddit API query
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}

    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and contains the necessary data
    if response.status_code == 200:
        # Extract the data from the JSON response
        data = response.json()
        posts = data['data']['children']
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post['data']['title'])
    else:
        # Print None if the subreddit is invalid or if an error occurred
        print(None)

