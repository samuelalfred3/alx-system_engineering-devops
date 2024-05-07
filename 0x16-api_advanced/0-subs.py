#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent header
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code != 200:
        return 0

    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers

# For testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

