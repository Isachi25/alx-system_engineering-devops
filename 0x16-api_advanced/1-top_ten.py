#!/usr/bin/python3
"""Prints top 10 posts"""
import requests


def top_ten(subreddit):
    """Prints top 10 posts"""
    URL = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    HEADERS = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(URL, headers=HEADERS)
    posts = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not posts:
        return print('None')
    for post in posts[0:10]:
        print(post.get('data', {}).get('title'))
