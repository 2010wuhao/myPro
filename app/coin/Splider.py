#! /usr/bin/env python3
#-*- coding :utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen("https://www.feixiaohao.com/newcoin/#CNY")
soup = BeautifulSoup(response.read())

f = open('./test.txt', 'w+')
for link in soup.find_all('tr'):
    f.write("|")
    f.write(link.get_text())

f.seek(0)
a = 0
fnew = open('./testnew.txt', 'w')
for line in f.readlines():
    data = line.strip()
    if(len(data) != 0):
        fnew.write(data)
        fnew.write(",")
        # fnew.write("\n")
    #     a = 0
    # elif (a==0):
    #     fnew.write("\n")
    #     a = 1

# fnew.seek(0)

# ffnew = open('./new.txt', 'w')
# for line in fnew.readlines():
#     if(line):


fnew.close
f.close
