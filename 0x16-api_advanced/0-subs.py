#!/usr/bin/python3
"""Return number of subreddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subreddit subscribers"""
    URL = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    HEADERS = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
