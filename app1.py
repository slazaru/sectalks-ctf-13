#!/usr/bin/env python3

nginx = '''
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
'''

robotspage = '''
Disallow: /admin
'''

forbiddenpage = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>403 Forbidden</title>
<h1>Forbidden</h1>
<p>This page can only be accessed locally due to security concerns.</p>
'''

import requests
from flask import Flask, request, abort, make_response

app = Flask(__name__)

@app.route('/')
def mainpage():
  resp = make_response(nginx)
  resp.headers['Server'] = 'nginx'
  return resp
  
@app.route('/robots.txt')
def retrobotspage():
  resp = make_response(robotspage)
  resp.headers['Server'] = 'nginx'
  return resp

@app.route('/admin')
def adminpage():
  if request.headers.get('X-Forwarded-For') != None and request.headers.get('X-Forwarded-For') == '127.0.0.1':
    resp = make_response('sectalks{f0rwarded-4-me-and-me-only}')
    resp.headers['Server'] = 'nginx'
    return resp
  else:
    resp = make_response(forbiddenpage, 403)
    resp.headers['Server'] = 'nginx'
    return resp

app.run(host='0.0.0.0', port=5001, threaded=True)



