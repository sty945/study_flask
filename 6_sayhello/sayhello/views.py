# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/28 11:20

# Author: sty

# File: views.py


from flask import flash, redirect, url_for, render_template

from sayhello import app
from sayhello import db

from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    # for message in messages:
    #     print(message.body, message.name)
    return render_template('index.html', form=form, messages=messages)


