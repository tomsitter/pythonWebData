import json
import urllib

#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json'

url = raw_input('Enter URL: ')

data = urllib.urlopen(url).read()
js = json.loads(data)

total = 0
for comment in js['comments']:
    total += comment['count']

print total
