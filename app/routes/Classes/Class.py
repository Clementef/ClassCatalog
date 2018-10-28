from mongoengine import Document, ListField, EmbeddedDocument, EmbeddedDocumentField, ReferenceField, StringField, IntField
from .Teacher import Teacher


class Period(EmbeddedDocument):
    number = IntField()
    teachers = ReferenceField(Teacher)


class Class(Document):
    name = StringField()
    periods = ListField(EmbeddedDocumentField(Period))