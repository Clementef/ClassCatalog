from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CourseForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")
