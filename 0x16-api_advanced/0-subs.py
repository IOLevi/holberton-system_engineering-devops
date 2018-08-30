#!/usr/bin/python3
'number of subs in a module'

import requests
import sys

def number_of_subscribers(subreddit):
    'calculates the number of subscribers'
    response = requests.get("http://www.reddit.com/r/{}/about.json".format(subreddit), headers= {"user-agent": 'levi'}).json()

    try:
        return (response['data']['subscribers'])
    except:
        return 0

