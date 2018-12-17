from mongoengine import Document, StringField


class Course(Document):

    name = StringField()
    number = StringField()