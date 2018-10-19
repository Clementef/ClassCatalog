from mongoengine import Document, StringField

class Teacher(Document):
    name = StringField(required=True)