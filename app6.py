#!/usr/bin/env python3

import requests
from flask import Flask, request, abort, render_template_string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

loginpage = '''
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div class="container">
<h2>Login</h2>
<p>Please note, only current employees of Corpo Pty Ltd are allowed to use this page. No hackers allowed!</p>

<form action="/submit" name="postForm" method="post">
<div class="card" style="width: 18rem;">
<div class="input-group form-group">
	<div class="input-group-prepend">
		<span class="input-group-text"><i class="fas fa-user"></i></span>
	</div>
	<input name="username" type="text" class="form-control" placeholder="email">
	
</div>
<div class="input-group form-group">
	<div class="input-group-prepend">
		<span class="input-group-text"><i class="fas fa-key"></i></span>
	</div>
	<input name="password" type="password" class="form-control" placeholder="password">
</div>
<div class="form-group">
	<input type="submit" value="Login" class="btn float-right login_btn">
</div>
</form>
</div>
</div>
'''

peoplepage = '''
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div class="container">
<h2>People</h2>
<p>These are our wonderful employees. They do a great job earning lots of money for the shareholders.</p>
<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Fleur Palatine</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: fleur.palatine@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Charlotte Hopkirk</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: charlotte.hopkirk@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Zeddicus Dresden</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: zeddicus.dresden@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Khelben Doom</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: khelben.doom@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Isabel Westfall</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: isabel.westfall@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Elizabeth Swanson</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: elizabeth.swanson@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Thoth Flagg</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: thoth.flagg@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">John Smith</h5>
        <p class="card-text">A wonderful person who has been working with us for X years!</p>
        <p class="card-text">Contact: john.smith@corpoptyltd.com</p>
        <a href="#" class="btn btn-primary">Link</a>
      </div>
    </div>
  </div>
  <br>
</div>
</div>
'''

mainpage = '''
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<div class="container">
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Corpo Pty Ltd</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/people">People <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">History <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Contact <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Legal <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/login">Login <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
<h2>Welcome!</h2>
<p>We are Corpo Pty Ltd!</p>
<p>Check out the wonderful people working at our corporation: <a href="/people">People</a>
<p>Employees, please login here: <a href="/login">Login</a>
</div>
'''


@app.route('/')
def indexpage():
  return mainpage
  
@app.route('/login')
def newpostpage():
  return loginpage
  
@app.route('/people') 
def thepeoplepage():
  return peoplepage

@app.route('/submit', methods=['POST'])
@limiter.limit("100/minute") 
def submitpage():
    try:
        username = request.form['username']
        password = request.form['password']
        if username.lower() == 'charlotte.hopkirk@corpoptyltd.com' and password == 'November2021':
            return 'sectalks{spray-n-pray}'
        elif username.lower() == 'zeddicus.dresden@corpoptyltd.com' and password == 'Password2021':
            return 'sectalks{spray-n-pray}'
        elif username.lower() == 'elizabeth.swanson@corpoptyltd.com' and password == 'October2021':
            return 'sectalks{spray-n-pray}'
        elif username.lower() == 'thoth.flagg@corpoptyltd.com' and password == 'Password123':
            return 'sectalks{spray-n-pray}'
        else:
            return 'Login failed!'
    except:
        return 'Error!'

app.run(host='0.0.0.0', port=5006, threaded=True)








