import ssl
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter URL - ')
url = 'http://www.dr-chuck.com/page1.htm'
#url = 'https://www.nytimes.com'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#retrieve all anchor tags

#coronaArticles = list()
tags = soup('a')
for tag in tags :
    print(tag.get('href',None))
    #if tag.find('corona') :
    #    coronaArticles.append(tag)

#print(*coronaArticles)
