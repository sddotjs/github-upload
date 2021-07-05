import re
str = '<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>'
print(re.search('href="(.+)"',str))
print(re.search('href=".+"',str))
print(re.search('http://.*',str))
print(re.search('<.*>',str))
