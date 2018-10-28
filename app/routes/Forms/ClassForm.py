from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ClassForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
