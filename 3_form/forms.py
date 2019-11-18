# -*- coding: utf-8 -*-

# !/usr/bin/env python

# Time: 2019/10/28 10:33

# Author: sty

# File: forms.py

from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField, TextAreaField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class LoginForm(FlaskForm):
    """
    basic form example
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class FortyTwoForm(FlaskForm):
    """
    custom validator
    """
    answer = IntegerField('The Number')
    submit = SubmitField()

    def validate_answer(form, field):
        if field.dat != 42:
            raise ValidationError("Must be 42")


class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileField(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField()


class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image', validators=[DataRequired()])
    submit = SubmitField()


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    save = SubmitField('Save')
    publish = SubmitField('Publish')




