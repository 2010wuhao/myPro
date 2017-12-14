#! /usr/bin/env python
#-*- coding :utf-8 -*-

class CityBean(object):

    def __init__(self,city,citycode,location):
        self.city = city
        self.citycode = citycode
        self.location = location

    def getCityWeather(self):
        pass