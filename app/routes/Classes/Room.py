from mongoengine import Document, StringField, ReferenceField
from .Teacher import Teacher
from .Course import Course


class Room(Document):

    location = StringField()

    teacher = ReferenceField(Teacher)
    course = ReferenceField(Course)
