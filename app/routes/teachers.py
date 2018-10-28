from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from app.routes import app

class teacherForm(FlaskForm):
    name = StringField("Enter your name:")
    submit = SubmitField()

@app.route("/teachers")
def teachers():

    return render_template("teachers.html")