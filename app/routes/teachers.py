from flask import render_template
from app.routes import app


@app.route("/teachers")
def teachers():

    form = TeacherForm(request.form)

    if form.validate() and request.method == "POST":

        teacherObj = Teacher()

        teacherObj.name = form.name.data

        teacherObj.save()

    return render_template("teachers.html",form=form)