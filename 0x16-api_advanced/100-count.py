#!/usr/bin/python3
"""
Counts occurrences of specific keywords in the titles of hot articles from a subreddit
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Counts occurrences of specific keywords in the titles of hot articles from a subreddit
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent header
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    if not posts:
        return None

    # Traverse through the titles and count occurrences of keywords
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if title.count(word.lower()):
                counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

    # Check if there are more pages of results
    after = data['data'].get('after')
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        # Print sorted count in descending order of frequency
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")

# For testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2:])

