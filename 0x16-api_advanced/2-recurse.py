#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[]):
    """
    Returns a list containing the titles of all hot articles for a given subreddit
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent header
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}  # Limiting to 100 posts per request
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    if not posts:
        return None

    # Extract titles and append to hot_list
    for post in posts:
        hot_list.append(post['data']['title'])

    # Check if there are more pages of results
    after = data['data'].get('after')
    if after:
        # Recursively call the function with the next page's URL
        params['after'] = after
        recurse(subreddit, hot_list)

    return hot_list

# For testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

