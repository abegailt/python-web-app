from hashlib import md5
from app import db, models


class Task(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done    = db.Column(db.Boolean, default=False)


    def __init__(self, content):
        self.content = content
        self.done    = False


    def __repr__(self):
        return '<Content %s>' % self.content