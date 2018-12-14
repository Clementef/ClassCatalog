from flask import render_template, request
from app.routes import app
from .Forms import CourseForm
from .Classes import Course


@app.route("/classes", methods=["POST", "GET"])
def classes():

    form = CourseForm(request.form)

    if form.validate() and request.method == "POST":

        courseObj = Course()

        courseObj.name = form.name.data

        courseObj.save()

    return render_template("courses.html", form=form)