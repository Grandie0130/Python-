# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 04:30:03 2024

@author: User
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '歡迎來到首頁！'

@app.route('/hello/<string:name>')
def hello(name):
    return '{}, 歡迎來到Flask！'.format(name)

if __name__ == '__main__':
    app.run()