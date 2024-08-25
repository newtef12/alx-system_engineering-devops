#!/usr/bin/python3
"""
Reddit API hot articles
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively query the Reddit API to get titles of hot articles for a given
    subreddit.
    :param subreddit: The subreddit to retrieve hot articles from
    :param hot_list: A list to store the titles of hot articles
    :return: A list containing titles of hot articles, or None
             if no results are found
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "bruka request"}

    subreddit_info = requests.get(url, headers=headers, allow_redirects=False)

    if subreddit_info.status_code == 200:
        data = subreddit_info.json().get('data', {})
        posts = data.get('children', [])
        if posts:
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))

            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        return None
