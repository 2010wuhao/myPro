#! /usr/bin/env python3
#-*- coding :utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


class Splider:

    def __init__(self):
        print("Splider __init__")

    def initData(self):
        response = urllib.request.urlopen(
            "https://www.feixiaohao.com/newcoin/#CNY")
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

        fnew.close
        f.close

    def getCoin(self):
        fnew = open('./testnew.txt', 'w')
        data = ''
        for line in fnew.readlines():
            data += line
        return data


splider = Splider()
splider.initData()
