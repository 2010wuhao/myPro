#!/usr/bin/env python
# coding=utf-8

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Flask!</h1>"

    if __name__ == "__main__":
        application.run('0.0.0.0')
