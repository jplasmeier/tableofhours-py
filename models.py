# models.py
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    due_date = db.Column(db.DateTime())
    duration = db.Column(db.Integer)
    risk = db.Column(db.Float())
    str_location = db.Column(db.String())

    def __init__(self, title, description, due_date, duration, risk, str_location):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.duration = duration
        self.risk = risk
        self.str_location = str_location

    def __repr__(self):
        return '<id {}>'.format(self.id)
