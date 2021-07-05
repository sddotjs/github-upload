import json
import urllib.request, urllib.parse, urllib.error

#urllocation = 'http://py4e-data.dr-chuck.net/comments_761220.json'

while True:
    urllocation = input('Enter location: ')
    if len(address) < 1: break
print('Retrieving', urllocation)
uh = urllib.request.urlopen(urllocation)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

sum = 0
comments = info['comments']
#print(comments)
for item in comments:
    sum = sum + int(item['count'])
print(sum)
