#!/usr/bin/python3
'prints top ten hot posts'
import requests
import sys

def top_ten(subreddit):
    'prints top ten hot posts'
    response = requests.get("http://www.reddit.com/r/{}/hot.json".format(subreddit), headers= {"user-agent": 'levi'}, params={'limit': 8}).json()

    try:
        for i in response['data']['children']:
            print(i['data']['title'])
    except:
        print('None')

if __name__ == '__main__':
    top_ten(sys.argv[1])
