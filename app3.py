#!/usr/bin/env python3

import requests
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def mainpage():
  return 'main page'

app.run(host='0.0.0.0', port=5003, threaded=True)
