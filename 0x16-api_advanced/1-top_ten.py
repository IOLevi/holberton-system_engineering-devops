#!/usr/bin/python3
'prints top ten hot posts'
import requests
import sys


def top_ten(subreddit):
    'prints top ten hot posts'
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        allow_redirects=False,
        headers={
            "user-agent": 'levi'},
        params={
            'limit': 8}).json()

    try:
        for i in response['data']['children']:
            print(i['data']['title'])
    except BaseException:
        print('None')
