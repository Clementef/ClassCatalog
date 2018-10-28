from .Course import Course
from .Teacher import Teacher
from mongoengine import Document, ReferenceField


class Slot(Document):

    teacher = ReferenceField(Teacher)
    course = ReferenceField(Course)