from app.routes import app
from flask import render_template
from .Classes import Room


@app.route("/rooms")
def rooms():

    return render_template("rooms.html", rooms=Room.objects)
