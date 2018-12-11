from flask import render_template, request, redirect
from app.routes import app
from .Forms import Login


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    form = Login(request.form)

    if request.method == "POST" and form.validate():

        return redirect("/login")

    return render_template("login.html", form=form)
