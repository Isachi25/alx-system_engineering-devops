#!/usr/bin/python3
"""Get titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all
    hot articles for a given subreddit"""
    URL = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    HEADERS = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(URL, headers=HEADERS, params=params)
    posts = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not posts:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
