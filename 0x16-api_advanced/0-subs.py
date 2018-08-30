#!/usr/bin/python3
'number of subs in a module'

import requests
import sys


def number_of_subscribers(subreddit):
    'calculates the number of subscribers'
    response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(subreddit), allow_redirects=False,
                            headers={"user-agent": 'levi'}).json()

    try:
        return (response['data']['subscribers'])
    except BaseException:
        return 0
