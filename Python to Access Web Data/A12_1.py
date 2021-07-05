import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL - ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_761217.html'

#url = 'http://py4e-data.dr-chuck.net/comments_761217.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
sum = 0
for tag in tags :
    sum = sum + int(tag.getText())
print (sum)
