#! /usr/bin/env python
#-*- coding :utf-8 -*-

import os;

class JsonUtil(object):
    """docstring for getJsonFromFile"""
    def __init__(self):
        print "__init__ is call "

    def __getJson(self,fileName):
        print 'getJson fileName = ', fileName
        fileJson = open(fileName,'r+')
        fileContent = fileJson.read()
        fileJson.close
        return fileContent

    def getBjtq(self):
        return self.__getJson(BJ_TQ)

    def getBjzl(self):
        return self.__getJson(BJ_TQ_ZL)


    #du qu json wenjian
BJ_TQ_ZL = './json/bjkqzl.json'
BJ_TQ = './json/bjtq.json'
#a = JsonUtil()
#print a.getBjtq();
