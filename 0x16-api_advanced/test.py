
#!/usr/bin/python3
'number of subs in a module'

import requests
import sys


response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(sys.argv[1]), allow_redirects=False,
                            headers={"user-agent": 'levi'},).json()

print(type(response))
response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(sys.argv[1]), allow_redirects=False,
                            headers={"user-agent": 'levi'}, params={"after":None}).json()
print(type(response))
print(response)
