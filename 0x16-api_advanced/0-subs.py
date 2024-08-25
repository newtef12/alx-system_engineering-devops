#!/usr/bin/python3
"""This module queries the Reddit API and returns the
   number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Function that GETS subscriber count of a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "bruka request"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
