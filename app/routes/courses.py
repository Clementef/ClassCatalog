from flask import render_template, request
from app.routes import app
from .Forms import CourseForm
from .Classes import Course


@app.route("/courses", methods=["POST", "GET"])
def courses():
    return render_template("courses.html", results=Course.objects)