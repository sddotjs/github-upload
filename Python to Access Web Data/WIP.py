import re
str = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
result = re.search('\S+@\S+?',str)
print(result)
