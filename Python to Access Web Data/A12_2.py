import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = input('Enter Count: ')
position = input('Enter Position: ')

url = 'http://py4e-data.dr-chuck.net/known_by_Brianna.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#count = 7
#position = 18
#lastnames = list()
#url = 'http://py4e-data.dr-chuck.net/comments_761217.html'
while count > 0 :
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    iterator = 0
    for tag in tags :
        iterator = iterator + 1
        link = tag.get("href")
        lastname = tag.getText()
        if iterator == position : break
    count = count - 1
    url = link

print(lastname)
#lastname = url.split("_")
#lastname.reverse()
#print(lastname[0][:len(lastname[0])-5])


#lastnames.append(re.search('known_by_(.+).html'),link)
