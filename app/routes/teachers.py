from flask import render_template, request
from app.routes import app
from .Forms import TeacherForm
from .Classes import Teacher


@app.route("/teachers", methods=["POST", "GET"])
def teachers():
    return render_template("teachers.html", results=Teacher.objects)

# name id email