from flask import render_template
from app.routes import app


@app.route("/classes")
def classes():

    return render_template("classes.html")