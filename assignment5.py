import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)

counts = tree.findall('.//count')
total = sum(int(count.text) for count in counts)

print total
