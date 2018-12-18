from flask import render_template
from .Classes import Teacher, Course, Room, Section
from app.routes import app


@app.route("/teacher/<name>")
def teacherpage(name):
    # sections = []
    # for section in Section.objects:
    #     if section.teacher.name.replace(" ", "") == name:
    #         sections.append(section)

    for i in Teacher.objects:

        if name == i.name.replace(" ", ""):
            return render_template("teacherpage.html", teacher=i, sections=Section.objects(teacher=i).order_by("period"))

    return "Teacher not found"


@app.route("/course/<name>")
def coursepage(name):
    for i in Course.objects:

        if name == i.name.replace(" ", "").replace("/", ""):
            return render_template("coursepage.html", course=i, sections=Section.objects(course=i).order_by("period"))

    return "Course not found"


@app.route("/room/<name>")
def roompage(name):

    for i in Room.objects:

        if name in i.location:

            return render_template("roompage.html", room=i, sections=Section.objects(room=i).order_by("period"))

    return "Room not found"
