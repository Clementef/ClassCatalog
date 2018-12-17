from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField


class SearchForm(FlaskForm):
    searchterm = StringField("Search For")
    searchby = SelectField('Search By', choices=[('teacher','Teacher'), ('course','Course'), ('room','Room')])
    submit = SubmitField("Submit")