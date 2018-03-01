#! /usr/bin/env python
#-*- coding :utf-8 -*-

import os

from DataModel import model
from coin.Splider import splider
from flask import Flask, request


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()


@app.route('/weather/api/v1.0/get_weather', methods=['GET'])
def getWeather():
    city = request.values.get('city')
    citycode = request.values.get('citycode')
    location = request.values.get('location')
    # print type(city)
    # print type(citycode)
    # print type(location)
    return model.getWeatherJson(city, citycode, location)


@app.route('/weather/api/v1.0/get_citylist', methods=['GET'])
def getCityList():
    return model.getCityList()


@app.route('/coin/api/v1.0/coin_new', methods=['GET'])
def getCoin():
    print("getCoin is called!")
    return splider.getCoin()


@app.route('/coin/api/v1.0/coin_news', methods=['GET'])
def getNews():
    print("getNews is called!")
    return splider.getNews()


if __name__ == '__main__':
    app.run(debug=True)
