# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/20 15:22

# Author: sty

# File: app.py


import os
import sys

import click
from flask import Flask
from flask import redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))

db = SQLAlchemy(app)
