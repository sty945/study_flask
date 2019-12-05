# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/28 11:05

# Author: sty

# File: __init__.py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask('sayhello')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
# toolbar = DebugToolbarExtension(app)
# DEBUG_TB_INTERCEPT_REDIRECTS = False
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands
