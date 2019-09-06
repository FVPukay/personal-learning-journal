from peewee import *
import os

db_proxy = Proxy()


class Entry(Model):
    title = CharField()
    date = DateField()
    time_spent = IntegerField()
    what_you_learned = TextField()
    resources_to_remember = TextField()

    class Meta:
        database = db_proxy


if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('journal.db')
    db_proxy.initialize(db)


def initialize():
    """Initialize the database"""
    db_proxy.connect()
    db_proxy.create_tables([Entry], safe=True)
    db_proxy.close()
