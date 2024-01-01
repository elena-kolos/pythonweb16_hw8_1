
from mongoengine import *


class Author(Document):

    fullname = StringField(max_length=50)
    born_date = StringField(max_length=20)
    born_location = StringField(max_length=50)
    description = StringField()


class Quote(Document):

    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=20))
    quote = StringField(max_length=1200, required=True)

    meta = {'allow_inheritance': True}



