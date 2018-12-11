
from mongoengine import *
from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)
connect("classcatalog", host='mongodb://admin:1superadmin@ds039950.mlab.com:39950/classcatalog')


from .routes import *
