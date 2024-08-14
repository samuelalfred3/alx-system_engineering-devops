#!/usr/bin/python3
"""
2-recurse module
This module contains the function `recurse` which recursively queries the Reddit API to return
a list of titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to return a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of titles collected so far. Defaults to an empty list.

    Returns:
        list: A list containing the titles of all hot articles, or None if the subreddit is invalid.
    """
    # Define the URL for the Reddit API query
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'python:subreddit.hot.articles:v1.0 (by /u/yourusername)'}

    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the JSON response
        data = response.json()
        posts = data['data']['children']

        # Append titles to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more pages of results
        after = data['data']['after']
        if after:
            # Recursive call to get the next page of results
            recurse(subreddit, hot_list)
        return hot_list
    else:
        # Return None if the subreddit is invalid or if an error occurred
        return None

