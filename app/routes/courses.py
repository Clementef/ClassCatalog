from flask import render_template
from app.routes import app
from .Classes import Course


@app.route("/courses", methods=["POST", "GET"])
def courses():
    return render_template("courses.html", results=Course.objects.order_by("name"))
