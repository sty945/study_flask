# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/28 11:05

# Author: sty

# File: __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
