import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#urllocation = 'http://py4e-data.dr-chuck.net/comments_761219.xml'

while True:
    urllocation = input('Enter location: ')
    if len(address) < 1: break
print('Retrieving', urllocation)
uh = urllib.request.urlopen(urllocation)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('.//count')
sum = 0
for item in results:
    sum = sum + int(item.text)
print(sum)
