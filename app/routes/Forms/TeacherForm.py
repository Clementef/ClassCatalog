from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TeacherForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")