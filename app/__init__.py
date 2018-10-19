
from mongoengine import *
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = 'A^JXuBxf0ow'
connect("", host='')

from .routes import *