# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/28 11:38

# Author: sty

# File: models.py


from datetime import datetime

from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    # timestamp用于存储留言发表时间戳，采用默认的当前时间
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)