#!/usr/bin/python3
'returns a list of top posts'
import requests
import sys

def recurse(subreddit, hot_list=[]):
    'recursively return a list of all hot posts'
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        allow_redirects=False,
        headers={
            "user-agent": 'levi'}, params={'limit':100}).json()
        
    def re(data, hot_list=[], index=0):
        'actual recursion'
        try:
            data['data']['children'][index]['data']['title']
            re(data, after, hot_list, index + 1)
        except BaseException:
            after = data['data']['after']
            if after:
                new = requests.get("https://www.reddit.com/r/{}/hot.json".format(subreddit), params={'limit':100, 'after':after}, allow_redirects=False, headers={"user-agent":'levi'}).json()
                re(new, hot_list)
            return hot_list

        hot_list.append(data['data']['children'][index]['data']['title'])
        return hot_list

    mylist = re(response)
    return mylist if mylist else None
