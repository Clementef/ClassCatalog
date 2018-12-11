
from mongoengine import *
from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)
connect("classcatalog", host='mongodb://admin:1superadmin@ds048319.mlab.com:48319/classcatalog')


from .routes import *
