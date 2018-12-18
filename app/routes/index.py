import requests
from app.routes import app
from flask import render_template, session, redirect, request
from requests_oauth2.services import GoogleClient
from requests_oauth2 import OAuth2BearerToken
from .Forms import SearchForm
from .misc import searchteachers, searchcourses, searchroom

google_auth = GoogleClient(
    client_id=("961404899755-6sibtis1hhfs6qtnt4u1ak6r5s2j8vm6"
               ".apps.googleusercontent.com"),
    client_secret="gHwNeWmkH-BjmAAIkNvc5eGl",
    redirect_uri="http://localhost:5000/oauth2callback"
    # "http://localhost:5000/oauth2callback"
    # "https://computerinv-216303.appspot.com/oauth2callback"
)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    results = None

    searchterm = ''
    searchby='teacher'

    if form.validate() and request.method == "POST":
        searchterm = form.searchterm.data
        form.searchterm.data = ''
        searchby = form.searchby.data
        form.searchby.data = ''

    if searchby == 'teacher':
        results = searchteachers(searchterm)
    elif searchby == 'course':
        results = searchcourses(searchterm)
    elif searchby == 'room':
        results = searchroom(searchterm)

    return render_template("index.html", form=form, searchterm=searchterm, searchby=searchby, results=results)


@app.route('/login')
def login():
    if not session.get("access_token"):
        return redirect("/oauth2callback")
    with requests.Session() as s:
        s.auth = OAuth2BearerToken(session["access_token"])
        r = s.get("https://www.googleapis.com/plus/v1/people/me?access_token={}".format(session.get("access_token")))
    r.raise_for_status()
    data = r.json()
    session["displayName"] = data["displayName"]
    session["routeName"] = data["displayName"].replace(" ", "_")
    if data["emails"][0]["value"][1] == "_":
        return "Students not allowed"
    elif data["emails"][0]["value"][-8:] != "@ousd.org":
        return "Must be OT Teacher"
    return redirect("/")


@app.route("/oauth2callback")
def google_oauth2callback():
    code = request.args.get("code")
    error = request.args.get("error")
    if error:
        return "error :( {!r}".format(error)
    if not code:
        return redirect(google_auth.authorize_url(
            scope=["profile", "email"],
            response_type="code",
        ))
    data = google_auth.get_token(
        code=code,
        grant_type="authorization_code",
    )
    session["access_token"] = data.get("access_token")
    return redirect("/login")


@app.route("/logout")
def logout():
    session.pop("access_token")
    session.pop("displayName")

    return redirect("/")