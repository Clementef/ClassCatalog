from mongoengine import Document, ListField, EmbeddedDocument, EmbeddedDocumentField, ReferenceField, StringField, IntField


class Course(Document):

    name = StringField()

    subject = StringField()

