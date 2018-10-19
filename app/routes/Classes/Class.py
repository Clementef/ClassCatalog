from mongoengine import Document, ListField, EmbeddedDocument, EmbeddedDocumentField, ReferenceField
from .Teacher import Teacher


class Period(EmbeddedDocument):
    teachers = ReferenceField(Teacher)


class Class(Document):
    periods = ListField(EmbeddedDocumentField(Period))