#!/usr/bin/python3

from flask import Flask, request, session, g, redirect, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import quote, quote_plus
from functools import wraps
from storage import *
#import toml

app = Flask(__name__)
app.secret_key = '1'

config = {}
config['password'] = None

def login_success(message):
    session['login_ok'] = True
    next_url = session.pop('next_url', None)
    return redirect(next_url) if next_url else message

def login_required(endpoint):
    @wraps(endpoint)
    def wrap(*args, **kwargs):
        if 'login_ok' in session:
            return endpoint(*args, **kwargs)
        else:
            session['next_url'] = request.url
            with Storage() as s:
                redir = 'login_GET' if s.pw_is_set() else 'set_password_GET'
                return redirect(url_for(redir))
    return wrap

@app.route('/set_password', methods = ['GET'])
def set_password_GET():
    return render_template('set_password.html')

@app.route('/set_password', methods = ['POST'])
def set_password_POST():
    with Storage() as s:
        if 'login_ok' in session or not s.pw_is_set():
            new_password = request.form['password']
            new_hash = generate_password_hash(new_password)
            s.pw_set(new_hash)
            return login_success('Welcome')
        else:
            return 'Go away', 403

@app.route('/login', methods = ['GET'])
def login_GET():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login_POST():
    with Storage() as s:
        password = request.form['password']
        saved_hash = s.pw_get()
        if check_password_hash(saved_hash, password):
            return login_success('Welcome back')
        else:
            return 'Go away', 401

@app.route('/search')
@login_required
def search_GET():
    with Storage() as s:
        g.query = request.args['q']
        g.query_quoted = quote(g.query)
        g.templates = s.tpl_get_all()
        return render_template('search.html')

