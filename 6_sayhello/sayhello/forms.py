# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/11/28 15:42

# Author: sty

# File: forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    """
    问候表单
    """
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()

