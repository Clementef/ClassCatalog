from flask import render_template
from .Classes import Teacher, Course, Room
from app.routes import app


@app.route("/teacher/<name>")
def teacherpage(name):

    for i in Teacher.objects:

        if name == i.name.replace(" ", ""):

            return render_template("teacherpage.html", teacher=i)

    return


@app.route("/course/<name>")
def coursepage(name):

    for i in Course.objects:

        if name == i.name.replace(" ", "").replace("/", ""):

            return render_template("coursepage.html", course=i)

    return "Course Not Found"
