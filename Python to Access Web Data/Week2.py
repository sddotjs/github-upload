import re

filehandle = open(r"C:\Users\sachi\Documents\Python for Everybody\Python to Access Web Data\regex_sum_761215.txt","r")
data = filehandle.read()
all_nums = re.findall('([0-9]+)',data)
all_nums_int = list(map(int,all_nums))
print(sum(all_nums_int))


#Convereted to 2 line program
#print(sum(list(map(int,re.findall('([0-9]+)',open(r"C:\Users\sachi\Documents\Python for Everybody\Python to Access Web Data\regex_sum_761215.txt","r").read()))))
#import socket
#mysoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
