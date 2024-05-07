#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent header
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']
    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data']['title'])

# For testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

