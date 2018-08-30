#!/usr/bin/python3
'returns a list of top posts'
import requests
import sys

def recurse(subreddit, hot_list=[]):
    'recursively return a list of all hot posts'
    response = requests.get("http://www.reddit.com/r/{}/hot.json".format(subreddit), headers= {"user-agent": 'levi'}).json()

    try:
        for i in response['data']['children']:
            print(i['data']['title'])
    except:
        print('None')

if __name__ == '__main__':
    recurse(sys.argv[1])
