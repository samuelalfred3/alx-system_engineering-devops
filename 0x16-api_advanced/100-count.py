#!/usr/bin/python3
"""
100-count module
This module contains the function `count_words` which recursively queries the Reddit API to count
the occurrences of given keywords in the titles of hot articles for a given subreddit.
"""

import requests
import re
import time

def count_words(subreddit, word_list, hot_list=[]):
    """
    Recursively queries the Reddit API to count occurrences of given keywords in the titles
    of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        hot_list (list): Accumulator list of post titles. Defaults to an empty list.

    Returns:
        None: Prints results to standard output.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.hot.words.counter:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        if response.status_code == 429:
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                print(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
                time.sleep(int(retry_after))
                return count_words(subreddit, word_list, hot_list)
        else:
            print(f"Request failed: {e}")
        return

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            hot_list.append(post['data']['title'].lower())
        
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, hot_list)
        else:
            count_keyword_occurrences(word_list, hot_list)
    else:
        print("Invalid subreddit or error fetching data.")
        return

def count_keyword_occurrences(word_list, hot_list):
    """
    Count occurrences of keywords in the list of hot article titles.

    Args:
        word_list (list): List of keywords to count.
        hot_list (list): List of article titles.

    Returns:
        None: Prints results to standard output.
    """
    keyword_counts = {word.lower(): 0 for word in word_list}
    word_pattern = re.compile(r'\b\w+\b', re.IGNORECASE)

    for title in hot_list:
        words = word_pattern.findall(title)
        for word in words:
            if word.lower() in keyword_counts:
                keyword_counts[word.lower()] += 1

    keyword_counts = {k: v for k, v in keyword_counts.items() if v > 0}
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))

    if sorted_keywords:
        for keyword, count in sorted_keywords:
            print(f"{keyword}: {count}")
    else:
        print("No matching keywords found.")

