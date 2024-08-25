#!/usr/bin/python3
""" This module queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Function that GETs subreddit top 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'bruka request'}
    req = requests.get(url, headers=headers)
    if (req.status_code == 404):
        print("None")
    elif 'data' not in req.json():
        print("None")
    else:
        req = req.json()
        for post in req['data']['children']:
            print(post['data']['title'])
