from flask import render_template
from app.routes import app

class teacherForm(FlaskForm):


@app.route("/teachers")
def teachers():

    return render_template("teachers.html")