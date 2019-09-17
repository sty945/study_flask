# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/9/17 13:58

# Author: sty

# File: app.py



from flask import Flask, redirect, abort, make_response, json, jsonify, url_for, request, session
from urllib.parse import urlparse, urljoin
from jinja2.utils import generate_lorem_ipsum

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World</h1>'

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = '<h1>Hello, %s</h1>' % name
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'
        return response

@app.route('/hi')
def hi():
    name = request.args.get('name')
    response = '<h1>Hello, %s!</h1>' % name

@app.route("/sty")
def hi_sty():
    return redirect('http://www.baidu.com')

@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' % (2018 - year)

@app.route('/colors/<any(blue, white, red):color>')
def three_colors(color):
    return '<p> i love you like love mine'


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == "coffee":
        abort(418)
    else:
        return 'a drop of tea'

@app.route('/note', defaults={'content_type':'text'})
@app.route('/note/<content_type>')
def note(content_type):
    content_type = content_type.lower()
    if content_type == 'text':
        body = '''Note
        to: Peter
        from: Jane
        heading: Reminder
        body: Don't forget the party!
        '''
        response = make_response(body)
        response.mimetype = 'text/plain'
    elif content_type == 'html':
        body = '''<!DOCTYPE html>
<html>
<head></head>
<body>
  <h1>Note</h1>
  <p>to: Peter</p>
  <p>from: Jane</p>
  <p>heading: Reminder</p>
  <p>body: <strong>Don't forget the party!</strong></p>
</body>
</html>
        '''
        response = make_response(body)
        response.mimetype = 'text/html'
    elif content_type == 'xml':
        body = '''<?xml version="1.0" encoding="UTF-8"?>
        <note>
          <to>Peter</to>
          <from>Jane</from>
          <heading>Reminder</heading>
          <body>Don't forget the party!</body>
        </note>
        '''
        response = make_response(body)
        response.mimetype = 'application/xml'
    elif content_type == 'json':
        body = { "note":{
            "to": "Peter",
            "from": "Jane",
            "heading": "Reminder",
            "body": "Don't forget the party!"
        }
        }
        response = jsonify(body)
    else:
        abort(400)
    return response

@app.route('/foo')
def foo():
    data = {
        'name': 'Grey Li',
        'gender': 'male'
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))

@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page'

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


# redirect to last page
@app.route('/foo1')
def foo1():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)


@app.route('/bar1')
def bar1():
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' \
           % url_for('do_something', next=request.full_path)

@app.route('/do-something')
def do_something():
    # return redirect(url_for('hello'))
    return redirect_back()

@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
<h1>A very long post</h1>
<div class="body">%s</div>
<button id="load">Load More</button>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script type="text/javascript">
$(function() {
    $('#load').click(function(){
        $.ajax({
            url: '/more',
            type: 'get',
            success: function(data){
                $('.body').append(data);
            }
        })
    })
})
</script>
    ''' % post_body

@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)

def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
