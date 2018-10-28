
from mongoengine import *
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = 'A^JXuBxf0ow'
connect("classcatalog", host='mongodb://admin:1superadmin@ds039950.mlab.com:39950/classcatalog')


from .routes import *