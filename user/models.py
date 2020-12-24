from app import db
import datetime


class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    bio = db.StringField(max_length=200)
