from flask import render_template, request
from app.routes import app
from .Forms import ClassForm
from .Classes import Class


@app.route("/classes", methods=["POST", "GET"])
def classes():

    form = ClassForm(request.form)

    if form.validate() and request.method == "POST":

        classObj = Class()

        classObj.name = form.name.data

        classObj.save()

    return render_template("classes.html", form=form)
