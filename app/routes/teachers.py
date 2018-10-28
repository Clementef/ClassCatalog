from flask import render_template
from app.routes import app


@app.route("/teachers")
def teachers():

    return render_template("teachers.html")