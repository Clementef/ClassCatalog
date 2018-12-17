from .Course import Course
from .Teacher import Teacher
from .Room import Room
from mongoengine import Document, ReferenceField, StringField


class Section(Document):

    year = StringField()
    period = StringField()
    course = ReferenceField(Course)
    teacher = ReferenceField(Teacher)
    room = ReferenceField(Room)