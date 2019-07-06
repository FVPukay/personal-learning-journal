from peewee import *

import datetime

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    title = CharField(max_length=50)
    date = DateField()
    time_spent = IntegerField()
    what_you_learned = TextField()
    resources_to_remember = TextField()

    class Meta:
        database = DATABASE


def initialize():
    """Initialize the database"""
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()
