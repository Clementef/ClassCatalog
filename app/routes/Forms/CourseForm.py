from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CourseForm(FlaskForm):
    name = StringField("Name")
    subject = StringField("Subject")
    submit = SubmitField("Submit")
