#! /usr/bin/env python
#-*- coding :utf-8 -*-

import os

from DataModel import model
from flask import Flask, request


def creat_app():
    app = Flask(__name__)
    return app

app = creat_app()

@app.route('/weather/api/v1.0/get_weather',methods=['GET'])
def getWeather():
    city = request.values.get('city')
    citycode = request.values.get('citycode')
    location = request.values.get('location')
    print type(city)
    print type(citycode)
    print type(location)
    return model.getWeatherJson(city,citycode,location)

@app.route('/weather/api/v1.0/get_citylist',methods=['GET'])
def getCityList():
    return model.getCityList()

if __name__ == '__main__':
    app.run(debug=True)
