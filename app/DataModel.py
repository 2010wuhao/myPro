#! /usr/bin/env python
#-*- coding :utf-8 -*-

import os
import sys
import urllib
import urllib2


class DataModel:

    __host = 'http://jisutqybmf.market.alicloudapi.com'
    __path_city = '/weather/city'
    __path_weather = '/weather/query'
    __method = 'GET'
    __appcode = '79cb709ca36241cb9acd3327ac7652a5'
    __url_city = __host + __path_city
    __url_weather = __host + __path_weather

    def __init__(self):
        print 'Data model __init__'

    def getCityList(self):
        return self.__getData(self.__url_city)

    def getWeatherJson(self, city, citycode, location):
        querys = ''
        if(isinstance(city,unicode)):
            city_str = city.encode("utf-8")
            querys += 'city=' + city_str

        if(isinstance(citycode,unicode)):
            citycode_str = citycode.encode("utf-8")
            querys += '&citycode=' + citycode_str

        if(isinstance(location,unicode)):
            location_str = location.encode("utf-8")
            querys += '&location=' + location_str

        url = self.__url_weather + '?' + querys
        print('url = ', url)
        return self.__getData(url)

    def __getData(self, url):
        request = urllib2.Request(url)
        request.add_header('Authorization', 'APPCODE ' + self.__appcode)
        response = urllib2.urlopen(request)
        content = response.read()
        return content

model = DataModel();
