#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed in a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}
    response = requests.get(url, headers=headers)  # allow_redirects=True by default

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)
