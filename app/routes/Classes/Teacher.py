from mongoengine import Document, StringField


class Teacher(Document):

    name = StringField()
    number = StringField()
    email = StringField()