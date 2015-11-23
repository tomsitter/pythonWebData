import urllib
import json

api_link = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

address = raw_input('Enter location: ')

url = api_link + urllib.urlencode({'sensor': 'false', 'address': address})

data = urllib.urlopen(url).read()
js = json.loads(data)

print js['results'][0]['place_id']
