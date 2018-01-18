#! /usr/bin/env python
#-*- coding :utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

request = urllib2.Request("https://www.feixiaohao.com/newcoin/#CNY")
response = urllib2.urlopen(request)
soup = BeautifulSoup(response.read())

f = open('./test.txt', 'w+')
for link in soup.find_all('tr'):
    f.write("------------------")
    f.write(link.get_text().encode('utf-8'))

f.seek(0)
a = 0
fnew = open('./testnew.txt', 'w')
for line in f.readlines():
    data = line.strip()
    if(len(data)!=0):
        fnew.write(data)
        # fnew.write("|")
        fnew.write("\n")
    #     a = 0
    # elif (a==0):
    #     fnew.write("\n")
    #     a = 1


        

fnew.close
f.close

# for i in soup.select('table > tbody'):
#     tr = i.select("tr");
#     print tr[0].text
#     for j in tr:
#         print j.select("td")[1].text

#title = soup.select('table > tbody > tr:nth-child(1)')[0].get_text()
#print title;




# url = "https://www.feixiaohao.com/newcoin/"
# web_data = urllib2.urlopen(url)
# soup = BeautifulSoup(web_data.text,'lxml')
# title = soup.select('table > tbody > tr:nth-child(1) > td:nth-child(1) > a')[0].get_text()
# print soup.prettify();