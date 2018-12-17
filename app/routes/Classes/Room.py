from mongoengine import Document, StringField, ReferenceField
from .Section import Section


class Room(Document):

    location = StringField()

    section = ReferenceField(Section)