from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Login(FlaskForm):

    password = StringField("Enter Password")
    submit = SubmitField("Submit")
