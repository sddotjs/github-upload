import urllib.request, urllib.parse, urllib.error

filehandle = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

for line in filehandle :
    print (line.decode().strip())
