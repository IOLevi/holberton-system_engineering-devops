#!/usr/bin/python3
'returns a list of top posts'
import requests
import sys


def re(data, hot_list=[], index=0):
    'actual recursion'
    try:
        data['data']['children'][index]['data']['title']
        re(data, hot_list, index + 1)
    except BaseException:
        return hot_list
    hot_list.append(data['data']['children'][index]['data']['title'])
    return hot_list


def recurse(subreddit, hot_list=[]):
    'recursively return a list of all hot posts'
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        allow_redirects=False,
        headers={
            "user-agent": 'levi'}).json()

    return re(response)
