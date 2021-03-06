#! /usr/bin/env python3
#-*- coding :utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


class Splider:

    def __init__(self):
        print("Splider __init__")

    def initData(self):
        #  # 获取某个币的文本介绍 begin
        # response = urllib.request.urlopen(
        #     "https://www.feixiaohao.com/coindetails/bitcoin/")
        # soup = BeautifulSoup(response.read())
        # div = soup.find_all('div', class_='artBox')

        # for p in div:
        #     print(p.get_text())
        # # 获取某个币的文本介绍 end

        # 获取某个币的文本介绍 begin
        response = urllib.request.urlopen(
            "https://www.feixiaohao.com/currencies/bitcoin/")
        soup = BeautifulSoup(response.read())
        div = soup.find_all('div', class_='cell maket')

        for p in div:
            print(p.get_text())
        # 获取某个币的文本介绍 end

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
                fnew.write("#")

        fnew.close
        f.close

    def getCoin(self):
        fnew = open('./testnew.txt', 'r')
        data = ''
        for line in fnew.readlines():
            data += line
        return data

    def getNews(self):
        response = urllib.request.urlopen(
            "http://www.biknow.com/")
        soup = BeautifulSoup(response.read())
        f = open('./news.txt', 'w+')
        for link in soup.find_all(id='jiazai'):
            for li in link.find_all('li'):
                f.write("|")
                f.write(li.get_text())

        f.seek(0)
        a = 0
        fnew = open('./newsnew.txt', 'w')
        newsData = ''
        for line in f.readlines():
            data = line.strip()
            if(len(data) != 0):
                fnew.write(data)
                newsData += data
                fnew.write('#')

        fnew.close
        f.close
        return newsData


splider = Splider()
splider.initData()
# splider.getCoin()
# splider.getNews()
