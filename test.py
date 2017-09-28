#! /usr/bin/env python
#-*- coding :utf-8 -*-
import os

from flask import Flask
app = Flask(__name__)

#user lib
from testFile import JsonUtil

#du qu json wenjian
JsonUtil = JsonUtil()

@app.route('/')
def hello_world():
    return JsonUtil.getBjtq()

if __name__ == '__main__':
    app.DEBUG=True
    app.run()