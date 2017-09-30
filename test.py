#! /usr/bin/env python
#-*- coding :utf-8 -*-
import os

from flask import Flask

def creat_app():
    app = Flask(__name__)
    return app

testFlaskApp = creat_app()

#user lib
from testFile import JsonUtil

#du qu json wenjian
JsonUtil = JsonUtil()

@testFlaskApp.route('/')
def hello_world():
    return JsonUtil.getBjtq()

if __name__ == '__main__':
    testFlaskApp.DEBUG=True
    testFlaskApp.run()