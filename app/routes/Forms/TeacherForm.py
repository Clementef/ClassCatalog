from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TeacherForm(FlaskForm):
    name = StringField("Enter your name:")
    submit = SubmitField()